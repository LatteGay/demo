# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg_shop = "backgrounds/coffee_shop.png"
image bg_apartment = "backgrounds/apartment_kitchen.png"
image bg_cobedroom = im.Scale("backgrounds/bed-bedroom-room-furniture(oil2).jpg", 1920, 1080)
image bg_fallsidewalk = im.Scale("backgrounds/fallsidewalk.png", 1920, 1080)
image bg_busystreet = im.Scale("backgrounds/busystreet.png", 1920, 1080)
image bg_park = im.Scale("backgrounds/background_spaceocean.png", 1920, 1080)
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
