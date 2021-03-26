import numpy as np
import random
from PIL import ImageFont, ImageDraw, Image
from os import listdir
from os.path import isfile, join
import string
import uuid
import json
from config import OUTPATH


def file_list(mypath):
    onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def create_image(background,font,symbol,font_size,col,path):
    image = Image.open(background)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    image=image.resize((200,200))
    font_pil = ImageFont.truetype(font, font_size)
    ascent, descent = font_pil.getmetrics()   
    text_width = font_pil.getmask('A').getbbox()[2]
    text_height = ascent + descent+15
    a=(200-text_width)//2
    b=(200-text_height)//2
    #image=image.crop((2,2,20+text_width,20+text_height))
    draw=ImageDraw.Draw(image)
    draw.text((a,b),symbol,col,font=font_pil)
    image_id="img"+str(uuid.uuid4())
    im1=image.save(OUTPATH+"/out/imgs/"+image_id+".jpeg")
    data={}
    data['image']={
        'image_id':image_id,
        'character':symbol,
        'background':background[background.rfind('/')+1:],
        'font_style':font[font.rfind('/')+1:],
        'font_size':font_size,
        'font_color':col}
    with open(OUTPATH+"/out/json/" +image_id +'.json', 'w') as f:
        json.dump(data, f)

def generator(path):
	bgs=file_list(path+'/BG_PAPER')
	font_pack=file_list(path+'/font_files')
	font_colour=[(0,0,0),(25,25,25),(65,65,65)]
	font_sizes=range(5,116,10)
	#font_sizes=[15,55,115]   ###range(15,116,10)
	symbols=list(string.printable[:94])
	symbols.append(u"\u00A9")
	symbols.append(u"\u2122")
	symbol.append(" ")
    #symbols=['A','3','S','@']

	for k,font in enumerate(font_pack):
		for symbol in symbols:
			for font_size in font_sizes:
				for col in font_colour:	
					for background in bgs:	
						yield background,font,symbol,font_size,col
        print("Percent Completed : ",((k+1)/len(font_pack))*100)




