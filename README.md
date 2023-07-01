# Package robocopy

Copies file data from one location to another.

## Usage
### Import the library
`pip install py-robocopy`

## Syntax
`robocopy <source> <destination> [<file>[ ...]] [<options>]`

For example, to copy a file named yearly-report.mov from c:\reports to a file share \\marketing\videos while enabling multi-threading for higher performance (with the /mt parameter) and the ability to restart the transfer in case it's interrupted (with the /z parameter), type:
`robocopy c:\reports "\\marketing\videos" yearly-report.mov /mt /z`

For more details : https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy

## Parameters
### Parameter	Description
- `<source>`	Specifies the path to the source directory.
- `<destination>`	Specifies the path to the destination directory.
- `<file>`	Specifies the file or files to be copied. Wildcard characters (* or ?) are supported. If you don't specify this parameter, *.* is used as the default value.
- `<options>`	Specifies the options to use with the robocopy command, including copy, file, retry, logging, and job options.

