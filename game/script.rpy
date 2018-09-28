# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg_shop = "backgrounds/coffee_shop.png"
image bg_cs_lounge = "backgrounds/bg_cs_lounge.png"
image bg_apartment = "backgrounds/bg_appartment.png"
image bg_cobedroom = "backgrounds/bg_room.png"
image bg_fallsidewalk = im.Scale("backgrounds/fallsidewalk.png",1920,1080)
image bg_busystreet = "backgrounds/busystreet.png"
image bg_park = "backgrounds/bg_park.png"
image bg_dorm = "backgrounds/bg_dorm.png"
# The game starts here.

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
    label j_scenea14:
    label end:
    #show CoWorker

    # These display lines of dialogue.

    #"<Insert Generic COFFEE HOUSE NAME Here>"

    #CoWorker "HELLO WELCOME TO COFFEE SHOP?"

    # This ends the game.

    return
