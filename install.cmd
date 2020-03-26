pyinstaller -F --noconsole ^
--add-binary dialogs/dialogs.pyd;dialogs ^
--add-binary dialogs/options.pyd;dialogs ^
--add-binary commands.pyd;. ^
--add-binary drawer.pyd;. ^
--add-binary menu.pyd;. ^
--add-binary version.pyd;. ^
--add-binary wxdb.pyd;. ^
--add-binary configs.pyd;. ^
--add-binary database.pyd;. ^
--add-binary linker.pyd;. ^
--add-binary player.pyd;. ^
--hidden-import wx ^
main.pyw
