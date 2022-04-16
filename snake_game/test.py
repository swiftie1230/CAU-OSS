import sys
import random 
import pygame


# screen size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

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

    myfont = pygame.font.SysFont("arial", 16, True, True)
    score = 0

    # Boolean value for End clause 
    running = True

    while(running):
        clock.tick(10)
        drawGrid(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (255,255,255))
        screen.blit(text, (15,10))

        # If you click X button (quit button), then you exit the game
        # The exit button and logic not implemented yet
        # So once the X button is pressed, it is closed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

main()