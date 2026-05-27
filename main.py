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

  def getMotor1(self):
    return self.motorcontrollerA.get_position()

  def getMotor2(self):
    return self.motorcontrollerA.get_position()
  
  def getPush1(self):
    if self.pushcontroller1 > 50:
      return True
    return False
    
  def getPush2(self):
    if self.pushcontroller2 > 50:
      return True
    return False
    
class Button:
  def __init__(self, x, y, width, height, text, bgColor, textColor, function=None, hoverColor=None):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.bgColor = bgColor
    self.textColor = textColor
    self.hoverColor = hoverColor
    self.function = function
  
  def draw(self):
    # complete this later
    pygame.draw.rect()
    # add the text here

  def update(self):
    mousex, mousey = pygame.mouse.get_pos()
    if self.x > mousex > self.x + self.width and self.y > mousey > self.y+height:
      pass
      # add hover and call function

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


