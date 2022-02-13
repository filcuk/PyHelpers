# Count lines in all open documents
# https://community.notepad-plus-plus.org/topic/199/how-to-count-the-whole-project-code-lines/3?_=1644760743626&lang=en-GB

from Npp import *
all_files_line_count = 0
tuple_list = notepad.getFiles()
for tuple in tuple_list:
    filename = tuple[0]
    if filename == "new  0": continue
    notepad.activateFile(filename)
    this_files_line_count = editor.getLineCount()
    all_files_line_count += this_files_line_count
notepad.messageBox("The total line count of all open files is: " + str(all_files_line_count), "", MESSAGEBOXFLAGS.OK)