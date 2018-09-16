layeredimage boss:
    group base:
        attribute work default

image side boss_side =  LayeredImageProxy("rival", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))

define Boss = Character("Jun", image= "boss",  who_color="#fff2d3")
define Boss_side = Character("Jun", image= "boss_side",  who_color="#fff2d3")
