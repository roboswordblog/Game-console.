from buildhat import Motor
import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))

def text():
  pass

class ControlManagement:
  def __init__(self):
    self.motorcontrollerA = Motor("A")
    self.motorcontrollerB = Motor("B")
    self.pushController1 = None
    self.pushController2 = None
    self.mode = 1

class Button:
  pass


class WindowManage:
  def __init__(self):
    self.function = None

  def gameChoose(self):
  pass
  
  def pong(self):
    pass

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.display.update()


