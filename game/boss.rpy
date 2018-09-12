layeredimage boss:
    group base:
        attribute work default

image side boss_side =  LayeredImageProxy("rival", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))
image boss = LayeredImageProxy("boss", Transform (zoom=0.95))

define Boss = Character("Jun", image= "rival",  who_color="#c8ffc8")
define Boss_side = Character("Jun", image= "coworker_side",  who_color="#f85f22")
