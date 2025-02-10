from PyQt5.QtWidgets import QToolBar

def create_toolbar(main_window, actions):
    toolbar = QToolBar("Main Toolbar", main_window)
    main_window.addToolBar(toolbar)

    toolbar.addAction(actions['new'])
    toolbar.addAction(actions['open'])
    toolbar.addAction(actions['save'])
    toolbar.addSeparator()
    toolbar.addAction(actions['undo'])
    toolbar.addAction(actions['redo'])
    toolbar.addSeparator()
    toolbar.addAction(actions['cut'])
    toolbar.addAction(actions['copy'])
    toolbar.addAction(actions['paste'])
    toolbar.addSeparator()
    toolbar.addAction(actions['zoom_in'])
    toolbar.addAction(actions['zoom_out'])
    toolbar.addSeparator()
    toolbar.addAction(actions['set_font'])

    return toolbar 