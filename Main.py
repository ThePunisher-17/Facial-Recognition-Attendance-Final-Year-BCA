import sys

from PySide6.QtWidgets import QApplication

from Project import Project

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Project()
    with open("style.qss") as f:
        widget.setStyleSheet(f.read())
    widget.show()
    sys.exit(app.exec())