import pygame
import random 
import time
import sys
import numpy as np
import pickle

# screen size
SCREEN_SIZE = 800

GRID_SIZE = 20
GRID_NUM = SCREEN_SIZE / GRID_SIZE

FPS = 60

pygame.init()

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
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

DIRECTION = [
    (0, -1), # UP
    (-1, 0), # LEFT
    (0, 1), # DOWN
    (1, 0) # RIGHT
]

class Snake(object):
    def __init__(self, genome, surface, food):
        self.length = 1
        # set start point to center
        self.positions = [((SCREEN_SIZE / 2), (SCREEN_SIZE / 2))]
        self.color = (40,50,90)
        self.directions = [DIRECTION[UP]]

        self.timer = 0
        self.last_fruit_time = 0
        self.surface = surface

        # fitness
        self.fitness = 0.
        self.last_dist = np.inf
        self.genome = genome
        pass
    
    def draw(self, surface):
        for i in range(len(self.positions)):
            if i == 0:
                if len(self.positions) == 1:
                    snake_head_image = pygame.image.load('snake_game/imgs/snake_head.png')
                else:
                    snake_head_image = pygame.image.load('snake_game/imgs/snake_head1.png')
                snake_head_image = pygame.transform.scale(snake_head_image, (GRID_SIZE, GRID_SIZE))
                if self.directions[i] == DIRECTION[UP]:
                    rotate = 180
                elif self.directions[i] == DIRECTION[DOWN]:
                    rotate = 0
                elif self.directions[i] == DIRECTION[LEFT]:
                    rotate = 270
                elif self.directions[i] == DIRECTION[RIGHT]:
                    rotate = 90
                snake_head_image = pygame.transform.rotate(snake_head_image, rotate)
                surface.blit(snake_head_image, (self.positions[i][0], self.positions[i][1]))
            elif i == len(self.positions) - 1:
                snake_tail_image = pygame.image.load('snake_game/imgs/snake_tail.png')
                snake_tail_image = pygame.transform.scale(snake_tail_image, (GRID_SIZE, GRID_SIZE))
                if self.directions[i] == DIRECTION[UP]:
                    rotate = 180
                elif self.directions[i] == DIRECTION[DOWN]:
                    rotate = 0
                elif self.directions[i] == DIRECTION[LEFT]:
                    rotate = 270
                elif self.directions[i] == DIRECTION[RIGHT]:
                    rotate = 90
                snake_tail_image = pygame.transform.rotate(snake_tail_image, rotate)
                surface.blit(snake_tail_image, (self.positions[i][0], self.positions[i][1]))
            else:
                r = pygame.Rect((self.positions[i][0], self.positions[i][1]), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, (93, 216, 228), r, 1)
    
    # head for interact food
    def get_head(self):
        return self.positions[0]

    def turn(self, UDLR):
        #set directions
        if self.length > 1 and (UDLR[0]*-1, UDLR[1]*-1) == self.directions[0]:
            return
        else:
            self.directions[0] = UDLR
    
    def move(self):
        now = self.get_head()
        x, y = self.directions[0]
        new = (((now[0] + (x*GRID_SIZE)) % SCREEN_SIZE), (now[1] + (y*GRID_SIZE)) % SCREEN_SIZE)
        if len(self.positions) > 2 and new in self.positions[2:]:
            # it means end of game by collision with own body
            print('own body! ', end='')
            self.fitness -= 200
            with open('log.txt','a') as file:
                file.write('own body! ')
            return False
        elif now[0] == 0 and x == -1:
            # it means the game is ended because of the collision with the left wall
            print('leftwall! ', end='')
            with open('log.txt','a') as file:
                file.write('leftwall! ')
            return False
        elif new[0] == 0 and x == 1:
            # it means the game is ended because of the collision with the right wall
            print('rightwall! ', end='')
            with open('log.txt','a') as file:
                file.write('rightwall! ')
            return False
        elif now[1] == 0 and y == -1: 
            # it means end of game by collision with the upper wall
            print('upperwall! ', end='')
            with open('log.txt','a') as file:
                file.write('upperwall! ')
            return False
        elif new[1] == 0 and y == 1: 
            # it means end of game by collision with the below wall
            print('below wall! ', end='')
            with open('log.txt','a') as file:
                file.write('below wall! ')
            return False
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
            self.directions.insert(0, self.directions[0])
            if len(self.directions) > self.length:
                self.directions.pop()
            return True

    def get_inputs(self, food):
        head = self.positions[0]
        result = [1., 1., 1., 0., 0., 0.] # [:3] - 장애물과의 거리, [3:] - 사과 위치 방향, 앞쪽, 왼쪽, 오른쪽

        # 갈 수 있는 경로
        current_direction = DIRECTION.index(self.directions[0])
        possible_dirs = [
            self.directions[0], # 직진
            DIRECTION[(current_direction + 1) % 4], # 좌회전
            DIRECTION[(current_direction + 3) % 4] # 우회전
        ]

        # 장애물 식별
        # range(0, 1, 0.1), 0: 위험, 1: 안전 (장애물에 가까울 수록 0에 가까운 값)
        for i, p_dir in enumerate(possible_dirs):
            for j in range(10):
                guess_head = head + p_dir * (j + 1) * GRID_SIZE
                #print(guess_head[0], guess_head[1])
                if (
                guess_head[0] <= 0 or
                guess_head[0] >= SCREEN_SIZE or
                guess_head[1] <= 0 or
                guess_head[1] >= SCREEN_SIZE or
                guess_head in self.positions
                ):
                    result[i] = j * 0.1
                    break

        #print(food.position)
        #print(type(possible_dirs[1]))
        #print(np.array(possible_dirs[1]).tolist())
        if np.any(head == food.position) or np.sum(np.array(head) * np.array(possible_dirs[0])) < np.sum(np.array(food.position) * np.array(possible_dirs[0])):
            result[3] = 1 # 사과가 앞쪽에 있는 경우
        elif np.sum(np.array(head) * np.array(possible_dirs[1])) < np.sum(np.array(food.position) * np.array(possible_dirs[1])):
            result[4] = 1 # 사과가 왼쪽에 있는 경우
        else:
            result[5] = 1 # 사과가 오른쪽에 있는 경우

        return np.array(result)
      
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

