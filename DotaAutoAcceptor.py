from lib.py_imageLib import *
from lib.CustomErrors import TemplateNotFoundError
import sys
print 'Running Dota Auto Acceptor'
print 'Press Ctrl+C to exit'
print 'Program will end after the game is accepted'
print 'You need to restart the program again for another game' 
while(True):
	#print find_img(r'/templates/Dota_Accept.JPG',0.7)
	if find_img(r'/templates/dotaIcon.JPG',0.7) == True:
		x,y = image_recog(r'/templates/dotaIcon.JPG',0.7)
		if (x,y) != (-999,-999):
			set_mouse_pos(x,y)
			click_mouse('left')
	if find_img(r'/templates/dotaIconOrng.JPG',0.7) == True:
		x,y = image_recog(r'/templates/dotaIconOrng.JPG',0.7)
	 	if (x,y) != (-999,-999):
	 		set_mouse_pos(x,y)
	 		click_mouse('left')
	#print find_img(r'/templates/dotaIcon.JPG',0.7) 
	#print find_img(r'/templates/dotaIconOrng.JPG',0.7)
	if find_img(r'/templates/Dota_Accept.JPG',0.7) == True:
		x,y = image_recog(r'/templates/Dota_Accept.JPG',0.7)
		if (x,y) != (-999,-999):
			set_mouse_pos(x,y)
			click_mouse('left')
			break
