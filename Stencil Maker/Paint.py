import pygame, sys, random, json, time
from pygame.locals import *
import cv2
from button import MyButton
import pygame_textinput
import PyQt5
import random

#Tool Booleans Definition
global save
global load
global size
global fill
global colors

pygame.init()
def Fill(Surf, Point, Color):
    arr = pygame.surfarray.array3d(Surf)
    swapPoint = (Point[1], Point[0])
    cv2.floodFill(arr, None, swapPoint, Color)
    pygame.surfarray.blit_array(Surf, arr)

def colorButton(colors, rgb):
	drawColor = rgb
	colors = False
	return drawColor, False

def colorButtons(drawColor, colors):
	if redBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (255, 0, 0))
	elif orangeBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (255, 128, 0))
	elif yellowBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (255, 255, 0))
	elif greenBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (0, 255, 0))
	elif blueBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (0, 0, 255))
	elif purpleBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (102, 0, 204))
	elif whiteBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (255, 255, 255))
	elif blackBtn.rect.collidepoint(pygame.mouse.get_pos()) and colors == True:
		drawColor, colors = colorButton(colors, (0, 0, 0))
	return drawColor, colors

def saveCanvas(save):
	if save == True:
		pygame.draw.rect(screen,white,(900,12.5,500,25))
		saveinput.update(events)
		screen.blit(saveinput.get_surface(), (900, 12.5))
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN and save == True:
				rect = pygame.Rect(0, 150, screen.get_width(), screen.get_height() - 150)
				sub = screen.subsurface(rect)
				pygame.image.save(sub, f"{saveinput.input_string}.png")
				save = False
	return save

def loadCanvas(load):
	if load == True:
		pygame.draw.rect(screen,white,(900,12.5,500,25))
		saveinput.update(events)
		screen.blit(loadinput.get_surface(), (900, 12.5))
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN and load == True:
				pygame.draw.rect(screen,barColor,(0,0,screen.get_width(),150))
				image = pygame.image.load(f"{loadinput.input_string}.png")
				screen.blit(image, (0, 150))
				load = False
	return load

def sizePoint(size, width):
	if size == True:
		pygame.draw.rect(screen,white,(900,12.5,500,25))
		saveinput.update(events)
		screen.blit(loadinput.get_surface(), (900, 12.5))
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN and size == True:
				pygame.draw.rect(screen,barColor,(0,0,screen.get_width(),150))
				width = int(sizeinput.input_string)
				size = False
	return size, width

def fillSelected():
	if fill == True:
		if pygame.mouse.get_pressed() == (1,0,0):
			Fill(screen, pygame.mouse.get_pos(), drawColor)

def updateButtons():
	if colors == True:
		greenBtn.draw_button()
		redBtn.draw_button()
		orangeBtn.draw_button()
		yellowBtn.draw_button()
		blackBtn.draw_button()
		blueBtn.draw_button()
		purpleBtn.draw_button()
		whiteBtn.draw_button()

	sizeinput.update(events)
	loadinput.update(events)

	colorBtn.draw_button()
	clearBtn.draw_button()
	saveBtn.draw_button()
	loadBtn.draw_button()
	sizeBtn.draw_button()
	eraseBtn.draw_button()
	fillBtn.draw_button()
	quitBtn.draw_button()
	pygame.display.update()

def toolButtons(isSave, isLoad, isSize, isFill, isColors):
	global save
	global load
	global size
	global fill
	global colors
	if(isSave != "null"):
		save = isSave
	if(isLoad != "null"):
		load = isLoad
	if(isSize != "null"):
		size = isSize
	if(isFill != "null"):
		fill = isFill
	if(isColors != "null"):
		colors = isColors

def draw():
	if pygame.mouse.get_pressed() == (1,0,0):
		px, py = pygame.mouse.get_pos()
		pos = (px, py)
		dots.append(pos)
		if(len(dots) >= 2):
			pygame.draw.lines(screen, drawColor, False, dots, width)
	if pygame.mouse.get_pressed() == (0,0,0):
		dots.clear()
