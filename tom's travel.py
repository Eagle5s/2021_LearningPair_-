import random
import pygame
import os

pygame.init()


screen_width = 700
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("tom")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))

credit= pygame.image.load(os.path.join(image_path, "credit.png"))

intro_image1= pygame.image.load(os.path.join(image_path, "intro1.png"))
intro_image2= pygame.image.load(os.path.join(image_path, "intro2.png"))
intro_image3= pygame.image.load(os.path.join(image_path, "intro3.png"))
intro_image4= pygame.image.load(os.path.join(image_path, "intro4.png"))
intro_image5= pygame.image.load(os.path.join(image_path, "intro5.png"))
intro_image6= pygame.image.load(os.path.join(image_path, "intro6.png"))
intro_image7= pygame.image.load(os.path.join(image_path, "intro7.png"))
intro_image8= pygame.image.load(os.path.join(image_path, "intro8.png"))

die_sound = pygame.mixer.Sound('images/die.mp3')
Acid_sound = pygame.mixer.Sound('images/jump.mp3')

running = True

def intro():
    screen.blit(intro_image1, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image2, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image3, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image4, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image5, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image6, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image7, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(intro_image8, (0, 0)) 
    pygame.display.update()
    pygame.time.delay(3000)
    play()



def play():
    tom = pygame.image.load(os.path.join(image_path, "tom.png"))
    tom_size = tom.get_rect().size
    tom_width = tom_size[0]
    tom_height = tom_size[0]
    tom_x_pos = (screen_width / 2) - (tom_width / 2)
    tom_y_pos = screen_height - tom_height
    

    to_x = 0
    tom_speed = 15 


    acid = pygame.image.load(os.path.join(image_path, "Acid.png"))
    acid_size = acid.get_rect().size
    acid_width = acid_size[0]
    acid_height = acid_size[1]
    acid_x_pos = random.randint(0, screen_width - acid_width)
    acid_y_pos = 0
    acid_speed = 20
    Acid_sound.play()
    
        

   
    global running
    
    while running:
        dt = clock.tick(30)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= tom_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += tom_speed
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
    
        
        tom_x_pos += to_x
        
        
        if tom_x_pos < 0:
            tom_x_pos = 0
        elif tom_x_pos > screen_width - tom_width:
            tom_x_pos = screen_width - tom_width

        acid_y_pos += acid_speed

        if acid_y_pos > screen_height:
            acid_y_pos = 0
            acid_x_pos = random.randint(0, screen_width - acid_width)
    

        tom_rect = tom.get_rect()
        tom_rect.left = tom_x_pos
        tom_rect.top = tom_y_pos

        acid_rect = acid.get_rect()
        acid_rect.left = acid_x_pos
        acid_rect.top = acid_y_pos
        
        screen.blit(background, (0, 0))
        screen.blit(tom, (tom_x_pos, tom_y_pos))
        screen.blit(acid, (acid_x_pos, acid_y_pos))

        if tom_rect.colliderect(acid_rect):
              print("죽었습니다")
              die_sound.play()
              running = False
              screen.blit(credit, (0, 0)) 
              pygame.display.update()
              pygame.time.delay(3000)
              
        if running == False:
            isNeedToRestart = True 
            while isNeedToRestart:    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                        isNeedToRestart = True
                        running = True
                        pygame.display.update()
                        if running == True:
                            play()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                        isNeedToRestart = False
                        print("게임 끝")
                        break
                break
                        
        pygame.display.update()
            
intro()

         
pygame.quit()

