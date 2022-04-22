import pygame
from pygame.locals import *
import numpy as np
import cv2
import sys
import joblib

import pygments 

# window size
WINDOWSIZEX = 640
WINDOWSIZEY = 400
BOUNDARY = 5
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

IMAGE_SAVE = False
MODEL = joblib.load('model')
# fonts
# FONT = pygame.font.Font("freesansbold.tff",18)

iswriting = False

number_xcord = []
number_ycord = []
image_cnt = 1
PREDICT = True

# pygame.display.set_caption('Digit Board')
# Initialize 
# pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode((WINDOWSIZEX,WINDOWSIZEY))


# while TRUE:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#         if event.type == MOUSEMOTION and  iswriting:
#             xcord,ycord = event.pos
#             pygame.draw.circle(DISPLAY_SURFACE,WHITE,(xcord,ycord),4,0)

#             number_xcord.append(xcord)
#             number_ycord.append(ycord)
        
#         if event.type == MOUSEBUTTONDOWN:
#             iswriting = True

        # if event.type == MOUSEBUTTONUP:
        #     iswriting = False
        #     number_xcord = sorted(number_xcord)
        #     number_ycord = sorted(number_ycord)

        #     rec_min_x ,rec_max_x = max(number_xcord[0] - BOUNDARY,0),min(WINDOWSIZEX, number_xcord[-1]+BOUNDARY)
        #     rec_min_y ,rec_max_y = max(number_ycord[0] - BOUNDARY,0),min(WINDOWSIZEX, number_ycord[-1]+BOUNDARY)
            

        #     number_xcord = []
        #     number_ycord = []

        #     img_arr = np.array(pygame.PixelArray(DISPLAY_SURFACE))[rec_min_x:rec_max_x,rec_min_y:rec_max_y].T.astype(np.float32)

            # if IMAGE_SAVE:
            #     cv2.imwrite("image.png")
            #     image_cnt += 1
            
            # if PREDICT:
            #     image = cv2.resize(img_arr,(28,28))
            #     image = np.pad(image,(10,10),'constant',constant_values=0)
            #     image = cv2.resize(image,(28,28))/255

            #     label = str(LABELS(np.argmax(MODEL.predict(image.reshape(1,28,28,1)))))