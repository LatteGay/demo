
layeredimage friend:
    group base:
        attribute placeholder default

image side asher_side =  LayeredImageProxy("rival", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))

define Asher = Character("Asher", image= "friend",  who_color="#c8ffc8")
define Asher_side = Character("Asher", image= "asher_side",  who_color="#f85f22")
