import pygame
import random
import json
import time
import sys
import os

# screen size
SCREEN_SIZE = 800
GRID_SIZE = 20
GRID_NUM = SCREEN_SIZE / GRID_SIZE

pygame.init()

white = (255, 255, 255)

titleImg = pygame.image.load("snake_game/imgs/title.png")
startImg = pygame.image.load("snake_game/imgs/single.png")
quitImg = pygame.image.load("snake_game/imgs/quit.png")
clickStartImg = pygame.image.load("snake_game/imgs/clickedsingle.png")
clickQuitImg = pygame.image.load("snake_game/imgs/clickedquit.png")
saveImg = pygame.image.load("snake_game/imgs/save.png")
loadImg = pygame.image.load("snake_game/imgs/load.png")
clicksaveImg = pygame.image.load("snake_game/imgs/clickedsave.png")
clickloadImg = pygame.image.load("snake_game/imgs/clickedload.png")
gameOverImg = pygame.image.load("snake_game/imgs/gameover.png")
goMenuImg = pygame.image.load("snake_game/imgs/gomenu.png")
clickgoMenuImg = pygame.image.load("snake_game/imgs/clickedgomenu.png")
resumeImg = pygame.image.load("snake_game/imgs/resume.png")
clickresumeImg = pygame.image.load("snake_game/imgs/clickedresume.png")
restartImg = pygame.image.load("snake_game/imgs/restart.png")
clickrestartImg = pygame.image.load("snake_game/imgs/clickedrestart.png")
rankingImg = pygame.image.load("snake_game/imgs/ranking.png")
clickrankingImg = pygame.image.load("snake_game/imgs/clickedranking.png")
pausetitleImg = pygame.image.load("snake_game/imgs/pausetitle.png")
clickDualImg = pygame.image.load("snake_game/imgs/clickeddual.png")
dualImg = pygame.image.load("snake_game/imgs/dual.png")
clickAutoImg = pygame.image.load("snake_game/imgs/clickedauto.png")
autoImg = pygame.image.load("snake_game/imgs/auto.png")

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Hello CAU_OSS Snake Game!")

clock = pygame.time.Clock()

global gameChoice

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

data_dual = {
    "length_1" : 0,
    "length_2" : 0,
    "position_1" : [(0, 0)],
    "position_2" : [(SCREEN_SIZE - GRID_SIZE, SCREEN_SIZE)],
    "direction_1" : [DOWN],
    "direction_2" : [UP],
    "food_position_1" : (0,0),
    "food_position_2" : (0,0)
}

ranking = {

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
    mainmenu()

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

def gameover_dual(screen, player):
    global myfont

    if player == 1:
        text1 = "Player2 Won!"
    elif player == 2:
        text1 = "Player1 Won!"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        gameDisplay.fill(white)
    
        # show GAME OVER !!!
        titletext = gameDisplay.blit(gameOverImg, (400 - (gameOverImg.get_width()/2),300))
        
        # show Enter name
        myfont = pygame.font.SysFont("arial", 23, True, True)
        text = myfont.render(text1, 1, (0,0,0))
        screen.blit(text, (400 - (text.get_width()/2),400))
        
        # show Go menu Button
        menuButton = Button(goMenuImg, 400 - (goMenuImg.get_width()/2),510, goMenuImg.get_width(),goMenuImg.get_height(), clickgoMenuImg, (400 - clickgoMenuImg.get_width()/2),508, mainmenu)      
        
        pygame.display.update()
        clock.tick(15)
    
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
    
        # show GAME OVER !!!
        titletext = gameDisplay.blit(gameOverImg, (400 - (gameOverImg.get_width()/2),300))
        
        # show Enter name
        myfont = pygame.font.SysFont("arial", 23, True, True)
        text = myfont.render(text1, 1, (0,0,0))
        screen.blit(text, (400 - (text.get_width()/2),400))
        
        # show Go menu Button
        menuButton = Button(goMenuImg,
                            400 - (goMenuImg.get_width()/2),510,
                            goMenuImg.get_width(),goMenuImg.get_height(),
                            clickgoMenuImg,
                            (400 - clickgoMenuImg.get_width()/2),508,
                            mainmenu
                            )      
        
        pygame.display.update()
        clock.tick(15)

def getrank():
    global ranking
    
    print("load data")
    try:
        with open('ranking.txt') as rank_file:
            ranking = json.load(rank_file)
        
        ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse = True))
    except:
        return