def tools(drawColor):
	global colors
	if pygame.mouse.get_pressed() == (1,0,0):
		if clearBtn.rect.collidepoint(pygame.mouse.get_pos()):
			screen.fill(backgroundColor)
			toolButtons(False, False, False, False, False)
		elif colorBtn.rect.collidepoint(pygame.mouse.get_pos()):
			toolButtons(False, False, False, False, True)
		elif saveBtn.rect.collidepoint(pygame.mouse.get_pos()):
			toolButtons(True, False, False, "null", False)
		elif loadBtn.rect.collidepoint(pygame.mouse.get_pos()):
			toolButtons(False, True, False, "null", False)
		elif sizeBtn.rect.collidepoint(pygame.mouse.get_pos()):
			toolButtons(False, False, True, False, False)
		elif eraseBtn.rect.collidepoint(pygame.mouse.get_pos()):
			drawColor = backgroundColor
			toolButtons(False, False, False, False, False)
		elif fillBtn.rect.collidepoint(pygame.mouse.get_pos()):
			toolButtons(False, False, False, True, False)
		elif quitBtn.rect.collidepoint(pygame.mouse.get_pos()):
			pygame.quit()
			sys.exit()
		drawColor, colors = colorButtons(drawColor, colors)
	return drawColor
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
drawColor = (0, 0, 0)
backgroundColor = (255, 255, 255)
barColor = (96, 96, 96) 

#Setup
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(backgroundColor)
pygame.display.flip()
pygame.display.set_caption("Stencil Maker")


#Drawing Vars
dots = []
width = 10

#Tool Buttons
colorBtn = MyButton(screen, "Color", 380, 25, 100, 50, 255, 128, 0)
clearBtn = MyButton(screen, "Clear", 270, 25, 100, 50, 255, 128, 0)
saveBtn = MyButton(screen, "Save", 50, 25, 100, 50, 255, 128, 0)
loadBtn = MyButton(screen, "Load", 160, 25, 100, 50, 255, 128, 0)
sizeBtn = MyButton(screen, "Size", 490, 25, 100, 50, 255, 128, 0)
eraseBtn = MyButton(screen, "Erase", 600, 25, 100, 50, 255, 128, 0)
fillBtn = MyButton(screen, "Fill", 710, 25, 100, 50, 255, 128, 0)
quitBtn = MyButton(screen, "Quit", 820, 25, 100, 50, 255, 128, 0)

#Color Buttons
greenBtn = MyButton(screen, "", 490, 80, 140, 50, 0, 255, 0)
yellowBtn = MyButton(screen, "", 350, 80, 140, 50, 255, 255, 0)
redBtn = MyButton(screen, "", 70, 80, 140, 50, 255, 0, 0)
orangeBtn = MyButton(screen, "", 210, 80, 140, 50, 255, 128, 0)
blueBtn = MyButton(screen, "", 630, 80, 140, 50, 0, 0, 255)
purpleBtn = MyButton(screen, "", 770, 80, 140, 50, 102, 0, 204)
blackBtn = MyButton(screen, "", 910, 80, 140, 50, 0, 0, 0)
whiteBtn = MyButton(screen, "", 1050, 80, 140, 50, 200, 200, 200)

#Inputs
sizeinput = pygame_textinput.TextInput()
loadinput = pygame_textinput.TextInput()
saveinput = pygame_textinput.TextInput()

#Tool Booleans Declaration
save = False
load = False
size = False
fill = False
colors = False

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		draw()
		drawColor = tools(drawColor)
	pygame.draw.rect(screen,barColor,(0,0,screen.get_width(),150))
	save = saveCanvas(save)
	load = loadCanvas(load)
	size, width = sizePoint(size, width)
	fillSelected()
	clock.tick(1000)
	updateButtons()
pygame.quit()