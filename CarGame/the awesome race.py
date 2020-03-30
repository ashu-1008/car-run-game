import pygame,sys,random,os,time,math

from pygame.locals import *

#some constants

CARMAXSPEED=8
CARMINSPEED=2
OBJECTSPEED=5
FPS=400
life=3
move_left = move_right = move_up = move_down = False
score=0
#font type
font1='Algerian'
font2='Andalus'
font3='Calibri Light'
font4='Arial Black'
font5='Bauhaus 93'

#color
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
DARKGREEN=(0,150,0)



#some functions
#writing for event in pygame.event.get(): in every function slows down program,
#write it only once in game's main event handler
#and call exit only once in main game event handler not in every function with while loop
def Exit():
    pygame.quit()
    sys.exit()
def Exit1( event ):
    if (event.type == QUIT ) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            Exit()   

def WaitForPlayerToPressKey( event ):
    while True:
        Exit1( event)
        if event.type == KEYDOWN :          
            return

def CarHasHitObject(car,objects):
    for c in objects:
        if playerRect.colliderect(c['rect']):
            return True
    return False

def drawText(text, font, surface, x, y,TEXTCOLOR):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#set up the pygame
pygame.init()
frames=pygame.time.Clock()
SURFACE=pygame.display.set_mode((0,0),FULLSCREEN)
pygame.display.set_caption("The Game")
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

#half dimensions of window
window_width_x=SURFACE.get_rect().centerx
window_height_y=SURFACE.get_rect().centery
width=2*SURFACE.get_rect().centerx
height=2*SURFACE.get_rect().centery
#font objects
titlefont_1 = pygame.font.SysFont( font1,125)
titlefont_2 = pygame.font.SysFont( font2,40)
titlefont_3 = pygame.font.SysFont( font1,120)
titlefont_4 = pygame.font.SysFont( font4, 20)
titlefont_5 = pygame.font.SysFont( font2,60)

#loading screen
SURFACE.fill(WHITE)
drawText("LOADING.",titlefont_4, SURFACE, window_width_x-50, window_height_y,BLACK)
pygame.display.update()
#car images
car1=pygame.transform.scale( pygame.image.load('images\car5.png'), (250,210))
car2=pygame.transform.scale( pygame.image.load('images\car1.png'), (260,250))
car3=pygame.transform.scale( pygame.image.load('images\car3.png'), (230,250))
car4=pygame.transform.scale( pygame.image.load('images\car2.png'), (230,250))
car5=pygame.transform.scale( pygame.image.load('images\car4.png'), (200,250))


car=[ car1, car2, car3, car4, car5 ]

#Images

#start background image
BGStartImageScaled = pygame.transform.scale ( pygame.image.load('images\start.png'),(int(width*0.6),height) )
BGStartImageRect = BGStartImageScaled.get_rect()
BGStartImageRect.centerx = SURFACE.get_rect().centerx
BGStartImageRect.centery = SURFACE.get_rect().centery
high_bg_image=pygame.transform.scale(pygame.image.load("images\high_image.jpg"),(width,height))
#startimage
StartImageScaled = pygame.transform.scale( pygame.image.load( 'images\start5.png'), (350,150))
StartImageRect = pygame.Rect( -width*0.12,height*0.32, 330,150)
StartImageX = BGStartImageRect.centerx-530

#high_score
high_image=pygame.transform.scale(pygame.image.load('images\high_score.png'),(270,100))
high_image_rect=pygame.Rect(-width*0.1,height*0.55,320,150)
SURFACE.fill(WHITE)
drawText("LOADING..",titlefont_4, SURFACE, window_width_x-50, window_height_y,BLACK)
pygame.display.update()
#end image
EndImageScaled = pygame.transform.scale( pygame.image.load('images\end2.png'), (270,100))
EndImageRect = pygame.Rect(-width*0.1,height*0.75,320,100)

#arrows
back_arrow=pygame.transform.scale( pygame.image.load('images\Back_arrow.png'), (70,40))
back_arrow_rect=pygame.Rect(width*0.02,height*0.02,70,40)
#right arrow
RightImageScaled = pygame.transform.scale( pygame.image.load('images\Arrow.png'), (50,50))
RightImageRect = pygame.Rect(BGStartImageRect.centerx-300,450,50,50)

