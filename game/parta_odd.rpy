#Scene 1 a
label scene_a1:
    $snooze = 0

    scene bg_cobedroom
    "Blake shifts back under the covers with a groan, squeezing her eyes shut against the sunlight peeking into her messy room. She blindly reaches around her bedside, deciding she now hated the song she'd set as her alarm a few days ago."
    "She'd vowed to be a more responsible, punctual adult at her new job. She'd give herself time to wake up, look presentable, eat something and maybe (hopefully) become a functioning human being by the time she arrived at the coffee shop."
    "{b}{i} But sleep… {/i}{/b}"

    label .alarm1:
        menu:
            "Get up":
                jump .get_up
            "Press snooze. Just five more minutes.":
                "Blake curses aloud the second time and seriously debates the merits of throwing her phone. She can hear cupboards being slammed outside and wonders if her roommate is actually purposefully trying to wake her up. It's not Blake's fault she's not a morning person."
                "She grabs at her phone again. 7:10AM. That would give her half an hour, and thankfully they lived within walking distance…"
                $snooze += 1
                scene black with fade

    label .alarm2:
        scene bg_cobedroom with fade
        menu:
            "Get up":
                jump .get_up
            "Snooze. No, really, five more minutes.":
                if snooze < 4:
                    $snooze += 1
                    scene black with fade
                    pause
                    jump .alarm2
                else:
                    scene black with fade
                    pause
                    jump .get_up

    label .get_up:
        if snooze < 2:
            scene bg_cobedroom
            "There's a heavy series of knocks against the door."
            show rival
            pause
            Rival "Hey, Blake, are you getting up or do I have to yank the covers off you again?"
            CW_side "Yeah, yeah. I'm coming out."
            Rival "We had that talk years ago."
            CW_side angry "You asshole. You know what I mean!"
            Rival "Just hurry up"
            hide rival
            "Blake forces herself up and sighs. She already misses her bed, but she takes the clothes haphazardly lying over the back of the chair and starts getting dressed. It's a better option than Shay barking at her. And threatening her with cold water."

            "Blake's sure she would go through with it, too."

            "She exits her room with her shirt half-tucked into her jeans and hair still mussed from sleep under her hat. Shay is sitting at the dining table munching away at her breakfast. She doesn’t even look up from her phone."
            scene bg_apartment
            show rival
            Rival "Good morning, sleepyhead."
            CW_side "Morning."

            "There is a slice of toast in the toaster left. Blake doesn’t even bother with the collection of spreads next to her and shoves a corner of the toast into her mouth."

            Rival "I don't know how you can eat that dry."
            CW_side "...You put salt in your coffee."
            Rival "Touche."

            "The two friends finish their breakfast in contented silence, save Shay sometimes making noises at her phone. Shay slings her bag over her shoulder and opens the door."

            Rival "Ready to go?"
            CW_side "Let’s do this."

        else:
            "In her sleepy haze, Blake doesn’t notice the sound of her bedroom door opening. She does, however, notice when the covers are flung off her."
            CW_side angry "Argh!" with hpunch
            scene bg_cobedroom
            show rival
            Rival "Up." #[Angry]
            CW_side angry- "Five minutes?"
            Rival "How many times have you said that to yourself this morning?"
            CW_side sad "It’s too early for you to call me out like that."
            Rival "Your shift is in half an hour.  You're going to be late. Get up or I'll throw ice water on you and then leave without you anyway."

            "Blake groans. Time for another day at work."

            "Ten minutes later, Blake stumbles out of her room, hat perched haphazardly on her head. Shay is already halfway out the door."
            Rival "Finally. I thought you’d slipped and hit your head or something."
            CW_side sad- "Yeah yeah, you’re hilarious. Let’s go."

        jump j_scenea2
