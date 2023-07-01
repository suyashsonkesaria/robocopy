# Package robocopy

Syntax
robocopy <source> <destination> [<file>[ ...]] [<options>]

For example, to copy a file named yearly-report.mov from c:\reports to a file share \\marketing\videos while enabling multi-threading for higher performance (with the /mt parameter) and the ability to restart the transfer in case it's interrupted (with the /z parameter), type:
robocopy c:\reports "\\marketing\videos" yearly-report.mov /mt /z

For more details : https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy


