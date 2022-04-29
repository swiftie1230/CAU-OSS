import pygame
import random 
import time
import sys

# screen size
SCREEN_SIZE = 800

GRID_SIZE = 20
GRID_NUM = SCREEN_SIZE / GRID_SIZE

pygame.init()

white = (255, 255, 255)

titleImg = pygame.image.load("snake_game/imgs/title.png")
startImg = pygame.image.load("snake_game/imgs/starticon.png")
quitImg = pygame.image.load("snake_game/imgs/quiticon.png")
clickStartImg = pygame.image.load("snake_game/imgs/clickedStartIcon.png")
clickQuitImg = pygame.image.load("snake_game/imgs/clickedQuitIcon.png")

display_size = 800
gameDisplay = pygame.display.set_mode((display_size, display_size))
pygame.display.set_caption("Hello CAU_OSS Snake Game!")

clock = pygame.time.Clock()

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()


def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (210,310))
        startButton = Button(startImg,290,420,60,20,clickStartImg,250,418,main)
        quitButton = Button(quitImg,440,420,60,20,clickQuitImg,440,418,quitgame)
        pygame.display.update()
        clock.tick(15)

# Food Class
class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (200, 0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_NUM-1) * GRID_SIZE, random.randint(0,GRID_NUM-1) * GRID_SIZE)

    def draw(self, surface):
        food_image = pygame.image.load("snake_game/imgs/apple.png")
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
        self.positions = [((SCREEN_SIZE / 2), (SCREEN_SIZE / 2))]
        self.color = (40,50,90)
        self.directions = [random.choice([UP, DOWN, LEFT, RIGHT])]
        pass
    
    def draw(self, surface):
        for i in range(len(self.positions)):
            if i == 0:
                if len(self.positions) == 1:
                    snake_head_image = pygame.image.load('snake_game/imgs/snake_head.png')
                else:
                    snake_head_image = pygame.image.load('snake_game/imgs/snake_head1.png')
                snake_head_image = pygame.transform.scale(snake_head_image, (GRID_SIZE, GRID_SIZE))
                if self.directions[i] == UP:
                    rotate = 180
                elif self.directions[i] == DOWN:
                    rotate = 0
                elif self.directions[i] == LEFT:
                    rotate = 270
                elif self.directions[i] == RIGHT:
                    rotate = 90
                snake_head_image = pygame.transform.rotate(snake_head_image, rotate)
                surface.blit(snake_head_image, (self.positions[i][0], self.positions[i][1]))
            elif i == len(self.positions) - 1:
                snake_tail_image = pygame.image.load('snake_game/imgs/snake_tail.png')
                snake_tail_image = pygame.transform.scale(snake_tail_image, (GRID_SIZE, GRID_SIZE))
                if self.directions[i] == UP:
                    rotate = 180
                elif self.directions[i] == DOWN:
                    rotate = 0
                elif self.directions[i] == LEFT:
                    rotate = 270
                elif self.directions[i] == RIGHT:
                    rotate = 90
                snake_tail_image = pygame.transform.rotate(snake_tail_image, rotate)
                surface.blit(snake_tail_image, (self.positions[i][0], self.positions[i][1]))
            else:
                r = pygame.Rect((self.positions[i][0], self.positions[i][1]), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, (93,216, 228), r, 1)
    
    # head for interact food
    def get_head(self):
        return self.positions[0]

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_SIZE / 2) , (SCREEN_SIZE / 2))]
        self.directions = [random.choice([UP, DOWN, LEFT, RIGHT])]
        global score
        score = 0

    def turn(self, UDLR):
        #set directions
        if self.length > 1 and (UDLR[0]*-1, UDLR[1]*-1) == self.directions[0]:
            return
        else:
            self.directions[0] = UDLR

    
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
        x, y = self.directions[0]
        new = (((now[0] + (x*GRID_SIZE)) % SCREEN_SIZE), (now[1] + (y*GRID_SIZE)) % SCREEN_SIZE)
        if len(self.positions) > 2 and new in self.positions[2:]:
            # it means end of game by collision with own body
            self.reset()
        
        elif now[0] == 0 and x == -1:
            # it means the game is ended because of the collision with the left wall
            self.reset()
        elif new[0] == 0 and x == 1:
            # it means the game is ended because of the collision with the right wall
            self.reset() 
        
        elif now[1] == 0 and y == -1: 
            # it means end of game by collision with the upper wall
            self.reset()
        elif new[1] == 0 and y == 1: 
            # it means end of game by collision with the below wall
            self.reset()
        
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
            self.directions.insert(0, self.directions[0])
            if len(self.directions) > self.length:
                self.directions.pop()
      
# draw Grid
def drawGrid(surface):
    for y in range(0, int(GRID_NUM)):
        for x in range(0, int(GRID_NUM)):
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
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
    
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
            snake.directions.append(snake.directions[-1])
            food.randomize_position()
        
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (255,255,255))
        screen.blit(text, (15,10))

        pygame.display.update()

#main()
mainmenu()