#COWORKER SPIRTES N STUFF FILES
init python:
    class Picker(object):
        def __init__(self, options):
            self.options =  [ i.split() for i in options ]

        def __call__(self, attributes):
            rv = set(attributes)

            for i in self.options:
                if i[0] in attributes:
                    rv.update(i[1:])

            return rv

define Customer = Character("Marlliey", image= "customer")
#define customer_side = Character("Marlliey", image= "customer_side")

layeredimage customer:
    group combos:
        attribute upset null

    attribute_function Picker([
    "upset customer_left_arm_hip customer_right_arm_hips customer_head_sad"
    ])

    group base:
        attribute dress1 default
    group left_arm auto
    group right_arm auto
    group crossed:
        attribute arms default
    group head auto:
        attribute neutral default
    group blush auto
