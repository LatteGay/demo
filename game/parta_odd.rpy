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
#Scene 1 a
label scene_a3:
    scene bg_shop
    "Blake arrives at work with time to spare. It's early and thankfully quiet, save one of her new coworkers swiftly prepping for the day. Maybe she’s a little bit grateful towards Shay’s need to be punctual."
    show mc
    MC "Hey Blake! Just in time. Jun’s letting us try some of her new banana bread fresh outta the oven. Get it while it’s hot!"
    "Jun walks over with a small plate with a number of small pieces of bread. It smells delicious."
    hide mc
    show boss
    Boss "Go ahead, it’s a new recipe that I’ve been wanting to try out for a while now."
    "Blake pops a piece into her mouth. Granted, she tends to live on toast and instant noodles, but it's probably one of the best things she's ever tasted. She just manages to catch herself and stop from swearing, considering she's in polite company."
    CW_side happy "Wow. It's amazing. Thumbs up, boss"
    "Jun flashes a warm smile at her."

    Boss "I’m glad. I’ll be putting these out later. Please let the customers know that it’s new and to try it."
    CW_side happy- " Yes, ma’am."

    "sets down the tray, leaves them with some instructions and heads off into the back. Blake waits until she's out of earshot and turns to Maya."
    hide boss
    show mc
    CW_side "This is like, the fifth new recipe that’s been introduced since I started here. Does it happen often?"
    "Maya sighs. She looks troubled."

    MC "No, I just think she’s just a little tense about  that new (insert chain name) that’s opened up nearby."
    CW_side "Oh. She’s worried about losing business to them?"
    MC "Enough to be noticable. We haven't really been open that long ourselves, y'know? We've got some regulars, but we're still a small business and I guess we're not really that established yet. Jun's been coming up with all sorts of ideas, trying to put out ads..."

    "She finishes putting out some of the other freshly baked pastries. Maya shakes her head and smiles faintly at Blake."

    MC "Enough about that. Can you help me finish making sure all the syrup bottles are full? It’s supposed to be hot today, we’ll probably get a ton of cold drinks."
    CW_side "Sure thing."

    "Time passes uneventfully. Between the two of them, they manage to get the pre-opening duties completed and the store opens. Customers have started to trickle in when Asher finally arrives, looking harried and windswept."
    MC "About time."

    "Asher disappears into the storeroom and emerges a minute later. Blake catches a glimpse of Jun’s unamused face before the storeroom door closes again."

    show friend at left
    hide mc
    show mc at right
    Asher "There was an accident at the intersection. I had to get off the bus and walk."
    MC "That’s okay. Just get to grinding the coffee beans, I’m still on newbie duty."
    Asher "No problem. You holding up okay, Blake?"
    CW_side "Getting the hang of it I hope."
    MC "You're doing fine."
    Asher "Yeah, you’re keeping up with that one girl who orders something new and ridiculous everyday."

    "Blake groans."

    CW_side sad "Yeah, how the hell does she come up with these things? It’s actually a new one every single day."
    Asher "Dunno, at least she hasn’t asked you to make a frappuccino with no ice,  and then yell at you when it predictably comes out a disaster."
    CW_side "...Has that happened to you?"
    Asher "Yup, on my second day too."
    MC "I had someone yell at me because their ice was melting in their drink. Said I gave them the wrong ice cubes because they were supposed to stay big."
    CW_side "What."
    MC "My fourth day."
    Asher "People are dumb. You’ll become numb to it soon, I promise. Come and join us in the “dead inside at work” club!"
    CW_side "You guys are the worst at being reassuring. You’re like an awkward dad trying to reassure his teenager’s angst."
    Asher "Well, they don’t call me daddy for nothing."

    "Maya makes a noise of disgust."

    MC "Stop. No one calls you that. I don’t want to know if your boyfriend calls you that either, so don’t tell me."

    "Asher merely bites his lip and winks at her. Maya makes another disgusted noise."

    MC "Stop scarring me and the newbie and go and do your job."
    hide friend
    hide mc
    show mc
    "Asher laughs as he disappears into the storeroom. Maya rubs her eyes tiredly."

    CW_side "This conversation took a turn I wasn’t prepared for."
    MC "Welcome to the family. You’ll get used to it soon."

    jump j_scenea4
