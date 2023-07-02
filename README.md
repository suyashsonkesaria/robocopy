# Package py-robocopy

Copies files/data from one location to another.

## Description:
py-robocopy is a Python library that serves as a wrapper for Robocopy, a robust file copying and synchronization tool available in Windows. It provides a convenient and straightforward interface to interact with Robocopy commands and perform advanced file operations within your Python applications.

### Key Features:
- Seamless Integration: py-robocopy seamlessly integrates with your Python projects, enabling you to leverage the capabilities of Robocopy directly from your codebase.

- File Copying and Synchronization: The library simplifies file copying and synchronization tasks by utilizing Robocopy's powerful features. You can specify source and destination directories, define files to be copied, and control various copying options.

- Advanced Copying Options: py-robocopy supports a wide range of advanced options provided by Robocopy. This includes copying subdirectories, preserving file attributes and timestamps, handling retries on failed copies, and mirroring directory structures.

- Logging and Error Handling: The library offers built-in logging functionality, allowing you to track the progress of copying operations and save the output to log files. It also provides error-handling mechanisms to manage exceptions during the copying process.

- Platform Compatibility: While Robocopy is primarily a Windows utility, py-robocopy is designed to work seamlessly on Windows systems where Robocopy is available.

### Use Cases:

- Automating file backup and synchronization tasks within Python applications.
- Building data migration and replication tools that require efficient file copying.
- Developing file management utilities with advanced copying options.
- Integrating file synchronization functionality into custom scripts or workflows

### Install the library
`pip install py-robocopy`

## Usage

```
from RoboCopy import robocopy
robocopy.copy(<source-file-path>,<destination-file-path>,<options>)
```

## Examples

### Basic File Copy

```
from RoboCopy import robocopy
robocopy.copy("C:\\source_folder", "D:\\destination_folder")
```
This example demonstrates a basic file copy operation using robocopy. It copies all files and subdirectories from the source folder `C:\\source_folder` to the destination folder `D:\\destination_folder`.

###  File Copy with Options
```
from RoboCopy import robocopy

options = '/Z /R:3 /W:5'
robocopy.copy("C:\\source_folder", "D:\\destination_folder", options)
```
In this example, the `options` parameter is used to specify additional options for the copying operation. The `/Z` option enables restartable mode, allowing the copying process to be resumed in case of interruption. The `/R:3` option sets the number of retries on failed copies to 3, and the `/W:5` option sets the wait time between retries to 5 seconds.

## Syntax
`robocopy <source> <destination> [<file>[ ...]] [<options>]`

For example, to copy a file named yearly-report.mov from c:\reports to a file share \\marketing\videos while enabling multi-threading for higher performance (with the /mt parameter) and the ability to restart the transfer in case it's interrupted (with the /z parameter), type:
`robocopy c:\reports "\\marketing\videos" yearly-report.mov /mt /z`

For more details : https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy

## Parameters
### Parameter	Description
<table aria-label="Table 1" class="table table-sm">
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;source&gt;</code></td>
<td>Specifies the path to the source directory.</td>
</tr>
<tr>
<td><code>&lt;destination&gt;</code></td>
<td>Specifies the path to the destination directory.</td>
</tr>
<tr>
<td><code>&lt;file&gt;</code></td>
<td>Specifies the file or files to be copied. Wildcard characters (<strong>*</strong> or <strong>?</strong>) are supported. If you don't specify this parameter, <code>*.*</code> is used as the default value.</td>
</tr>
<tr>
<td><code>&lt;options&gt;</code></td>
<td>Specifies the options to use with the <strong>robocopy</strong> command, including <strong>copy</strong>, <strong>file</strong>, <strong>retry</strong>, <strong>logging</strong>, and <strong>job</strong> options.</td>
</tr>
</tbody>
</table>

