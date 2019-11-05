#!/usr/bin/python
# -*- coding: latin-1 -*-
# DO NOT TOUCH THE PREVIOUS TWO LINES!
# They make the "scandic letters" function properly.
# If you are having problems with the scandics, 
# try to change your file encodings to latin-1.
# (Or everything, including the above line,
# to utf-8.) If this does not work, roll into
# a ball and cry about how unfair life is.
"""
CONVERTER.PY:
This Converter rearranges and parses namelists.

Expected input:
List of names in the format of
"
Lastname1,Firstname1
Lastname2,Firstname2
...etc...
"
(You can export excel-files to this format
by saving them as .csv -files.)
Output:
List of strings of the form
"
...
"OUTPUTPRETEXT"+{LastnameN}{FirstnameN}
...
"

DESCRIPTION:
This script is for sorting a list of names
in order to create name tags
for a large event.
The output file is a .tex-file 
(tags.tex by default) called
by a main .tex-file (doc2.tex by default)
that creates name-tags from the namelist
file. The nametags should be created
n-per-page, where n is the variable
TAGSPERPAGE below, in a similar way every
page. With this program the thus created
nametags should be in such an order, that
cutting the printed pages all in one and
setting the piles on top of each other,
all the name tags should be in alphabetical order.
This script formats all names first to lowercase
and then recapitalizes them later on.

Below are variables named with ALL CAPITAL LETTERS.
They are meant to be modified by you if necessary
without needing to alter the actual code.

The actual sorting magic of this algorithm can be
found from "# TAG: Magic".




Written by: Rami Luisto
Original idea, C-version
and tex-files created by: Jan Cristina
"""

"""
TO DO: 

-smarter sorting
-handle scandinavian alphabets and turn them
into \"a etc for LaTeX-compatibility
-allow institution output for conference organizing
-make nameparsing more secure: 
look for  # (This part might be unstable for 
names like "Lars.droptable- Fuckswithyou---"")
"""


# Modifying the following two lines you can affect
# the input- and output files
# used when constructing the tag-lists.
# TAGSPERPAGE specifies how many name-tags
# are going to be used per page.
INPUTFILENAME = "namelist.csv"
OUTPUTFILENAME = "tags.tex"

# The following defines the amount of
# nametags to be fitted per page.
TAGSPERPAGE = 24

# The following is the text used in
# "fill-in" nametags needed. Leave empty ("")
# to create blankos or add a voiding-text 
# if needed.
FILLINTEXT = ""

# The following can be changed to alter
# the format of text printed to the output file.
# The with the default text "\confpin"
# the script will print the following kinds of lines:
# "\confpin{Lastname}{Firstname}".
# If you wish to alter this more fundamentally, see 
# lines below the comment "# TAG: File output text."
OUTPUTPRETEXT = "\confpin"


# If you are having problems with the script,
# replace "False" with "True" in the following
# line. This will make the script to print 
# out to terminal what it is doing. This should be helpful
# in figuring out if something is wrong.
DEBUG = False



#
# IF YOU DO NOT KNOW HOW TO PROGRAM,
# DO NOT TOUCH ANYTHING WRITTEN 
# BELOW!!!!
#

if DEBUG: print "Script is starting."

# Can't touch this.
# (We only use the 'math.floor' -function from 'math'.)
import math


# Opening the specified input- and output files
# in read- ("r") and write ("w") modes, respectively.
namefile = open(INPUTFILENAME,"r")
if DEBUG: print "Input file opened OK."
outputfile = open(OUTPUTFILENAME,"w")
if DEBUG: print "Output file opened OK."

# Reading the file to a list, the 'splitlines()'
# -function breaks the contents 'namefile.read()'
# of the input file 'namefile' to list entries
# based on newlines.
namelist_raw = namefile.read().splitlines()
if DEBUG: print "Read file to list."

# Creating a list of names by appending
# non-empty lines of 'namelist_raw'
# to our new list 'namelist'
# and changing everything to
# lowercase for easier sorting.
namelist = []
for j in range(len(namelist_raw)):
    if namelist_raw[j] != '':
        namelist.append(namelist_raw[j].lower())
if DEBUG: print "Removed empty lines and transformed to lower case."

# Sorting list. This sorting does not function
# properly if the names are not in lower case.
namelist = sorted(namelist)
if DEBUG: print "List of names sorted."

# Appending fill-in tags. (Used for printing the tags,
# basically we want the number of name tags to equal the number
# of pages times the number of name tags per page.)
for j in range(TAGSPERPAGE - (len(namelist) % TAGSPERPAGE)):
    namelist.append(FILLINTEXT)
