import os
import sys
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

def test():
    app = QApplication(sys.argv)
    from modules.ui import MainWindow
    window = MainWindow(lambda: None, lambda: None)
    window.resize(640, 600)
    window.show()
    
    # Process events to allow layout calculation
    app.processEvents()
    
    scroll = window.centralWidget()
    bar = scroll.verticalScrollBar()
    print("Initial search:")
    print("Scrollbar value:", bar.value())
    print("Scrollbar range:", bar.minimum(), "to", bar.maximum())
    
    # Let's wait a bit and check if focus movement changed it
    def print_later():
        print("Later search (after focus/events):")
        print("Scrollbar value:", bar.value())
        print("Scrollbar range:", bar.minimum(), "to", bar.maximum())
        sys.exit(0)
        
    QTimer.singleShot(500, print_later)
    app.exec()

if __name__ == '__main__':
    test()