## Copy options
<div class="has-inner-focus"><table aria-label="Table 2" class="table table-sm">
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>/s</td>
<td>Copies subdirectories. This option automatically excludes empty directories.</td>
</tr>
<tr>
<td>/e</td>
<td>Copies subdirectories. This option automatically includes empty directories.</td>
</tr>
<tr>
<td>/lev:<code>&lt;n&gt;</code></td>
<td>Copies only the top <em>n</em> levels of the source directory tree.</td>
</tr>
<tr>
<td>/z</td>
<td>Copies files in restartable mode. In restartable mode, should a file copy be interrupted, Robocopy can pick up where it left off rather than recopying the entire file.</td>
</tr>
<tr>
<td>/b</td>
<td>Copies files in backup mode allowing Robocopy to override file and folder permission settings (ACLs). This allow copying of files you might otherwise not have access to assuming it's being run under an account with sufficient privileges.</td>
</tr>
<tr>
<td>/zb</td>
<td>Copies files in restartable mode. If file access is denied, switches to backup mode.</td>
</tr>
<tr>
<td>/j</td>
<td>Copies using unbuffered I/O (recommended for large files).</td>
</tr>
<tr>
<td>/efsraw</td>
<td>Copies all encrypted files in EFS RAW mode.</td>
</tr>
<tr>
<td>/copy:<code>&lt;copyflags&gt;</code></td>
<td>Specifies which file properties to copy. The valid values for this option are:<ul><li><strong>D</strong> - Data</li><li><strong>A</strong> - Attributes</li><li><strong>T</strong> - Time stamps</li><li><strong>X</strong> - Skip alt data streams</li><li><strong>S</strong> - NTFS access control list (ACL)</li><li><strong>O</strong> - Owner information</li><li><strong>U</strong> - Auditing information</li></ul>The default value for the <strong>/COPY</strong> option is <strong>DAT</strong> (data, attributes, and time stamps). The <strong>X</strong> flag is ignored if either <strong>/B</strong> or <strong>/ZB</strong> is used.</td>
</tr>
<tr>
<td>/dcopy:<code>&lt;copyflags&gt;</code></td>
<td>Specifies what to copy in directories. The valid values for this option are:<ul><li><strong>D</strong> - Data</li><li><strong>A</strong> - Attributes</li><li><strong>T</strong> - Time stamps</li><li><strong>E</strong> - Extended attribute</li><li><strong>X</strong> - Skip alt data streams</li></ul>The default value for this option is <strong>DA</strong> (data and attributes).</td>
</tr>
<tr>
<td>/sec</td>
<td>Copies files with security (equivalent to <strong>/copy:DATS</strong>).</td>
</tr>
<tr>
<td>/copyall</td>
<td>Copies all file information (equivalent to <strong>/copy:DATSOU</strong>).</td>
</tr>
<tr>
<td>/nocopy</td>
<td>Copies no file information (useful with <strong>/purge</strong>).</td>
</tr>
<tr>
<td>/secfix</td>
<td>Fixes file security on all files, even skipped ones.</td>
</tr>
<tr>
<td>/timfix</td>
<td>Fixes file times on all files, even skipped ones.</td>
</tr>
<tr>
<td>/purge</td>
<td>Deletes destination files and directories that no longer exist in the source. Using this option with the <strong>/e</strong> option and a destination directory, allows the destination directory security settings to not be overwritten.</td>
</tr>
<tr>
<td>/mir</td>
<td>Mirrors a directory tree (equivalent to <strong>/e</strong> plus <strong>/purge</strong>). Using this option with the <strong>/e</strong> option and a destination directory, overwrites the destination directory security settings.</td>
</tr>
<tr>
<td>/mov</td>
<td>Moves files, and deletes them from the source after they're copied.</td>
</tr>
<tr>
<td>/move</td>
<td>Moves files and directories, and deletes them from the source after they're copied.</td>
</tr>
<tr>
<td>/a+:[RASHCNET]</td>
<td>Adds the specified attributes to copied files.  The valid values for this option are: <ul><li><strong>R</strong> - Read only</li><li><strong>A</strong> - Archive</li><li><strong>S</strong> - System</li><li><strong>H</strong> - Hidden</li><li><strong>C</strong> - Compressed</li><li><strong>N</strong> - Not content indexed</li><li><strong>E</strong> - Encrypted</li><li><strong>T</strong> - Temporary</li></ul></td>
</tr>
<tr>
<td>/a-:[RASHCNETO]</td>
<td>Removes the specified attributes from copied files. The valid values for this option are: <ul><li><strong>R</strong> - Read only</li><li><strong>A</strong> - Archive</li><li><strong>S</strong> - System</li><li><strong>H</strong> - Hidden</li><li><strong>C</strong> - Compressed</li><li><strong>N</strong> - Not content indexed</li><li><strong>E</strong> - Encrypted</li><li><strong>T</strong> - Temporary</li><li><strong>O</strong> - Offline</li></ul></td>
</tr>
<tr>
<td>/create</td>
<td>Creates a directory tree and zero-length files only.</td>
</tr>
<tr>
<td>/fat</td>
<td>Creates destination files by using 8.3 character-length FAT file names only.</td>
</tr>
<tr>
<td>/256</td>
<td>Turns off support for paths longer than 256 characters.</td>
</tr>
<tr>
<td>/mon:<code>&lt;n&gt;</code></td>
<td>Monitors the source and runs again when more than <em>n</em> changes are detected.</td>
</tr>
<tr>
<td>/mot:<code>&lt;m&gt;</code></td>
<td>Monitors the source and runs again in <em>m</em> minutes if changes are detected.</td>
</tr>
<tr>
<td>/rh:hhmm-hhmm</td>
<td>Specifies run times when new copies may be started.</td>
</tr>
<tr>
<td>/pf</td>
<td>Checks run times on a per-file (not per-pass) basis.</td>
</tr>
<tr>
<td>/ipg:<code>&lt;n&gt;</code></td>
<td>Specifies the inter-packet gap to free bandwidth on slow lines.</td>
</tr>
<tr>
<td>/sj</td>
<td>Copies junctions (soft-links) to the destination path instead of link targets.</td>
</tr>
<tr>
<td>/sl</td>
<td>Don't follow symbolic links and instead create a copy of the link.</td>
</tr>
<tr>
<td>/mt:<code>&lt;n&gt;</code></td>
<td>Creates multi-threaded copies with <em>n</em> threads. <em>n</em> must be an integer between 1 and 128. The default value for <em>n</em> is 8. For better performance, redirect your output using <strong>/log</strong> option.<p>The <strong>/mt</strong> parameter can't be used with the <strong>/ipg</strong> and <strong>/efsraw</strong> parameters.</p></td>
</tr>
<tr>
<td>/nodcopy</td>
<td>Copies no directory info (the default <strong>/dcopy:DA</strong> is done).</td>
</tr>
<tr>
<td>/nooffload</td>
<td>Copies files without using the Windows Copy Offload mechanism.</td>
</tr>
<tr>
<td>/compress</td>
<td>Requests network compression during file transfer, if applicable.</td>
</tr>
<tr>
<td>/sparse</td>
<td>Enables retaining sparse state during copy.</td>
</tr>
</tbody>
</table></div>

