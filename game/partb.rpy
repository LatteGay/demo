# Scene B1
label scene_b1:
    scene bg_fallsidewalk with fade
    "The first snow comes early and unexpectedly this year. Marllie draws herself further into her scarf as the wind picks up, cold air ruffling her loose hair. She regrets leaving her beanie at home. "
    "She picks up her pace, hoping the snow doesn’t get worse. It’s a route she knows well by now, having taken it nearly every day for the past eight months."
    scene bg_shop with fade
    "Marllie sighs in relief as she steps into the coffee shop’s warm interior. It’s relatively quiet, a few patrons scattered around the tables. No surprise really, considering the weather and how early it is in the morning. Still, it’s routine now, and she likes to take advantage of the free wifi and cozy atmosphere."
    Customer_side "{i}{b}Well, I might have one more reason than that...{/b}{/i}"
    "She makes a beeline straight for the counter. Blake’s leaning on the countertop looking half-asleep, but she perks up once Marllie approaches."
    show coworker angry with dissolve
    Customer_side "Good morning!"
    CW "Bah humbug."
    Customer_side "Aw, so grumpy. No patented Customer Service Smile for me today?"
    CW "Request denied. Please try again later."
    "Marllie chuckles. Blake does quirk a small one for her anyway."
    CW -angry "Whaddya want to drink? If you stick around for another forty five minutes-ish, Jun’s got a new cake coming out."
    Customer_side "If that’s what I can smell, I’ll definitely be staying."
    "Jun happens to be meandering about the register. She pauses her efforts briefly."
    show coworker at left with moveinleft
    show boss at right with moveinright
    Boss "You’re always so sweet, Marllie. First piece is on the house. Just make sure to let us know how it tastes. "
    Customer_side "Oh, thank you so much!"
    CW "Nice. And your drink?"
    Customer_side "Latte in a mug, please. Triple shot."
    CW "2\% milk again?"
    Customer_side "If you’re offering."
    "Blake tsks, a slow grin forming on her mouth as she keys in the order."
    CW happy "Wow, can’t believe you would make me actually have to turn around and bend down to reach the other fridge to get the milk. So much extra work."
    Boss "What else am I paying you for, Blake?"
    CW "Looking pretty?"
    "Jun rolls her eyes fondly."
    Boss "I’ll have to give you a raise then. Come on, hop to it."
    "Blake offers her a lazy salute."
    CW "Yes, ma’am!"
    hide boss with moveoutright
    show coworker at center with moveinright
    "Marllie leans against the counter while Blake works. The article she’s supposed to be finishing lingers at the back of her mind. She has a ton of research to do and the time to do so feels as though its rapidly diminishing."
    "But still she lingers a the counter, unwilling to take her seat just yet. Marllie watches as Blake makes her drink. There’s a bright blue bandage on Blake’s left thumb that wasn’t there yesterday."
    Customer_side "Did you burn yourself already this morning?"
    "Blake looks confused for a second before she follows Marllie’s line of sight."
    # TODO panic expression here??
    CW -happy "Oh! No, not this morning. I was, ah, trying to julienne some carrots last night for dinner. Didn’t really go too well."
    Customer_side  "Trying the whole cooking thing again, are you?"
    CW "Heh. Yeah, the recipe was simple enough to follow. I’m just still not entirely trusted around sharp knives still. Shay’s banned me from dinner prep for the next month because, I quote: \“We’re not close enough to share blood. Neither of us are dying yet.\” "
    Customer_side "You’ll get better with practice. I wouldn’t want you hurting yourself, though."
    CW "I guess I’d better keep myself immaculate if I want to keep looking this good."
    Customer_side "You always look good."
    "Marllie lets out a distressed squeak when she realises she’s actually said that aloud."
    # TODO MORE PANIC
    Customer_side "{b}{i}Oh no.{/i}{/b}"
    CW "What was that? Didn’t quite catch it."
    Customer_side "N-nothing! I uh. I’d better get back to my work. Big assignment to do. Thanks for the coffee!"
    CW "Sure. I’ll come see how it’s going when I’m on my break?"
    Customer_side "Y-yeah. I’d like that."
    hide coworker with fade
    "Marllie scuttles off to her usual table, letting her loose hair fall around her face to hide her red cheeks. It’s a familiar routine now, so it doesn’t take too long for her to set up."
    "Asher stumbles in, hood over his head and trailing in snow. It must have picked up outside since. He offers Marllie a friendly wave as he heads into the back, coming out a minute later sans-coat. He swiftly puts his apron on while Blake chatters with him. He says something and Blake lightly punches him on the arm."
    "Marllie picks up her coffee, eager to take her first sip but the foam on top catches her eye."
    "Blake’s replaced the usual generic coffee art for a simple dog. It’s a little lopsided, one floppy ear bigger than the other but it’s adorable. There’s even a sprinkle of chocolate powder around the dog, presumably representing a small flurry of snow."
    "A familiar warmth unfurls in her chest. Marllie cracks a smile, putting the mug back down to capture a quick photo. She glances up briefly, watches as Blake’s gaze snaps away to the opposite side of the shop."
    Customer_side "{b}{i}She’s so cute.{/i}{/b}"
    Customer_side "{b}{i}The dog. The dog’s cute.{/i}{/b}"
    Customer_side sad "{b}{i}...Who am I even kidding?{/i}{/b}"
    jump j_sceneb2
