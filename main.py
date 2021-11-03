from ursina import *
from ursina import texture
from ursina import collider
from SkyViewCamera import *

class Main_box(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='plane',
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.color(0,0,0.9),
            scale=1.5*3,
        )
    
    def on_click(self):
        print('dd')


class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        self.po = position
        self.lock_on_mouse = False
        super().__init__(
            parent=scene,
            position=position,
            model='plane',
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.color(0,0,0.9),
            scale=1.5
        )

    def on_mouse_enter(self):
        self.scale=1.5*3
        self.lock_on_mouse = True

    def on_mouse_exit(self):
        self.scale=1.5
        self.lock_on_mouse = False

app = Ursina()

maplist = []
for z in range(13):
    map_m = []
    for x in range(13):
        voxel = Voxel((x*1.5, 0, z*1.5))
        voxel.collider = 'box'
        voxel.collider = BoxCollider(voxel, center=(0,0,0), size=(0.7,0,0.7))
        voxel.rotation_y = 90
        voxel.visible = True
        map_m.append(voxel)
    maplist += [map_m]

main_box = Main_box()

def update():
    x = 0
    for i in maplist:
        z = 0
        for j in i:
            if j.intersects():
                j.hide()
            else:
                j.show()
            if x >= 1 and x <= 11 and z >= 1 and z <= 11:
                if j.lock_on_mouse:
                    main_box.position = j.po
            z += 1
        x+=1
    
    #hit_info = voxel.intersects()
    #if hit_info.hit:
    #    voxel.hide()

player = SkyViewCamera(y=5, origin_y=10)

app.run()