# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.

label splashscreen:
    "This is a release for Yuri Game Jam 2018 and is still a work in progress. We are working on a more polished version that is going to be released in about a month. Please look forward to version 2.0!"
    return

label start:
    label j_scenea1:
    jump scene_a1
    label j_scenea2:
    jump scene_a2
    label j_scenea3:
    jump scene_a3
    label j_scenea4:
    jump scene_a4
    label j_scenea5:
    jump scene_a5
    label j_scenea6:
    jump scene_a6
    label j_scenea7:
    jump scene_a7
    label j_scenea8:
    jump scene_a8
    label j_scenea9:
    jump scene_a9
    label j_scenea10:
    jump scene_a10
    label j_scenea11:
    jump scene_a11
    label j_scenea12:
    jump scene_a12
    label j_scenea13:
    jump scene_a13
    label j_sceneb1:
    jump scene_b1
    label j_sceneb2:
    jump scene_b2
    label j_sceneb3:
    jump scene_b3
    label j_sceneb4:
    jump scene_b4
    label j_sceneb5:
    jump scene_b5
    label j_sceneb6:
    jump scene_b6
    label j_sceneb7:
    jump scene_b7
    label j_sceneb8:
    jump scene_b8
    label j_sceneb9:
    jump scene_b9
    label j_sceneb10:
    jump scene_b10
    label j_sceneb11:
    jump scene_b11
    label j_scene_epilogue:
    jump scene_epilogue
    label end:
    call credits

    #show CoWorker

    # These display lines of dialogue.

    #"<Insert Generic COFFEE HOUSE NAME Here>"

    #CoWorker "HELLO WELCOME TO COFFEE SHOP?"

    # This ends the game.
    return

    label credits:
    play music love_beat loop fadein 3.0
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Writer', '{a=http://shepardtsoni.tumblr.com/}shepardtsoni{/a}'), ('Writer', '{a=http://elystias.tumblr.com/}elystias{/a}'), ('Sprites and CG', '{a=http://magicalzebra.tumblr.com/}magicalzebra{/a} Jasmine Lau'), ('Sprite Colorist', '{a=http://fiori-ed-orrori.tumblr.com/}fiori-ed-orrori{/a}'),  ('Backgrounds', '{a=http://sarahanne-art.tumblr.com/}sarahannebirch{/a}'), ('Programming', '{a=http://hiddenbooty.tumblr.com/}hiddenbootyz{/a}'), ('Programming', '{a=http://hiddenexample.tumblr.com/}hiddenexample{/a}'), ('Music', 'TazLazuli')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
