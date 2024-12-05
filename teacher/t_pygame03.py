# draw를 사용해서 원 그리기
# 키보드를 누를 때마다 좌표를 사용해서 움직임

import pygame # We will use the Pygame library.

pygame.init() #pygame initialize

background = pygame.display.set_mode((480, 360))
#I set the horizontal and vertical length of the game screen. 480 is horizontal and 360 is vertical.
pygame.display.set_caption("벽돌 게임")
# This will create a title for the game window.

x_pos = background.get_size()[0]//2 #240
y_pos = background.get_size()[1]//2 #180

play = True
while play:
    for event in pygame.event.get(): #for 문을 작동시켜서 파이게임에서 발생하는 이벤트가 있다면 그것을 get()을 통해 가져온다.
        # print(event.type) 어떤 이벤트가 발생하는지 출력하기
        if event.type == pygame.QUIT: # 그 이벤트가 무엇인지에 대해 말함. 포문으로 하나하나 검사를 하는데 만약 파이게임에서 가져온 이벤트가 quit이라면 게임을 종료하고 싶은 것이므로 와일문에서 true를 false로 바꿔 와일문을 빠져나오고
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               print('up') 
            if event.key == pygame.K_DOWN:
               print('down')
            if event.key == pygame.K_LEFT:
               print('left')
            if event.key == pygame.K_RIGHT:
               print('right')

        

pygame.quit() # 파이게임을 닫음
# print(pygame.) 어떤 명령어가 있는지 확인할 수 있음