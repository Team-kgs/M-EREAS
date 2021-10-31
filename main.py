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

for z in range(8):
    for x in range(8):
        voxel = Voxel((x*1.5, 0, z*1.5))
        voxel.rotation_y = 90

player = SkyViewCamera(y=2, origin_y=3)
# ground = Entity(model='plane', scale=20, texture='white_cube', texture_scale=(20,20,20), collider='plane')

app.run()