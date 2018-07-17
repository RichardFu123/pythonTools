'''
Created by Shawn on 2018/7/17
'''


from PIL import Image
import os.path
import glob


def convertImgSize(filename,outdir,width=128,height=128):
    img=Image.open(filename)
    try:
        new=img.resize((width,height),Image.BILINEAR)
        new.save(os.path.join(outdir,os.path.basename(filename)))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    for filename in glob.glob('./trainImage/*.png'):
        convertImgSize(filename,'./trainImage128')
