import pygame
from constants import *

def main():
  print("Starting asteroids!")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print("You have closed the window, quiting asteroids.")
        running = False
    
    screen.fill("black")

    # render your game

    # flip() the display to put your work on screen
    pygame.display.flip() # refreshes screen
    clock.tick(60) # limits to 60fps

if __name__ == "__main__":
  main()