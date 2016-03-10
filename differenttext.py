#!/usr/bin/python
import difflib
text1="""text1:
aaaaaa
bbbbbb
tjjjj
uuyuuu
difflib document v7.4
add string
"""
text1_lines=text1.splitlines()
text2="""text2:
aaaaaa
bbbbbb
yijj
iytyu
difflib document v7.5
"""
text2_lines=text2.splitlines()

d=difflib.HtmlDiff()
#diff=d.compare(text1_lines,text2_lines)

print d.make_file(text1_lines,text2_lines)
