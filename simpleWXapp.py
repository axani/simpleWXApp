import wx
from MainFrame import MainFrame

# Debug mode for development
debug = True

def main():
	app = wx.App(redirect=False)
	window = MainFrame(None)
	app.SetTopWindow(window)

	if debug:
		from wx import py
		crust = py.crust.CrustFrame(window)
		del py
		crust.SetSize((750, 600))
		crust.Show(True)
		crust.shell.interp.locals['app'] = app
	
	window.Show()
	app.MainLoop()

# Only execute when run as main script (not when imported module) 
if __name__ == '__main__':
	main()