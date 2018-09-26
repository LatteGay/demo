
layeredimage bestie:
    group base:
        attribute outfit1 default
    group head:
        attribute neutral default

image side bestie_side =  LayeredImageProxy("bestie", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))

define Bestie = Character("Asher",   image= "bestie",  who_color="#fff2d3",callback=talk_sound, cb_char=3)
define Bestie_side = Character("Asher", image= "bestie_side", who_color="#fff2d3",callback=talk_sound, cb_char=3)
