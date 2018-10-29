# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define dis = { "master" : Dissolve(0.5) }
image bg_shop = "backgrounds/bg_cs_main.png"
image bg_cs_lounge = "backgrounds/bg_cs_lounge.png"
image bg_apartment = "backgrounds/bg_appartment.png"
image bg_cobedroom = "backgrounds/bg_room.png"
image bg_fallsidewalknight =im.Scale( im.MatrixColor("backgrounds/fallsidewalk.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0)),1920,1080)
image bg_fallsidewalk = im.Scale("backgrounds/fallsidewalk.png",1920,1080)
image bg_busystreet = "backgrounds/bg_street.png"
image bg_park = "backgrounds/bg_park.png"
image bg_dorm = "backgrounds/bg_dorm.png"
image email2 =  Transform("emails/email2.PNG", yoffset=-300)
image snow = Snow("backgrounds/snow.png")

define audio.goodmorning = "music/Good-Morning.mp3"
define audio.happy = "music/Happy-Song.mp3"  #coffee shop theme 1
define audio.dolphin = "music/I-spoke-to-a-dolphin-and-this-is-what-it-told-me.mp3"
define audio.nameless = "music/Nameless-Beat.mp3" #coffee shop theme 2
define audio.park = "music/Park-Avenue.mp3" #sadish song
define audio.see = "music/See-You-There.mp3"
define audio.water = "music/Water-Song.mp3"
define audio.jazz = "music/My-Name-is-Jazz.mp3"
define audio.city = "music/City-Lights.mp3"
define audio.flying = "music/Flying.mp3"
define audio.theloop = "music/The-Loop.mp3"
define audio.juxtaposition = "music/juxtaposition.mp3"
define audio.love_beat = "music/Love-Beat.mp3" # date song
define audio.alarm = "music/sfx/android-oxygen.mp3"
define audio.espresso = "music/sfx/Making-Espresso.mp3"
define audio.bg_coffeeshop = "music/sfx/CoffeeShopNoise.mp3"
define audio.phonevibratelong= "music/sfx/Phone_Vibrating-Sound_Explorer.mp3"
define audio.bg_car = "music/sfx/ambience_busy_street_road.mp3"
# The game starts here.

label splashscreen:
    "This is a release for Yuri Game Jam 2018 and is still a work in progress. We are working on a more polished version that is going to be released in about a month"
    return

label start:
    # label j_scenea1:
    # jump scene_a1
    # label j_scenea2:
    # jump scene_a2
    # label j_scenea3:
    # jump scene_a3
    # label j_scenea4:
    # jump scene_a4
    # label j_scenea5:
    # jump scene_a5
    # label j_scenea6:
    # jump scene_a6
    # label j_scenea7:
    # jump scene_a7
    # label j_scenea8:
    # jump scene_a8
    # label j_scenea9:
    # jump scene_a9
    # label j_scenea10:
    # jump scene_a10
    # label j_scenea11:
    # jump scene_a11
    # label j_scenea12:
    # jump scene_a12
    # label j_scenea13:
    # jump scene_a13
    # label j_sceneb1:
    # jump scene_b1
    # label j_sceneb2:
    # jump scene_b2
    # label j_sceneb3:
    # jump scene_b3
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

    #show CoWorker

    # These display lines of dialogue.

    #"<Insert Generic COFFEE HOUSE NAME Here>"

    #CoWorker "HELLO WELCOME TO COFFEE SHOP?"

    # This ends the game.

    return
