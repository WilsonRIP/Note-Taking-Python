from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTextEdit,
                             QMessageBox, QFileDialog, QInputDialog, QFontDialog,
                             QMenu, QColorDialog, QDialog, QLineEdit, QCheckBox,
                             QPushButton, QHBoxLayout, QLabel)
from PyQt5.QtCore import QFileInfo, QSettings, QDir, Qt
from PyQt5.QtGui import QFont, QColor, QTextCursor, QTextDocument
from actions import create_actions
from menus import create_menus
from toolbar import create_toolbar
from statusbar import create_statusbar
from highlighter import Highlighter
from help_window import HelpWindow
import datetime

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Find and Replace")

        self.find_edit = QLineEdit()
        self.replace_edit = QLineEdit()
        self.case_check = QCheckBox("Case Sensitive")
        self.whole_word_check = QCheckBox("Whole Words Only")
        self.find_button = QPushButton("Find")
        self.replace_button = QPushButton("Replace")
        self.replace_all_button = QPushButton("Replace All")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Find:"))
        layout.addWidget(self.find_edit)
        layout.addWidget(QLabel("Replace:"))
        layout.addWidget(self.replace_edit)
        layout.addWidget(self.case_check)
        layout.addWidget(self.whole_word_check)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.find_button)
        button_layout.addWidget(self.replace_button)
        button_layout.addWidget(self.replace_all_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.find_button.clicked.connect(self.find)
        self.replace_button.clicked.connect(self.replace)
        self.replace_all_button.clicked.connect(self.replace_all)

    def find(self):
        text = self.find_edit.text()
        if text:
            self.parent().find_text(text, self.case_check.isChecked(), self.whole_word_check.isChecked())

    def replace(self):
        find_text = self.find_edit.text()
        replace_text = self.replace_edit.text()
        if find_text:
            self.parent().replace_text(find_text, replace_text, self.case_check.isChecked(), self.whole_word_check.isChecked())

    def replace_all(self):
        find_text = self.find_edit.text()
        replace_text = self.replace_edit.text()
        if find_text:
            self.parent().replace_all_text(find_text, replace_text, self.case_check.isChecked(), self.whole_word_check.isChecked())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_current_tab)
        self.layout.addWidget(self.tabs)

        self.current_file_path = None

        # Settings
        self.settings = QSettings("MySoft", "TextEditor")
        font_name = self.settings.value("font", "Courier New")
        font_size = self.settings.value("font_size", 12)
        self.font = QFont(str(font_name), int(font_size))

        # Initialize actions, menus, toolbar, statusbar
        self.create_actions_dict = create_actions(self)
        for name, action in self.create_actions_dict.items():
            setattr(self, f"{name}_action", action)

        self.create_menus = create_menus(self)
        self.create_toolbar = create_toolbar(self, self.create_actions_dict)
        self.status_bar, self.status_label = create_statusbar(self)

    def new_file(self):
        text_edit = QTextEdit()
        text_edit.setFont(self.font)
        self.highlighter = Highlighter(text_edit.document(), 'python')
        tab_name, ok = QInputDialog.getText(self, "New Document", "Document Name:")
        if ok and tab_name:
            self.tabs.addTab(text_edit, tab_name)
            self.tabs.setCurrentWidget(text_edit)
            self.current_file_path = None
            self.update_status_bar()
        else:
            self.tabs.addTab(text_edit, "New Document")
            self.tabs.setCurrentWidget(text_edit)
            self.current_file_path = None
            self.update_status_bar()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;Python Files (*.py);;JavaScript Files (*.js);;All Files (*.*)")
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                text_edit = QTextEdit()
                text_edit.setFont(self.font)
                text_edit.setText(text)

                file_info = QFileInfo(file_path)
                extension = file_info.suffix().lower()
                if extension == 'py':
                    language = 'python'
                elif extension == 'js':
                    language = 'javascript'
                else:
                    language = 'text'
                self.highlighter = Highlighter(text_edit.document(), language)

                tab_name = file_info.fileName()
                self.tabs.addTab(text_edit, tab_name)
                self.tabs.setCurrentWidget(text_edit)
                self.current_file_path = file_path
                self.update_status_bar()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")

    def save_file(self):
        if self.current_file_path:
            self.save_file_as(self.current_file_path)
        else:
            self.save_file_as()

    def save_file_as(self, file_path=None):
        if not file_path:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", "",
                                                     "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                current_tab = self.tabs.currentWidget()
                if current_tab:
                    text = current_tab.toPlainText()
                    with open(file_path, 'w') as file:
                        file.write(text)
                    self.current_file_path = file_path
                    file_info = QFileInfo(file_path)
                    tab_name = file_info.fileName()
                    self.tabs.setTabText(self.tabs.currentIndex(), tab_name)

                    self.update_status_bar()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")

    def close_tab(self, index):
        widget = self.tabs.widget(index)
        if widget is not None:
            self.tabs.removeTab(index)
            widget.deleteLater()
            self.update_status_bar()

    def exit_app(self):
        self.close()

    def undo(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.undo()
            self.update_status_bar()

    def redo(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.redo()
            self.update_status_bar()

    def cut(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.cut()
            self.update_status_bar()

    def copy(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.copy()
            self.update_status_bar()

    def paste(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.paste()
            self.update_status_bar()

    def select_all(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.selectAll()

    def zoom_in(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.zoomIn()
            self.update_status_bar()

    def zoom_out(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.zoomOut()
            self.update_status_bar()

    def update_status_bar(self):
        if self.tabs.count() > 0:
            current_tab = self.tabs.currentWidget()
            word_count = self.get_word_count()
            if self.current_file_path:
                file_info = QFileInfo(self.current_file_path)
                file_name = file_info.fileName()
                self.status_label.setText(f"{file_name} | Words: {word_count}")
            else:
                self.status_label.setText(f"New Document | Words: {word_count}")
        else:
            self.status_label.setText("Ready")

    def set_font(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            font, ok = QFontDialog.getFont(self.font, self)
            if ok:
                self.font = font
                current_tab.setFont(self.font)

    def set_text_color(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            color = QColorDialog.getColor(current_tab.textColor(), self)
            if color.isValid():
                current_tab.setTextColor(color)

    def toggle_bold(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            if current_tab.fontWeight() == QFont.Bold:
                current_tab.setFontWeight(QFont.Normal)
            else:
                current_tab.setFontWeight(QFont.Bold)

    def toggle_underline(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.setFontUnderline(not current_tab.fontUnderline())

    def toggle_strikethrough(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            format = current_tab.currentCharFormat()
            format.setFontStrikeOut(not format.fontStrikeOut())
            current_tab.setCurrentCharFormat(format)

    def show_help(self):
        help_window = HelpWindow()
        help_window.exec_()

    def find_and_replace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec_()

    def find_text(self, text, case_sensitive, whole_words):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            flags = QTextDocument.FindFlags()
            if case_sensitive:
                flags |= QTextDocument.FindCaseSensitively
            if whole_words:
                flags |= QTextDocument.FindWholeWords

            cursor = current_tab.textCursor()
            cursor.setPosition(0)  # Start from the beginning
            current_tab.setTextCursor(cursor)

            found = current_tab.find(text, flags)
            if not found:
                QMessageBox.information(self, "Find", f"'{text}' not found.")

    def replace_text(self, find_text, replace_text, case_sensitive, whole_words):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            flags = QTextDocument.FindFlags()
            if case_sensitive:
                flags |= QTextDocument.FindCaseSensitively
            if whole_words:
                flags |= QTextDocument.FindWholeWords

            cursor = current_tab.textCursor()
            if cursor.hasSelection() and cursor.selectedText() == find_text:
                cursor.insertText(replace_text)
            else:
                # Move to the next occurrence
                cursor.setPosition(cursor.position())
                current_tab.setTextCursor(cursor)
                found = current_tab.find(find_text, flags)
                if found:
                    cursor = current_tab.textCursor()
                    cursor.insertText(replace_text)

    def replace_all_text(self, find_text, replace_text, case_sensitive, whole_words):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            flags = QTextDocument.FindFlags()
            if case_sensitive:
                flags |= QTextDocument.FindCaseSensitively
            if whole_words:
                flags |= QTextDocument.FindWholeWords

            cursor = current_tab.textCursor()
            cursor.setPosition(0)  # Start from the beginning
            current_tab.setTextCursor(cursor)

            while current_tab.find(find_text, flags):
                cursor = current_tab.textCursor()
                cursor.insertText(replace_text)

    def get_word_count(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            text = current_tab.toPlainText()
            words = text.split()
            return len(words)
        return 0

    def go_to_line(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            line_num, ok = QInputDialog.getInt(self, "Go to Line", "Line Number:", 1, 1)
            if ok:
                cursor = current_tab.textCursor()
                cursor.setPosition(0)  # Reset position
                cursor.movePosition(QTextCursor.Down, QTextCursor.MoveAnchor, line_num - 1)
                current_tab.setTextCursor(cursor)

    def insert_date_time(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            now = datetime.datetime.now()
            current_tab.insertPlainText(now.strftime("%Y-%m-%d %H:%M:%S"))

    def clear_all_text(self):
        current_tab = self.tabs.currentWidget()
        if current_tab:
            current_tab.clear()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        font_action = context_menu.addAction("Set Font")
        font_action.triggered.connect(self.set_font)
        context_menu.exec_(event.globalPos())

    def closeEvent(self, event):
        self.save_font_settings()
        super().closeEvent(event)

    def save_font_settings(self):
        self.settings.setValue("font", self.font.family())
        self.settings.setValue("font_size", self.font.pointSize())

    def update_current_tab(self, index):
        if index >= 0:
            self.current_file_path = None
            self.update_status_bar() 