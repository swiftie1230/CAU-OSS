import pygame
import random
import json
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
saveImg = pygame.image.load("snake_game/imgs/save.png")
loadImg = pygame.image.load("snake_game/imgs/load.png")
clicksaveImg = pygame.image.load("snake_game/imgs/clickedSaveIcon.png")
clickloadImg = pygame.image.load("snake_game/imgs/clickedLoadIcon.png")
gameOverImg = pygame.image.load("snake_game/imgs/gameover.png")
goMenuImg = pygame.image.load("snake_game/imgs/gomenu.png")
clickgoMenuImg = pygame.image.load("snake_game/imgs/clickedgomenu.png")
resumeImg = pygame.image.load("snake_game/imgs/resume.png")
clickresumeImg = pygame.image.load("snake_game/imgs/clickedgomenu.png")
restartImg = pygame.image.load("snake_game/imgs/restart.png")
clickrestartImg = pygame.image.load("snake_game/imgs/clickedrestart.png")

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Hello CAU_OSS Snake Game!")

clock = pygame.time.Clock()

# move
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

load = 0
resume = 0


# for test
data = {
    "score" : 0,
    "positions" : [((SCREEN_SIZE / 2), (SCREEN_SIZE / 2))],
    "directions" : [UP],
    "food_position" : (0,0)
}

ranking = {
    "test": 1,
    "jun":3
}

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

def create_save():
    return data

def write_save(new_save):
    with open('save.txt','w') as save_file:
        json.dump(new_save,save_file)

def savegame():
    new_save = create_save()
    print(new_save["score"])
    print(new_save["positions"])
    print(new_save["directions"])
    
    write_save(new_save)
    print("save done")

def loadgame():
    global load
    load = 1
    main()

def quitgame():
    print("end game...")
    pygame.quit()
    sys.exit()

def write_rank(name):
    ranking[name] = data["score"]
    pygame.display.update()
        
    with open('ranking.txt','w') as save_file:
        json.dump(ranking,save_file)
    
def gameover(screen):
    global myfont
    text1 = "Please Enter Your Name"
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(text1)> 0:
                        text1 = text1[:-1]
                elif event.key == pygame.K_RETURN:
                    write_rank(text1)
                    mainmenu()
                    break
                else:
                    text1 += event.unicode
        gameDisplay.fill(white)
    
        titletext = gameDisplay.blit(gameOverImg, (210,310))
        menuButton = Button(goMenuImg,260,420,60,20,clickgoMenuImg,260,418,mainmenu)      
        
        myfont = pygame.font.SysFont("arial", 16, True, True)
        text = myfont.render(text1, 1, (0,0,0))
        screen.blit(text, (15,10))
        pygame.display.update()
        clock.tick(15)

def getrank():
    global ranking
    
    print("load data")
    with open('ranking.txt') as rank_file:
        ranking = json.load(rank_file)
        
    ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse = True))
    print(ranking)
    

def showrank():
    getrank()
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        myfont = pygame.font.SysFont("arial", 16, True, True)
        
        tmp = 0
        for name, sc in ranking.items():
            rank = myfont.render(str(tmp+1) + ". " + name+ " : " + str(sc), 1, (0,0,0))
            screen.blit(rank, (40,100+tmp*50))
            tmp += 1
        
        quitButton = Button(quitImg,490,420,60,20,clickQuitImg,490,418,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

def mainmenu():
    global load
    load = 0
    
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (210,310))
        startButton = Button(startImg,190,420,60,20,clickStartImg,190,418,main)
        saveButton = Button(saveImg,290,420,60,20,clicksaveImg,290,418,showrank)
        loadButton = Button(loadImg,390,422,60,20,clickloadImg,390,418,loadgame)
        quitButton = Button(quitImg,490,420,60,20,clickQuitImg,490,418,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def resumegame():
    global resume
    resume = 1
    main()

def pausemenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (210,310))
        resumeButton = Button(resumeImg,190,420,60,20,clickresumeImg,190,418,resumegame)
        restartButton = Button(restartImg,290,420,60,20,clickrestartImg,290,418,mainmenu)
        loadButton = Button(saveImg,390,422,60,20,clicksaveImg,390,418,savegame)
        quitButton = Button(quitImg,490,420,60,20,clickQuitImg,490,418,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

# Food Class
class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (200, 0, 0)
        self.randomize_position()
    
    def set_state(self):
        self.position = data["food_position"]
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_NUM-1) * GRID_SIZE, random.randint(0,GRID_NUM-1) * GRID_SIZE)

    def draw(self, surface):
        food_image = pygame.image.load("snake_game/imgs/apple.png")
        food_image = pygame.transform.scale(food_image, (GRID_SIZE, GRID_SIZE))
        surface.blit(food_image, (self.position[0], self.position[1]))
    