#left arrow
LeftImageScaled = pygame.transform.flip(RightImageScaled,True,True )
LeftImageRect = pygame.Rect(BGStartImageRect.centerx-600,450,50,50)

#main game images

store1_image_scaled=pygame.transform.scale(
    pygame.image.load('images\store1.png'),(175,150))
store2_image_scaled=pygame.transform.scale(
    pygame.image.load('images\store2.png'),(200,150))
store4_image_scaled=pygame.transform.scale(
    pygame.image.load('images\store4.png'),(120,130))
store5_image_scaled=pygame.transform.scale(
    pygame.image.load('images\store5.png'),(60,50))
store7_image_scaled=pygame.transform.scale(
    pygame.image.load('images\store7.png'),(80,60))
store9_image_scaled=pygame.transform.scale(
    pygame.image.load('images\store9.png'),(120,120))

#life
life_image=pygame.transform.scale(pygame.image.load('images\life.png'),(30,30))

#stores name of screen player is currently on, it also acts as key for screen reference
current_screen = "start_menu"
SURFACE.fill(WHITE)
drawText("LOADING...",titlefont_4, SURFACE, window_width_x-50, window_height_y,BLACK)
pygame.display.update()
#update high score
class high:
    high_score_list=0
    def __init__(self):
        self.first_highscore=0
        self.second_highscore=0
        self.third_highscore=0
        self.fourth_highscore=0
        self.fifth_highscore=0


        
    def high_score_read(self):
        global high_score_list
        if not os.path.exists("high_score.dat"):
            f=open("high_score.dat",'w')
            f.write(str(0)+' ')
            f.write(str(0)+' ')
            f.write(str(0)+' ')
            f.write(str(0)+' ')
            f.write(str(0))
            f.close()
        f=open("high_score.dat",'r')
        high_score_list=f.read().split(' ')
        f.close()
    
    def display(self):
        f=open("high_score.dat",'r')
        high_score_list=f.readline().split(' ')
        self.first_highscore='1.  '+high_score_list[0]
        self.second_highscore='2.  '+high_score_list[1]
        self.third_highscore='3.  '+high_score_list[2]
        self.fourth_highscore='4.  '+high_score_list[3]
        self.fifth_highscore='5.  '+high_score_list[4]
        f.close()
        
    def modify(self):
        for i in high_score_list:                
              #i=int(i)       
                
                if score > int(i):
                    file_new=open("high_score.dat",'w')
                    ind=high_score_list.index(str(i))
                    for a in range(4,0,-1):
                        if score > int(high_score_list[a]):
                            high_score_list[a]=high_score_list[a-1]
                    
                    
                    high_score_list[ind]=str(score)
                    file_new.write(' '.join(high_score_list))
                    
                    file_new.close()
                    break
        current_screen='game_over_draw'            
            
                
high_object=high()
high_object.high_score_read()

#start menu draw
def start_menu_draw ( SURFACE ):
    #start background image
    SURFACE.blit(BGStartImageScaled,( width*0.4,0))
    

    #to play again
    

    #game title1
    drawText("THE AWESOME RACE...", titlefont_1, SURFACE, BGStartImageRect.centerx-650,
             BGStartImageRect.centery-330, RED)

    #exit1
    drawText("PRESS ESCAPE_KEY TO EXIT...", titlefont_4, SURFACE, BGStartImageRect.centerx+340,
             BGStartImageRect.centery+330, RED)

    #startimage
    if StartImageRect.left<width*0.12:
        StartImageRect.move_ip(10,0)
        high_image_rect.move_ip(10,0)
        EndImageRect.move_ip(10,0)
        SURFACE.blit(StartImageScaled,(StartImageRect.left,StartImageRect.top))
        SURFACE.blit(high_image,(high_image_rect.left,high_image_rect.top))
        SURFACE.blit(EndImageScaled,(EndImageRect.left,EndImageRect.top))
        
    else:
        SURFACE.blit(StartImageScaled,(StartImageRect.left,StartImageRect.top))
        SURFACE.blit(high_image,(high_image_rect.left,high_image_rect.top))
        SURFACE.blit(EndImageScaled,(EndImageRect.left,EndImageRect.top))
    

