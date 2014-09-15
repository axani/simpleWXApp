import wx

class myButtonSubclass(wx.Button):
	def __init__(self, *args, **kwargs):
		wx.Button.__init__(self, *args, **kwargs)
		print 'Button loaded'