## File selection options
<div class="has-inner-focus"><table aria-label="Table 4" class="table table-sm">
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>/a</td>
<td>Copies only files for which the <strong>Archive</strong> attribute is set.</td>
</tr>
<tr>
<td>/m</td>
<td>Copies only files for which the <strong>Archive</strong> attribute is set, and resets the <strong>Archive</strong> attribute.</td>
</tr>
<tr>
<td>/ia:<code>[RASHCNETO]</code></td>
<td>Includes only files for which any of the specified attributes are set.  The valid values for this option are: <ul><li><strong>R</strong> - Read only</li><li><strong>A</strong> - Archive</li><li><strong>S</strong> - System</li><li><strong>H</strong> - Hidden</li><li><strong>C</strong> - Compressed</li><li><strong>N</strong> - Not content indexed</li><li><strong>E</strong> - Encrypted</li><li><strong>T</strong> - Temporary</li><li><strong>O</strong> - Offline</li></ul></td>
</tr>
<tr>
<td>/xa:<code>[RASHCNETO]</code></td>
<td>Excludes files for which any of the specified attributes are set. The valid values for this option are: <ul><li><strong>R</strong> - Read only</li><li><strong>A</strong> - Archive</li><li><strong>S</strong> - System</li><li><strong>H</strong> - Hidden</li><li><strong>C</strong> - Compressed</li><li><strong>N</strong> - Not content indexed</li><li><strong>E</strong> - Encrypted</li><li><strong>T</strong> - Temporary</li><li><strong>O</strong> - Offline</li></ul></td>
</tr>
<tr>
<td>/xf <code>&lt;filename&gt;[ ...]</code></td>
<td>Excludes files that match the specified names or paths. Wildcard characters (<strong>*</strong> and <strong>?</strong>) are supported.</td>
</tr>
<tr>
<td>/xd <code>&lt;directory&gt;[ ...]</code></td>
<td>Excludes directories that match the specified names and paths.</td>
</tr>
<tr>
<td>/xc</td>
<td>Excludes existing files with the same timestamp, but different file sizes.</td>
</tr>
<tr>
<td>/xn</td>
<td>Source directory files newer than the destination are excluded from the copy.</td>
</tr>
<tr>
<td>/xo</td>
<td>Source directory files older than the destination are excluded from the copy.</td>
</tr>
<tr>
<td>/xx</td>
<td>Excludes extra files and directories present in the destination but not the source. Excluding extra files won't delete files from the destination.</td>
</tr>
<tr>
<td>/xl</td>
<td>Excludes "lonely" files and directories present in the source but not the destination. Excluding lonely files prevents any new files from being added to the destination.</td>
</tr>
<tr>
<td>/im</td>
<td>Include modified files (differing change times).</td>
</tr>
<tr>
<td>/is</td>
<td>Includes the same files. Same files are identical in name, size, times, and all attributes.</td>
</tr>
<tr>
<td>/it</td>
<td>Includes "tweaked" files. Tweaked files have the same name, size, and times, but different attributes.</td>
</tr>
<tr>
<td>/max:<code>&lt;n&gt;</code></td>
<td>Specifies the maximum file size (to exclude files bigger than <em>n</em> bytes).</td>
</tr>
<tr>
<td>/min:<code>&lt;n&gt;</code></td>
<td>Specifies the minimum file size (to exclude files smaller than <em>n</em> bytes).</td>
</tr>
<tr>
<td>/maxage:<code>&lt;n&gt;</code></td>
<td>Specifies the maximum file age (to exclude files older than <em>n</em> days or date).</td>
</tr>
<tr>
<td>/minage:<code>&lt;n&gt;</code></td>
<td>Specifies the minimum file age (exclude files newer than <em>n</em> days or date).</td>
</tr>
<tr>
<td>/maxlad:<code>&lt;n&gt;</code></td>
<td>Specifies the maximum last access date (excludes files unused since <em>n</em>).</td>
</tr>
<tr>
<td>/minlad:<code>&lt;n&gt;</code></td>
<td>Specifies the minimum last access date (excludes files used since <em>n</em>) If <em>n</em> is less than 1900, <em>n</em> specifies the number of days. Otherwise, <em>n</em> specifies a date in the format YYYYMMDD.</td>
</tr>
<tr>
<td>/xj</td>
<td>Excludes junction points, which are normally included by default.</td>
</tr>
<tr>
<td>/fft</td>
<td>Assumes FAT file times (two-second precision).</td>
</tr>
<tr>
<td>/dst</td>
<td>Compensates for one-hour DST time differences.</td>
</tr>
<tr>
<td>/xjd</td>
<td>Excludes junction points for directories.</td>
</tr>
<tr>
<td>/xjf</td>
<td>Excludes junction points for files.</td>
</tr>
</tbody>
</table></div>

Robocopy, short for "Robust File Copy," is a command-line utility available in Windows operating systems. It is used for copying and synchronizing files and directories, and it offers more advanced features than the regular file copy command (copy or xcopy). Robocopy was first introduced with the Windows NT 4.0 Resource Kit and has since been included as a standard command-line tool in subsequent versions of Windows.

Robocopy is a powerful tool for advanced file copying and synchronization tasks, and it can be particularly useful when dealing with large file sets or when you need to maintain file attributes, timestamps, and NTFS permissions during the copying process.
