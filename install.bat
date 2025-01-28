@echo off
@robocopy "%~dp0\EOL_comments" "%programfiles%\EOL_comment_CLI" /e /v
reg query HKCU\environment /v path  | findstr /C:"%programfiles%\EOL_comment_CLI">nul && echo "already in path" || reg add HKCU\Environment\ /v Path /t REG_EXPAND_SZ /d "%path%;%programfiles%\EOL_comment_CLI"