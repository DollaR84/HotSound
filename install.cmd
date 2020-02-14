pyinstaller -F --noconsole ^
--add-binary api.pyd;. ^
--add-binary menu.pyd;. ^
--add-binary tree.pyd;. ^
--add-binary version.pyd;. ^
--hidden-import wx ^
main.pyw
