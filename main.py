from ursina import *
from ursina import texture
from ursina import collider
from ursina import hit_info
from ursina.prefabs.first_person_controller import FirstPersonController
from SkyViewCamera import *

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        self.on_mouse_enter_value = False
        super().__init__(
            parent=scene,
            position=position,
            model='plane',
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.color(0,0,0.9),
            scale=1.5,
        )

    def on_mouse_enter(self):
        self.on_mouse_enter_value = True
    
    def on_mouse_exit(self):
        self.on_mouse_enter_value = False

app = Ursina()

maplist = []
for z in range(13):
    map_m = []
    for x in range(13):
        voxel = Voxel((x*1.5, 0, z*1.5))
        voxel.rotation_y = 90
        map_m.append(voxel)
    maplist += [map_m]

def test_maplist_error(map_position):
    pass

def update():
    z=0 
    for i in maplist:
        x=0
        for j in i:
            if j.on_mouse_enter_value:
                print('x:',str(x)+',', 'z:',str(z))
                m = maplist
                # test_maplist_error 함수 정의해서 에러 걸러내게 만드셈
                # m[z][x], m[z+1][x], m[z-1][x], m[z][x+1], m[z][x-1], m[z+1][x+1], m[z+1][x-1], m[z-1][x+1], m[z-1][x-1]
                
            else:
                j.show()
            x+=1
        z+=1


    #hit_info = voxel.intersects()
    #if hit_info.hit:
    #    voxel.hide()

player = SkyViewCamera(y=5, origin_y=10)

app.run()