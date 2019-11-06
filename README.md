# ConferenceNameTags
A combination of Python and LaTeX to generate conference name tags smartly

The idea is, that when you have a conference with 50+ participants but you are doing the nametags by yourself (i.e. your gradstudents are) 
it would be nice if the nametags were printed in such a way that you can:
1) Take the printed stack of papers.
2) Cut the stack with a big cutter.
3) Place newly formed small stacks on top of each other.
4) Have the resulting stack in alphabethical order.

This combination of Python and Latex does just that if you do as follows
1) Get your list of participants in an excel file with their LastName, FirstName(, Affiliation) in sequential rows. 
2) Export the data to a namelist.csv with rows separated with commas.
3) Run Converter.py in the same folder, receive tags.tex -file. (If you need Affiliation, run ConverterTri.py)
4) Compile doc2.tex -file (or doc2Tri.tex) and get your nametags.

Notes:
-The outlook of your nametags can be controlled by editing the doc2.tex -file. 
-The ConverterTri.py and doc2Tri.tex -files are slightly modified versions of the standard ones, it would make sense
to have just one file with a parameter. (He said already in 2014 and never did it.)
-Python files by Rami Luisto, .tex -files originally by Jan Cristina but altered and commented by Rami Luisto.

