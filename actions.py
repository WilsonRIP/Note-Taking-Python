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

    return actions 