# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventConfigurationNew.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 565)
        Dialog.setMinimumSize(QtCore.QSize(618, 565))
        Dialog.setMaximumSize(QtCore.QSize(618, 565))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ec_frame = QtWidgets.QFrame(Dialog)
        self.ec_frame.setMinimumSize(QtCore.QSize(600, 300))
        self.ec_frame.setMaximumSize(QtCore.QSize(725, 300))
        self.ec_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ec_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ec_frame.setObjectName("ec_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ec_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.event_creation_status_label = QtWidgets.QLabel(self.ec_frame)
        self.event_creation_status_label.setText("")
        self.event_creation_status_label.setObjectName("event_creation_status_label")
        self.horizontalLayout_10.addWidget(self.event_creation_status_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.button_save_event = QtWidgets.QPushButton(self.ec_frame)
        self.button_save_event.setMinimumSize(QtCore.QSize(100, 0))
        self.button_save_event.setObjectName("button_save_event")
        self.horizontalLayout_10.addWidget(self.button_save_event)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_event_description = QtWidgets.QLabel(self.ec_frame)
        self.label_event_description.setObjectName("label_event_description")
        self.verticalLayout_7.addWidget(self.label_event_description)
        self.textbox_event_description = QtWidgets.QPlainTextEdit(self.ec_frame)
        self.textbox_event_description.setMaximumSize(QtCore.QSize(16777215, 250))
        self.textbox_event_description.setObjectName("textbox_event_description")
        self.verticalLayout_7.addWidget(self.textbox_event_description)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_event_name = QtWidgets.QLabel(self.ec_frame)
        self.label_event_name.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_event_name.setObjectName("label_event_name")
        self.verticalLayout_4.addWidget(self.label_event_name)
        self.textbox_event_name = QtWidgets.QPlainTextEdit(self.ec_frame)
        self.textbox_event_name.setMinimumSize(QtCore.QSize(0, 0))
        self.textbox_event_name.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textbox_event_name.setObjectName("textbox_event_name")
        self.verticalLayout_4.addWidget(self.textbox_event_name)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_event_start = QtWidgets.QLabel(self.ec_frame)
        self.label_event_start.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_event_start.setObjectName("label_event_start")
        self.verticalLayout_5.addWidget(self.label_event_start)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.ec_frame)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_5.addWidget(self.dateTimeEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_event_end = QtWidgets.QLabel(self.ec_frame)
        self.label_event_end.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_event_end.setObjectName("label_event_end")
        self.verticalLayout_6.addWidget(self.label_event_end)
        self.date_event_end = QtWidgets.QDateTimeEdit(self.ec_frame)
        self.date_event_end.setObjectName("date_event_end")
        self.verticalLayout_6.addWidget(self.date_event_end)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.ec_label = QtWidgets.QLabel(self.ec_frame)
        self.ec_label.setMaximumSize(QtCore.QSize(16777215, 28))
        self.ec_label.setObjectName("ec_label")
        self.gridLayout_3.addWidget(self.ec_label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ec_frame)
        self.dc_frame = QtWidgets.QFrame(Dialog)
        self.dc_frame.setMinimumSize(QtCore.QSize(600, 0))
        self.dc_frame.setMaximumSize(QtCore.QSize(725, 210))
        self.dc_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dc_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dc_frame.setObjectName("dc_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dc_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_18 = QtWidgets.QLabel(self.dc_frame)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_root_directory = QtWidgets.QLabel(self.dc_frame)
        self.label_root_directory.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_root_directory.setObjectName("label_root_directory")
        self.verticalLayout_15.addWidget(self.label_root_directory)
        self.label_red_team_folder = QtWidgets.QLabel(self.dc_frame)
        self.label_red_team_folder.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_red_team_folder.setObjectName("label_red_team_folder")
        self.verticalLayout_15.addWidget(self.label_red_team_folder)
        self.label_blue_team_folder = QtWidgets.QLabel(self.dc_frame)
        self.label_blue_team_folder.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_blue_team_folder.setObjectName("label_blue_team_folder")
        self.verticalLayout_15.addWidget(self.label_blue_team_folder)
        self.label_white_team_folder = QtWidgets.QLabel(self.dc_frame)
        self.label_white_team_folder.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_white_team_folder.setObjectName("label_white_team_folder")
        self.verticalLayout_15.addWidget(self.label_white_team_folder)
        self.horizontalLayout_6.addLayout(self.verticalLayout_15)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.textbox_root_directory = QtWidgets.QPlainTextEdit(self.dc_frame)
        self.textbox_root_directory.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textbox_root_directory.setObjectName("textbox_root_directory")
        self.verticalLayout_13.addWidget(self.textbox_root_directory)
        self.textbox_red_team_folder = QtWidgets.QPlainTextEdit(self.dc_frame)
        self.textbox_red_team_folder.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textbox_red_team_folder.setObjectName("textbox_red_team_folder")
        self.verticalLayout_13.addWidget(self.textbox_red_team_folder)
        self.textbox_blue_team_folder = QtWidgets.QPlainTextEdit(self.dc_frame)
        self.textbox_blue_team_folder.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textbox_blue_team_folder.setObjectName("textbox_blue_team_folder")
        self.verticalLayout_13.addWidget(self.textbox_blue_team_folder)
        self.textbox_white_team_folder = QtWidgets.QPlainTextEdit(self.dc_frame)
        self.textbox_white_team_folder.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textbox_white_team_folder.setObjectName("textbox_white_team_folder")
        self.verticalLayout_13.addWidget(self.textbox_white_team_folder)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.root_directory_pushButton = QtWidgets.QPushButton(self.dc_frame)
        self.root_directory_pushButton.setObjectName("root_directory_pushButton")
        self.verticalLayout_2.addWidget(self.root_directory_pushButton)
        self.red_team_directory_pushButton = QtWidgets.QPushButton(self.dc_frame)
        self.red_team_directory_pushButton.setObjectName("red_team_directory_pushButton")
        self.verticalLayout_2.addWidget(self.red_team_directory_pushButton)
        self.blue_team_directory_pushButton = QtWidgets.QPushButton(self.dc_frame)
        self.blue_team_directory_pushButton.setObjectName("blue_team_directory_pushButton")
        self.verticalLayout_2.addWidget(self.blue_team_directory_pushButton)
        self.white_team_directory_pushButton = QtWidgets.QPushButton(self.dc_frame)
        self.white_team_directory_pushButton.setObjectName("white_team_directory_pushButton")
        self.verticalLayout_2.addWidget(self.white_team_directory_pushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.button_start_ingestion = QtWidgets.QPushButton(self.dc_frame)
        self.button_start_ingestion.setMinimumSize(QtCore.QSize(100, 0))
        self.button_start_ingestion.setObjectName("button_start_ingestion")
        self.horizontalLayout_13.addWidget(self.button_start_ingestion)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addWidget(self.dc_frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(600, 0))
        self.buttonBox.setMaximumSize(QtCore.QSize(725, 500))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_save_event.setText(_translate("Dialog", "Save Event"))
        self.label_event_description.setText(_translate("Dialog", "Description"))
        self.label_event_name.setText(_translate("Dialog", "Event Name"))
        self.label_event_start.setText(_translate("Dialog", "Event Start Timestamp"))
        self.label_event_end.setText(_translate("Dialog", "Event End Timestamp"))
        self.ec_label.setText(_translate("Dialog", "Event Configuration - Create New"))
        self.label_18.setText(_translate("Dialog", "Directory Configuration"))
        self.label_root_directory.setText(_translate("Dialog", "Root Directory"))
        self.label_red_team_folder.setText(_translate("Dialog", "Red Team Folder"))
        self.label_blue_team_folder.setText(_translate("Dialog", "Blue Team Folder"))
        self.label_white_team_folder.setText(_translate("Dialog", "White Team Folder "))
        self.root_directory_pushButton.setText(_translate("Dialog", "Browse"))
        self.red_team_directory_pushButton.setText(_translate("Dialog", "Browse"))
        self.blue_team_directory_pushButton.setText(_translate("Dialog", "Browse"))
        self.white_team_directory_pushButton.setText(_translate("Dialog", "Browse"))
        self.button_start_ingestion.setText(_translate("Dialog", "Start Data Ingestion"))
