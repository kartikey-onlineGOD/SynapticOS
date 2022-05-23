from asyncio.windows_events import NULL
import pygame
import info
import time
import sys 
import SnakeGame as Sng
import Calculator as cc
import Notes as cal
import Browser as br
import MS as ms
from threading import Thread
import FM


NAME = "Synapsic"

#Display setup
pygame.display.set_caption(NAME) 
pygame.init()  
screen = pygame.display.set_mode((1200,800))

def main( ):
    global NAME , BG
    import random
    import Weather as ww
    import math 
    pygame.display.set_caption(NAME) 
    pygame.font.init()

    #Assets Fonts
    myfont1 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 40)
    myfont2 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 51)
    myfont3 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 53)
    myfont4 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 58)
    myfont5 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 24)

    #Images and BG loading
    background_image = pygame.image.load("Assets\\Images\\Desktop_main_screen.png") 
    browser = pygame.image.load("Assets\\Images\\Browser_logo.png")
    search = pygame.image.load("Assets\\Images\\Search_logo.png")
    calculator = pygame.image.load("Assets\\Images\\calculator_icon.png")
    notepad = pygame.image.load("Assets\\Images\\notepad_icon.png")
    snake = pygame.image.load("Assets\\Images\\snake.png")
    music_icon = pygame.image.load("Assets\\Images\\Music_Icon.png")
    programIcon = pygame.image.load('Assets\\Images\\SYNAPSIC_logo.png')

    pygame.display.set_icon(programIcon)

    def Time_and_Date(screen):
        from time import time, ctime
        t = time()
        tm = ctime(t)
        tm = tm.split(" ")
        date = tm[1] + " " + tm[2] 
        year = tm[4]
        day = tm[0]
        tim = tm[3].split(":")
        try:
            hour = tim[0] + ":" + tim[1]
        except:
            hour = tim[0]
        

        t1 = myfont1.render(date, True, (255, 255, 255))
        t2 = myfont2.render(year, True, (255, 255, 255))
        t3 = myfont2.render(day, True, (255, 255, 255))
        t4 = myfont3.render(hour,True, (255,255,255))

        screen.blit(t1,(440,220))
        screen.blit(t2,(443,260))
        screen.blit(t3,(440,310))
        screen.blit(t4,(620,205))

        l = ww.main()
        temp = str(l[0]) + "°C"
        t5 = myfont4.render(temp,True,(255,255,255))
        screen.blit(t5,(620,260))

        k = str(l[1]).split(" ")
        cast= k[2] + " " + k[3]
        t6 = myfont5.render(cast,True,(255,255,255))
        screen.blit(t6,(610,330))

        pygame.draw.rect(screen,(255,255,255),(590,200,1,170))


    def LowerBar():
        pygame.draw.rect(screen,(5,5,5),(0,740,1200,60))
        logo = pygame.image.load("Assets\\Images\\SYNAPSIC_logo.png") 
        screen.blit(logo, [20, 746])
        screen.blit(search,[70,735])
        pygame.draw.rect(screen,(50,50,50),(140,750,1,40))
        screen.blit(browser,[155,740])
        screen.blit(calculator,[215,740])
        screen.blit(notepad,[275,740])
        screen.blit(snake,[343,750])
        screen.blit(music_icon,[410,750])

    scrch = 0
    def Search(screen,scrch):
        #pygame.draw.rect(screen,(50,50,50),(20,700,200,40))
        print(scrch)
        if scrch == 0:
            scrch = 1
        elif scrch == 1:
            scrch = 0
        return scrch
        pygame.display.update()

    done = False
    while not done:  
        for event in pygame.event.get():  
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit("")    
                done = True 
            if event.type == pygame.MOUSEBUTTONDOWN :
                if pos[1] >= 730 and pos[1]<= 800 :
                    if pos[0] >= 340 and pos[0] <= 395:
                        Sng.main()
                    if pos[0] >=215 and pos[0] <=275 :
                        cc.run()
                    if pos[0] >= 0 and pos[0] <= 50:
                        lockscreen()
                    if pos[0] >=  70 and pos[0] <= 120:
                        FM.main()
                    if pos[0] >= 280 and pos[0] <= 330:
                        cal.main()
                    if pos[0] >= 145 and pos[0] <= 215:
                        br.main()
                    if pos[0] >= 395 and pos[0] <= 445:
                        ms.main()

                #refrence
                print(pos)
                        

                        

        screen.blit(background_image, [0, 0])
        LowerBar()
        if scrch == 1:
            pygame.draw.rect(screen,(50,50,50),(5,695,200,40))

        Time_and_Date(screen)
        
        pygame.display.update()

