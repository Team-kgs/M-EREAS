from ursina import *
from ursina import texture
from ursina import collider
from ursina.prefabs.first_person_controller import FirstPersonController
from SkyViewCamera import *

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='plane',
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.color(0,0,0.9),
            scale=1.5
        )

app = Ursina()

maplist = [[i+1 for i in range(13)]]+[[1,'x','x','x',5,'x','x','x',9,'x','x','x',13] for i in range(3)] 
print(maplist)

num = 1

for i in maplist:
    for j in i:
        if str(j) == 'x':
            print(x_num)
            if x_num == 5:
                voxel = Voxel((7*1.5, 0, 3*1.5))
                voxel.rotation_y = 90
                voxel.scale=1.5*3
                voxel.highlight_color = color.color(30,1,1) 
                x_num = 0
            x_num+=1
        else:
            voxel = Voxel((j*1.5, 0, num*1.5))
            voxel.rotation_y = 90
    num+=1


player = SkyViewCamera(y=5, origin_y=10)
# ground = Entity(model='plane', scale=20, texture='white_cube', texture_scale=(20,20,20), collider='plane')

app.run()