import pynput
from PIL import Image, ImageFilter, ImageEnhance
from scipy.misc import imsave
import time
import linedraw

class ImageDrawer:
    def __init__(self, start_x, start_y):
        self.controller = pynput.mouse.Controller()
        self.start_x = start_x
        self.start_y = start_y
        self.is_pressed = False
        self.pre_line = None
        self.ratio = 1.0
    def drawLine(self,line):
        time.sleep(0.1)
        self.controller.press(pynput.mouse.Button.left)
        for k,point in enumerate(line[1:]):
            
            time.sleep(0.01)
            #self.controller.move(5,5)
            #print point[0]-line[k][0],point[1]-line[k][1]
            self.controller.move((point[0]-line[k][0])/self.ratio, (point[1]-line[k][1])/self.ratio)
            #time.sleep(0.5)
            
        self.controller.release(pynput.mouse.Button.left)
    def drawImage(self, path):
        lines = linedraw.sketch(path) 
        self.controller.position = (self.start_x, self.start_y)
        self.drawLine(lines[0])
        self.pre_line = lines[0]
        for line in lines[1:]:
            
            self.controller.move((line[0][0]-self.pre_line[-1][0])/self.ratio, (line[0][1]-self.pre_line[-1][1])/self.ratio)
            self.drawLine(line)
            self.pre_line = line

                    



if __name__ == '__main__':
    time.sleep(2)
    i = ImageDrawer(370,180)


    i.drawImage('images/5.jpg')
