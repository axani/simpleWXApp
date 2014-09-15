import wx

class myButtonSubclass(wx.Button):

	# *args and **kwargs takes all the same argument as the standard window
	def __init__(self, *args, **kwargs):
		wx.Button.__init__(self, *args, **kwargs)
		print 'Button loaded'