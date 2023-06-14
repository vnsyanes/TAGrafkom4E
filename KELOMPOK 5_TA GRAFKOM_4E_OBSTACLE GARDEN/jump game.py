from ursina import *
import random
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()


flower = Entity(model = "Flower.obj", double_sided = True,texture = "flowers-01.png",scale =1.5, x = 25, z = -10, y = -1.5)
flower = Entity(model = "Flower.obj", double_sided = True,texture = "flowers-01.png",scale =1.5, x = 20, z = -5, y = -1.5)
piknik = Entity(model="food.obj",double_sided = True, scale =1.5,x = 20,z = -8, y = -1.5)
Sphere = Entity(model="AlanTree.fbx", scale = 0.3,z = 30, y = -1.5, x = 0, rotation_x= -90, collider='sphere')
tree = Entity(model = "tree_leaf.fbx", texture = "tree2_tex.png",rotation_x=180,double_sided = True, scale = -0.010, position= (20,-1.5,-5))
grid = Entity(model=Grid(20,20), scale=18, color=color.white, rotation_x=90, z=9, y = -1, collider = 'box')
scene = Entity(model="scene.gltf", scale = 0.65,z = 10, y = -1.5)
ground = Entity(model="plane",scale = 60, collider = "box", color=color.green, texture="grass", y=-1.5, z = 10)
Sky()


start = Entity(model = 'cube', scale=(2,1,2), color=color.red, collider = 'box', x =0,z=0)
finish = Entity(model = 'cube', scale=(2,1,2), color=color.green, collider = 'box', x =0,z=20)


#ss
# wall bagian belakang
bwall1 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =0,y=-0.1,z=-20)
bwall2 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =6.7,y=-0.1,z=-20)
bwall3 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =13.4,y=-0.1,z=-20)
bwall4 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =20.1,y=-0.1,z=-20)
bwall5 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =26.8,y=-0.1,z=-20)
bwall6 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-6.7,y=-0.1,z=-20)
bwall7 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-13.4,y=-0.1,z=-20)
bwall8 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-20.1,y=-0.1,z=-20)
bwall9 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-26.8,y=-0.1,z=-20)

# wall bagian kanan
rwall1 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=10)
rwall2 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=16.7)
rwall3 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=23.4)
rwall4 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=30.1)
rwall5 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=36.8)
rwall7 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=3.3)
rwall8 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=-3.4)
rwall9 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=-10.1)
rwall10 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =30,y=-0.1,z=-16.8)

# wall bagian kiri
lwall1 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=10)
lwall2 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=16.7)
lwall3 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=23.4)
lwall4 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=30.1)
lwall5 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=36.8)
lwall7 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=3.3)
lwall8 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=-3.4)
lwall9 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=-10.1)
lwall10 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', rotation_y=90, x =-30,y=-0.1,z=-16.8)

# wall bagian depan
fwall1 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =0,y=-0.1,z=40)
fwall2 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =6.7,y=-0.1,z=40)
fwall3 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =13.4,y=-0.1,z=40)
fwall4 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =20.1,y=-0.1,z=40)
fwall5 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =26.8,y=-0.1,z=40)
fwall6 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-6.7,y=-0.1,z=40)
fwall7 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-13.4,y=-0.1,z=40)
fwall8 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-20.1,y=-0.1,z=40)
fwall9 = Entity(model = 'cube', scale=(7,3,0), texture = 'wall.png', collider = 'box', x =-26.8,y=-0.1,z=40)

cords = []
blocks = []
z = 0 # block depan belakang
x = 0 # block kiri kanan
for i in range(6):
    z += 3
    for u in range(3):
        x = random.randrange(-8,8,3) 
        cords.append((x,z))
        print(cords)
        bb = Entity(model = 'cube', scale=(2,1,2),texture='stone.jpg', collider = 'box', x =x,z=z)
        blocks.append(bb)

# player
player = FirstPersonController(collider = 'box', position=(0.5,1,0.5))

player.original_speed = player.speed

def input(key):
    if key == 'shift':
        player.speed = player.original_speed * 2
    elif key == 'shift up':
        player.speed = player.original_speed
    elif key == 'escape':
        application.quit()
        
# untuk close aplikasi
def close_app():
    application.quit()
    
# update function dimana block menghilang setelah tersentuh selama 2 detik 
# function menang kalah
def update():   
    count = 0   
    hit_info = player.intersects()
    if hit_info.hit:
        if hit_info.entity in blocks:
            hit_info.entity.fade_out(duration=2)
            destroy(hit_info.entity,delay=2)
        elif hit_info.entity == grid: # jika terkena grid maka game over
            end_game('GAME OVER')    
        elif hit_info.entity == finish: # jika menyentuh block finish maka menang  
            end_game('YOU WON ')

     
# pop up info menang kalah       
def end_game(user_message):
    message = Text(text = user_message, scale=2, origin=(0,0), background=True, color=color.blue)
    application.pause()
    mouse.locked = False

app.run()