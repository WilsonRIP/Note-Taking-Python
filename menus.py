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
    edit_menu.addAction(main_window.select_all_action)
    edit_menu.addSeparator()
    edit_menu.addAction(main_window.find_replace_action)
    edit_menu.addAction(main_window.clear_all_action)

    # View menu
    view_menu = menu_bar.addMenu("&View")
    view_menu.addAction(main_window.zoom_in_action)
    view_menu.addAction(main_window.zoom_out_action)
    view_menu.addSeparator()
    view_menu.addAction(main_window.go_to_line_action)

    # Format menu
    format_menu = menu_bar.addMenu("&Format")
    format_menu.addAction(main_window.set_font_action)
    format_menu.addAction(main_window.set_color_action)
    format_menu.addSeparator()
    format_menu.addAction(main_window.insert_date_time_action)
    format_menu.addSeparator()

    # Styling submenu
    styling_menu = format_menu.addMenu("&Styling")
    styling_menu.addAction(main_window.bold_action)
    styling_menu.addAction(main_window.underline_action)
    styling_menu.addAction(main_window.strikethrough_action)

    # Help menu (added last to be on the right)
    help_menu = menu_bar.addMenu("&Help")
    help_menu.addAction(main_window.help_action) 