def showrank():
    getrank()
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        myfont = pygame.font.SysFont("arial", 21, True, True)
        Nofont = pygame.font.SysFont("arial", 40, True, True)
        
        Button_width = startImg.get_width()
        Button_height = startImg.get_height()
        
        if(is_it_rank()):
            quitButton = Button(quitImg,600,400-Button_height/2,Button_width,Button_height,clickQuitImg,598,400-Button_height/2,mainmenu)
            tmp = 0
            for name, sc in ranking.items():
                rank = myfont.render(str(tmp+1) + ". " + name+ " : " + str(sc), 1, (0,0,0))
                #SCREEN -> 800 120~570
                screen.blit(rank, (200,120+tmp*50))
                tmp += 1
                if tmp == 10:
                    break
        else:
            text = Nofont.render("There is No Rank", 1, (0,0,0))
            screen.blit(text, (400-(text.get_width()/2),300))
            quitButton = Button(quitImg,400-Button_width/2,600,Button_width,Button_height,clickQuitImg,400-Button_width/2,600,mainmenu)
            
        pygame.display.update()
        clock.tick(15)
        
def is_it_save():
    file_path = "./save.txt"
    return(os.path.isfile(file_path)) 

def is_it_rank():
    file_path = "./ranking.txt"
    return(os.path.isfile(file_path)) 

def pausemenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        
        Button_width = startImg.get_width()
        Button_height = startImg.get_height()
        
        
        pausetitletext = gameDisplay.blit(pausetitleImg, (400-(pausetitleImg.get_width()/2),220))
        
        if gameChoice == 1:
            resumeButton  = Button(resumeImg,100,420,Button_width,Button_height,clickresumeImg,100,418,resumegame)
            restartButton = Button(restartImg,260,420,Button_width,Button_height,clickrestartImg,260,418,main)
            saveButton = Button(saveImg,415,420,Button_width,Button_height,clicksaveImg,415,418,savegame)
            quitButton = Button(quitImg,550,420,Button_width,Button_height,clickQuitImg,550,418,mainmenu)
        
        else:
            resumeButton  = Button(resumeImg,100,420,Button_width,Button_height,clickresumeImg,100,418,resumegame)
            restartButton = Button(restartImg,330,420,Button_width,Button_height,clickrestartImg,330,418,dualgame)
            quitButton = Button(quitImg,550,420,Button_width,Button_height,clickQuitImg,550,418,mainmenu)

        pygame.display.update()
        clock.tick(15)

# pause for dual mode
def pausemenu_dual():
    menu = True
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        
        Button_width = startImg.get_width()
        Button_height = startImg.get_height()
        
        
        pausetitletext = gameDisplay.blit(pausetitleImg, (400-(pausetitleImg.get_width()/2),220))
        
        resumeButton  = Button(resumeImg,100,420,Button_width,Button_height,clickresumeImg,100,418,resumegame)
        restartButton = Button(restartImg,330,420,Button_width,Button_height,clickrestartImg,330,418,dualgame)
        quitButton = Button(quitImg,550,420,Button_width,Button_height,clickQuitImg,550,418,mainmenu)

        pygame.display.update()
        clock.tick(15)



