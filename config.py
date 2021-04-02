#PROCESS=58
#FILEPATH='/home/ubuntu/data-generator'
#OUTPATH='/home/ubuntu/data/ocr'
PROCESS=2
FILEPATH='/home/saurabhyadav007/Proj/data-generator'
OUTPATH='/home/saurabhyadav007/Proj/data/ocr'
#SYMBOLS LIST
symbols=list(string.printable[:94])
symbols.append(u"\u00A9")
symbols.append(u"\u2122")
symbols.append(" ")

#FONT SIZES
font_sizes=range(15,116,10)

#FONT COLOUR
font_colour=[(0,0,0),(25,25,25),(65,65,65)]