#start menu handler
def start_menu_eventhandler ( event ) :
     global current_screen
     if event.type == MOUSEBUTTONDOWN:
        mousecoordinates = pygame.mouse.get_pos()             #to get mouse position

        if StartImageRect.collidepoint(mousecoordinates):         #move to car select screen           
            current_screen = "car_select"
        elif high_image_rect.collidepoint(mousecoordinates):         #move to car select screen
            current_screen = "high_score"         

        elif EndImageRect.collidepoint(mousecoordinates):       #end program
            Exit()

def high_score_draw(SURFACE):
    global high_object
    SURFACE.blit(high_bg_image,( 0,0))
    drawText("HIGH SCORE", titlefont_1, SURFACE, width*0.3,height*0.1, WHITE)
    high_object.high_score_read()
    high_object.display()
    drawText(high_object.first_highscore, titlefont_2, SURFACE,width*0.35,height*0.3 , WHITE)
    drawText(high_object.second_highscore, titlefont_2, SURFACE,width*0.35,height*0.4 , WHITE)
    drawText(high_object.third_highscore, titlefont_2, SURFACE,width*0.35,height*0.5 , WHITE)
    drawText(high_object.fourth_highscore, titlefont_2, SURFACE,width*0.35,height*0.6 , WHITE)
    drawText(high_object.fifth_highscore, titlefont_2, SURFACE,width*0.35,height*0.7 , WHITE)
    
    drawText("PRESS ESCAPE_KEY TO EXIT...", titlefont_4, SURFACE, BGStartImageRect.centerx+340,
             BGStartImageRect.centery+330, RED)
    
    
    SURFACE.blit(back_arrow,(width*0.02,height*0.02))
def high_score_eventhandler(event):
    global current_screen
    if event.type == MOUSEBUTTONDOWN:
        mousecoordinates = pygame.mouse.get_pos()
        if back_arrow_rect.collidepoint(mousecoordinates):
           current_screen = "start_menu"
#car select screen
c_rect=pygame.Rect(BGStartImageRect.centerx-550,400,200,200)
selected_car = None                 #stores selected car object 
car_index = 0                           #stores index of current car displayed
car_rect = None

car_show_rect = pygame.Rect( BGStartImageRect.centerx-550, 400, 250, 250)

#car select draw
def car_select_draw ( SURFACE ):
    global life,score,sequencer
    score=0
    life=3
    sequencer = 0.0

    SURFACE.blit(BGStartImageScaled,( width*0.4,0))

    #game title2
    drawText("SELECT YOUR CAR...",titlefont_1,SURFACE,BGStartImageRect.centerx-650,
             BGStartImageRect.centery-330,RED)

    #exit2
    drawText("PRESS ESCAPE_KEY TO EXIT...",titlefont_4,SURFACE,BGStartImageRect.centerx+340,
             BGStartImageRect.centery+330,RED)
        
    #arrows
    SURFACE.blit(LeftImageScaled,(BGStartImageRect.centerx-600,450))
    SURFACE.blit(RightImageScaled,(BGStartImageRect.centerx-300,450))
    SURFACE.blit(back_arrow,(width*0.02,height*0.02))                                                                 
    #draw current car
    SURFACE.blit( car[ car_index ], ( car_show_rect.centerx - car[ car_index].get_width()/2, car_show_rect.centery - car[ car_index].get_height()/2 ) )
    

#car select eventhandler
def car_select_eventhandler (event) :
    if event.type == MOUSEBUTTONDOWN:
        global current_screen, car_index, selected_car, car_rect
        mousecoordinates = pygame.mouse.get_pos()             #to get mouse position

        if c_rect.collidepoint(mousecoordinates):                       #select current car
            selected_car = car[ car_index ]
            car_rect = selected_car.get_rect()
            car_rect.center = ( window_width_x - selected_car.get_width()/2 , height - selected_car.get_height() + 50 )
            current_screen = "main_game"

        elif LeftImageRect.collidepoint(mousecoordinates):          #scrool left
            if car_index == 0:
                car_index = 4
            else:
                car_index -= 1
        
        elif RightImageRect.collidepoint(mousecoordinates):         #scroll right
            if car_index == 4:
                car_index = 0
            else:
                car_index += 1
        if back_arrow_rect.collidepoint(mousecoordinates):
           current_screen = "start_menu"