# Scene B2
label scene_b2:
    scene bg_shop with fade
    "The yawn Marllie lets out cracks her jaw. She winces, rubbing at it as she leans back in her chair."
    "It’s close to lunchtime now, so the cafe is starting to fill up again. It’s not as busy as Marllie is used to, but there’s no shortage of suited businessmen coming in for their fix of complicated caffeine."
    "Marllie cocks her head to one side, cheek propped up against a hand as she watches Blake try to keep up with the flow of people.  She catches Blake’s eye at a break in the line, and she laughs as the other girl shoots her a pleading look."
    "Marllie has time to shoot her a thumbs up before the next customer comes up to the counter. As Blake gets back to work, Marllie turns her attention back to her laptop."
    Customer_side "{b}{i}Hmm, maybe my internship supervisor should have replied by now. I did send the first message two days ago. {/i}{/b}"
    # TODO EMAIL HERE
    "This is actually going to happen! She shoots another quick email thanking them and confirming she’ll be there and sinks into her seat."
    "This time next week, she’ll have already started her internship."
    "There’s a huge weight off her shoulders but at the same time, the familiar dread settles into the pit of her stomach as the reality of the internship truly sinks in."
    "She’d done this before in previous years. But it never got any less nerve wracking."
    "New people. New schedule. New rules. New expectations."
    "Marllie’s never been good with change, no matter how temporary. And she’s never really been good with people either."
    "She attempts a calming breath and resolves not to think too much about it; nothing that can be done now. Instead, she continues with her assignment."
    "She completely loses track of time again."
    show coworker with moveinleft
    CW "You're nearly out. Want another coffee?"
    "Marllie's head snaps up. She hadn't heard Blake approach, too engrossed in her work. She rubs at her eyes and offers Blake a smile."
    Customer_side happy "Yes, please. And I love the dog you made for me. I almost didn’t want to drink it."
    show coworker happy
    "Blake grins, showing teeth. It makes Marllie's chest flutter."
    CW "Coming right up. Coincidentally, it'll be finished just on time for my break."
    hide coworker with moveoutleft
    "She trots off. Marllie saves her work for the fiftieth time in half an hour and closes the laptop lid, shoving it aside. She needs a break herself."
    show coworker with moveinleft
    "Blake returns a moment later and sets the cup down on the table. She sits with a huff, readjusts her hat and runs her fingers through her hair. Marllie tries not to openly stare."
    CW "Don’t worry about paying. My treat."
    Customer_side "Aww, you didn’t have to do that."
    "Blake waves her hand dismissively."
    CW "Wanted to. How’s work going?"
    Customer_side "Good, I think. I got an email back about the internship. I start next week."
    "Marllie immediately finds herself embraced in a warm hug. She stiffens for a second, the contact sudden but not… unwelcome. She can’t help herself -- she sinks into it, winding her arms around Blake’s waist."
    "Blake is so much taller anyway, and the fact she’s standing and Marllie is still sitting makes the hug a little awkward. Still, she can smell the coffee on Blake’s uniform, and the shampoo she uses as long hair tickles her cheek."
    "Blake is the one who breaks it, far sooner than Marllie would have liked. Blake clears her throat."
    # TODO PANIC
    CW "S-sorry! I should have asked first. I’m just so happy for you. And proud of you."
    Customer_side "Thank you, Blake. That means a lot."
    CW "I know how hard you’ve been working. You deserve it."
    # TODO BLUSH
    "Marllie isn’t used to receiving such a barrage of compliments. She stares bashfully into her mug of coffee."
    CW "D’you wanna help me walk the dogs again later? We can get some dinner before too if you’re up for it."
    "Marllie’s glad for the change of topic and even happier for the offer. Spending time with some dogs and Blake is a perfect way to celebrate.  She beams."
    Customer_side "Of course I would. Same time as usual?"
    CW "Same time as usual."
    Customer_side "I can’t wait!"
    hide coworker
    jump j_sceneb3
