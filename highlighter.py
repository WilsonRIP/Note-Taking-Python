from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import Qt, QRegularExpression

class Highlighter(QSyntaxHighlighter):
    def __init__(self, document, language='python'):
        super().__init__(document)
        self.language = language
        self.highlighting_rules = []
        self.setup_rules()

    def setup_rules(self):
        if self.language == 'python':
            self.setup_python_rules()
        elif self.language == 'javascript':
            self.setup_javascript_rules()
        # Add more languages here

    def setup_python_rules(self):
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(Qt.darkBlue))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def',
                    'del', 'elif', 'else', 'except', 'False', 'finally', 'for',
                    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None',
                    'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True',
                    'try', 'while', 'with', 'yield']
        keyword_patterns = [r'\b' + keyword + r'\b' for keyword in keywords]
        for pattern in keyword_patterns:
            self.highlighting_rules.append((pattern, keyword_format))

        class_format = QTextCharFormat()
        class_format.setForeground(QColor(Qt.darkMagenta))
        class_format.setFontWeight(QFont.Bold)
        class_pattern = r'\b[A-Z][a-zA-Z]+\b'
        self.highlighting_rules.append((class_pattern, class_format))

        string_format = QTextCharFormat()
        string_format.setForeground(QColor(Qt.darkGreen))
        string_pattern = r'".*"|\'.*\''
        self.highlighting_rules.append((string_pattern, string_format))

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(Qt.gray))
        comment_pattern = r'#[^\n]*'
        self.highlighting_rules.append((comment_pattern, comment_format))
    
    def setup_javascript_rules(self):
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(Qt.darkBlue))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = ['var', 'let', 'const', 'function', 'if', 'else', 'switch', 'case',
                    'default', 'for', 'while', 'do', 'break', 'continue', 'return',
                    'try', 'catch', 'finally', 'throw', 'new', 'delete', 'typeof',
                    'instanceof', 'in', 'void', 'debugger', 'with', 'class', 'extends',
                    'super', 'import', 'export', 'from', 'async', 'await', 'yield']
        keyword_patterns = [r'\b' + keyword + r'\b' for keyword in keywords]
        for pattern in keyword_patterns:
            self.highlighting_rules.append((pattern, keyword_format))

        string_format = QTextCharFormat()
        string_format.setForeground(QColor(Qt.darkGreen))
        string_pattern = r'".*"|\'.*\''
        self.highlighting_rules.append((string_pattern, string_format))

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(Qt.gray))
        comment_pattern = r'//[^\n]*|/\*[\s\S]*?\*/'
        self.highlighting_rules.append((comment_pattern, comment_format))

        number_format = QTextCharFormat()
        number_format.setForeground(QColor(Qt.red))
        number_pattern = r'\b\d+(\.\d*)?([eE][-+]?\d+)?\b'
        self.highlighting_rules.append((number_pattern, number_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            iterator = expression.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format) 