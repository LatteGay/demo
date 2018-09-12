
layeredimage bestie:
    group base:
        attribute placeholder default

image side bestie_side =  LayeredImageProxy("bestie", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))
image bestie = LayeredImageProxy("bestie", Transform (zoom=0.95))

define Bestie = Character("Asher",   image= "bestie_1",  who_color="#c8ffc8")
define Bestie_side = Character("Asher", image= "bestie_side", who_color="#f85f22")
