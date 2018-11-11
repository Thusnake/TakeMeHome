# import the pygame module, so you can use it
import pygame

FPS = 60
playtime = 0
 
def main():
   
  pygame.init()
  pygame.display.set_caption("minimal program")
   
  screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
   
  running = True
   
  # main loop
  while running:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
   
   
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
  # call the main function
  main()
