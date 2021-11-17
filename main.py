from ursina import *
from ursina import texture
from ursina import collider
from ursina import text
from ursina.prefabs.first_person_controller import FirstPersonController
from SkyViewCamera import *
import requests
import json

Text.default_font = './assets/BMJUA_ttf.ttf'

class Main_box(Button):
    def __init__(self):
        self.open_field = True
        super().__init__(
            parent=scene,
            model='plane',
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.color(0,0,0.9),
            scale=1.5*3,
        )
    
    def on_click(self):
        self.open_field = False

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

class alarm_window(Text):
    def __init__(self, alarm_str):
        super().__init__(
            parent=camera.ui,
            text=alarm_str,
            position=(-.425, .1)
        )

def show_alarm_window(alarm_str):
    alarm = alarm_window(alarm_str)
    alarm.create_background(padding=0.05, color=color.black66)  
    Button(model='quad', parent=alarm, scale=(0.25, 0.1), origin = (-.5,.5), color=color.black66)

class Fake_Building(Button):
    def __init__(self):
        self.built_billding = False
        self.go_to_R_store = False
        self.render_position = (0, 0)
        super().__init__(
            model='cube',
            color=color.color(0,0,0, 0.66),
            scale_y=1.1, 
            position=(0,0.55,0),
            highlight_color=color.color(0,0,0, 0.66)
        )
    
    def on_click(self):
        if self.built_billding:
            self.remove()
            self.go_to_R_store = True
            res = requests.post(URL+'chain/add_block', data=json.dumps({
                            'Sender': 'USER',
                            'Receiver': 'ChainSERVER',
                            'Map Position': tuple(self.render_position),
                        }))
            show_alarm_window('  '*(int(len(res.text)/2.07))+'MAP TOKEN\n\n'+res.text)
            mouse.locked = False
    
class store_Building(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture='white_cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.color(0,0,0.9),
            scale_y=1.1,
            position=(0,0.55,0)
        )
    

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
F_store = Fake_Building()
F_store.parent = main_box
R_store = store_Building()
R_store.parent = main_box
R_store.hide()
McDonald_text = Text(text='McDonald', parent=R_store, position=(-0.14, 0.7), scale=3)
player = SkyViewCamera(x=5, y=7, z=-3, origin_y=10, rotation=(30,10,0))

FPS_player_lock = False

URL = 'http://127.0.0.1:5000/'

def update():
    if FPS_player_lock == False:
        x = 0
        for i in maplist:
            z = 0
            for j in i:
                if main_box.open_field:
                    if j.intersects():
                        j.hide()
                    else:
                        j.show()
                    
                    if x >= 1 and x <= 11 and z >= 1 and z <= 11:
                        if j.lock_on_mouse:
                            main_box.position = j.po
                else:
                    j.on_mouse_exit()
                    F_store.highlight_color=color.color(0,0,0,0.50)
                    F_store.render_position = main_box.position
                    F_store.built_billding = True
                    if F_store.go_to_R_store:
                        R_store.show()
                z += 1
            x+=1
    
    #hit_info = voxel.intersects()
    #if hit_info.hit:
    #    voxel.hide()

def input(key):
    if held_keys['control'] and key == 'r':
        FirstPersonController()
        for i in maplist:
            for j in i:
                j.collider = BoxCollider(j, center=(0,0,0), size=(1.5, 0, 1.5))

app.run()