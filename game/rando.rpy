layeredimage rando:
    group base:
        attribute placeholder default

image side rando_side =  LayeredImageProxy("rando", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))

define Rando = Character("Customer", image= "rando",  who_color="#fff2d3")
define Rando_side = Character("Customer", image= "rando_side",  who_color="#fff2d3")
