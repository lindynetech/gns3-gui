# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/builtin/ui/ethernet_hub_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EthernetHubWizard(object):
    def setupUi(self, EthernetHubWizard):
        EthernetHubWizard.setObjectName("EthernetHubWizard")
        EthernetHubWizard.resize(585, 423)
        EthernetHubWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiServerTypeGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.verticalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.verticalLayout.addWidget(self.uiVMRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.verticalLayout.addWidget(self.uiLocalRadioButton)
        self.gridLayout_2.addWidget(self.uiServerTypeGroupBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        EthernetHubWizard.addPage(self.uiServerWizardPage)
        self.uiNameWizardPage = QtWidgets.QWizardPage()
        self.uiNameWizardPage.setObjectName("uiNameWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiNameWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiNameWizardPage)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiNameWizardPage)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiPortsLabel = QtWidgets.QLabel(self.uiNameWizardPage)
        self.uiPortsLabel.setObjectName("uiPortsLabel")
        self.gridLayout.addWidget(self.uiPortsLabel, 1, 0, 1, 1)
        self.uiPortsSpinBox = QtWidgets.QSpinBox(self.uiNameWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPortsSpinBox.sizePolicy().hasHeightForWidth())
        self.uiPortsSpinBox.setSizePolicy(sizePolicy)
        self.uiPortsSpinBox.setMinimum(0)
        self.uiPortsSpinBox.setMaximum(65535)
        self.uiPortsSpinBox.setProperty("value", 8)
        self.uiPortsSpinBox.setObjectName("uiPortsSpinBox")
        self.gridLayout.addWidget(self.uiPortsSpinBox, 1, 1, 1, 1)
        EthernetHubWizard.addPage(self.uiNameWizardPage)

        self.retranslateUi(EthernetHubWizard)
        QtCore.QMetaObject.connectSlotsByName(EthernetHubWizard)

    def retranslateUi(self, EthernetHubWizard):
        _translate = QtCore.QCoreApplication.translate
        EthernetHubWizard.setWindowTitle(_translate("EthernetHubWizard", "New Ethernet hub"))
        self.uiServerWizardPage.setTitle(_translate("EthernetHubWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("EthernetHubWizard", "Please choose a server type to run your new Ethernet hub."))
        self.uiServerTypeGroupBox.setTitle(_translate("EthernetHubWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("EthernetHubWizard", "Run the Ethernet hub on a remote computer"))
        self.uiVMRadioButton.setText(_translate("EthernetHubWizard", "Run the Ethernet hub on the GNS3 VM"))
        self.uiLocalRadioButton.setText(_translate("EthernetHubWizard", "Run the Ethernet hub on your local computer"))
        self.uiRemoteServersGroupBox.setTitle(_translate("EthernetHubWizard", "Remote server"))
        self.uiRemoteServersLabel.setText(_translate("EthernetHubWizard", "Run on:"))
        self.uiNameWizardPage.setTitle(_translate("EthernetHubWizard", "Name"))
        self.uiNameWizardPage.setSubTitle(_translate("EthernetHubWizard", "Please choose a descriptive name for the new Ethernet hub."))
        self.uiNameLabel.setText(_translate("EthernetHubWizard", "Name:"))
        self.uiPortsLabel.setText(_translate("EthernetHubWizard", "Number of ports:"))