def mainmenu():
    global gameChoice
    global load
    load = 0
    
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(titleImg, (400-(titleImg.get_width()/2),220))
        
        Button_width = startImg.get_width()
        Button_height = startImg.get_height()
        
        singleButton = Button(startImg,125,420,Button_width,Button_height,clickStartImg,125,418, main)
        dualButton = Button(dualImg,325,420,Button_width,Button_height,clickDualImg,325,418,dualgame)
        autoButton = Button(autoImg,525,420,Button_width,Button_height,clickAutoImg,525,418,autogame)
        
        rankingButton = Button(rankingImg,125,520,Button_width,Button_height,clickrankingImg,125,518,showrank)
        
        if(is_it_save()):
            loadButton = Button(loadImg,325,520,Button_width,Button_height,clickloadImg,325,518,loadgame)
        else:
            loadButton = Button(clickloadImg,325,520,Button_width,Button_height,clickloadImg,325,518,None)
        
        quitButton = Button(quitImg,525,520,Button_width,Button_height,clickQuitImg,525,518,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def resumegame():
    global resume
    resume = 1
    if gameChoice == 1:
        main()
    elif gameChoice == 2:
        dualgame()
    elif gameChoice == 3:
        autogame()

# Food Class
class Food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (200, 0, 0)
        self.randomize_position()
    
    def set_state(self):
        self.position = data["food_position"]

    def set_state1(self):
        self.position = data_dual["food_position_1"]

    def set_state2(self):
        self.position = data_dual["food_position_2"]
    
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

    def set_snake1(self):
        self.length = 1
        # set start point to left-top
        self.positions = [(0, SCREEN_SIZE)]
        self.color = (40,50,90)
        self.directions = [DOWN] 

    def set_snake2(self):
        self.length = 1
        # set start point to right-bottom
        self.positions = [(SCREEN_SIZE - GRID_SIZE, SCREEN_SIZE)]
        self.color = (40,50,90)
        self.directions = [UP]
    
    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_SIZE / 2) , (SCREEN_SIZE / 2))]
        self.directions = [UP]
        global score
        score = 0

    def reset_snake1(self):
        self.length = 1
        self.positions = [(0 , SCREEN_SIZE)]
        self.directions = [DOWN]
        # global score
        # score = 0

    def reset_snake2(self):
        self.length = 1
        self.positions = [(SCREEN_SIZE - GRID_SIZE, SCREEN_SIZE)]
        self.color = (40,50,90)
        self.directions = [UP]


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

    # set state for snake_1 in dual mode
    def set_state_1(self):
        print("setting state for player 1...")
        print(data_dual["position_1"])
        print(data_dual["direction_1"])    

        self.length = data_dual["length_1"] 
        self.positions = data_dual["position_1"]
        self.directions = data_dual["direction_1"]

    # set state for snake_2 in dual_mode
    def set_state_2(self):
        print("setting state for player 2...")
        print(data_dual["position_2"])
        print(data_dual["direction_2"])    

        self.length = data_dual["length_2"]
        self.positions = data_dual["position_2"]
        self.directions = data_dual["direction_2"]

    
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
    
    def auto_x(self, now_food):
        now_head = self.get_head()
        if(now_food[0] - now_head[0] == 0):
            if (now_food[1] == now_head[1]):
                pass
            self.auto_y(now_food)
        # food in left
        elif(now_food[0] - now_head[0] < 0):
            self.turn(LEFT)
        elif(now_food[0] - now_head[0] > 0):
            self.turn(RIGHT)
            
    def auto_y(self, now_food):
        now_head = self.get_head()
        if(now_food[1] - now_head[1] == 0):
            if (now_food[0] == now_head[0]):
                pass
            self.auto_x(now_food)
        # food in left
        elif(now_food[1] - now_head[1] < 0):
            self.turn(UP)
        elif(now_food[1] - now_head[1] > 0):
            self.turn(DOWN)
    
    def find_turn(self):
        for di in [UP, DOWN, LEFT, RIGHT]:
            if(self.can_go(di)):
                self.turn(di)
                return
            # it means end game - ring shaped snake
            else:
                pass
                
    def can_go(self, UDLR):
        now_head = self.get_head()
        tmp = (now_head[0]+20*UDLR[0], now_head[1]+20*UDLR[1])    
        print("tmp : ", tmp)
        
        if(tmp in self.positions or (tmp[0] < 0 or tmp[0] > 800) or (tmp[1] < 0 or tmp[1] > 800)):
            return 0
        else:
            return 1
        
    def move_auto(self, food_position): 
        now_head = self.get_head()
        now_food = food_position
        
        # print("now_direction: ",self.directions)
        # print("now_position: ",self.positions)
        # print("now_head: ",now_head)
        # print("now_food: ",now_food)
        
        #self.auto_x(now_food)
        # food in right
        
        
        if(now_food[0] - now_head[0] == 0):
            #turn right
            if(now_food[1] - now_head[1] == 0):
                #get food
                pass
            
            elif(now_food[1] - now_head[1] > 0):
                if(self.directions[0] == DOWN):
                    pass
                if(self.can_go(DOWN)):
                    self.turn(DOWN)
                else:
                    self.find_turn()
                    
            elif(now_food[1] - now_head[1] < 0):
                if(self.directions[0] == UP):
                    pass
                if(self.can_go(UP)):
                    self.turn(UP)
                else:
                    self.find_turn()
                
            #go until now_food[0] == now_head[0]
        # food in left
        elif(now_food[0] - now_head[0] < 0):
            if(self.directions[0] == LEFT):
                pass
            if(self.can_go(LEFT)):
                self.turn(LEFT)
            else:
                self.find_turn()
                
        elif(now_food[0] - now_head[0] > 0):
            if(self.directions[0] == RIGHT):
                pass
            if(self.can_go(RIGHT)):
                self.turn(RIGHT)
            else:
                self.find_turn()
        
    def key_handling(self):
        for event in pygame.event.get():
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

    # move function for dual mode
    # have player parameter for displaying winner 
    def move_dual(self, screen, player):
        now = self.get_head()
        
        x, y = self.directions[0]
        new = (((now[0] + (x*GRID_SIZE)) % SCREEN_SIZE), (now[1] + (y*GRID_SIZE)) % SCREEN_SIZE)
        
        position2 = []
        
        if player == 1:
            position2 = data_dual["position_2"]
        elif player == 2:
            position2 = data_dual["position_1"]

        # it means end of game by collision with own body
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
            gameover_dual(screen, player)
       
       # it means end of game by collision with other snake
        elif new in position2[:]:
            self.reset()
            gameover_dual(screen, player)
        
        elif now[0] == 0 and x == -1:
            # it means the game is ended because of the collision with the left wall
            self.reset()
            gameover_dual(screen, player)
        elif new[0] == 0 and x == 1:
            # it means the game is ended because of the collision with the right wall
            self.reset() 
            gameover_dual(screen, player)
        elif now[1] == 0 and y == -1: 
            # it means end of game by collision with the upper wall
            self.reset()
            gameover_dual(screen, player)
        elif new[1] == 0 and y == 1: 
            # it means end of game by collision with the below wall
            self.reset()
            gameover_dual(screen, player)


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
# screen_dual = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), 0, 32)
    
