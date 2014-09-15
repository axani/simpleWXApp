# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from AppControls import myButtonSubclass
import wx
import wx.xrc

###########################################################################
## Class simpleWXAppWindow
###########################################################################

class simpleWXAppWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 193,147 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.myButton = myButtonSubclass( self, wx.ID_ANY, u"ButtonLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxSizer.Add( self.myButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.myButton.Bind( wx.EVT_BUTTON, self.buttonAction )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buttonAction( self, event ):
		event.Skip()
	

