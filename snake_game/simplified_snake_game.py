import sys
import random 
import pygame


# screen size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# Food Class
class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (200, 0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0,GRID_HEIGHT-1) * GRID_SIZE)

    def draw(self, surface):
        food_image = pygame.image.load('snake_game/imgs/apple.png')
        food_image = pygame.transform.scale(food_image, (GRID_SIZE, GRID_SIZE))
        surface.blit(food_image, (self.position[0], self.position[1]))
        

# move
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake(object):
    def __init__(self):
        self.length = 1
        # set start point to center
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.color = (40,50,90)
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        pass
    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)
    
    # head for interact food
    def get_head(self):
        return self.positions[0]

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2) , (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        global score
        score = 0

    def turn(self, UDLR):
        #set direction
        if self.length > 1 and (UDLR[0]*-1, UDLR[1]*-1) == self.direction:
            return
        else:
            self.direction = UDLR
    
    def key_handling(self):
        for event in pygame.event.get():
            # If you click X button (quit button), then you exit the game
            # The exit button and logic not implemented yet
            # So once the X button is pressed, it is closed.
            if event.type == pygame.QUIT: # game exit
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN: # key input
                if event.key== pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
    
    def move(self):
        now = self.get_head()
        x, y = self.direction
        new = (((now[0] + (x*GRID_SIZE)) % SCREEN_WIDTH), (now[1] + (y*GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            # it means end of game
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
      
# draw Grid
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                # is 2nd parameter color?
                pygame.draw.rect(surface, (0, 0, 0), r)
            else:
                rr =pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (20, 20, 20), rr)


def main():
    # library initalize
    pygame.init()
    
    # make object trace time
    clock = pygame.time.Clock()

    # screen initalize
    #FULLSCREEN : 전체 화면 모드를 사용
    #HWSURFACE : 하드웨어 가속 사용. 전체 화면 모드에서만 가능
    #OPENGL : OpenGL 사용 가능한 디스플레이를 초기화
    #DOUBLEBUF : 더블 버퍼 모드를 사용. HWSURFACE or OPENGL에서 사용을 추천
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    
    # surface == 2D object / 색이나 이미지를 가지는 빈 시트
    surface = pygame.Surface(screen.get_size())
    
    # Surface to the same pixel format as the one you use for final display
    surface = surface.convert()
    drawGrid(surface)
    
    global score
    score = 0
    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("arial", 16, True, True)

    # Boolean value for End clause 
    running = True

    while(running):
        clock.tick(10)
        drawGrid(surface)
        
        snake.move()
        snake.key_handling()
        
        food.draw(surface)
        snake.draw(surface)
        
        if snake.get_head() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (255,255,255))
        screen.blit(text, (15,10))

        pygame.display.update()

main()