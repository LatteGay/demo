#COWORKER SPIRTES N STUFF FILES
layeredimage customer:
    group base:
        attribute dress1 default
    group left_arm auto:
        attribute crossed default
    group right_arm auto:
        attribute crossed default
    group head auto:
        attribute neutral default
    group blush auto

image side customer_side =  LayeredImageProxy("coworker", Transform(crop=(0, 0, 800, 550), zoom=0.8, xoffset=40, yoffset=-200))
image customer = LayeredImageProxy("customer", Transform (zoom=0.95))

define Customer = Character("Marlliey", image= "customer")
define Customer_side = Character("Marlliey", image= "customer_side")
