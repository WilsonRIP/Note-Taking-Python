from PyQt5.QtWidgets import QStatusBar, QLabel

def create_statusbar(main_window):
    status_bar = QStatusBar()
    main_window.setStatusBar(status_bar)
    status_label = QLabel("Ready")
    status_bar.addWidget(status_label)
    return status_bar, status_label 