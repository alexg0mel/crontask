import wx
from wx import html2


class MyApp(wx.App):

    def OnInit(self):
        WebFrame(None, "Surfing the Web").Show()
        return True


class WebFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        self._browser = html2.WebView.New(self)
        self._browser.LoadURL("https://www.google.com")  # home page

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._browser, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.Bind(html2.EVT_WEBVIEW_TITLE_CHANGED, self.OnTitle)

    def OnTitle(self, event):
        self.Title = event.GetString()


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