def lockscreen():
    global NAME , BG
    import time
    import random
    import Weather as ww
    import math 
    pygame.display.set_caption(NAME) 
    pygame.font.init()
    myfont1 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 30)
    myfont2 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 24)
    myfont3 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 53)
    myfont4 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 58)
    myfont5 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 24)

    #Images and BG loading
    background_image = pygame.image.load("Assets\\Images\\Desktop_main_screen.png") 
    user = pygame.image.load("Assets\\Images\\User_icon.png") 

    def login(screen):
        draw_rect_alpha(screen)
        log = myfont1.render("Username", True, (255, 255, 255))
        screen.blit(log,(525,400))
        pas = myfont1.render("Password", True, (255, 255, 255))
        screen.blit(pas,(525,490))

        s = pygame.Surface((560,45))  
        s.set_alpha(250)               
        s.fill((200,200,200))        
        screen.blit(s,(320,440))

        s = pygame.Surface((560,45))  
        s.set_alpha(250)               
        s.fill((200,200,200))        
        screen.blit(s,(320,530))

    name = ""
    pas = ""
    name= ''
    done = False
    ogp = " "
    while not done:  
        for event in pygame.event.get():  
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit("")  
                done = True 
            if pos[0] >= 320 and pos[0] <= 880:
                if pos[1] >= 440 and pos[1] <= 495:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            name= name+ "a"
                        elif event.key == pygame.K_b:
                            name= name+ "b"
                        elif event.key == pygame.K_c:
                            name= name+ "c"
                        elif event.key == pygame.K_d:
                            name= name+ "d"
                        elif event.key == pygame.K_e:
                            name= name+ "e"
                        elif event.key == pygame.K_f:
                            name= name+ "f"
                        elif event.key == pygame.K_g:
                            name= name+ "g"
                        elif event.key == pygame.K_h:
                            name= name+ "h"
                        elif event.key == pygame.K_i:
                            name= name+ "i"
                        elif event.key == pygame.K_j:
                            name= name+ "j"
                        elif event.key == pygame.K_k:
                            name= name+ "k"
                        elif event.key == pygame.K_l:
                            name= name+ "l"
                        elif event.key == pygame.K_m:
                            name= name+ "m"
                        elif event.key == pygame.K_n:
                            name= name+ "n"
                        elif event.key == pygame.K_o:
                            name= name+ "o"
                        elif event.key == pygame.K_p:
                            name= name+ "p"
                        elif event.key == pygame.K_q:
                            name= name+ "q"
                        elif event.key == pygame.K_r:
                            name= name+ "r"
                        elif event.key == pygame.K_s:
                            name= name+ "s"
                        elif event.key == pygame.K_t:
                            name= name+ "t"
                        elif event.key == pygame.K_u:
                            name= name+ "u"
                        elif event.key == pygame.K_v:
                            name= name+ "v"
                        elif event.key == pygame.K_w:
                            name= name+ "w"
                        elif event.key == pygame.K_x:
                            name= name+ "x"
                        elif event.key == pygame.K_y:
                            name= name+ "y"
                        elif event.key == pygame.K_z:
                            name= name+ "z"
                        elif event.key == pygame.K_BACKSPACE:
                            name= name[:-1]
                        elif event.key == pygame.K_SPACE:
                            name = name + " "
                        elif event.key == pygame.K_RETURN:
                            ogp = info.checkUser(name)
                            break
                        elif event.key == pygame.K_1:
                            name= name+ "1"
                        elif event.key == pygame.K_2:
                            name= name+ "2"
                        elif event.key == pygame.K_3:
                            name= name+ "3"
                        elif event.key == pygame.K_4:
                            name= name+ "4"
                        elif event.key == pygame.K_5:
                            name= name+ "5"
                        elif event.key == pygame.K_6:
                            name= name+ "6"
                        elif event.key == pygame.K_7:
                            name= name+ "7"
                        elif event.key == pygame.K_8:
                            name= name+ "8"
                        elif event.key == pygame.K_9:
                            name= name+ "9"
                        elif event.key == pygame.K_0:
                            name= name + "0"

            if pos[0] >= 320 and pos[0] <= 880:
                if pos[1] >= 530 and pos[1] <= 575:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            pas = pas + "a"
                        elif event.key == pygame.K_b:
                            pas = pas+ "b"
                        elif event.key == pygame.K_c:
                            pas = pas+ "c"
                        elif event.key == pygame.K_d:
                            pas = pas+ "d"
                        elif event.key == pygame.K_e:
                            pas= pas+ "e"
                        elif event.key == pygame.K_f:
                            pas= pas+ "f"
                        elif event.key == pygame.K_g:
                            pas= pas+ "g"
                        elif event.key == pygame.K_h:
                            pas= pas+ "h"
                        elif event.key == pygame.K_i:
                            pas= pas+ "i"
                        elif event.key == pygame.K_j:
                            pas= pas+ "j"
                        elif event.key == pygame.K_k:
                            pas= pas+ "k"
                        elif event.key == pygame.K_l:
                            pas= pas+ "l"
                        elif event.key == pygame.K_m:
                            pas= pas+ "m"
                        elif event.key == pygame.K_n:
                            pas= pas+ "n"
                        elif event.key == pygame.K_o:
                            pas= pas+ "o"
                        elif event.key == pygame.K_p:
                            pas= pas+ "p"
                        elif event.key == pygame.K_q:
                            pas= pas+ "q"
                        elif event.key == pygame.K_r:
                            pas= pas+ "r"
                        elif event.key == pygame.K_s:
                            pas= pas+ "s"
                        elif event.key == pygame.K_t:
                            pas= pas+ "t"
                        elif event.key == pygame.K_u:
                            pas= pas+ "u"
                        elif event.key == pygame.K_v:
                            pas= pas+ "v"
                        elif event.key == pygame.K_w:
                            pas= pas+ "w"
                        elif event.key == pygame.K_x:
                            pas= pas+ "x"
                        elif event.key == pygame.K_y:
                            pas= pas+ "y"
                        elif event.key == pygame.K_z:
                            pas= pas+ "z"
                        elif event.key == pygame.K_BACKSPACE:
                            pas= pas[:-1]
                        elif event.key == pygame.K_SPACE:
                            pas = pas + " "
                        elif event.key == pygame.K_RETURN:
                            if pas == ogp :
                                screen.fill((0,0,0))
                                main()
                            else:
                                wrongpass(screen)
                                print("Wrong Bro")

                        elif event.key == pygame.K_1:
                            pas= pas+ "1"
                        elif event.key == pygame.K_2:
                            pas= pas+ "2"
                        elif event.key == pygame.K_3:
                            pas= pas+ "3"
                        elif event.key == pygame.K_4:
                            pas= pas+ "4"
                        elif event.key == pygame.K_5:
                            pas= pas+ "5"
                        elif event.key == pygame.K_6:
                            pas= pas+ "6"
                        elif event.key == pygame.K_7:
                            pas= pas+ "7"
                        elif event.key == pygame.K_8:
                            pas= pas+ "8"
                        elif event.key == pygame.K_9:
                            pas= pas+ "9"
                        elif event.key == pygame.K_0:
                            pas= pas + "0"
            if pos[0] <= 10 and pos[1] <= 10 :
                main()                           

                


        screen.blit(background_image, [0, 0])
        screen.blit(user,[480,130])
        login(screen)
        log = myfont2.render(name, True, (0, 0, 0))
        screen.blit(log,(330,445))
        x = "*" * len(pas)
        pa = myfont2.render(x,True,(0,0,0))
        screen.blit(pa,(330,535)) 
        
        pygame.display.update()



def wrongpass(screen):
    myfont2 = pygame.font.Font('Assets\\Fonts\\Raleway-Thin.ttf', 24)
    msg= myfont2.render("Wrong Password", True, (0, 0, 0))
    screen.blit(msg,(330,535))
    time.sleep(2)


def draw_rect_alpha(surface):
    s = pygame.Surface((600,210))  
    s.set_alpha(200)               
    s.fill((35,35,35))        
    surface.blit(s, (300,380)) 

if __name__ == '__main__':
    lockscreen()
else:
    main()


