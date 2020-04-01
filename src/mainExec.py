import sys

from main import functionality as UIFunctionality
from eventconfiguration import EventConfiguration
from ingestion_functionality import IngestionFunctionality
from SPLUNKInterface import SPLUNKInterface
from manage_tables import manage_tables as TableFunctionality

from PyQt5 import QtWidgets, QtGui, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == "__main__":
    event_config = EventConfiguration(name="main")
    ingestion = IngestionFunctionality()
    splunk = SPLUNKInterface()
    table_manager = TableFunctionality()
    ui_f = UIFunctionality(table_manager=table_manager, splunk=splunk,
                           ingest_funct=ingestion, event_config=event_config)

    app = QApplication([])
    PICK = QtWidgets.QMainWindow()
    ui = ui_f
    ui.setupUi(PICK)
    PICK.show()
    ui.resize_ui_components(PICK)
    sys.exit(app.exec_())