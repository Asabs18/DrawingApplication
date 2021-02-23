# REQUIRED REFERENCES:
import PySide2, RLPy, os
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.shiboken2 import wrapInstance

#------------------------------------------------
# A color dialog class
#------------------------------------------------
class myPickColorDialog:
    def __init__ (self, parent = None):
        # init class variables
        self.getSelectedColor_Color = None
        self.pickColor_dlg = None
        self.pyside_dialog = None
        self.color_dlg = None

        # create RL Dialog
        self.pickColor_dlg = RLPy.RUi.CreateRDialog()
        self.pickColor_dlg.SetWindowTitle("Select Color")
        self.pickColor_dlg.SetModal(True)
    
        # Wrap to PySide Dialog
        self.pyside_dialog = wrapInstance(int(self.pickColor_dlg.GetWindow()), QtWidgets.QDialog)
        self.pyside_dialog.setObjectName('myColorPicker')
        # get layout
        self.color_layout = self.pyside_dialog.layout()
        # create color dialog widget
        self.color_dlg = QColorDialog()
        #put border around just RL dialog window
        self.pyside_dialog.setStyleSheet("#myColorPicker {border :  1px solid gray}")
        # add widget to layout
        self.color_layout.addWidget(self.color_dlg)
        # connect signals
        self.color_dlg.colorSelected.connect(self.__getSelectedColor_selected)
        self.color_dlg.finished.connect(self.__getSelectedColor_finished)

    #---------------------------------------
    # executes on clicking OK to select a color
    #---------------------------------------
    def __getSelectedColor_selected(self,value):
        # save color selected
        self.getSelectedColor_Color = value
        # close RL dialog, done
        self.pickColor_dlg.Close()

    #---------------------------------------
    # executes when color dialog closes, not RL dialog
    #---------------------------------------
    def __getSelectedColor_finished(self,value):
        # close RL dialog, cancel
        self.pickColor_dlg.Close()

    #---------------------------------------
    # show color dialog and get color
    #---------------------------------------
    # Returns selected color or None on cancel
    #---------------------------------------
    def getSelectedColor(self, currColor = None):
        # set color to none for cancel
        self.getSelectedColor_Color = None
        if currColor is not None:
            self.color_dlg.setCurrentColor(currColor)
        # show dialog
        self.pyside_dialog.exec()
        # return selected color, or None if cancelled
        return self.getSelectedColor_Color
