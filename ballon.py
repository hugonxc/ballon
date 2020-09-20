import pyxel
from body import *

FPS = 60
dt = 1 / FPS
pyxel.init(180, 120, fps=FPS)
pyxel.load("./assets/ballon.pyxres")

sp = Space()
 
sky = sp.add_sprite(
    img=1,
    img_x=0,
    img_y=0,
    width=180,
    height=120,
    color_bkg = pyxel.COLOR_BLACK,
    pos=(0, 0),
    vel=(0,0),
)

ballon = sp.add_sprite(
    img=0,
    img_x=2,
    img_y=0,
    width=13,
    height=16,
    color_bkg = pyxel.COLOR_BLACK,
    pos=(0, 103),
    vel=(0,0),
)

mountain = sp.add_sprite(
    img=0,
    img_x=0,
    img_y=16,
    width=63,
    height=32,
    color_bkg = pyxel.COLOR_BLACK,
    pos=(60, 90),
    vel=(0,0),
)

force = 0

def show_force(force):
    pyxel.text(0, 0, "force:" + str(force), 0)


def show_velocity(vx, vy):
    x = str(round(vx, 2))
    y = str(round(vy, 2))

    pyxel.text(150, 0, "x:"+x, 0)
    pyxel.text(150, 7, "y:"+y, 0)    


def ballon_control():
    global force
    # Add force for each dt
    if (pyxel.btn(pyxel.KEY_UP) or
       pyxel.btn(pyxel.KEY_DOWN) or  
       pyxel.btn(pyxel.KEY_LEFT) or 
       pyxel.btn(pyxel.KEY_RIGHT)):
        
        force += 1

    #  Apply force based on the arrow key
    if pyxel.btnr(pyxel.KEY_UP):
        ballon.apply_force(0, -force)
        force = 0

    if pyxel.btnr(pyxel.KEY_DOWN):
        ballon.apply_force(0, force)
        force = 0

    if pyxel.btnr(pyxel.KEY_LEFT):
        ballon.apply_force(-force, 0)
        force = 0

    if pyxel.btnr(pyxel.KEY_RIGHT):
        ballon.apply_force(force, 0)
        force = 0

    #Handbrake 
    if pyxel.btn(pyxel.KEY_SPACE):
        b_force_x = (ballon.mass * ballon.velocity_x) / dt
        b_force_y = (ballon.mass * ballon.velocity_y) / dt

        ballon.apply_force(-b_force_x, -b_force_y)

def win():
    if ballon.position_y >= 103:
        if ballon.position_x >= 140 and ballon.position_x <= 150:
            pyxel.text(70, 50, "Well Done!", pyxel.frame_count % 16)

def update():
    ballon_control()
    sp.update(dt)
 
def draw():
    pyxel.cls(pyxel.COLOR_BLACK)

    # Draw bodies
    sp.draw()

    # Print force and velocity for user 
    show_force(force)
    show_velocity(ballon.velocity_x, ballon.velocity_y)

    win()

pyxel.run(update, draw)