def create_menus(main_window):
    menu_bar = main_window.menuBar()

    # File menu
    file_menu = menu_bar.addMenu("&File")
    file_menu.addAction(main_window.new_action)
    file_menu.addAction(main_window.open_action)
    file_menu.addAction(main_window.save_action)
    file_menu.addAction(main_window.save_as_action)
    file_menu.addSeparator()
    file_menu.addAction(main_window.exit_action)

    # Edit menu
    edit_menu = menu_bar.addMenu("&Edit")
    edit_menu.addAction(main_window.undo_action)
    edit_menu.addAction(main_window.redo_action)
    edit_menu.addSeparator()
    edit_menu.addAction(main_window.cut_action)
    edit_menu.addAction(main_window.copy_action)
    edit_menu.addAction(main_window.paste_action)

    # View menu
    view_menu = menu_bar.addMenu("&View")
    view_menu.addAction(main_window.zoom_in_action)
    view_menu.addAction(main_window.zoom_out_action)
    
    # Format menu
    format_menu = menu_bar.addMenu("&Format")
    format_menu.addAction(main_window.create_actions_dict['set_font'])

    # Help menu
    help_menu = menu_bar.addMenu("&Help") 