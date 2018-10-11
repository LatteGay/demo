################# phone code stars ###################

image phone = "images/cellphone_template/phone.png"


# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.3 yoffset 100

transform phone_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300


transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1

transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message


#### labels to shortcut stuff so you dont need to copypaste stuff repeatedly! #####

label phone_start:
    window hide
    show phone at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_msg:
    $ renpy.pause()
    hide screen phone_message
    $ renpy.pause(0.1)
    return

label phone_msg2:
    $ renpy.pause()
    hide screen phone_message2
    $ renpy.pause(0.1)
    return

label phone_msgi:
    $ renpy.pause()
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return


label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return

label phone_end:
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    show phone at phone_hide
    $ renpy.pause(0.2)
    return

label message(who, what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return

label reply_message(what):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    return

label message_img(who, what,img):
    $ renpy.pause()
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    return


label message_start(who, what):
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    return

######### phone code ends here ##########


# ################Parallax###############
# init 800 python:
#     class MouseParallax(renpy.Displayable):
#         def __init__(self,layer_info):
#             super(renpy.Displayable,self).__init__()
#             self.xoffset,self.yoffset=0.0,0.0
#
#             self.sort_layer=sorted(layer_info,reverse=True)
#             cflayer=[]
#             masteryet=False
#             for m,n in self.sort_layer:
#                 if(not masteryet)and(m<0):
#                     cflayer.append("master")
#                     masteryet=True
#                 cflayer.append(n)
#             if not masteryet:
#                 cflayer.append("master")
#             cflayer.extend(["transient","screens","overlay"])
#             config.layers=cflayer
#             config.overlay_functions.append(self.overlay)
#             return
#         def render(self,width,height,st,at):
#             return renpy.Render(width,height)
#         def parallax(self,m):
#             func = renpy.curry(trans)(disp=self, m=m)
#             return Transform(function=func)
#         def overlay(self):
#             ui.add(self)
#             for m,n in self.sort_layer:
#                 renpy.layer_at_list([self.parallax(m)],n)
#             return
#         def event(self,ev,x,y,st):
#             import pygame
#             if ev.type==pygame.MOUSEMOTION:
#                 self.xoffset,self.yoffset=((float)(x)/(config.screen_width))-0.5,((float)(y)/(config.screen_height))-0.5
#             return
#     #MouseParallax([(-20,"farthestBack"),(-50,"farBack"),(-80,"back"),(-30,"front"),(50,"inyourface")])
#
#     MouseParallax([(farthestBackValue,"farthestBack"),(farBackValue,"farBack"),(backValue,"back"),(-30,"front"),(50,"inyourface")])
#
#     def trans(d, st, at, disp=None, m=None):
#         d.xoffset, d.yoffset = int(round(m*disp.xoffset)), int(round(m*disp.yoffset))
#         return 0
