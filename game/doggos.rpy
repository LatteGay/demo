layeredimage cookie:
    group base auto:
        attribute closed default
define Cookie = Character("Cookie", image= "cookie",  who_color="#fff2d3")
image side Cookie_side = LayeredImageProxy("cookie", Transform(crop=(0, 0, 800, 550)))

layeredimage alfredo:
    group base auto:
        attribute closed default
define Alfredo = Character("Alfredo", image= "alfredo",  who_color="#fff2d3")
image side Alfredo = LayeredImageProxy("alfredo", Transform(crop=(0, 0, 800, 550)))
