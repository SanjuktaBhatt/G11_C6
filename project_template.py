import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)

player=pygame.Rect(50,200,20,20)
#Use list comprehension to creata e lis of bricks for the wall


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C6")
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  #Create a for loop to draw each brick
  
  pygame.draw.rect(screen,DARKBLUE,player)
  pygame.display.flip()
pygame.quit()
