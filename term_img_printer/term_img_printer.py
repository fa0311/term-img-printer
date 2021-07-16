from term_printer import ColorRGB, cprint
import cv2

def imgprint(file:str,ysize:int=1,xsize:int=1,output:str="  "):
    img = cv2.imread(file)
    height = img.shape[0]
    width = img.shape[1]
    for y in range(0, height, ysize):
        for x in range(0, width, xsize):
            imgBox = img[y, x]
            cprint(output, attrs=[ColorRGB(int(imgBox[2]), int(imgBox[1]), int(imgBox[0]), is_bg=True)], end="")
        print("")