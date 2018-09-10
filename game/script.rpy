# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg_shop = "backgrounds/coffee_shop.png"
image bg_apartment = "backgrounds/apartment_kitchen.png"
image bg_cobedroom = im.Scale("backgrounds/bed-bedroom-room-furniture(oil2).jpg", 1920, 1080)
image bg_fallsidewalk = im.Scale("backgrounds/fallsidewalk.png", 1920, 1080)
image bg_busystreet = im.Scale("backgrounds/busystreet.png", 1920, 1080)
# The game starts here.

label start:
    label j_scenea1:
    jump scene_a1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    label j_scenea2:
    jump scene_a2
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    label j_scenea3:
    label j_scenea4:
    jump scene_a4
    label j_scenea5:
    label j_scenea6:
    #show CoWorker

    # These display lines of dialogue.

    #"<Insert Generic COFFEE HOUSE NAME Here>"

    #CoWorker "HELLO WELCOME TO COFFEE SHOP?"

    # This ends the game.

    return
