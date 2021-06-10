import os
from os import listdir
from os.path import isfile, join
import re

#PROCESS=58
#FILEPATH='/home/ubuntu/data-generator'
#OUTPATH='/home/ubuntu/data/ocr'
PROCESS=2
FILEPATH='/home/saurabhyadav007/Proj/data-generator'
OUTPATH='/home/saurabhyadav007/Proj/data/ocr'

#LINE_SOURCES
mypath="/home/saurabhyadav007/Proj/data/Lineleveldata/hindi_texts/"
filename=[]
lines=[]
listfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
for txtfile in listfiles:
    with open(txtfile, 'r') as f:
        for lines in f:
            lines.append(lines[:-1])

#FONT SIZES
font_sizes=[25]

#FONT COLOUR
font_colour=[(0,0,0)]
