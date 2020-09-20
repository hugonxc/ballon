import pyxel

class Body:
    def __init__(self, pos=(0, 0), vel=(0, 0), mass=1.0, color=0):
        self.position_x, self.position_y = pos
        self.velocity_x, self.velocity_y = vel
        self.mass = mass
        self.color = color
 
        self.force_x = 0.0
        self.force_y = 0.0
 
    def apply_force(self, fx, fy):
        self.force_x += fx
        self.force_y += fy        
 
    def update_velocity(self, dt):
        acc_x = self.force_x / self.mass
        acc_y = self.force_y / self.mass
        
        self.velocity_x += acc_x * dt
        self.velocity_y += acc_y * dt
 
        self.force_x = self.force_y = 0.0
 
    def update_position(self, dt):
        self.position_x += self.velocity_x * dt
        self.position_y += self.velocity_y * dt
 
    def draw(self):
        pyxel.pset(self.position_x, self.position_y, self.color)
 

class Circle(Body):
    def __init__(self, radius, *args, **kwargs):
        self.radius = radius
        super().__init__(*args, **kwargs)
    
    def draw(self):
        pyxel.circ(self.position_x, self.position_y, self.radius, self.color)
 
class Rect(Body):
    def __init__(self, width, height, *args, **kwargs):
        self.width = width
        self.height = height
        super().__init__(*args, **kwargs)
    
    def draw(self):
        pyxel.rect(self.position_x, self.position_y, self.width, self.height, self.color)

class Sprite(Body):
    def __init__(self, width, height, img, img_x, img_y, color_bkg, *args, **kwargs):
        self.width = width
        self.height = height
        self.img = img
        self.img_x = img_x
        self.img_y = img_y
        self.color_bkg = color_bkg
        super().__init__(*args, **kwargs)
    
    def draw(self):
        pyxel.blt(self.position_x, self.position_y, self.img, self.img_x, self.img_y, self.width, self.height, self.color_bkg)

class Space:
    def __init__(self):
        self.bodies = []
 
    def add_body(self, body):
        self.bodies.append(body)
 
    def add_circle(self, *args, **kwargs):
        circle = Circle(*args, **kwargs)
        self.add_body(circle)
        return circle
 
    def add_rect(self, *args, **kwargs):
        rect = Rect(*args, **kwargs)
        self.add_body(rect)
        return rect

    def add_sprite(self, *args, **kwargs):
        sprite = Sprite(*args, **kwargs)
        self.add_body(sprite)
        return sprite
 
    def update(self, dt):
        for body in self.bodies:
            body.update_velocity(dt)
 
        for body in self.bodies:
            body.update_position(dt)
 
    def draw(self):
        for body in self.bodies:
            body.draw()