# Бібліотеки

from pygame import *

# Класи

class GameSprite(sprite.Sprite):
	def __init__(self):
		pass
	def reset(self):
		pass

class Player(GameSprite):
    def update_right(self):
        pass
    def update_left(self):
        pass

# Вікно

win_width = 600  # window width
win_height = 500 # window height

window = display.set_mode((win_width, win_height))
fil = (200, 255, 255)
window.fill(fil)

game = True
finish = False

clock = time.Clock() # Годинник
FPS = 60


while game:
	for e in event.get():
		if e.type == QUIT:
			game = False
	if finish != True:
		window.fill(backround)
	display.update()
	clock.tick(FPS)