class Snake(object):
    def __init__(self):
        self.length = 1
        # set start point to center
        self.positions = [((SCREEN_SIZE / 2), (SCREEN_SIZE / 2))]
        self.color = (40,50,90)
        self.directions = [UP]
        pass
    
    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_SIZE / 2) , (SCREEN_SIZE / 2))]
        self.directions = [UP]
        global score
        score = 0

    def set_state(self):
        print("setting state..")
        print(data["score"])
        print(data["positions"])
        print(data["directions"])
        
        self.length = data["score"] + 1
        self.positions = data["positions"]
        self.directions = data["directions"]
        global score
        score = data["score"]
    
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
                elif event.key == pygame.K_ESCAPE:
                    pausemenu()
    
    def move(self, screen):
        now = self.get_head()
        
        x, y = self.directions[0]
        new = (((now[0] + (x*GRID_SIZE)) % SCREEN_SIZE), (now[1] + (y*GRID_SIZE)) % SCREEN_SIZE)
        
        # it means end of game by collision with own body
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
            gameover(screen)
        elif now[0] == 0 and x == -1:
            # it means the game is ended because of the collision with the left wall
            self.reset()
            gameover(screen)
        elif new[0] == 0 and x == 1:
            # it means the game is ended because of the collision with the right wall
            self.reset() 
            gameover(screen)
        elif now[1] == 0 and y == -1: 
            # it means end of game by collision with the upper wall
            self.reset()
            gameover(screen)
        elif new[1] == 0 and y == 1: 
            # it means end of game by collision with the below wall
            self.reset()
            gameover(screen)
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
    
def main():
    global resume
    global score
    global load
    
    # surface == 2D object / 색이나 이미지를 가지는 빈 시트
    surface = pygame.Surface(screen.get_size())
    
    # Surface to the same pixel format as the one you use for final display
    surface = surface.convert()
    drawGrid(surface)
    
    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("arial", 16, True, True)
    
    if (load == 1):
        print("load data")
        with open('save.txt') as save_file:
            global data
            data = json.load(save_file)
        # list to tuple
        for i in range(0,len(data["positions"])):
            data["positions"][i] = tuple(data["positions"][i])
        for i in range(0,len(data["directions"])):
            data["directions"][i] = tuple(data["directions"][i])
            
        data["food_position"] = tuple(data["food_position"])
        
        snake.set_state()
        food.set_state()
        load = 0
        
    elif (resume == 1):
        snake.set_state()
        food.set_state()
        resume = 0
        
    else:
        score = 0
        
    # Boolean value for End clause 
    running = True
    while(running):
        clock.tick(10)
        drawGrid(surface)
        
        snake.move(screen)
        snake.key_handling()
        
        food.draw(surface)
        snake.draw(surface)
        
        if snake.get_head() == food.position:
            snake.length += 1
            score += 1
            snake.directions.append(snake.directions[-1])
            food.randomize_position()
        
        data["score"] = score
        data["positions"] = snake.positions
        data["directions"] = snake.directions
        data["food_position"] = food.position

        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (255,255,255))
        screen.blit(text, (15,10))
        
        pygame.display.update()

#main()
mainmenu()