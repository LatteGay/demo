layeredimage boss:

        group base:
            attribute outfit1 default
        group left_arm auto:
            attribute down1 default
        group right_arm auto:
            attribute down1 default
        group head auto:
            attribute neutral default

image side boss_side =  LayeredImageProxy("boss", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=-80, yoffset=-200))

define Boss = Character("Jun", image= "boss",  who_color="#fff2d3")
define Boss_side = Character("Jun", image= "boss_side",  who_color="#fff2d3")