# Scene B3
label scene_b3:   
    scene bg_fallsidewalk with fade
    "It’s pitch black by the time Marllie finally arrives home. She honestly hadn’t meant to stay out so late, but it’s easy to lose track of time with the company she had. Shivering slightly, Marllie fumbles with her keys, and then for the lightswitch once she opens the door."
    scene bg_dorm with fade
    "The dorm still looks new, apart from the papers littered about her living space and the desk that hosts a pile of leftover food she’s been too tired to put away."
    Customer_side "{b}{i}Eugh, I should probably do something about those before they start to stink.{/i}{/b}"
    "She glances at the stack of boxes again."
    Customer_side "{b}{i}Eh… later.{/i}{/b}"
    "She sits down lazily instead after fumbling to take off her coat. Her scarf is still wrapped around her mouth, as the room hasn't had enough time to warm yet and she's still cold from her walk. She kicks off her boots and flops back into the cushions."
    "Her feet are sore from the long walk with Blake. They’d gone around the dog park three times, and it was a fair distance away in itself. The snow hadn’t settled thankfully -- it was just cold."
    "Marllie reaches into her pocket and taps away at her phone."
    call phone_start
    call message_start("me", "I’m home safely. Did you get home okay?")
    call message("Blake <3", "ytes and no")
    call message("Blake <3", "i got home fine but i left a mess in the kitchen earlier lol")
    call message("Blake <3", "shay almost suffocated me with my sock when i walked back in")
    call message("Blake <3", "my bad")
    call message("Blake <3", "X.X")
    call message("me", "Oh dear.")
    call message("me", "Wait, is the kitchen and the sock related?")
    call message("Blake <3", "well lets just say that i fdound my missing laundry")
    call message("me", "I’m not even going to ask.")
    call message("Blake <3", "i mean i dont have answers lamo")
    call message("Blake <3", "lamp")
    call message("Blake <3", "lmao")
    call message("Blake <3", "fuck")
    call message("me", "...Go to bed, Blake. I’ll see you tomorrow morning.")
    call message("Blake <3", "ok mom")
    call message("me", "Goodnight!!")
    call message("Blake <3", "gniught")
    call message("Blake <3", "<3 <3 zzzzZZZ")
    call phone_end
    "Marllie smiles at the exchange, despite the typos. And the lack of punctuation. And the six different texts Blake chose to send instead of one with proper sentences. It had been a pet peeve of Marllie’s at first, but now she didn’t mind at all. Even when it meant her phone was going off at all hours of the day."
    "Okay. Or maybe she liked her phone going off at all hours of the day."
    "It had been… lonely, moving to a new town. Not that… well, not that she had many people to leave behind in the first place."
    "Just her parents and a handful of friends. And she missed them, yes, but some freedom and some independence had been nice."
    Customer_side "{b}{i}Hopefully I’ll make some new friends at the internship. Or some networking contacts at the very least.{/i}{/b}"
    "She wouldn't leave Blake behind of course. They’d have to see each other less, but they could keep meeting up. They’d keep texting. And she’d still be able to drop by sometimes."
    "And she was absolutely excited about the internship itself. Scared, too... It was just such a good opportunity."
    "She’d just… miss them. Her."
    "She turns onto her back with a groan at her own thought process."
    Customer_side -happy "{b}{i}Jesus, Marllie. Get a grip. You’re not moving to the other side of the world.{/i}{/b}"
    "She’s moving forward, but that doesn’t mean everything is going to be different."
    "She looks at at the texts again, her lips twitching upwards."
    Customer_side happy "{b}{i}Goodnight, Blake.{/i}{/b}"
    jump j_sceneb4