#main_game draw
def main_game_draw( SURFACE ) :
    
    SURFACE.fill(DARKGREEN)
    pygame.draw.polygon(SURFACE,BLACK,((window_width_x*0.9,0),(window_width_x*1.1,0)
                    ,(window_width_x*2,2*window_height_y),(0,2*window_height_y)))
    pygame.draw.polygon(SURFACE,WHITE,((window_width_x*0.9,0)
                    ,(window_width_x*0.05,2*window_height_y),(window_width_x*0.07,2*window_height_y)))
    pygame.draw.polygon(SURFACE,WHITE,((window_width_x*1.1,0)
                    ,(window_width_x*1.95,2*window_height_y),(window_width_x*1.93,2*window_height_y)))
    
    SURFACE.blit(car[car_index ],(BGStartImageRect.centerx*0.8,window_height_y*1.5))
    SURFACE.blit(store1_image_scaled,(window_width_x*0.07,window_height_y))
    SURFACE.blit(store2_image_scaled,(window_width_x*1.7,window_height_y*0.4))    
    SURFACE.blit(store4_image_scaled,(window_width_x*0.5,window_height_y*1))
    SURFACE.blit(store5_image_scaled,(window_width_x*1.2,window_height_y*0.05))
    SURFACE.blit(store9_image_scaled,(window_width_x*1.18,window_height_y*0.46))
    SURFACE.blit(store7_image_scaled,(window_width_x*1.28,window_height_y*0.7))
    SURFACE.blit(store7_image_scaled,(window_width_x*1.16,window_height_y*0.7))
    SURFACE.blit(store7_image_scaled,(window_width_x*1.22,window_height_y*0.7))
    
    
    drawText("THE AWESOME RACE...",titlefont_1,SURFACE,BGStartImageRect.centerx-500,
                  BGStartImageRect.centery-330,RED)
    
    drawText("PRESS ESCAPE_KEY TO EXIT...",titlefont_4,SURFACE,BGStartImageRect.centerx+340,
                     BGStartImageRect.centery+330,RED)
    drawText("Press Enter_Key TO Start...",titlefont_2,SURFACE,BGStartImageRect.centerx-200,
                     BGStartImageRect.centery-20,RED)
    

#def road(size,SURFACE,image,i):
        

data_dict = { 'house_left' : [[50, 250], [ window_width_x + 120, 0]],
              'house_right' : [[50, 250], [ window_width_x - 120 , width ]],
              'barr_small' : [ 20, 70],
              'barr_medium' : [ 20, 190] ,
              'barr_big' : [ 20, 200]};

house1 = pygame.image.load('images\house1.png')
house2 = pygame.image.load('images\house2.png')
mark = pygame.image.load('images\mark.png')
barr1 = pygame.image.load('images\Barr1.png')
barr2 = pygame.image.load('images\Barr2.png')
barr3 = pygame.image.load('images\Barr3.png')
barr4 = pygame.image.load('images\Barr4.png')
barr5 = pygame.image.load('images\Barr5.png')

diff = 10
speed_mul = 2
house_diff = 150
barr_diff = 400
car_speed = 15
accelerate = False

objects_house = { 'house_left' : [ house1, house2, store1_image_scaled, store2_image_scaled, store5_image_scaled ] ,
            'house_right' : [ house1, house2, store1_image_scaled, store2_image_scaled, store5_image_scaled ] };

objects_barr = { 'barr_small' : [ barr2, barr3],
              'barr_medium' : [ barr1, barr5] ,
              'barr_big' : [ barr4 ] };

barr_path = [ [window_width_x -50 , width*3/4 ] , [window_width_x +50, width/4 ], [window_width_x , width/2 ] ]

