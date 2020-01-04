@echo off
cd c:\windows\system32

rem NOTE: These commands require administrator access.

NET stop spooler
NET start spooler
exit
