
define MC = Character("Maya", image= "mc",  who_color="#6359d1")
define MC_side = Character("Maya", image= "mc_side",  who_color="#f85f22")

layeredimage mc:
    group base:
        attribute placeholder default

image side mc_side =  LayeredImageProxy("mc", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))