def add_house_l( obj_list_house_l ) :
    key = objects_house.keys()[0]
    obj_size = [ data_dict[key][0][0] , data_dict[key][0][1] ]
    obj_pos = [ data_dict[key][1][0] + random.randint(-diff,diff),
                    data_dict[key][1][1] + random.randint(-diff,diff) ]

    t_diff = 0
    if obj_list_house_l : 
        t_diff = obj_list_house_l[-1][3] + house_diff + random.randint(-diff,diff) 
    obj_list_house_l.append( [ random.choice(objects_house[key]) , obj_size , [ ( obj_pos[0] , 0 ), ( obj_pos[1], height + 100 )] , t_diff , key] )

def add_house_r( obj_list_house_r ) :
    key = objects_house.keys()[1]
    obj_size = [ data_dict[key][0][0] , data_dict[key][0][1] ]
    obj_pos = [ data_dict[key][1][0] + random.randint(-diff,diff),
                    data_dict[key][1][1] + random.randint(-diff,diff) ]

    t_diff = 0
    if obj_list_house_r : 
        t_diff = obj_list_house_r[-1][3] + house_diff + random.randint(-diff,diff) 
    obj_list_house_r.append( [ random.choice(objects_house[key]) , obj_size , [ ( obj_pos[0] , 0 ), ( obj_pos[1], height + 100 )] , t_diff , key] )

def add_mark( obj_list_mark ) :
    t_diff = 0
    if obj_list_mark : 
        t_diff = obj_list_mark[-1][3] + 100 
    obj_list_mark.append( [ mark , [ 10, 100 ] , [ ( window_width_x, 0 ), ( window_width_x, height )] , t_diff , 'mark'] )

def add_barr( obj_list_barr ) :
    key = random.choice(objects_barr.keys())
    obj_size = [ data_dict[key][0] , data_dict[key][1] ]
    obj_path = random.choice( barr_path )
    obj_pos =  [ obj_path[0] , obj_path[1] ]

    t_diff = 0
    if obj_list_barr : 
        t_diff = obj_list_barr[-1][3] + barr_diff + random.randint(-diff,diff) 
    obj_list_barr.append( [ random.choice(objects_barr[key]) , obj_size , [ ( obj_pos[0] , -100 ), ( obj_pos[1], height +100 )] , t_diff , key] )


obj_list_house_l = obj_list_house_r = obj_list_mark = obj_list_barr = []
def assign_objects( ):
    global obj_list_house_l, obj_list_house_r, obj_list_mark, obj_list_barr
    obj_list_house_l = []
    for i in range(0,5):
        add_house_l( obj_list_house_l )

    obj_list_house_r = []
    for i in range(0,5):
        add_house_r( obj_list_house_r )

    obj_list_mark = []
    for i in range(0,8):
        add_mark( obj_list_mark )

    obj_list_barr = []
    for i in range(0,5):
        add_barr( obj_list_barr )


def reset( ):
    global obj_list_house , obj_list_mark, accelerate, sequencer, inc_score, car_rect, move_left, move_right, is_collision
    
    obj_list_house = obj_list_mark = []
    accelerate = False
    sequencer = 0.0
    inc_score=0
    is_collision = False
    car_rect.center = ( window_width_x - (selected_car.get_width()/2) + 50 , height - selected_car.get_height() + 50 )
    move_left = move_right = False



#main game eventhandler
def main_game_eventhandler( event ) :
    if event.type == KEYDOWN and event.key ==K_RETURN:
        global current_screen
        current_screen ="main_game_run"
        reset()
        assign_objects()
        


