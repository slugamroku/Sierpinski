import pygame

canvas_width = 800
canvas_height = 800
bg_color = (0, 0, 0)
line_color = (255, 0, 0)

class Triangle():
    def __init__(self, starting_point, width, height, setpoint_level, parent_level):
        self.starting_point = starting_point
        self.width = width
        self.height = height
        self.setpoint_level = setpoint_level
        self.parent_level = parent_level

        self.actual_level = parent_level +1
        
        self.vertex1 = self.starting_point
        self.vertex2 = (self.starting_point[0]+self.width, self.starting_point[1])
        self.vertex3 = (self.starting_point[0]+self.width//2, self.starting_point[1]+self.height)

    def draw(self):
        pygame.draw.line(gameDisplay, line_color, self.vertex1, self.vertex2, 1)
        pygame.draw.line(gameDisplay, line_color, self.vertex2, self.vertex3, 1)
        pygame.draw.line(gameDisplay, line_color, self.vertex3, self.vertex1, 1)
        self.divide()

    def divide(self):
        if self.actual_level <= self.setpoint_level:
            self.child1 = Triangle(self.starting_point, self.width//2, self.height//2, self.setpoint_level, self.actual_level)
            self.child2 = Triangle((self.starting_point[0]+self.width//2, self.starting_point[1]), self.width//2, self.height//2, self.setpoint_level, self.actual_level)
            self.child3 = Triangle((self.starting_point[0]+self.width//4, self.starting_point[1]+self.height//2), self.width//2, self.height//2, self.setpoint_level, self.actual_level)
            self.child1.draw()
            self.child2.draw()
            self.child3.draw()

pygame.init()

gameDisplay = pygame.display.set_mode((canvas_width, canvas_height))
gameDisplay.fill(bg_color)

base = Triangle((0, 0), canvas_width, canvas_height, 10, 0)
base.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
