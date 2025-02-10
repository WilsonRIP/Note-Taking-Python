from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTextEdit, QMessageBox, QFileDialog, QInputDialog, QFontDialog, QMenu
from PyQt5.QtCore import QFileInfo, QSettings, QDir
from PyQt5.QtGui import QFont
from actions import create_actions
from menus import create_menus
from toolbar import create_toolbar
from statusbar import create_statusbar
from highlighter import Highlighter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_current_tab)
        self.layout.addWidget(self.tabs)

        self.current_file_path = None  # Initialize current_file_path

        # Settings
        self.settings = QSettings("MySoft", "TextEditor")
        font_name = self.settings.value("font", "Courier New")
        font_size = self.settings.value("font_size", 12)
        self.font = QFont(str(font_name), int(font_size))

        # Initialize and create actions, menus, toolbar, and statusbar
        self.create_actions_dict = create_actions(self)
        for name, action in self.create_actions_dict.items():
            setattr(self, f"{name}_action", action)

        self.create_menus = create_menus(self)
        self.create_toolbar = create_toolbar(self, self.create_actions_dict)
        self.status_bar, self.status_label = create_statusbar(self)

        self.new_file()  # Open a default new tab on startup

    def new_file(self):
        text_edit = QTextEdit()
        text_edit.setFont(self.font)
        self.highlighter = Highlighter(text_edit.document(), 'python')  # Default to Python
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
        file_path, _ = QFileDialog.getOpenFileName(self, self, "Open File", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                text_edit = QTextEdit()
                text_edit.setFont(self.font)
                text_edit.setText(text)

                # Determine language from file extension
                file_info = QFileInfo(file_path)
                extension = file_info.suffix().lower()
                if extension == 'py':
                    language = 'python'
                else:
                    language = 'text'  # Default
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
            file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                current_tab = self.tabs.currentWidget()
                if current_tab:
                    text = current_tab.toPlainText()
                    with open(file_path, 'w') as file:
                        file.write(text)
                    self.current_file_path = file_path
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
        current_tab = self.tabs.currentWidget()
        if current_tab:
            if self.current_file_path:
                file_info = QFileInfo(self.current_file_path)
                file_name = file_info.fileName()
                self.status_label.setText(f"Current File: {file_name}")
            else:
                self.status_label.setText("New Document")
        else:
            self.status_label.setText("Ready")

    def set_font(self):
        font, ok = QFontDialog.getFont(self.font, self, "Select Font")
        if ok:
            self.font = font
            for i in range(self.tabs.count()):
                text_edit = self.tabs.widget(i)
                text_edit.setFont(self.font)
            self.save_font_settings()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        font_action = context_menu.addAction("Set Font")
        font_action.triggered.connect(self.set_font)
        context_menu.exec_(event.globalPos())

    def closeEvent(self, event):
        # Save settings on close
        self.save_font_settings()
        super().closeEvent(event)

    def save_font_settings(self):
        self.settings.setValue("font", self.font.family())
        self.settings.setValue("font_size", self.font.pointSize())

    def update_current_tab(self, index):
        if index >= 0:
            self.current_file_path = None  # Reset file path when switching tabs
            self.update_status_bar() 