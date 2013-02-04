# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aston.ui'
#
# Created: Fri Feb  1 14:37:03 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(694, 537)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plotArea = QtGui.QVBoxLayout()
        self.plotArea.setObjectName(_fromUtf8("plotArea"))
        self.verticalLayout.addLayout(self.plotArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuExport = QtGui.QMenu(self.menuFile)
        self.menuExport.setObjectName(_fromUtf8("menuExport"))
        self.menuChromatogram = QtGui.QMenu(self.menubar)
        self.menuChromatogram.setObjectName(_fromUtf8("menuChromatogram"))
        self.menuIntegrand = QtGui.QMenu(self.menuChromatogram)
        self.menuIntegrand.setObjectName(_fromUtf8("menuIntegrand"))
        self.menuSpectrum = QtGui.QMenu(self.menubar)
        self.menuSpectrum.setObjectName(_fromUtf8("menuSpectrum"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setEnabled(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuPeaks = QtGui.QMenu(self.menuSettings)
        self.menuPeaks.setEnabled(False)
        self.menuPeaks.setObjectName(_fromUtf8("menuPeaks"))
        self.menuExtras = QtGui.QMenu(self.menuSettings)
        self.menuExtras.setEnabled(True)
        self.menuExtras.setObjectName(_fromUtf8("menuExtras"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.filesDockWidget = QtGui.QDockWidget(MainWindow)
        self.filesDockWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filesDockWidget.setFloating(False)
        self.filesDockWidget.setObjectName(_fromUtf8("filesDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.fileTreeView = QtGui.QTreeView(self.dockWidgetContents)
        self.fileTreeView.setObjectName(_fromUtf8("fileTreeView"))
        self.verticalLayout_4.addWidget(self.fileTreeView)
        self.filesDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.filesDockWidget)
        self.settingsDockWidget = QtGui.QDockWidget(MainWindow)
        self.settingsDockWidget.setObjectName(_fromUtf8("settingsDockWidget"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_settings = QtGui.QVBoxLayout()
        self.verticalLayout_settings.setObjectName(_fromUtf8("verticalLayout_settings"))
        self.horizontalLayout_4.addLayout(self.verticalLayout_settings)
        self.settingsDockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.settingsDockWidget)
        self.spectraDockWidget = QtGui.QDockWidget(MainWindow)
        self.spectraDockWidget.setObjectName(_fromUtf8("spectraDockWidget"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.dockWidgetContents_5)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.specArea = QtGui.QVBoxLayout()
        self.specArea.setObjectName(_fromUtf8("specArea"))
        self.horizontalLayout_3.addLayout(self.specArea)
        self.spectraDockWidget.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.spectraDockWidget)
        self.methodDockWidget = QtGui.QDockWidget(MainWindow)
        self.methodDockWidget.setEnabled(True)
        self.methodDockWidget.setObjectName(_fromUtf8("methodDockWidget"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.methodTreeView = QtGui.QTreeView(self.dockWidgetContents_2)
        self.methodTreeView.setObjectName(_fromUtf8("methodTreeView"))
        self.verticalLayout_2.addWidget(self.methodTreeView)
        self.methodDockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.methodDockWidget)
        self.compoundDockWidget = QtGui.QDockWidget(MainWindow)
        self.compoundDockWidget.setObjectName(_fromUtf8("compoundDockWidget"))
        self.dockWidgetContents_6 = QtGui.QWidget()
        self.dockWidgetContents_6.setObjectName(_fromUtf8("dockWidgetContents_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.compoundTreeView = QtGui.QTreeView(self.dockWidgetContents_6)
        self.compoundTreeView.setObjectName(_fromUtf8("compoundTreeView"))
        self.verticalLayout_3.addWidget(self.compoundTreeView)
        self.compoundDockWidget.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.compoundDockWidget)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExportChromatogram = QtGui.QAction(MainWindow)
        self.actionExportChromatogram.setObjectName(_fromUtf8("actionExportChromatogram"))
        self.actionChromatogram_as_CSV = QtGui.QAction(MainWindow)
        self.actionChromatogram_as_CSV.setEnabled(False)
        self.actionChromatogram_as_CSV.setObjectName(_fromUtf8("actionChromatogram_as_CSV"))
        self.actionExportSpectra = QtGui.QAction(MainWindow)
        self.actionExportSpectra.setObjectName(_fromUtf8("actionExportSpectra"))
        self.actionSpectra_as_CSV = QtGui.QAction(MainWindow)
        self.actionSpectra_as_CSV.setEnabled(False)
        self.actionSpectra_as_CSV.setObjectName(_fromUtf8("actionSpectra_as_CSV"))
        self.actionExportSelectedItems = QtGui.QAction(MainWindow)
        self.actionExportSelectedItems.setEnabled(True)
        self.actionExportSelectedItems.setObjectName(_fromUtf8("actionExportSelectedItems"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSearch_Database = QtGui.QAction(MainWindow)
        self.actionSearch_Database.setEnabled(False)
        self.actionSearch_Database.setObjectName(_fromUtf8("actionSearch_Database"))
        self.actionSave_to_Database = QtGui.QAction(MainWindow)
        self.actionSave_to_Database.setEnabled(False)
        self.actionSave_to_Database.setObjectName(_fromUtf8("actionSave_to_Database"))
        self.actionSequence = QtGui.QAction(MainWindow)
        self.actionSequence.setEnabled(False)
        self.actionSequence.setObjectName(_fromUtf8("actionSequence"))
        self.actionStructure = QtGui.QAction(MainWindow)
        self.actionStructure.setEnabled(False)
        self.actionStructure.setObjectName(_fromUtf8("actionStructure"))
        self.actionCalculate_Info = QtGui.QAction(MainWindow)
        self.actionCalculate_Info.setObjectName(_fromUtf8("actionCalculate_Info"))
        self.actionAutoAlignChromatogram = QtGui.QAction(MainWindow)
        self.actionAutoAlignChromatogram.setEnabled(False)
        self.actionAutoAlignChromatogram.setObjectName(_fromUtf8("actionAutoAlignChromatogram"))
        self.actionSubtractAddChromatogram = QtGui.QAction(MainWindow)
        self.actionSubtractAddChromatogram.setEnabled(False)
        self.actionSubtractAddChromatogram.setObjectName(_fromUtf8("actionSubtractAddChromatogram"))
        self.actionRevert = QtGui.QAction(MainWindow)
        self.actionRevert.setEnabled(True)
        self.actionRevert.setObjectName(_fromUtf8("actionRevert"))
        self.actionEditFilters = QtGui.QAction(MainWindow)
        self.actionEditFilters.setObjectName(_fromUtf8("actionEditFilters"))
        self.actionSmoothChromatogram = QtGui.QAction(MainWindow)
        self.actionSmoothChromatogram.setObjectName(_fromUtf8("actionSmoothChromatogram"))
        self.actionAlign_Chromatogram = QtGui.QAction(MainWindow)
        self.actionAlign_Chromatogram.setObjectName(_fromUtf8("actionAlign_Chromatogram"))
        self.actionCalculate_Isotopic = QtGui.QAction(MainWindow)
        self.actionCalculate_Isotopic.setEnabled(False)
        self.actionCalculate_Isotopic.setObjectName(_fromUtf8("actionCalculate_Isotopic"))
        self.actionExport_Peak_List = QtGui.QAction(MainWindow)
        self.actionExport_Peak_List.setEnabled(False)
        self.actionExport_Peak_List.setObjectName(_fromUtf8("actionExport_Peak_List"))
        self.actionIdentify = QtGui.QAction(MainWindow)
        self.actionIdentify.setEnabled(False)
        self.actionIdentify.setObjectName(_fromUtf8("actionIdentify"))
        self.actionFiles = QtGui.QAction(MainWindow)
        self.actionFiles.setCheckable(True)
        self.actionFiles.setChecked(True)
        self.actionFiles.setObjectName(_fromUtf8("actionFiles"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setCheckable(True)
        self.actionSettings.setChecked(False)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionPeaks = QtGui.QAction(MainWindow)
        self.actionPeaks.setCheckable(True)
        self.actionPeaks.setChecked(True)
        self.actionPeaks.setObjectName(_fromUtf8("actionPeaks"))
        self.actionSpectra = QtGui.QAction(MainWindow)
        self.actionSpectra.setCheckable(True)
        self.actionSpectra.setChecked(True)
        self.actionSpectra.setObjectName(_fromUtf8("actionSpectra"))
        self.actionMethods = QtGui.QAction(MainWindow)
        self.actionMethods.setCheckable(True)
        self.actionMethods.setEnabled(False)
        self.actionMethods.setObjectName(_fromUtf8("actionMethods"))
        self.actionCompounds = QtGui.QAction(MainWindow)
        self.actionCompounds.setCheckable(True)
        self.actionCompounds.setEnabled(False)
        self.actionCompounds.setObjectName(_fromUtf8("actionCompounds"))
        self.actionAll_Items_as_CSV = QtGui.QAction(MainWindow)
        self.actionAll_Items_as_CSV.setObjectName(_fromUtf8("actionAll_Items_as_CSV"))
        self.actionLegend = QtGui.QAction(MainWindow)
        self.actionLegend.setCheckable(True)
        self.actionLegend.setObjectName(_fromUtf8("actionLegend"))
        self.actionIntegrateStatSlope = QtGui.QAction(MainWindow)
        self.actionIntegrateStatSlope.setCheckable(True)
        self.actionIntegrateStatSlope.setObjectName(_fromUtf8("actionIntegrateStatSlope"))
        self.actionIntegrateWavelet = QtGui.QAction(MainWindow)
        self.actionIntegrateWavelet.setCheckable(True)
        self.actionIntegrateWavelet.setChecked(False)
        self.actionIntegrateWavelet.setObjectName(_fromUtf8("actionIntegrateWavelet"))
        self.actionPeaksHide = QtGui.QAction(MainWindow)
        self.actionPeaksHide.setCheckable(True)
        self.actionPeaksHide.setObjectName(_fromUtf8("actionPeaksHide"))
        self.actionPeaksShow = QtGui.QAction(MainWindow)
        self.actionPeaksShow.setCheckable(True)
        self.actionPeaksShow.setObjectName(_fromUtf8("actionPeaksShow"))
        self.actionPeaksShowLabels = QtGui.QAction(MainWindow)
        self.actionPeaksShowLabels.setEnabled(False)
        self.actionPeaksShowLabels.setObjectName(_fromUtf8("actionPeaksShowLabels"))
        self.actionGraphFxnCollection = QtGui.QAction(MainWindow)
        self.actionGraphFxnCollection.setCheckable(True)
        self.actionGraphFxnCollection.setObjectName(_fromUtf8("actionGraphFxnCollection"))
        self.actionGraphMSMS = QtGui.QAction(MainWindow)
        self.actionGraphMSMS.setCheckable(True)
        self.actionGraphMSMS.setEnabled(False)
        self.actionGraphMSMS.setObjectName(_fromUtf8("actionGraphMSMS"))
        self.actionIntegrateSimple = QtGui.QAction(MainWindow)
        self.actionIntegrateSimple.setCheckable(True)
        self.actionIntegrateSimple.setChecked(True)
        self.actionIntegrateSimple.setEnabled(True)
        self.actionIntegrateSimple.setObjectName(_fromUtf8("actionIntegrateSimple"))
        self.actionGraphIRMS = QtGui.QAction(MainWindow)
        self.actionGraphIRMS.setCheckable(True)
        self.actionGraphIRMS.setObjectName(_fromUtf8("actionGraphIRMS"))
        self.actionFIA = QtGui.QAction(MainWindow)
        self.actionFIA.setCheckable(True)
        self.actionFIA.setObjectName(_fromUtf8("actionFIA"))
        self.actionCopy_Settings_from_Other_DB = QtGui.QAction(MainWindow)
        self.actionCopy_Settings_from_Other_DB.setObjectName(_fromUtf8("actionCopy_Settings_from_Other_DB"))
        self.actionTop_Trace = QtGui.QAction(MainWindow)
        self.actionTop_Trace.setCheckable(True)
        self.actionTop_Trace.setChecked(True)
        self.actionTop_Trace.setObjectName(_fromUtf8("actionTop_Trace"))
        self.actionTop_File_Vis_Traces = QtGui.QAction(MainWindow)
        self.actionTop_File_Vis_Traces.setCheckable(True)
        self.actionTop_File_Vis_Traces.setObjectName(_fromUtf8("actionTop_File_Vis_Traces"))
        self.actionTop_File_All_Traces = QtGui.QAction(MainWindow)
        self.actionTop_File_All_Traces.setCheckable(True)
        self.actionTop_File_All_Traces.setObjectName(_fromUtf8("actionTop_File_All_Traces"))
        self.actionTop_File_All_Isotopic = QtGui.QAction(MainWindow)
        self.actionTop_File_All_Isotopic.setCheckable(True)
        self.actionTop_File_All_Isotopic.setObjectName(_fromUtf8("actionTop_File_All_Isotopic"))
        self.actionSimple = QtGui.QAction(MainWindow)
        self.actionSimple.setCheckable(True)
        self.actionSimple.setChecked(True)
        self.actionSimple.setObjectName(_fromUtf8("actionSimple"))
        self.actionWavelet = QtGui.QAction(MainWindow)
        self.actionWavelet.setCheckable(True)
        self.actionWavelet.setObjectName(_fromUtf8("actionWavelet"))
        self.actionStatistical_Slope = QtGui.QAction(MainWindow)
        self.actionStatistical_Slope.setCheckable(True)
        self.actionStatistical_Slope.setObjectName(_fromUtf8("actionStatistical_Slope"))
        self.actionEvent = QtGui.QAction(MainWindow)
        self.actionEvent.setCheckable(True)
        self.actionEvent.setObjectName(_fromUtf8("actionEvent"))
        self.actionGraphFIA = QtGui.QAction(MainWindow)
        self.actionGraphFIA.setCheckable(True)
        self.actionGraphFIA.setObjectName(_fromUtf8("actionGraphFIA"))
        self.actionTwo_Pass_Peak_Find = QtGui.QAction(MainWindow)
        self.actionTwo_Pass_Peak_Find.setCheckable(True)
        self.actionTwo_Pass_Peak_Find.setEnabled(False)
        self.actionTwo_Pass_Peak_Find.setObjectName(_fromUtf8("actionTwo_Pass_Peak_Find"))
        self.actionIntegrate = QtGui.QAction(MainWindow)
        self.actionIntegrate.setObjectName(_fromUtf8("actionIntegrate"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setText(_fromUtf8(""))
        self.action.setObjectName(_fromUtf8("action"))
        self.actionColor_Scheme = QtGui.QAction(MainWindow)
        self.actionColor_Scheme.setObjectName(_fromUtf8("actionColor_Scheme"))
        self.actionPeak_Finder = QtGui.QAction(MainWindow)
        self.actionPeak_Finder.setObjectName(_fromUtf8("actionPeak_Finder"))
        self.actionIntegrator = QtGui.QAction(MainWindow)
        self.actionIntegrator.setObjectName(_fromUtf8("actionIntegrator"))
        self.actionGraph_Peaks_Found = QtGui.QAction(MainWindow)
        self.actionGraph_Peaks_Found.setCheckable(True)
        self.actionGraph_Peaks_Found.setObjectName(_fromUtf8("actionGraph_Peaks_Found"))
        self.actionGraph_Style = QtGui.QAction(MainWindow)
        self.actionGraph_Style.setObjectName(_fromUtf8("actionGraph_Style"))
        self.menuExport.addAction(self.actionExportChromatogram)
        self.menuExport.addAction(self.actionExportSpectra)
        self.menuExport.addAction(self.actionExportSelectedItems)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuIntegrand.addAction(self.actionTop_Trace)
        self.menuIntegrand.addAction(self.actionTop_File_Vis_Traces)
        self.menuIntegrand.addAction(self.actionTop_File_All_Isotopic)
        self.menuIntegrand.addAction(self.actionTop_File_All_Traces)
        self.menuChromatogram.addAction(self.actionIntegrate)
        self.menuChromatogram.addAction(self.actionPeak_Finder)
        self.menuChromatogram.addAction(self.actionTwo_Pass_Peak_Find)
        self.menuChromatogram.addAction(self.actionIntegrator)
        self.menuChromatogram.addAction(self.menuIntegrand.menuAction())
        self.menuChromatogram.addSeparator()
        self.menuChromatogram.addAction(self.actionAutoAlignChromatogram)
        self.menuChromatogram.addAction(self.actionEditFilters)
        self.menuChromatogram.addAction(self.actionRevert)
        self.menuSpectrum.addAction(self.actionSearch_Database)
        self.menuSpectrum.addAction(self.actionSave_to_Database)
        self.menuSpectrum.addAction(self.actionSequence)
        self.menuSpectrum.addAction(self.actionStructure)
        self.menuWindows.addAction(self.actionFiles)
        self.menuWindows.addAction(self.actionSettings)
        self.menuWindows.addAction(self.actionSpectra)
        self.menuWindows.addAction(self.actionMethods)
        self.menuWindows.addAction(self.actionCompounds)
        self.menuPeaks.addAction(self.actionPeaksHide)
        self.menuPeaks.addAction(self.actionPeaksShow)
        self.menuPeaks.addAction(self.actionPeaksShowLabels)
        self.menuExtras.addAction(self.actionGraph_Peaks_Found)
        self.menuExtras.addAction(self.actionGraphFxnCollection)
        self.menuExtras.addAction(self.actionGraphFIA)
        self.menuExtras.addAction(self.actionGraphIRMS)
        self.menuExtras.addAction(self.actionGraphMSMS)
        self.menuSettings.addAction(self.actionGraph_Style)
        self.menuSettings.addAction(self.actionLegend)
        self.menuSettings.addAction(self.actionColor_Scheme)
        self.menuSettings.addAction(self.menuPeaks.menuAction())
        self.menuSettings.addAction(self.menuExtras.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChromatogram.menuAction())
        self.menubar.addAction(self.menuSpectrum.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Aston", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuExport.setTitle(_translate("MainWindow", "Export", None))
        self.menuChromatogram.setTitle(_translate("MainWindow", "Chromatogram", None))
        self.menuIntegrand.setTitle(_translate("MainWindow", "Integrand", None))
        self.menuSpectrum.setTitle(_translate("MainWindow", "Spectrum", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuPeaks.setTitle(_translate("MainWindow", "Peaks", None))
        self.menuExtras.setTitle(_translate("MainWindow", "Extras", None))
        self.filesDockWidget.setWindowTitle(_translate("MainWindow", "Files", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Seach by Name", None))
        self.settingsDockWidget.setWindowTitle(_translate("MainWindow", "Settings", None))
        self.spectraDockWidget.setWindowTitle(_translate("MainWindow", "Spectra", None))
        self.methodDockWidget.setWindowTitle(_translate("MainWindow", "Methods", None))
        self.compoundDockWidget.setWindowTitle(_translate("MainWindow", "Compounds", None))
        self.actionOpen.setText(_translate("MainWindow", "Open Folder", None))
        self.actionExportChromatogram.setText(_translate("MainWindow", "Visible Chromatogram", None))
        self.actionChromatogram_as_CSV.setText(_translate("MainWindow", "Chromatogram as CSV", None))
        self.actionExportSpectra.setText(_translate("MainWindow", "Visible Spectra", None))
        self.actionSpectra_as_CSV.setText(_translate("MainWindow", "Spectra as CSV", None))
        self.actionExportSelectedItems.setText(_translate("MainWindow", "Selected Items", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionSearch_Database.setText(_translate("MainWindow", "Search Database", None))
        self.actionSave_to_Database.setText(_translate("MainWindow", "Save to Database", None))
        self.actionSequence.setText(_translate("MainWindow", "Sequence", None))
        self.actionStructure.setText(_translate("MainWindow", "Structure", None))
        self.actionCalculate_Info.setText(_translate("MainWindow", "Calculate Info", None))
        self.actionAutoAlignChromatogram.setText(_translate("MainWindow", "Auto-Align Chromatogram", None))
        self.actionSubtractAddChromatogram.setText(_translate("MainWindow", "Subtract/Add Chromatogram", None))
        self.actionRevert.setText(_translate("MainWindow", "Revert to Original", None))
        self.actionEditFilters.setText(_translate("MainWindow", "Edit Filters...", None))
        self.actionSmoothChromatogram.setText(_translate("MainWindow", "Smooth Chromatogram", None))
        self.actionAlign_Chromatogram.setText(_translate("MainWindow", "Adjust Chromatogram", None))
        self.actionCalculate_Isotopic.setText(_translate("MainWindow", "Calculate Isotopic", None))
        self.actionExport_Peak_List.setText(_translate("MainWindow", "Export Peak List", None))
        self.actionIdentify.setText(_translate("MainWindow", "Quick Identify", None))
        self.actionFiles.setText(_translate("MainWindow", "Files", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionPeaks.setText(_translate("MainWindow", "Peaks", None))
        self.actionSpectra.setText(_translate("MainWindow", "Spectra", None))
        self.actionMethods.setText(_translate("MainWindow", "Methods", None))
        self.actionCompounds.setText(_translate("MainWindow", "Compounds", None))
        self.actionAll_Items_as_CSV.setText(_translate("MainWindow", "All Items as CSV", None))
        self.actionLegend.setText(_translate("MainWindow", "Legend", None))
        self.actionIntegrateStatSlope.setText(_translate("MainWindow", "Drop", None))
        self.actionIntegrateWavelet.setText(_translate("MainWindow", "LeastSquares", None))
        self.actionPeaksHide.setText(_translate("MainWindow", "Hide", None))
        self.actionPeaksShow.setText(_translate("MainWindow", "Show", None))
        self.actionPeaksShowLabels.setText(_translate("MainWindow", "Show with Labels", None))
        self.actionGraphFxnCollection.setText(_translate("MainWindow", "Fxn Collection", None))
        self.actionGraphMSMS.setText(_translate("MainWindow", "MS-MS", None))
        self.actionIntegrateSimple.setText(_translate("MainWindow", "Simple", None))
        self.actionGraphIRMS.setText(_translate("MainWindow", "Gas Pulse (IRMS)", None))
        self.actionFIA.setText(_translate("MainWindow", "FIA", None))
        self.actionCopy_Settings_from_Other_DB.setText(_translate("MainWindow", "Load Settings from DB", None))
        self.actionTop_Trace.setText(_translate("MainWindow", "Top Trace", None))
        self.actionTop_File_Vis_Traces.setText(_translate("MainWindow", "Top File - Vis. Traces", None))
        self.actionTop_File_All_Traces.setText(_translate("MainWindow", "Top File - All Traces", None))
        self.actionTop_File_All_Isotopic.setText(_translate("MainWindow", "Top File - All (Isotopic)", None))
        self.actionSimple.setText(_translate("MainWindow", "Simple", None))
        self.actionWavelet.setText(_translate("MainWindow", "Wavelet", None))
        self.actionStatistical_Slope.setText(_translate("MainWindow", "StatSlope", None))
        self.actionEvent.setText(_translate("MainWindow", "Event", None))
        self.actionGraphFIA.setText(_translate("MainWindow", "Flow Injection", None))
        self.actionTwo_Pass_Peak_Find.setText(_translate("MainWindow", "Two Pass Peak Find", None))
        self.actionIntegrate.setText(_translate("MainWindow", "Integrate", None))
        self.actionColor_Scheme.setText(_translate("MainWindow", "Color Scheme", None))
        self.actionPeak_Finder.setText(_translate("MainWindow", "Peak Finder", None))
        self.actionIntegrator.setText(_translate("MainWindow", "Integrator", None))
        self.actionGraph_Peaks_Found.setText(_translate("MainWindow", "Peaks Found", None))
        self.actionGraph_Style.setText(_translate("MainWindow", "Graph Style", None))

