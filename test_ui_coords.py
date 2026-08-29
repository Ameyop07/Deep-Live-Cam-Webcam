import os
import sys
from PySide6.QtWidgets import QApplication
from modules.gettext import LanguageManager
import modules.globals

def test():
    app = QApplication(sys.argv)
    from modules.ui import MainWindow
    window = MainWindow(lambda: None, lambda: None)
    window.resize(640, 600)
    window.show()
    
    # Process events to allow layout calculation
    app.processEvents()
    
    print("MainWindow size:", window.width(), "x", window.height())
    scroll = window.centralWidget()
    print("Scroll area size:", scroll.width(), "x", scroll.height())
    
    root = scroll.widget()
    print("Root widget size:", root.width(), "x", root.height())
    
    print("\nChildren geometries inside root Layout:")
    layout = root.layout()
    for i in range(layout.count()):
        item = layout.itemAt(i)
        if item.widget():
            w = item.widget()
            print(f"Widget {w.__class__.__name__} ({w.objectName()}): size={w.width()}x{w.height()}, pos={w.x()},{w.y()}, visible={w.isVisible()}")
        elif item.layout():
            lay = item.layout()
            print(f"Layout {lay.__class__.__name__}: count={lay.count()}")
            # print child widgets of sub-layout
            for j in range(lay.count()):
                sub_item = lay.itemAt(j)
                if sub_item.widget():
                    w = sub_item.widget()
                    print(f"  -> Widget {w.__class__.__name__} ({w.objectName()}): size={w.width()}x{w.height()}, pos={w.x()},{w.y()}, visible={w.isVisible()}")
    
    sys.exit(0)

if __name__ == '__main__':
    test()
