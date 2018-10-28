#COWORKER SPIRTES N STUFF FILES
layeredimage customer:
    group base auto:
        attribute dress1 default
    group left_arm auto:
        attribute crossed1 default
    group right_arm auto:
        attribute crossed1 default
    group head auto:
        attribute neutral default
    group blush auto

image side customer_side =  LayeredImageProxy("customer", Transform(crop=(0, 0, 800, 650), zoom=0.8))

define Customer = Character("Marllie", image= "customer", who_color="#fff2d3")
define Marrlley = Character("Marrlley", image= "customer", who_color="#fff2d3")
define BandM = Character("Blake&Marley", image= "customer_side", who_color="#fff2d3")
define Customer_side = Character("Marllie", image= "customer_side", who_color="#fff2d3")
