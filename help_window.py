from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit

class HelpWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keyboard Shortcuts")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout(self)

        shortcuts_text = """
        <b>File:</b><br>
        New: Ctrl+N<br>
        Open: Ctrl+O<br>
        Save: Ctrl+S<br>
        Save As: Ctrl+Shift+S<br>
        Exit: Ctrl+Q<br>
        <br>
        <b>Edit:</b><br>
        Undo: Ctrl+Z<br>
        Redo: Ctrl+Y<br>
        Cut: Ctrl+X<br>
        Copy: Ctrl+C<br>
        Paste: Ctrl+V<br>
        Select All: Ctrl+A<br>
        Find and Replace: Ctrl+F<br>
        Clear All: N/A<br>
        <br>
        <b>View:</b><br>
        Zoom In: Ctrl++<br>
        Zoom Out: Ctrl+-<br>
        Go to Line: Ctrl+G<br>
        <br>
        <b>Format:</b><br>
        Bold: Ctrl+B<br>
        Underline: Ctrl+U<br>
        Strikethrough: Ctrl+Shift+S<br>
        Insert Date and Time: Ctrl+Shift+D<br>
        """
        label = QTextEdit()
        label.setReadOnly(True)
        label.setHtml(shortcuts_text)  # Use setHtml for rich text
        layout.addWidget(label) 