#obj motion
def obj_motion( SURFACE, size, line, img, i, init, key) :
    #line = [ (ix, iy), (fx,fy)]

    t = ( i - init )

    if t < 0 :
        return 0

    if t > line[1][1]:
        return 1 
    s = int( size[0] + (size[1] - size[0])*( t/height ))
    
    img_obj = None
    if key == 'mark' :
        t += int( 1.5*s * speed_mul )
        img_obj = pygame.transform.scale( img, (s/4 , s) )
    elif key == 'house_left' or key == 'house_right':
        t += int( s * speed_mul )
        img_obj = pygame.transform.scale( img, (s,s) )

    elif key == 'barr_small':
        t += int( 2*s * speed_mul )
        img_obj = pygame.transform.scale( img, (s,s) )
    elif key == 'barr_medium':
        t += int( s* speed_mul )
        img_obj = pygame.transform.scale( img, (s,s) )
    elif key == 'barr_big':
        t += int( 0.85*s * speed_mul )
        img_obj = pygame.transform.scale( img, (s,s) )
    
    x = int( line[0][0] + ( t*( line[0][0] - line[1][0] ) / ( line[0][1] - line[1][1] ) ) )
    pos = [ x - (s/2) , t - (s/2) - int( size[0] * speed_mul) - 200 ]

    SURFACE.blit( img_obj, pos )
    return pygame.Rect( pos[0], pos[1] , s, s )



side_rect_left = pygame.Rect( 0,0,width*0.16,height)
side_rect_right = pygame.Rect( width-width*0.16,0,width*0.16,height)

speedo=0
sequencer = 0.0
is_collision = False
invinsibility = False
i_time = 0
def main_game_run_draw(SURFACE):
    pygame.mouse.set_visible(False)
    global score,inc_score,speedo   
    SURFACE.fill(DARKGREEN)
    pygame.draw.polygon(SURFACE,BLACK,((window_width_x*0.9,0),(window_width_x*1.1,0)
                    ,(window_width_x*2,2*window_height_y),(0,2*window_height_y)))
    pygame.draw.polygon(SURFACE,WHITE,((window_width_x*0.9,0)
                    ,(window_width_x*0.05,2*window_height_y),(window_width_x*0.07,2*window_height_y)))
    pygame.draw.polygon(SURFACE,WHITE,((window_width_x*1.1,0)
                    ,(window_width_x*1.95,2*window_height_y),(window_width_x*1.93,2*window_height_y)))
    
    global sequencer, accelerate, move_left , move_right, current_screen, is_collision, invinsibility, i_time

    #draw left houses
    for i in obj_list_house_l :
        if obj_motion( SURFACE, i[1], i[2], i[0], sequencer, i[3], i[4]) == 1 :
            obj_list_house_l.pop( obj_list_house_l.index( i ) )
            add_house_l( obj_list_house_l )        

    #draw right houses
    for i in obj_list_house_r :
        if obj_motion( SURFACE, i[1], i[2], i[0], sequencer, i[3], i[4]) == 1 :
            obj_list_house_r.pop( obj_list_house_r.index( i ) )
            add_house_r( obj_list_house_r )

    #draw road markings
    for i in obj_list_mark :
        if obj_motion( SURFACE, i[1], i[2], i[0], sequencer, i[3], i[4]) == 1 :
            obj_list_mark.pop( obj_list_mark.index( i )  )
            add_mark( obj_list_mark )
    if accelerate :
        sequencer += 6
        inc_score+=1
        
    if inc_score==10:
        score+=1
        inc_score=0
    else :
        sequencer += 1    
    
    if score>50:
        if speedo<10:            
            speedo=score/50
        sequencer+=3*speedo
        

    if move_left :
        car_rect.move_ip( -car_speed , 0 )
    elif move_right :
        car_rect.move_ip( car_speed , 0 )

    if not invinsibility : 
        SURFACE.blit( selected_car, car_rect)
    else :
        if math.sin( time.time() * 40 ) > 0.0 :
            SURFACE.blit( selected_car, car_rect)

    #draw barriers and check for collision
    for i in obj_list_barr :
        run = obj_motion( SURFACE, i[1], i[2], i[0], sequencer, i[3], i[4])
        if run == 1 :
            obj_list_barr.pop( obj_list_barr.index( i )  )
            add_barr( obj_list_barr )
            continue
        elif run == 0 :
            continue
        elif car_rect.colliderect( run ) and not invinsibility :
            is_collision = True
    


    global life,high_score_list
    if   car_rect.colliderect(side_rect_left)  or car_rect.colliderect(side_rect_right): is_collision = True

    #on collision
    if is_collision :
        is_collision = False
        life-=1
        if life == 0:
            #game over
            high_object.modify()
            
        else:
            #still alive
            car_rect.center = ( window_width_x - (selected_car.get_width()/2) + 50 , height - selected_car.get_height() + 50 )
            invinsibility = True
            i_time = int(time.time())
            
    if invinsibility and ( time.time() - i_time) >= 2.0 :
        invinsibility = False
        i_time = 0
   
    global z,y,inc_size
    if life==0:
        current_screen='game_over_draw'
        
    drawText("PRESS ESCAPE_KEY TO EXIT...", titlefont_4, SURFACE, BGStartImageRect.centerx+340,
             BGStartImageRect.centery+330, RED)
    drawText("SCORE:", titlefont_4, SURFACE,width*0.05,
             height*0.08, WHITE)
    drawText(str(score), titlefont_4, SURFACE, width*0.11,
             height*0.08, RED)
    
    #life
    SURFACE.blit(life_image,(width*0.85,height*0.08))
    if life==3:
        SURFACE.blit(life_image,(width*0.88,height*0.08))
        SURFACE.blit(life_image,(width*0.91,height*0.08))
    elif life==2:
        SURFACE.blit(life_image,(width*0.88,height*0.08))
        


