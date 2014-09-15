import wx
import gui
from AppControls import myButtonSubclass

class MainFrame(gui.simpleWXAppWindow):
	
	def __init__(self, parent):
		gui.simpleWXAppWindow.__init__(self, parent)
		print 'App loaded'

	def buttonAction(self, event):
		print 'Button clicked'