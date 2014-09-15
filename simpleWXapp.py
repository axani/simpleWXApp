import wx
from MainFrame import MainFrame

# Debug mode for development
debug = False

def main():
	app = wx.App(redirect=False)
	window = MainFrame(None)
	app.SetTopWindow(window)
	
	window.Show()
	app.MainLoop()

# Only execute when run as main script (not when imported module) 
if __name__ == '__main__':
	main()