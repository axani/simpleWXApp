import wx

class myButtonSubclass(wx.Button):
	def __init__(self, parent,
			id = wx.ID_ANY, 
			label = u"ButtonLabel", 
			pos = wx.DefaultPosition, 
			size = wx.DefaultSize, 
			proportion = 0):
		wx.Button.__init__(self, parent, id, label, pos, size, proportion)
		print 'Button loaded'