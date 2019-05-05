import numpy as np
import cv2
import imutils
from PIL import ImageGrab
from pyrobot import Robot
import os
import time
from sys import exit
from CustomErrors import TemplateNotFoundError, LargeImageNotFoundError
# FUNCTIONALITY : method to recognize a template image in a large image and return the cordinates.Method also takes threshold values to
#                 find the correct match
#TODO: can be modified later to add the offset values for the co-ordinates
def image_recog(template_image, threshold):
    im = ImageGrab.grab()
    im.save(os.getcwd()+r'/tmp/Screenshot.png','PNG')
    large_image = os.getcwd()+r'/tmp/Screenshot.png'
    template = cv2.imread(os.getcwd() + template_image)
    try:
        if template is None:
            raise TemplateNotFoundError(os.getcwd() + template_image)
    except TemplateNotFoundError, args:
        print 'ERROR:', args.msg
        exit(1)
    ##if template is None:
        ##print 'Template image not found'
        ##return -999,-999
    print 'LOG  [INFO]     : Template image found'
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    (tH, tW) = template.shape[:2]
    image = cv2.imread(large_image)
    if image is None:
        print 'Large image not found'
        return  -999,-999
    print 'LOG  [INFO]     : Large image found'
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None
    # loop over the scales of the image
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break
            # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
        #print 'Result of matchTemplate method:',result
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
    print found        
    (_, maxLoc, r) = found
    print 'Solution after looping:',_, maxLoc, r
    if _ >= threshold and r == 1:
        print 'LOG  [INFO]     : Template matched'
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
        #cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
        #cv2.namedWindow('Image', 2)
        #cv2.imshow("Image", image)
        #cv2.waitKey(0)
        center_x,center_y = (startX+endX)/2, (startY+endY)/2
        #os.remove(large_image)
        return (center_x,center_y)

    else:
        print 'Possiblity of Incorrect match, hence closing the function'
        #os.remove(large_image)
        return  -999,-999

#method to start a program with full path of the application
def start_program(path):
    robot = Robot()
    robot.start_program(path)
    maximize_window()

#method to move the mouse and double click on x,y coordinaties provided
def move_double_click_left(region_x,region_y):
    robot = Robot()
    robot.set_mouse_pos(region_x,region_y)
    robot.double_click_mouse(button='left')

#method to set the postion of mouse on that particular coordinates
def set_mouse_pos(region_x,region_y):
    robot = Robot()
    robot.set_mouse_pos(region_x,region_y)

def click_mouse(button):
    robot = Robot()
    robot.click_mouse(button)

# type string which sends a string of characters instead of single keys
def type_string(string,delay=0.005):
    robot = Robot()
    robot.type_string(string,delay)

# wait method with parameter as no. of seconds
def wait(seconds):
    time.sleep(seconds)

def show_desktop():
    robot = Robot()
    robot.key_press(91)
    robot.key_press(77)
    robot.key_release(77)
    robot.key_release(91)

def maximize_window():
    robot = Robot()
    robot.key_press(91)
    robot.key_press('up_arrow')
    robot.key_release('up_arrow')
    robot.key_release(91)

def key_press(key):
    robot = Robot()
    robot.key_press(key)

def key_release(key):
    robot = Robot()
    robot.key_release(key)

def ctrl_press(letter):
    robot = Robot()
    robot.ctrl_press(letter)

def find_img(template_image,threshold):
    im = ImageGrab.grab()
    im.save(os.getcwd()+r'/tmp/Screenshot.png','PNG')
    large_image = os.getcwd()+r'/tmp/Screenshot.png'
    template = cv2.imread(os.getcwd() + template_image)
    try:
        if template is None:
            raise TemplateNotFoundError(os.getcwd() + template_image)
    except TemplateNotFoundError, args:
        print 'ERROR:', args.msg
        exit(1)    
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    (tH, tW) = template.shape[:2]
    image = cv2.imread(large_image)
    if image is None:
        return  -999,-999
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None
    # loop over the scales of the image
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break
            # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
        #print 'Result of matchTemplate method:',result
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
    (_, maxLoc, r) = found
    if _ >= threshold and r == 1:        
        #os.remove(large_image)
        return True
    else:
        print 'Image To be Matched not Found'
        #os.remove(large_image)
        return  False

    