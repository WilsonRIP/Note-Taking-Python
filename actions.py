from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon, QKeySequence

def create_actions(main_window):
    actions = {}

    # File actions
    actions['new'] = QAction(QIcon.fromTheme("document-new"), "New", main_window)
    actions['new'].setShortcut(QKeySequence.StandardKey.New)
    actions['new'].setStatusTip("Create a new document")
    actions['new'].triggered.connect(main_window.new_file)

    actions['open'] = QAction(QIcon.fromTheme("document-open"), "Open", main_window)
    actions['open'].setShortcut(QKeySequence.StandardKey.Open)
    actions['open'].setStatusTip("Open an existing document")
    actions['open'].triggered.connect(main_window.open_file)

    actions['save'] = QAction(QIcon.fromTheme("document-save"), "Save", main_window)
    actions['save'].setShortcut(QKeySequence.StandardKey.Save)
    actions['save'].setStatusTip("Save the current document")
    actions['save'].triggered.connect(main_window.save_file)

    actions['save_as'] = QAction("Save As...", main_window)
    actions['save_as'].setShortcut(QKeySequence.StandardKey.SaveAs)
    actions['save_as'].setStatusTip("Save the current document with a new name")
    actions['save_as'].triggered.connect(main_window.save_file_as)

    actions['exit'] = QAction("Exit", main_window)
    actions['exit'].setShortcut(QKeySequence.StandardKey.Quit)
    actions['exit'].setStatusTip("Exit the application")
    actions['exit'].triggered.connect(main_window.exit_app)

    # Edit actions
    actions['undo'] = QAction(QIcon.fromTheme("edit-undo"), "Undo", main_window)
    actions['undo'].setShortcut(QKeySequence.StandardKey.Undo)
    actions['undo'].setStatusTip("Undo the last action")
    actions['undo'].triggered.connect(main_window.undo)

    actions['redo'] = QAction(QIcon.fromTheme("edit-redo"), "Redo", main_window)
    actions['redo'].setShortcut(QKeySequence.StandardKey.Redo)
    actions['redo'].setStatusTip("Redo the last undone action")
    actions['redo'].triggered.connect(main_window.redo)

    actions['cut'] = QAction(QIcon.fromTheme("edit-cut"), "Cut", main_window)
    actions['cut'].setShortcut(QKeySequence.StandardKey.Cut)
    actions['cut'].setStatusTip("Cut the selected text to the clipboard")
    actions['cut'].triggered.connect(main_window.cut)

    actions['copy'] = QAction(QIcon.fromTheme("edit-copy"), "Copy", main_window)
    actions['copy'].setShortcut(QKeySequence.StandardKey.Copy)
    actions['copy'].setStatusTip("Copy the selected text to the clipboard")
    actions['copy'].triggered.connect(main_window.copy)

    actions['paste'] = QAction(QIcon.fromTheme("edit-paste"), "Paste", main_window)
    actions['paste'].setShortcut(QKeySequence.StandardKey.Paste)
    actions['paste'].setStatusTip("Paste the text from the clipboard")
    actions['paste'].triggered.connect(main_window.paste)
    
    actions['select_all'] = QAction(QIcon.fromTheme("edit-select-all"), "Select All", main_window)
    actions['select_all'].setShortcut(QKeySequence.StandardKey.SelectAll)
    actions['select_all'].setStatusTip("Select all text")
    actions['select_all'].triggered.connect(main_window.select_all)

    # View actions
    actions['zoom_in'] = QAction(QIcon.fromTheme("zoom-in"), "Zoom In", main_window)
    actions['zoom_in'].setShortcut(QKeySequence.StandardKey.ZoomIn)
    actions['zoom_in'].setStatusTip("Zoom in")
    actions['zoom_in'].triggered.connect(main_window.zoom_in)

    actions['zoom_out'] = QAction(QIcon.fromTheme("zoom-out"), "Zoom Out", main_window)
    actions['zoom_out'].setShortcut(QKeySequence.StandardKey.ZoomOut)
    actions['zoom_out'].setStatusTip("Zoom out")
    actions['zoom_out'].triggered.connect(main_window.zoom_out)

    # Format actions
    actions['set_font'] = QAction("Set Font", main_window)
    actions['set_font'].setStatusTip("Set the font for the editor")
    actions['set_font'].triggered.connect(main_window.set_font)

    actions['set_color'] = QAction("Set Text Color", main_window)
    actions['set_color'].setStatusTip("Set the text color")
    actions['set_color'].triggered.connect(main_window.set_text_color)

    actions['bold'] = QAction(QIcon.fromTheme("format-text-bold"), "Bold", main_window)
    actions['bold'].setShortcut(QKeySequence.StandardKey.Bold)
    actions['bold'].setStatusTip("Toggle bold")
    actions['bold'].triggered.connect(main_window.toggle_bold)

    actions['underline'] = QAction(QIcon.fromTheme("format-text-underline"), "Underline", main_window)
    actions['underline'].setShortcut(QKeySequence.StandardKey.Underline)
    actions['underline'].setStatusTip("Toggle underline")
    actions['underline'].triggered.connect(main_window.toggle_underline)

    actions['strikethrough'] = QAction(QIcon.fromTheme("format-text-strikethrough"), "Strikethrough", main_window)
    actions['strikethrough'].setShortcut(QKeySequence.fromString("Ctrl+Shift+S"))  # No standard shortcut
    actions['strikethrough'].setStatusTip("Toggle strikethrough")
    actions['strikethrough'].triggered.connect(main_window.toggle_strikethrough)

    # Find and Replace
    actions['find_replace'] = QAction(QIcon.fromTheme("edit-find-replace"), "Find and Replace", main_window)
    actions['find_replace'].setShortcut(QKeySequence.StandardKey.Find)  # Ctrl+F
    actions['find_replace'].setStatusTip("Find and replace text")
    actions['find_replace'].triggered.connect(main_window.find_and_replace)

    # Go to Line
    actions['go_to_line'] = QAction("Go to Line", main_window)
    actions['go_to_line'].setShortcut(QKeySequence.fromString("Ctrl+G"))
    actions['go_to_line'].setStatusTip("Go to a specific line")
    actions['go_to_line'].triggered.connect(main_window.go_to_line)

    # Insert Date and Time
    actions['insert_date_time'] = QAction("Insert Date and Time", main_window)
    actions['insert_date_time'].setShortcut(QKeySequence.fromString("Ctrl+Shift+D"))
    actions['insert_date_time'].setStatusTip("Insert the current date and time")
    actions['insert_date_time'].triggered.connect(main_window.insert_date_time)
    
    # Clear all text
    actions['clear_all'] = QAction("Clear All", main_window)
    actions['clear_all'].setStatusTip("Clear all text")
    actions['clear_all'].triggered.connect(main_window.clear_all_text)

    # Help action
    actions['help'] = QAction(QIcon.fromTheme("help-contents"), "Help", main_window)
    actions['help'].setStatusTip("Show keyboard shortcuts")
    actions['help'].triggered.connect(main_window.show_help)

    return actions 