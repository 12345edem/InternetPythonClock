import pygame
from pygame.locals import *
import os
import sys
import time
import ntplib
####################MAIN_FUNCTION##########################
def getTime():
	try:
		client = ntplib.NTPClient()
		response = client.request('pool.ntp.org')
		s = (time.strftime('%S',time.localtime(response.tx_time)))
		m = (time.strftime('%M',time.localtime(response.tx_time)))
		h = (time.strftime('%H',time.localtime(response.tx_time)))
		d = (time.strftime('%d',time.localtime(response.tx_time)))
		mn = (time.strftime('%m',time.localtime(response.tx_time)))
		y = (time.strftime('%Y',time.localtime(response.tx_time)))
		return s, m, h, d, mn, y
	except:
		print('Could not sync with time server.')
####################INITIALIZATION#########################
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode((200, 100), pygame.NOFRAME)
pygame.font.init()
font_color = (255, 255, 255)
font1 = pygame.font.Font("dg7.ttf", 40)
font2 = pygame.font.Font("dg7.ttf", 24)
font3 = pygame.font.Font("dg7.ttf", 20)
########################MAIN_LOOP#########################
while 1: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:           
			sys.exit()
	s, m, h, d, mn, y = getTime()
	smd = str(h) + ":" + str(m) + ":" + str(s)
	dmny = str(d) + "   " + str(mn) + "  " + str(y)
	smd_info = "hh     mm    ss"
	dmny_info = "d    mth    y"
	smd_text = font1.render(smd ,  True, font_color)
	dmny_text = font2.render(dmny , True, font_color)
	smd_info_text = font3.render(smd_info , True, font_color)
	dmny_info_text = font3.render(dmny_info , True, font_color)

	screen.fill((22, 22, 22))
	screen.blit(smd_text, (40, 20))
	screen.blit(dmny_text, (40, 60))
	screen.blit(smd_info_text, (50, 5))
	screen.blit(dmny_info_text, (45, 80))
	time.sleep(0.15)
	pygame.display.update()
