
import wx
import os
import wx.aui

g_FrameName = "TOOLWIN"
g_Version = "1.0.0"

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, g_FrameName, size = (1024, 768))
		
		self.InitMenu()
		
		self.m_AuiMgr = wx.aui.AuiManager(self)
		
		self.m_LeftPanel = wx.Panel(self, size = (400, 768))
		self.m_LeftSizer = wx.BoxSizer(wx.VERTICAL) 
		self.m_LeftPanel.SetSizer(self.m_LeftSizer)
		
		auiInfo = wx.aui.AuiPaneInfo()
		auiInfo.Left()
		auiInfo.CloseButton(False)
		auiInfo.Caption("left panel")
		self.m_AuiMgr.AddPane(self.m_LeftPanel, auiInfo)
		
		auiInfo = wx.aui.AuiPaneInfo()
		auiInfo.Centre()
		auiInfo.CloseButton(False)
		auiInfo.Caption("right panel")
		self.m_RightPanel = wx.Panel(self, size = (824, 768))
		self.m_AuiMgr.AddPane(self.m_RightPanel, auiInfo)
		
		'''
		self.m_TopPanel = wx.Panel(self)
		self.m_AuiMgr.AddPane(self.m_TopPanel, wx.aui.AuiPaneInfo().Top())
		
		self.m_BottomPanel = wx.Panel(self)
		self.m_AuiMgr.AddPane(self.m_BottomPanel, wx.aui.AuiPaneInfo().Bottom())
		'''
		
		self.CreateStatusBar()
		self.SetStatusText("hello status bar")
		self.CreateFileTree()
		
		self.m_AuiMgr.Update() 
		
	def __del__(self):
		self.m_AuiMgr.UnInit()
		
	## create menu and callback function
	def InitMenu(self):
		self.m_MenuBar = wx.MenuBar()
		self.m_FileMenu = wx.Menu()
		
		itemOpen = self.m_FileMenu.Append(-1, "&Open")
		self.Bind(wx.EVT_MENU, self.OnOpen, itemOpen)
		
		itemExit = self.m_FileMenu.Append(-1, "&Exit")
		self.Bind(wx.EVT_MENU, self.OnClose, itemExit)
		
		self.m_MenuBar.Append(self.m_FileMenu, "&File")
		self.SetMenuBar(self.m_MenuBar)
		
	def OnClose(self, event):
		print "OnClose Callback!"
	
	def OnOpen(self, event):
		print "OnOpen Callback!"
		wildcard = "Python source (*.py)|*.py|" \
			"Compiled Python (*.pyc)|*.pyc|" \
			"All files (*.*)|*.*"
		
		dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), 
				"", wildcard, wx.FD_OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			print dialog.GetPath() 
		dialog.Destroy()
		
	## create tree ctrl and callback function
	def CreateFileTree(self):
		imageList = wx.ImageList(16, 16)
		
		self.m_FldrIdx = imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
		self.m_FldrOpenIdx = imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, (16, 16)))
		self.m_FileIdx = imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
		
		self.m_FileTree = wx.TreeCtrl(self.m_LeftPanel)
		self.m_LeftSizer.Add(self.m_FileTree, 1, wx.ALL | wx.EXPAND) 
		self.m_FileTree.AssignImageList(imageList)
		
		self.m_FileTreeRoot = self.m_FileTree.AddRoot("hello")
		self.m_FileTree.SetItemImage(self.m_FileTreeRoot, self.m_FldrIdx, wx.TreeItemIcon_Normal)
		self.m_FileTree.SetItemImage(self.m_FileTreeRoot, self.m_FldrOpenIdx, wx.TreeItemIcon_Expanded)
		
		item1= self.m_FileTree.AppendItem(self.m_FileTreeRoot, "test1")
		self.m_FileTree.SetItemImage(item1, self.m_FldrIdx, wx.TreeItemIcon_Normal)
		self.m_FileTree.SetItemImage(item1, self.m_FldrOpenIdx, wx.TreeItemIcon_Expanded)
		
		for i in range(1, 50):
			item = self.m_FileTree.AppendItem(item1, "hello %d" % i)
			self.m_FileTree.SetItemImage(item, self.m_FileIdx, wx.TreeItemIcon_Normal)
	
		self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.m_FileTree)
		self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed, self.m_FileTree)
		self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.m_FileTree)
		#self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated, self.m_FileTree)
		#self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.OnItemExpanding, self.m_FileTree)
		
		self.m_FileTree.Expand(self.m_FileTreeRoot)
	
	def OnItemExpanded(self, event):
		print "OnItemExpanded:   ", self.m_FileTree.GetItemText(event.GetItem())
		
	def OnItemCollapsed(self, event):
		print "OnItemCollapsed:   ", self.m_FileTree.GetItemText(event.GetItem())
	
	def OnSelChanged(self, event):
		print "OnSelChanged:   ", self.m_FileTree.GetItemText(event.GetItem())
		
	def OnActivated(self, event):
		print "OnActivated:   ", self.m_FileTree.GetItemText(event.GetItem())
		
	def OnItemExpanding(self, event):
		print "OnItemExpanding:   ", self.m_FileTree.GetItemText(event.GetItem())
	
if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
