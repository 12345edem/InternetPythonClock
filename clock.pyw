import pygame
from pygame.locals import *
import sys
import time
import ntplib

err_v = 20#sec
####################MAIN_FUNCTION##########################
client = ntplib.NTPClient()
def getTime():
	try:
		response = client.request('pool.ntp.org')
		s = (time.strftime('%S',time.localtime(response.tx_time)))
		m = (time.strftime('%M',time.localtime(response.tx_time)))
		h = (time.strftime('%H',time.localtime(response.tx_time)))
		d = (time.strftime('%d',time.localtime(response.tx_time)))
		mn = (time.strftime('%m',time.localtime(response.tx_time)))
		y = (time.strftime('%Y',time.localtime(response.tx_time)))
		print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCONNECTION IS STABLE")
		return s, m, h, d, mn, y
	except:
		print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCOULD NOT SYNCH WITH THE TIME SERVER')
####################INITIALIZATION#########################
screen = pygame.display.set_mode((200, 100))
pygame.font.init()
font_color = (255, 255, 255)
font1 = pygame.font.Font("dg7.ttf", 40)
font2 = pygame.font.Font("dg7.ttf", 24)
font3 = pygame.font.Font("dg7.ttf", 20)

def check():
	try:
		s, m, h, d, mn, y = getTime()
		sr = int(s)
		hr = int(h)
		mr = int(m)
	except:
		pass
	return sr, mr , hr
########################MAIN_LOOP#########################
x = False
while x == False:
	try:
		s, m, h, d, mn, y = getTime()
		h_sys = int(h)
		m_sys = int(m)
		s_sys = int(s)
		x = True
	except:
		pass

i = 0
while 1: # main clock loop
	for event in pygame.event.get():
		if event.type == QUIT:           
			sys.exit()
	
	sys_time = s_sys + m_sys * 60 + h_sys * 60 * 60
	sys_time += 1
	i += 1
	if(i > err_v):
		s_sys, m_sys, h_sys = check()
		i = 0
		sys_time = s_sys + m_sys * 60 + h_sys * 60 * 60
	h_sys = sys_time // 3600
	m_sys = sys_time % 3600 // 60
	s_sys = sys_time % 3600 % 60

	#FORMAT TIME
	s_smd = str(s_sys)
	m_smd = str(m_sys)
	h_smd = str(h_sys)
	if s_sys < 10:
		s_smd = "0" + str(s_sys)
	if m_sys < 10:
		m_smd = "0" + str(m_sys)
	if h_sys < 10:
		h_smd = "0" + str(h_sys)

	smd = h_smd + ":" + m_smd + ":" + s_smd
	dmny = str(d) + "   " + str(mn) + "  " + str(y)
	smd_info = "hh   mm   ss"
	dmny_info = "d    mth     y"
	smd_text = font1.render(smd ,  True, font_color)
	dmny_text = font2.render(dmny , True, font_color)
	smd_info_text = font3.render(smd_info , True, font_color)
	dmny_info_text = font3.render(dmny_info , True, font_color)

	screen.fill((22, 22, 22))
	screen.blit(smd_text, (40, 20))
	screen.blit(dmny_text, (40, 60))
	screen.blit(smd_info_text, (50, 5))
	screen.blit(dmny_info_text, (45, 80))
	time.sleep(1)
	pygame.display.update()