def main():
    global gameChoice 
    global resume
    global score
    global load

    # single_player_mode
    gameChoice = 1
    
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
        print("resume game..")
        snake.set_state()
        food.set_state()
        resume = 0
        print(data)
        
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

# dual game mode
def dualgame():
    global gameChoice
    global resume
    global score
    global load

    # dual player mode
    gameChoice = 2
    
    # surface == 2D object / 색이나 이미지를 가지는 빈 시트
    surface = pygame.Surface(screen.get_size())
    
    # Surface to the same pixel format as the one you use for final display
    surface = surface.convert()
    drawGrid(surface)
    
    snake1 = Snake()
    snake1.set_snake1()
    
    snake2 = Snake()
    snake2.set_snake2()
    
    food1 = Food()
    food2 = Food()
        
    if (resume == 1):
        print("resume game..")
        snake1.set_state_1()
        snake2.set_state_2()
        food1.set_state1()
        food2.set_state2()
        resume = 0
        print(data)

    # Boolean value for End clause 
    running = True

    while(running):
        clock.tick(10)
        drawGrid(surface)
        
        snake1.move_dual(screen, 1)
        snake2.move_dual(screen, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # game exit
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # key input
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pausemenu_dual()
                
                else:
                    if event.key== pygame.K_UP:
                        snake2.turn(UP)
                    elif event.key == pygame.K_DOWN:
                        snake2.turn(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake2.turn(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake2.turn(RIGHT)
                    
                    if event.key == pygame.K_a:
                        snake1.turn(LEFT)
                    elif event.key == pygame.K_d:
                        snake1.turn(RIGHT)
                    elif event.key == pygame.K_w:
                        snake1.turn(UP)
                    elif event.key == pygame.K_s:
                        snake1.turn(DOWN)

        food1.draw(surface)
        food2.draw(surface)
        snake1.draw(surface)
        snake2.draw(surface)
        
        if snake1.get_head() == food1.position:
            snake1.length += 1
            snake1.directions.append(snake1.directions[-1])
            food1.randomize_position()
        elif snake1.get_head() == food2.position:
            snake1.length += 1
            snake1.directions.append(snake1.directions[-1])
            food2.randomize_position()

        if snake2.get_head() == food1.position:
            snake2.length += 1
            snake2.directions.append(snake2.directions[-1])
            food1.randomize_position()
        elif snake2.get_head() == food2.position:
            snake2.length += 1
            snake2.directions.append(snake2.directions[-1])
            food2.randomize_position()
        
        data_dual["length_1"] = snake1.length
        data_dual["position_1"] = snake1.positions
        data_dual["direction_1"] = snake1.directions
        data_dual["food_position_1"] = food1.position

        data_dual["length_2"] = snake2.length
        data_dual["position_2"] = snake2.positions
        data_dual["direction_2"] = snake2.directions
        data_dual["food_position_2"] = food2.position

        screen.blit(surface, (0,0))
        
        pygame.display.update()

def autogame():
    global gameChoice 
    global resume
    global score
    global load

    # auto_mode
    gameChoice = 3
    
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
        print("resume game..")
        snake.set_state()
        food.set_state()
        resume = 0
        print(data)
        
    else:
        score = 0
        
    # Boolean value for End clause 
    running = True
    while(running):
        clock.tick(10)
        drawGrid(surface)
        
        snake.move(screen)
        #snake.key_handling()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # game exit
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN: # key input
                if event.key == pygame.K_ESCAPE:
                    pausemenu()
                    
        snake.move_auto(food.position)
        
        food.draw(surface)
        snake.draw(surface)
        
        if snake.get_head() == food.position:
            snake.length += 1
            score += 1
            snake.directions.append(snake.directions[-1])
            food.randomize_position() 
            snake.move_auto(food.position)
        
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