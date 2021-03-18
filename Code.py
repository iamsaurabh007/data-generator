import numpy as np
import cv2
import random
from PIL import ImageFont, ImageDraw, Image
from os import listdir
from os.path import isfile, join
import string
import uuid
import json
from config import DOCPATH
path=DOCPATH #check

def file_list(mypath):
    onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

bgs=file_list(path+'/BG_PAPER')
font_pack=file_list(path+'/font_files')
font_colour=[(0,0,0),(20,20,20),(79,79,79)]
font_sizes=range(5,116,10)
symbols=list(string.printable[:94])
symbols.append(u"\u00A9")
symbols.append(u"\u2122")



def create_image(background,font,symbol,font_size,col):
    image = Image.open(background)
    font_pil = ImageFont.truetype(font, font_size)
    ascent, descent = font_pil.getmetrics()   
    text_width = font_pil.getmask('A').getbbox()[2]
    text_height = ascent + descent+15
    image=image.crop((2,2,20+text_width,20+text_height))
    draw=ImageDraw.Draw(image)
    draw.text((int(text_width/2)+5,int(ascent+3)),symbol,col,font=font_pil,anchor='ms')
    image_id="img"+str(uuid.uuid4())
    im1=image.save(path+"/out/"+image_id+".jpeg")
    data={}
    data['image']={
        'image_id':image_id,
        'character':symbol,
        'background':background[background.rfind('/')+1:],
        'font_style':font[font.rfind('/')+1:],
        'font_size':font_size,
        'font_color':col}
    with open(path+"/json/" +image_id +'.json', 'w') as f:
        json.dump(data, f)

def main():
	for background in bgs:
	    for font in font_pack:
	        for symbol in symbols:
	            for font_size in font_sizes:
	                for col in font_colour:
	                    #queue operation




if __name__ == '__main__':
	main()
