from buildhat import Motor, ForceSensor, ColorSensor, DistanceSensor
import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))

def text():
    pass

bullet_list = []

class ControlManagement:
    def __init__(self,player):
        self.motorcontrollerA = Motor("A")
        self.pushcontroller1 = ForceSensor("B")
        self.rgbPicker = ColorSensor("C")
        self.player = player
        self.distanceSensor = DistanceSensor("D")
        self.mode = 1
        self.pushcontroller1.when_pressed = self.player.shoot
        self.angleDistance = 0
        self.prevAngle = 0
     

    def update(self):
        angle = self.motorcontrollerA.get_position()
        self.angleDistance = angle - self.prevAngle
        self.prevAngle = angle
        self.player.color = self.rgbPicker.get_color()
        self.player.y += self.angleDistance
        for i in bullet_list:
            i.distance = self.distanceSensor.get_distance() / 5
        print(self.rgbPicker.get_color())
       
       
class Button:
    def __init__(self, x, y, width, height, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function

    def update(self):
        pass


class Bullet:
    def __init__(self, y, direction, distance=100):
        self.y = y
        self.distance = distance
        bullet_list.append(self)
        self.direction = direction
        self.x = 100 if direction == -1 else 500

    def update(self):
        if self.x > self.distance:
            bullet_list.remove(self)
            return
        else:
            self.x += self.direction /2

       

class Enemy:
    def __init__(self, x, y)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255,255,255)

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, 50, 100))
       

    def shoot(self):
        Bullet(self.y, -1)


player = Player(200, 200)
controlManagement = ControlManagement(player)

running = True
while running:
    window.fill((0,0,0))
    player.draw()
    for bullet in bullet_list:
        bullet.update()
    controlManagement.update()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