# Scene B4
label scene_b4:
    scene black
    "{b}{i}. . .{/i}{/b}"
    pause 0.5
    play sound alarm loop
    pause 2.0
    "{b}{i}. . .{/i}{/b}"
    Customer_side "{b}{i}Well, today’s the day.{/i}{/b}"
    "Marllie lets herself lie still for a second. She closes her eyes against her pillow as the nervousness begins to creep its way into her already. She groans."
    Customer_side "{b}{i}What if I run away? Move to some eastern European fishing village and become a fisherman. I can even learn to bake my own bread and I’ll ride a bike everywhere. It’ll be lovely.{/i}{/b}"
    scene bg_dorm with fade
    "She forces herself up before she can change her mind, slipping into the bathroom to brush her teeth. She winces at the dark circles under her eyes. Her sleep, disrupted by anxiety, has not been the most restful."
    scene bg_fallsidewalk with fade
    "Twenty minutes later, Marllie steps out of the shower still feeling subhuman. Breakfast is the same robotic process. Marllie is too focused on her feeling of impending doom to focus properly on what she’s doing. The bus ride there goes by in a blur."
    scene bg_busystreet with fade
    "Always punctual, Marllie arrives at the building fifteen minutes early. She stares up at it, taking in its imposing size and willing the nervous twisting in her stomach to calm."
    Customer_side "{b}{i}What if I can’t do this?{/i}{/b}"
    "Marllie has always done well in her classes, sure, but this is a completely different beast. Her parents encouraging words from last night, which had made her feel better at the time, feel hollow right now in the face of the fear locking her limbs."
    Customer_side "{b}{i}I’m going to fuck this up and fail this year. I don’t want to repeat it again. I -{/i}{/b}"
    "The vibrations from her phone going off in her pocket interrupt Marllie from her increasingly panicked thoughts. She digs it out, silently grateful for the momentary distraction..."
    "{b}{i}Blake <3\n(3) new messages{/i}{/b}"
    "Her eyes widen. She hurriedly pulls off a glove to unlock her phone."
    call phone_start
    call message_start("Blake <3", "hey my dude")
    call message("Blake <3", "i kwnow its ur first dayt at yuor new place today")
    call message("Blake <3", "just texting to wish u good luck!!! we    believe in you!!!")
    call message("Blake <3", ":thumbsup: :fist: :muscle: :dancer:")
    call message("", "Blake is typing…")
    # TODO CG
    call message("Blake <3", "(Attached is a photo of Blake, Maya and Asher squashed into the frame. They’re all smiling at the camera with a thumbs up)")
    call message("me", "Aww, thank you!! I appreciate this a lot this morning. Please let the others know too.")
    call message("Blake <3", "its all good friendo")
    call message("Blake <3", "i gotta go but")
    call message("Blake <3", "seriously tho")
    call message("Blake <3", "you got this")
    call message("Blake <3", "ur so smart and good at what u do")
    call message("Blake <3", "your supervisor is gonna be hella impressed as fuck")
    call message("Blake <3", "i believe in you even if u don’t")
    call message("Blake <3", "go get em friendo")
    call message("", "Blake is typing…")
    call message("", "Blake is typing…")
    call message("", "Blake is typing…")
    call message("Blake <3", "<3")
    # TODO PUT FLASH HERE???
    call message("me", "(Flashing of a heart emoji in the message box as Marllie inputs and deletes it repeatedly)")
    call message("me", "<3")
    call phone_end
    "Marllie puffs out a breath, the cold air leaving a visible mist. She reads through the texts again, staring at the photo."
    "Her heart is still thrumming wildly in her chest. The panic still has a vice grip around her heart, but it’s enough for a brief surge of confidence. Her phone goes back into her pocket, though she keeps a tight grip around it. The image sent to her stays in her mind."
    "She inhales, straightens, and steps inside."
    jump j_sceneb5