def main(genome, screen, surface):    
    global score
    score = 0
    #snake = Snake(genome=None)
    food = Food()
    snake = Snake(genome, surface, food)

    myfont = pygame.font.SysFont("arial", 16, True, True)

    snake.fitness = 0

    # Boolean value for End clause 
    running = True
    clock = pygame.time.Clock()

    while(running):
        snake.timer += 0.1
        if snake.fitness < -30 or snake.timer - snake.last_fruit_time > 0.1 * 60 * 5:
            print('Terminate! ', end='')
            snake.fitness -= 500
            with open('log.txt','a') as file:
                file.write('Terminate! ')
            break
        
        clock.tick(FPS) #기본 속도 10

        drawGrid(surface)
        
        #snake.move()
        #snake.key_handling()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.KEYDOWN:
                # QUIT
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                # PAUSE
                if e.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        for ee in pygame.event.get():
                            if ee.type == pygame.QUIT:
                                pygame.quit()
                            elif ee.type == pygame.KEYDOWN:
                                if ee.key == pygame.K_SPACE:
                                    pause = False

        inputs = snake.get_inputs(food)
        outputs = snake.genome.forward(inputs)
        #print(outputs)
        outputs = np.argmax(outputs) #최적의 방향 반환
        current_direction = DIRECTION.index(snake.directions[0])
        if outputs == 0: # 직진
            pass
        elif outputs == 1: # 좌회전
            snake.directions[0] = DIRECTION[(current_direction + 1) % 4]
        elif outputs == 2: # 우회전
            snake.directions[0] = DIRECTION[(current_direction + 3) % 4]
           
        if not snake.move():
            snake.fitness -= 200
            #print('score: %3d ' % score, end='')
            break
    
        if snake.get_head() == food.position:
            snake.length += 1
            score += 1
            snake.last_fruit_time = snake.timer
            snake.fitness += 100
            snake.directions.append(snake.directions[-1])
            food.randomize_position()
        
        # compute fitness
        #print(np.array(snake.positions[0])/GRID_SIZE)
        current_dist = np.linalg.norm(np.array(snake.positions[0])/GRID_SIZE - np.array(food.position)/GRID_SIZE)
        if snake.last_dist > current_dist:
            snake.fitness += 1.
        else:
            snake.fitness -= 1.5
        snake.last_dist = current_dist
        
        food.draw(surface)
        snake.draw(surface)

        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (255,255,255))
        screen.blit(text, (15,10))

        pygame.display.update()

    return snake.fitness, score

class MyCustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__":
            module = "training"
        return super().find_class(module, name)

if __name__ == '__main__':
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

    with open('snake_game/training/save.p', 'rb') as save_file:
        #unpickler = MyCustomUnpickler(save_file)
        # listgenome = unpickler.load()
        genome = pickle.load(save_file)

    #while True:
    #snake = Snake(genome, surface, food)
    fitness, score = main(genome, screen, surface)

    print('Fitness: %d score: %d' % (fitness, score))

#main()
#mainmenu()