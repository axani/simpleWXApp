import wx
import gui
from AppControls import myButtonSubclass

class MainFrame(gui.simpleWXAppWindow):
	
	def __init__(self, parent):
		# Create window frame
		# All gui-stuff is in gui.py
		gui.simpleWXAppWindow.__init__(self, parent)
		print 'App loaded'

	# Run this function when button is pressed
	def buttonAction(self, event):
		print 'Button clicked'