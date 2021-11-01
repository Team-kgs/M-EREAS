from ursina import *
from ursina import texture
from ursina import collider
from ursina import hit_info
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
            scale=1.5,
        )
    def on_mouse_enter(self):
        self.scale=1.5*6
        self.show()

    def on_mouse_exit(self):
        self.scale=1.5

app = Ursina()

maplist = []
for z in range(13):
    map_m = []
    for x in range(13):
        voxel = Voxel((x*1.5, 0, z*1.5))
        voxel.collider = 'box'
        voxel.collider = BoxCollider(voxel, center=(0,0,0), size=(0.5,0,0.5))
        voxel.rotation_y = 90
        voxel.visible = True
        map_m.append(voxel)
    maplist += [map_m]

def update():
    for i in maplist:
        for j in i:
            if j.intersects():
                j.hide()
            else:
                j.show()
    #hit_info = voxel.intersects()
    #if hit_info.hit:
    #    voxel.hide()

player = SkyViewCamera(y=5, origin_y=10)

app.run()