# Scene B5
label scene_b5:
    scene bg_fallsidewalk
    "Marllie steps off the bus, drawing her coat tighter around her as the sudden cold makes her shiver. It’s enough to chase away the tendrils of weariness building behind her eyes."
    "It’s finally the weekend. Though the first week of her internship has been much more enjoyable than expected, she’s relieved to return to familiarity."
    Customer_side "{b}{i}See the guys at the coffee shop, see Blake, walk some dogs, eat some dinner, and binge a whole season of a show. I’m so glad it’s Friday.{/i}{/b}"
    "Her feet take her to the shop on autopilot. There’s a smile on her face as she steps inside, wiping her shoes on the mat at the door"
    scene bg_shop with fade
    "It’s getting close to closing, but it’s already empty. There should be more people milling about. Maya, who is manning the front on her own, looks bored as she wipes down the counter slowly."
    Customer_side "{b}{i}Things have really changed, haven’t they?{/i}{/b}"
    "Not always in a bad way, though. It had been an awkward week on Marllie’s end after Maya had said no. Luckily, only Maya and Blake know, so she’s been saved some embarrassment."
    "Maya, for her part, has handled it well. She’d seemed uncomfortable briefly when Marllie had braved going again, but she’d still plastered on a smile and been as friendly as always. And Marllie might have admittedly been reading too much into it. She’d expected worse."
    "Eventually, they’d fallen back into a comfortable friendship. Any remaining awkwardness had disappeared months ago."
    "And while Maya had kept a respectful, professional distance initially, Blake had tried to keep her occupied and make her comfortable. Distracted her. It was nice."
    show mc with dissolve
    MC "Hi, Marllie!"
    "Marllie’s head turns in the direction of the waving figure at the register. She makes her way over, gracing Maya with a warm smile."
    Customer_side happy "Hey, Maya. Thank you for the photo that Blake sent me on Monday morning. I was freaking out a bit and seeing it made me feel a lot better."
    "Maya beams widely at her."
    MC "It’s no problem. Starting something like that is always nerve-wracking. I’m glad that it helped!"
    Customer_side "It really, really did."
    MC "Good. I was terrified too when I first got this job. But after the first day, it got a lot easier. You’ve done the hardest part."
    show mc at left with moveinleft
    show boss at right with moveinright
    "Just then, Jun steps out of the storeroom. She notices the two women conversing, stopping in her tracks once she makes eye-contact with Marllie. Marllie can’t help but notice the bags that lay beneath her eyes."
    
    
    
    
    jump j_sceneb6
    
    
    
    
    