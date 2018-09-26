init -2 python:
    # Talking Beeps
    #Register Audio Channel
    renpy.music.register_channel("Chan1", mixer= "sfx", loop=True)
    #play talk sounds
    def clicks(on=False, char=0):
        if on:
            if char==0:
                renpy.music.play("music/sfx/beep004.wav", channel="Chan1")
            if char==1:
                renpy.music.play("music/sfx/beep009.wav", channel="Chan1")
            if char==2:
                renpy.music.play("music/sfx/beep008.wav", channel="Chan1")
            if char==3:
                renpy.music.play("music/sfx/beep007.wav", channel="Chan1")
        else:
            renpy.music.stop(channel="Chan1", fadeout=0.1)


    def talk_sound(event, char=0,**kwargs):
            if event == "show" or event == "begin":
                clicks(True, char)
            if event == "slow_done" or event == "end":
                clicks(False, char)