def main_game_run_eventhandler(event):
    global move_left , move_right , move_up , move_down, sequencer , accelerate ,current_screen
    if event.type==KEYDOWN:
        if event.key==ord('l'):
            global life
            life=3
        if event.key == K_LEFT or event.key == ord('a'):
            move_right = False
            move_left = True
        if event.key == K_RIGHT or event.key == ord('d'):
            move_left = False
            move_right = True
        if event.key == K_UP or event.key == ord('w'):
            accelerate = True
            move_down = False
            move_up = True
        if event.key == K_DOWN or event.key == ord('s'):
            move_up = False
            move_down = True
    if  event.type==KEYUP:        
        if event.key == K_LEFT or event.key == ord('a'):
            move_left = False
        if event.key == K_RIGHT or event.key == ord('d'):
            move_right = False
        if event.key == K_UP or event.key == ord('w'):
            accelerate = False
            move_up = False
        if event.key == K_DOWN or event.key == ord('s'):
            move_down = False
    pass




def game_over_draw(SURFACE):
    pygame.mouse.set_visible(True)
    SURFACE.fill(BLACK)
    drawText("GAME OVER", titlefont_3, SURFACE,width*0.26,height*0.2 , RED)
    drawText("PRESS ESCAPE_KEY TO EXIT...", titlefont_4, SURFACE, BGStartImageRect.centerx+340,
             BGStartImageRect.centery+330, RED)
    drawText("Your Score is:%s"% str(score), titlefont_5, SURFACE, width*0.38,height*0.5 ,RED)
    drawText("Press Enter_Key TO PLAY AGAIN...",titlefont_2,SURFACE,width*0.03,height*0.9,WHITE)
    
def game_over_eventhandler(event):
    global current_screen
    if event.type==KEYDOWN and event.key==K_RETURN:
        current_screen='car_select'
        
    
    
#dictionary to store the reference of functions associated with the screens
#the keys are name of the screens and values are list of associated fuctions
screen_ref = { "start_menu" : [ start_menu_draw, start_menu_eventhandler ] ,
                    "car_select" : [ car_select_draw, car_select_eventhandler ] ,
                    "main_game" : [ main_game_draw, main_game_eventhandler ] ,
               "main_game_run":[main_game_run_draw,main_game_run_eventhandler],
               "game_over_draw":[game_over_draw,game_over_eventhandler],
               "high_score":[high_score_draw,high_score_eventhandler]}

#main event handler
#only drawing should be handled in this loop not loading images,as it takes time 
while True:

    SURFACE.fill(BLACK)
    
    for event in pygame.event.get():
        Exit1( event )

        #handle events of screen
        if screen_ref [ current_screen ][1] : 
            screen_ref [ current_screen ][1]( event )

    #draw the screen
    if screen_ref [ current_screen ][0] : 
        screen_ref [ current_screen ][0]( SURFACE )
    
    pygame.display.update()
    frames.tick(60)







    
