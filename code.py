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
    #image=image.resize((200,200))
    font_pil = ImageFont.truetype(font, font_size)
    ascent, descent = font_pil.getmetrics()  
    if symbol == ' ':
    	a=font_pil.getmask('-').getbbox()[2]
    else:
    	a=font_pil.getmask(symbol).getbbox()[2]   
    text_width = a
    text_height = ascent+descent
    text_width+=int(0.10*(text_width))
    text_height+=int(0.10*(text_height))
    image=image.resize((text_width+8,text_height))
    a=text_width//2
    b=ascent+int(0.05*(ascent))
    #image=image.crop((2,2,20+text_width,20+text_height))
    draw=ImageDraw.Draw(image)
    draw.text((4,b),symbol,col,font=font_pil,anchor="ls")
    #image.thumbnail([100,100], Image.ANTIALIAS)
    image_id="img"+str(uuid.uuid4())
    im1=image.save(OUTPATH+"/out/imgs/"+image_id+".jpeg")
    data={
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
    #font_sizes=range(15,116,10)
    font_sizes=[35,55,75,95,115]   ###range(15,116,10)
    symbols=list(string.printable[:94])
    symbols.append(u"\u00A9")
    symbols.append(u"\u2122")
    symbols.append(" ")
    #symbols=['A','g','I','@','`',"^"]

    # for k,font in enumerate(font_pack):
    #     for symbol in symbols:
    #         for font_size in font_sizes:
    #             for col in font_colour:
    #                 for background in bgs:
    #                     yield background,font,symbol,font_size,col
    #     print("Percent Completed : ",((k+1)/len(font_pack))*100)
        
    for k,font in enumerate(font_pack):
        for background in bgs:
            for font_size in font_sizes:
                for col in font_colour:
                    for symbol in symbols:
                        yield background,font,symbol,font_size,col
        print("Percent Completed : ",((k+1)/len(font_pack))*100)  

