from PyQt5 import QtWidgets
import importlib
import ConsoleConfig
import sys

if __name__ == "__main__" :
    import os
    os.environ['QT_IM_MODULE'] = 'ibus'
    app = QtWidgets.QApplication([])
    window = importlib.import_module(ConsoleConfig.event).AlertConsoleEvent()
    window.show()
    sys.exit(app.exec_())
    
    
