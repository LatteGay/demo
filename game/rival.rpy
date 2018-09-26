layeredimage rival:

    group base:
        attribute outfit1 default
    group left_arm auto:
        attribute down1 default
    group right_arm auto:
        attribute down1 default
    group head auto:
        attribute neutral default

image side rival_side =  LayeredImageProxy("rival", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))

define Rival = Character("Shay", image= "rival",  who_color="#fff2d3", callback=talk_sound, cb_char=1)
define Rival_side = Character("Shay", image= "rival_side",  who_color="#fff2d3", callback=talk_sound, cb_char=1)