if DEBUG: print "Empty tags appended."

# Separating first and last names to own lists.
# The program assumes that last name and first name
# are separated by a comma ','.
namelist_first = []
namelist_last = []
for j in range(len(namelist)):
    namelist_first.append(namelist[j].partition(",")[2])
    namelist_last.append(namelist[j].partition(",")[0])
if DEBUG: print "First and last names separated to own lists."

# Name parsing:
# Removing extra whitespace and capitalizing 
# first and last names.
if DEBUG: print "Beginning name parsing: removing extra whitespace and capitilizing."
for j in range(len(namelist)):
    # Parsing first name:
    # Stripping whitespace from the beginning and end of a name.
    if DEBUG: print "Parsing first name %s, removing whitespace." % namelist_first[j]
    namelist_first[j] = namelist_first[j].strip()
    # Capitalizing first letter of string.
    if DEBUG: print "Parsing first name %s, capitilizing first letter" % namelist_first[j]
    namelist_first[j] = namelist_first[j].capitalize()
    # Checking for dashes and spaces to capitalize second part of name.
    # (This part might be unstable for names like "Lars.droptable- Fuckswithyou---"")
    for i in range(len(namelist_first[j])):
        if DEBUG: print "Parsing first name %s, checking for dashes or spaces at index %d." % (namelist_first[j],i)
        if (namelist_first[j][i] == "-") or (namelist_first[j][i] == " "):
            if DEBUG: print "Parsing first name %s, found dash or whitespace at %d, capitilizing letter at %d." % (namelist_first[j],i,i+1)
            namelist_first[j] = namelist_first[j][:i+1] + namelist_first[j][i+1].upper() + namelist_first[j][i+2:]

    # Parsing last name:
    # Stripping whitespace from the beginning and end of a name.
    if DEBUG: print "Parsing last name %s, removing whitespace." % namelist_first[j]
    namelist_last[j] = namelist_last[j].strip()
    # Capitalizing first letter of string.
    if DEBUG: print "Parsing last name %s, capitilizing first letter" % namelist_first[j]
    namelist_last[j] = namelist_last[j].capitalize()
    # Checking for dashes to capitalize second part of name.
    # (This part might be unstable for names like "Lars.droptable- Fuckswithyou---"")
    for i in range(len(namelist_last[j])):
        if DEBUG: print "Parsing last name %s, checking for dashes or spaces at index %d." % (namelist_first[j],i)
        if (namelist_last[j][i] == "-" ) or (namelist_last[j][i] == " "):
            if DEBUG: print "Parsing lasst name %s, found dash or whitespace at %d, capitilizing letter at %d." % (namelist_first[j],i,i+1)
            namelist_last[j] = namelist_last[j][:i+1] + namelist_last[j][i+1].upper() + namelist_last[j][i+2:]
if DEBUG: print "Nameparsing success!"


# Next we rearrange the names to the needed form.
# 'pages' is the number of pages to be printed
pages = math.ceil(len(namelist)/TAGSPERPAGE)
if DEBUG: print "Number of pages counted."


# Fill the future sorted lists with empty strings
# so that we can access these lists by any index
# in range(len(namelist))
arranged_list_first = [""] * len(namelist)
arranged_list_last = [""] * len(namelist)
if DEBUG: print "Empty lists created for holding the sorted namelists."

# TAG: Magic
# THIS IS WHERE THE MAGIC HAPPENS.
# For each j the number
# (j % pages)*TAGSPERPAGE +  math.floor(j / pages)
# gives the correct position where it should be in the arranged list.
# The first term, "(j % pages)*TAGSPERPAGE", tells the place of name
# "name[j]" in page the number "math.floor(j / pages)".
if DEBUG: print "Magic starting..."
for j in range(len(namelist)):
    arranged_list_first[int((j % pages)*TAGSPERPAGE +  math.floor(j / pages))] = namelist_first[j]
    arranged_list_last[int((j % pages)*TAGSPERPAGE +  math.floor(j / pages))] = namelist_last[j]
if DEBUG: print "Magic success!"

# TAG: File output text.
# Writing the arranged list to the output file.
for j in range(len(arranged_list_first)):
    line = OUTPUTPRETEXT + "{%s}{%s}\n" % (str(arranged_list_first[j]),str(arranged_list_last[j]))
    outputfile.write(line)
if DEBUG: print "Wrote list to output."

# Closing all files.
namefile.close()
outputfile.close()

if DEBUG: print "Files closed."
if DEBUG: print "Quitting..."
