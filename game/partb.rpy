# Scene B1
label scene_b1:
    scene bg_fallsidewalk with fade
    "The first snow comes early and unexpectedly this year. Marllie draws herself further into her scarf as the wind picks up, cold air ruffling her loose hair. She regrets leaving her beanie at home. "
    "She picks up her pace, hoping the snow doesn’t get worse. It’s a route she knows well by now, having taken it nearly every day for the past eight months."
    scene bg_shop with fade
    "Marllie sighs in relief as she steps into the coffee shop’s warm interior. It’s relatively quiet, a few patrons scattered around the tables. No surprise really, considering the weather and how early it is in the morning. Still, it’s routine now, and she likes to take advantage of the free wifi and cozy atmosphere."
    Customer_side "{i}Well, I might have one more reason than that...{/i}"
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
    Customer_side "{i}Oh no.{/i}"
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
    Customer_side "{i}She’s so cute.{/i}"
    Customer_side "{i}The dog. The dog’s cute.{/i}"
    Customer_side sad "{i}...Who am I even kidding?{/i}"
    jump j_sceneb2
# Scene B2
label scene_b2:
    scene bg_shop with fade
    "The yawn Marllie lets out cracks her jaw. She winces, rubbing at it as she leans back in her chair."
    "It’s close to lunchtime now, so the cafe is starting to fill up again. It’s not as busy as Marllie is used to, but there’s no shortage of suited businessmen coming in for their fix of complicated caffeine."
    "Marllie cocks her head to one side, cheek propped up against a hand as she watches Blake try to keep up with the flow of people.  She catches Blake’s eye at a break in the line, and she laughs as the other girl shoots her a pleading look."
    "Marllie has time to shoot her a thumbs up before the next customer comes up to the counter. As Blake gets back to work, Marllie turns her attention back to her laptop."
    Customer_side "{i}Hmm, maybe my internship supervisor should have replied by now. I did send the first message two days ago. {/i}"
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
    Customer_side "{i}Eugh, I should probably do something about those before they start to stink.{/i}"
    "She glances at the stack of boxes again."
    Customer_side "{i}Eh… later.{/i}"
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
    Customer_side "{i}Hopefully I’ll make some new friends at the internship. Or some networking contacts at the very least.{/i}"
    "She wouldn't leave Blake behind of course. They’d have to see each other less, but they could keep meeting up. They’d keep texting. And she’d still be able to drop by sometimes."
    "And she was absolutely excited about the internship itself. Scared, too... It was just such a good opportunity."
    "She’d just… miss them. Her."
    "She turns onto her back with a groan at her own thought process."
    Customer_side -happy "{i}Jesus, Marllie. Get a grip. You’re not moving to the other side of the world.{/i}"
    "She’s moving forward, but that doesn’t mean everything is going to be different."
    "She looks at at the texts again, her lips twitching upwards."
    Customer_side happy "{i}Goodnight, Blake.{/i}"
    jump j_sceneb4
# Scene B4
label scene_b4:
    scene black
    "{i}. . .{/i}"
    pause 0.5
    play sound alarm loop
    pause 2.0
    "{i}. . .{/i}"
    Customer_side "{i}Well, today’s the day.{/i}"
    "Marllie lets herself lie still for a second. She closes her eyes against her pillow as the nervousness begins to creep its way into her already. She groans."
    Customer_side "{i}What if I run away? Move to some eastern European fishing village and become a fisherman. I can even learn to bake my own bread and I’ll ride a bike everywhere. It’ll be lovely.{/i}"
    scene bg_dorm with fade
    stop sound
    "She forces herself up before she can change her mind, slipping into the bathroom to brush her teeth. She winces at the dark circles under her eyes. Her sleep, disrupted by anxiety, has not been the most restful."
    scene bg_fallsidewalk with fade
    "Twenty minutes later, Marllie steps out of the shower still feeling subhuman. Breakfast is the same robotic process. Marllie is too focused on her feeling of impending doom to focus properly on what she’s doing. The bus ride there goes by in a blur."
    scene bg_busystreet with fade
    "Always punctual, Marllie arrives at the building fifteen minutes early. She stares up at it, taking in its imposing size and willing the nervous twisting in her stomach to calm."
    Customer_side "{i}What if I can’t do this?{/i}"
    "Marllie has always done well in her classes, sure, but this is a completely different beast. Her parents encouraging words from last night, which had made her feel better at the time, feel hollow right now in the face of the fear locking her limbs."
    Customer_side "{i}I’m going to fuck this up and fail this year. I don’t want to repeat it again. I -{/i}"
    "The vibrations from her phone going off in her pocket interrupt Marllie from her increasingly panicked thoughts. She digs it out, silently grateful for the momentary distraction..."
    "{i}Blake <3\n(3) new messages{/i}"
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
    Customer_side "{i}See the guys at the coffee shop, see Blake, walk some dogs, eat some dinner, and binge a whole season of a show. I’m so glad it’s Friday.{/i}"
    "Her feet take her to the shop on autopilot. There’s a smile on her face as she steps inside, wiping her shoes on the mat at the door"
    scene bg_shop with fade
    "It’s getting close to closing, but it’s already empty. There should be more people milling about. Maya, who is manning the front on her own, looks bored as she wipes down the counter slowly."
    Customer_side "{i}Things have really changed, haven’t they?{/i}"
    "Not always in a bad way, though. It had been an awkward week on Marllie’s end after Maya had said no. Luckily, only Maya and Blake know, so she’s been saved some embarrassment."
    "Maya, for her part, has handled it well. She’d seemed uncomfortable briefly when Marllie had braved going again, but she’d still plastered on a smile and been as friendly as always. And Marllie might have admittedly been reading too much into it. She’d expected worse."
    "Eventually, they’d fallen back into a comfortable friendship. Any remaining awkwardness had disappeared months ago."
    "And while Maya had kept a respectful, professional distance initially, Blake had tried to keep her occupied and make her comfortable. Distracted her. It was nice."
    show mc with dissolve
    MC "Hi, Marllie!"
    "Marllie’s head turns in the direction of the waving figure at the register. She makes her way over, gracing Maya with a warm smile."
    Customer_side happy "Hey, Maya. Thank you for the photo that Blake sent me on Monday morning. I was freaking out a bit and seeing it made me feel a lot better."
    show mc happy
    "Maya beams widely at her."
    MC "It’s no problem. Starting something like that is always nerve-wracking. I’m glad that it helped!"
    Customer_side "It really, really did."
    MC -happy "Good. I was terrified too when I first got this job. But after the first day, it got a lot easier. You’ve done the hardest part."
    show mc at left with moveinleft
    show boss at right with moveinright
    "Just then, Jun steps out of the storeroom. She notices the two women conversing, stopping in her tracks once she makes eye-contact with Marllie. Marllie can’t help but notice the bags that lay beneath her eyes."
    Boss "Good afternoon, Marllie. It’s good to see you here again."
    Customer_side -happy "Hi Jun! Long day?"
    Boss "You could say that."
    "Jun sighs and shakes her head, as if she’s trying to dispel her thoughts. She looks up again with a smile that looks a little too forced to be completely genuine."
    Boss "Ah, doesn’t matter. Congratulations on starting your new internship though!"
    Customer_side "Oh, thank you!"
    Customer_side "Wait, how did you know about it?"
    Boss "Well, you aren’t coming in at your usual times. And I caught the three of them taking that selfie for you. They told me."
    Customer_side "It really was very sweet."
    MC "Well, we’re all happy for you. We’ve all seen how much work you do on that laptop."
    Boss "We certainly have. I’m sure you’ll do a great job there."
    Customer_side "Thank you so much. I hope so."
    Boss "You will."
    "The phone rings from the office. Jun gives another tired smile."
    Boss "Duty calls; I have to take that. Congratulations again, Marllie."
    hide boss with moveoutright
    show mc at center with moveinright
    "Jun slips back through the door. Marllie turns to Maya once she’s certain she won’t be heard."
    Customer_side sad "Not that it’s really my business, but is everything okay? She looks… exhausted. "
    "Maya just sighs, shoulders drooping. It’s like Marllie’s words flipped a switch for Maya too."
    MC sad "There’s been a lot more to do since that Espresso Express opened up nearby. A lot more work for less people."
    Customer_side "It… it’s been emptier around here, hasn’t it? "
    MC "You’ve noticed, huh? Look, don’t worry. We’ll figure something out."
    "Her optimism is touching and far more sincere than Marllie had expected. Suddenly, two large hands grasp her shoulders. Marllie startles, then relaxes once she sees a familiar bright smile. For such a big guy, Asher is incredibly stealthy."
    show mc at left with moveinleft
    show bestie at right with moveinright
    Bestie "Hey, pretty lady! Congrats on surviving your first week!"
    Customer_side -sad "Thank you! Even though I’m technically only there for four days a week. But I do have class on that fifth day. And homework. And more assignments. Oh God, it does sound like a lot when I say it out loud."
    MC -sad "Ouch. But hey, it’s still a big thing! And it’s weird not seeing you at your usual table. "
    Bestie "Yeah, and you don’t have to work shifts with a moping Blake because of it."
    "Maya unsubtly nudges him in the ribs. Asher yelps."
    Bestie "Hey! What?"
    "Maya just rolls her eyes. "
    MC "Ignore him."
    MC "...But Blake will be back soon. She had to run to the bank before it closed."
    Customer_side "Oh! Okay, I guess I’ll go sit down then."
    "Maya roughly elbows Asher again, resulting in a similar reaction from earlier."
    Bestie "I didn’t say anything!"
    MC "Just in case."
    Bestie "Wow."
    MC "Want a coffee while you wait?"
    Customer_side "Yes please. And how about one of those pastries? I know it’s only been a few days, but I’ve desperately missed Jun’s baking."
    MC "You got it."
    hide bestie with moveoutright
    hide mc with moveoutleft
    scene bg_cs_lounge with fade
    "The chairs go up onto the table as she waits. Marllie has enough time to finish going through her news feed before Blake walks back in. "
    show coworker at center with fade
    "Blake’s face splits in a wide grin upon seeing her. Marllie finds herself swept up in a massive hug, almost lifted entirely off her feet. Her arms instinctively wrap around Blake to keep balance, and while Blake has let her down she has not let go."
    CW "I know it’s only been a few days, but man it’s not been the same here without you at all hours."
    Customer_side "I bet your breaks have been really boring, huh?"
    CW "You have no idea. I’ve been stuck talking to Asher."
    "Asher makes an offended noise from somewhere behind them."
    Bestie "I am a luxury that few can afford!"
    "Marllie laughs. Blake flips him off over her shoulder."
    CW "Can’t wait for you to tell me about your past few days."
    Customer_side "I already did."
    CW "Well it’s different when we talk in person. You go off on tangents more."
    Customer_side "And you like that?"
    CW "Duh."
    Customer_side "You’re weird."
    CW "Shay’s already told me that seven times this morning. It’s not an insult anymore."
    Customer_side "I didn’t really mean it as one."
    Bestie "This is some teenage church camp, middle of the night flirting right here."
    Customer_side "{i}Oh no.{/i}"
    "They both jump as Asher slides up next to them."
    show coworker at left with moveinleft
    show bestie at right with moveinright
    CW "Jesus, do you mind? Where did you even come from?"
    "Asher gestures vaguely around them."
    Bestie "Yes, actually, I do mind. You’re hugging in the middle of the floor I want to clean. It’s not my fault that you’re too engrossed in your… whatever it is you’re doing to notice."
    "Marllie looks down and only just notices the wet mop that Asher is holding. The rest of the floor has clearly been cleaned recently except the patch that her and Blake have been standing on."
    "A few more seconds and she realises that she and Blake never really separated after their hug. Blake’s hands are still loosely clasped around her wrists and they’re standing a little too close to be considered entirely friendly."
    CW "You could have just said “excuse me” like a reasonable person."
    "Marllie’s shoes squeak as she springs out of Blake’s personal space.  Blake startles, brows furrowing with concern."
    CW "Are you okay? "
    Customer_side sad "{i}Oh no.{/i}"
    Customer_side -sad "Y-yes. Yes, I’m fine, I just-"
    "Marllie stammers as she searches for a decent explanation. Asher looks between them both, eyes narrowed with suspicion. "
    Bestie "Okay, I have to ask. Are you two a thing now?"
    "Marllie instantly feels her cheeks and both her ears being set aflame by embarrassment. Blake makes a choking sound next to her."
    # TODO PANIC
    CW angry "Oh Jesus Christ, Asher."
    Customer_side "No!"
    CW "Of course we’re not!"
    Customer_side "I don’t know why you’d think that."
    CW "Yeah! I mean… yeah! Why would you think that?"
    "Marllie is trying and failing to look calm. She can’t imagine that she’s succeeding."
    "Asher arches an eyebrow."
    Bestie happy "Right… try that again, but more convincingly."
    CW "We’re just friends. God, Asher. Don’t you have dishes to wash instead?"
    "Asher holds one hand up in surrender and takes the hint to leave them alone. He backs away into the kitchen, wet mop still trailing behind him."
    Bestie -happy "Alright, alright. Point taken! You can have the floor. "
    show bestie happy with dissolve
    "Asher winks exaggeratedly at Blake before he disappears. Blake buries her face in her hands for a second before turning to Marllie."
    show coworker at center with moveinleft
    hide bestie with moveoutright
    CW sad "I’m so sorry about him."
    Customer_side "It’s… it’s okay."
    CW "I didn’t mean that you aren’t attractive. I mean… wait…"
    Customer_side "I… I didn’t make you feel like {i}you{/i} weren’t, did I?"
    CW "N-no! I know you didn’t mean it like that."
    Customer_side "Good, because you are. Not that I’m saying-"
    CW -sad "Good, because you are. Not that I’m saying-"
    Customer_side "Uh, thanks. You are too. And me either-"
    CW "Yeah. Of course."
    Customer_side "Yeah."
    "Marllie’s face is still burning. There’s a highly awkward silence between them now, Blake twisting the bottom of her apron in her hands over and over again."
    CW "Erm…"
    Customer_side "Yeah."
    CW "So… uh. Should we head off?"
    Customer_side "We can’t be late for the dogs."
    CW "Let me just say goodbye to Jun and Maya and grab my things. I’ll be two seconds."
    hide coworker with moveoutright
    "Blake scurries off to the back room. Marllie waits until she’s out of sight before she presses her cold hands to her still warm cheeks."
    # TODO PANIC
    Customer_side sad "{i}...Oh my God.{/i}"
    jump j_sceneb6
# Scene B6
label scene_b6:
    scene bg_fallsidewalk with fade
    "The awkward tension in the air still hovers around them like a thick fog. Marllie shivers as she steps out, wrapping her arms about herself. Despite the burning humiliation, there's a part of her that wishes Blake was still - "
    Customer_side -sad "{i}Nope. Stop that right now. Don’t embarrass yourself further.{/i}"
    show coworker outfit2 down2
    CW "You cold?"
    Customer_side "Yeah. I don’t think I’m wearing the right jacket for tonight. They like it pretty warm in that office."
    show coworker sad
    "Blake frowns and pulls her phone out. She checks the time briefly before slipping it back into her pocket."
    CW "Well… the dogs aren’t actually too far of a walk from your dorm building. If we hurry, you can get changed into something warmer and comfier. And you can put your bag down too. That thing does not look light. "
    Customer_side "That would be nice, actually."
    CW -sad "Want me to carry it for you?"
    # fixed in code not in script ("her"to "Marllie's")
    "It is getting difficult to carry. There is more in the bag than simply the laptop. Marllie's shoulders are already aching from the long week."
    Customer_side "Are you sure?"
    CW "Yeah. No problem."
    "As Blake chatters to Marllie about her week, she realises the tension has already melted away. They reach Marllie’s dorm after a short time. Blake sets the bag down on the floor with a huff while Marllie unlocks the door."
    scene bg_dorm with fade
    "She’d spent a couple of hours tidying the night before on a whim, having grown tired of the state of the place. At least it wasn’t her week to clean the bathroom she shared with her neighbour. Despite that, it’s still not up to the standard she’d like for a visitor. She kicks her basket of dirty laundry under her bed when she’s sure Blake isn’t looking."
    Customer_side "I’m sorry it’s still such a mess."
    show coworker outfit2 down2
    "Blake snorts."
    CW happy "Are you kidding? This is not a mess. You should’ve seen the apartment when Shay went away for three weeks. Took me an entire day to get it spotless again."
    "Marllie fumbles around in her wardrobe until she finds the clothes she’s looking for."
    Customer_side "{i}God, what I wouldn’t give to just go in sweatpants. I have to look somewhat presentable though.{/i}"
    Customer_side "It still amazes me sometimes that polar opposites like you and Shay can get along so well."
    show coworker
    CW "Yeah, you and everyone else. We’ve been hearing that since high school. Shay was pretty moody. Moodier. I’m… well, me."
    Customer_side "I mean you’ve only told me about her and I would agree with you."
    CW "She’s a really good, reliable friend. I also watched her go through her emo phase too, so that’s a lifetime of blackmail material that I have at my disposal."
    Customer_side "Blake!"
    CW "What? She has plenty on me too. She saw me when I had a mullet. So we’re just stuck with each other now."
    menu:
        "You had a mullet?":
            CW -happy "It was not by choice. I should never have tried a new hairdresser."
        "I need to see this right now.":
            CW -happy "You really don’t. Wasn’t even my choice."
            Customer_side happy "One day."
            CW "No."
    "Marllie pulls a sweater over her head and slips into her long coat. Out of the corner of her eye, she sees Blake’s eyes linger over her figure before looking away again."
    # TODO PANIC HERE
    Customer_side -happy "{i}Was that a good thing? Is there something wrong with my outfit?{/i}"
    Customer_side "{i}Wait… did she just check me out?{/i}"
    Customer_side "{i}No, Marllie. Don’t be ridiculous.{/i}"
    CW "There we go. You look much cozier."
    Customer_side "Always good to get out of clothes that you’ve been wearing all day. Ready to go?"
    CW "Hell yeah."
    Customer_side "After you, then."
    jump j_sceneb7
# Scene B7
label scene_b7:
    scene bg_park with fade
    show coworker outfit2 down2
    CW "I might have to walk these guys earlier in the day. It’s getting super dark and super cold, super early."
    Customer_side "Makes sense. Wouldn’t want anyone to catch a cold."
    CW "Tell that to them. You saw what happened when I told them we were going for walkies."
    "The dogs are both tugging incessantly on their leads, attempting to sniff at every tree they pass. They’d ran excitedly around the house the second Blake had said the magic word, both barking and yelping and climbing over each other in a fight to get out the door first."
    Customer_side "At least they’re happy. And warm in those thick coats. But if they keep this level of energy up, we’ll have to carry Alfredo back again."
    CW "Yeah. He’ll definitely sleep well tonight."
    Customer_side "I’m definitely feeling that. Pretty sure I’m just going to spend tomorrow lounging in bed."
    CW "You didn’t have to come if you’re exhausted."
    Customer_side "I wouldn’t miss this."
    "Blake offers her a warm smile. She snakes an arm around Marllie’s shoulders in a brief hug, tugging her close."
    CW"And I’m glad you’re here."
    "The walk is uneventful, save for some scuffling with Cookie when he tries to bolt after some birds."
    Customer_side "I spoke to Maya and Jun earlier. They seemed stressed. Is everything okay?"
    CW"They’re always stressed."
    Customer_side "Well, more than usual. You know what I mean."
    "Blake sighs. Cookie starts to pull harder, once again attempting to chase after the same flock of birds. Blake wrestles him back."
    CW"Well, you know that Espresso Express on the corner? Pretty sure people are going there instead. Big, mainstream franchise. Cheaper too. A lot of the college students are going there now, that’s for sure."
    Customer_side "That’s a lot of lost customers."
    CW"Luckily the office workers are still coming."
    Customer_side "Are they enough though?"
    CW"I dunno. It’ll be okay though, Jun and Maya have come up with some ideas to try and promote us a bit. Get more customers coming through the door."
    Customer_side "Stuff like what?"
    "Blake winks at her."
    CW "You’ll have to wait and see, o valued customer mine."
    "Marllie’s brows knit together. It’s concerning; she’s been going there almost every day since it opened. The last thing she wants is to see it closed. She’s seen firsthand the work and love that Jun and the others have put into it."
    Customer_side "{i}I wonder if there’s something I can do to help.{/i}"
    CW"I wanted to help brainstorm but all I could think of was getting one of those wacky inflatable tubes things in front of car dealerships. Or like, wearing one of those hotdog costumes, but a coffee cup."
    Customer_side "Who’d be the one wearing the costume?"
    CW "Me, probably. Everyone else would be the most serious coffee cups ever."
    Customer_side "Asher wouldn’t."
    show coworker happy
    "Blake snorts."
    CW "There’s not enough room in a suit for Asher and his ego."
    Customer_side "Well, if it would make you feel better, I would totally be convinced to visit the shop if you were outside in a costume. "
    CW hips2 "It’s a shame it wasn’t warmer. I could’ve stood outside in gym clothes and flexed. We could rebrand as a gay-friendly coffee shop."
    Customer_side "Well, I would also be convinced by that."
    Customer_side "{i}What.{/i}"
    "Blake wiggles her eyebrows at her. Marllie reddens and resists the urge to bury her face in her hands."
    Customer_side "{i}WHAT.{/i}"
    Customer_side "I didn’t say anything."
    CW "I gotta say, I’m flattered."
    Customer_side "{i}Please no. I’ve already had enough embarrassment for one day.{/i}"
    Customer_side "Must’ve been the wind you heard."
    CW "Uh huh. Of course! Silly me."
    "Blake seems to hesitate, and Marllie can tell she wants to say something else. She waits while Blake finds the words."
    CW "You know, I’ve really missed you being there. It’s not the same at all without you. I know most of the time we can’t actually talk, but..."
    "Blake trails off. Marllie can feel her stomach fluttering. She shifts a little closer to Blake and links their arms together as they walk, feeling brave suddenly."
    Customer_side "This internship is only for six weeks. Five more to go and I’ll be back to bothering you everyday again."
    CW -happy "I can’t wait."
    jump j_sceneb8
# Scene B8
label scene_b8:
    scene bg_cs_lounge with fade
    show email2 with easeinbottom
    pause
    Boss "Hey, I heard you were looking for me?"
    hide email2 with easeoutbottom
    show boss crossed1
    "The sound of a chair scraping Marllie look up from her phone. Jun drops into the empty chair across the table."
    Customer_side "Yes! I, um, wanted to ask if you could help me with something I’m doing for work."
    Boss "Well... I don’t know much about journalism, but I’m happy to help however I can."
    Customer_side "Cool! Alright, so I’ve only a week left for my internship. I got an email from my boss a couple of days ago and he’s been kind enough to give me a half page editor’s choice article. It’s supposed to be about somewhere I really enjoy going."
    "Jun’s left eyebrow almost disappears into her hairline."
    Boss crossed1 "And you want to write about this place?"
    Customer_side "Yeah! I love it here. And.. well. I know that you guys are having a bit of a rough time with customers right now. I know I don’t actually work here, but I still want to help out in any way that I can."
    "Jun’s mouth opens and closes a few times, almost as if she’s at a loss for words."
    Boss "I- yes! Okay. What do I need to do?"
    Customer_side "I was thinking of doing a little interview with my opinion piece. One of the biggest reasons I come here is because the atmosphere is… warm and welcoming. And really, that’s because of you. So I thought the best way to capture that would be letting you say how you feel."
    Boss "That’s always how I’d hoped it would feel."
    Customer_side "Are you available now? I’m waiting for Blake anyway so I have some free time."
    Boss "Yes."
    Customer_side "Okay! Great! It won’t take long anyway."
    "It takes them a good twenty minutes to get through the small list of questions, and it’s easy to see how much Jun cares. She talks animatedly throughout, pausing sometimes to choose her words more carefully. Marllie records it all on her phone, and after their talk, she knows exactly how she wants to frame her part."
    "Jun pushes herself up from her chair once they’re done. She still looks tired, but Marllie hopes this lifts some of that heavy weight from her shoulders. It’s another little push that might help The Daily Grind."
    Boss "And Marllie? Thank you. I really mean that."
    Customer_side "You don’t need to thank me. I told you, I love it here."
    Boss "I’m not usually a hugging person but can I give you a hug?"
    Customer_side "Oh! Um- of course!"
    "Jun does, squeezing Marlie tightly. Marllie returns it because the truth is this place has been a second home to her since she moved here, far away from all her family."
    Customer_side "{i}I hope this helps. I don't want it to end.{/i}"
    "Blake walks back in from her lunch. And she's one of the reasons this is so important to Marllie, isn't she? Even if nothing ever becomes of..."
    "Marllie doesn't want to finish that thought. Blake's one of the very few close friends she's ever had. Whether they're ever more doesn't matter, but it's another example of the fact they've all found something important here."
    "Jun releases her, and that's when they both notice the others staring at them curiously. Jun pays them no mind."
    Boss "You'll tell me as soon as the article is out, won't you? No matter what happens, I want it framed behind the counter. And in the back office."
    "Marllie smiles softly and nods."
    Customer_side "Of course I will."
    Boss "Good."
    "Jun glances at Blake attempting to subtly listen, still as stealthy as ever. Jun clears her throat."
    Boss "Hey, Blake? Did you know about this?"
    show coworker at right with easeinright
    CW "Honestly? I have no idea what’s going on. It’s all on her, whatever it is."
    Boss "I see. Well, I have some inventory I’m supposed to do, but…"
    "She turns to Marllie. Her smile reaches her eyes this time."
    Boss "Thank you again, Marllie."
    Customer_side "You’re welcome."
    Boss "Blake, take ten. There’s nothing for you to do yet anyway."
    CW "But I just got back…?"
    Boss "I know. It’s okay."
    hide boss with easeoutleft
    "Jun makes towards her office, pausing to whisper something to Blake as she passes. Marllie isn’t sure what was said -- presumably about work, and Blake’s expression is unreadable. Jun now gone, Blake comes over and swings her legs over the empty chair at Marllie’s table, leaning her arms over the backrest."
    show coworker at center with move
    CW "What’s got Jun in a hug mood?"
    Customer_side "I told her about the article for work."
    CW "Ahhhh. I don’t know why I didn’t piece that together in the first place. I can see that she’s thrilled about it."
    Customer_side "I’m surprised you managed to keep the secret from her for the few days that you knew."
    CW "I’m good at keeping secrets! Besides, it’s your thing. Wouldn’t have stolen your thunder like that. Did you get the chance to ask her the questions too?"
    Customer_side "Yep! All done. I kind of have an idea of how I want it to go now too. Which is good, since I’ve got like, a week to write, edit and get it approved."
    CW "You nervous?"
    Customer_side "Of course I am. When am I not nervous?"
    CW "Hey, your boss said that he’d be sad to see you go. Clearly you’re doing well enough too for him to give you this chance. You got this!"
    Customer_side "You always know what to say. Thank you, Blake."
    CW "Anytime."
    jump j_sceneb9
# Scene B10
label scene_b10:
    scene bg_apartment with fade
    show rival
    "Shay’s in the kitchen when they walk in. She looks over her shoulder at the sound of the door, then fully turns at the sight of Blake."
    Rival "The fuck happened to you?"
    "Blake merely grunts at her and flips her off."
    CW "Marllie, this is Shay. Shay, this is Marllie. Play nice."
    "With that, Blake sulks off into her room and closes the door."
    Customer_side "Um… she knocked it over when cleaning up. Got half a mug of coffee down her front."
    Rival "But it’s her day off today?"
    Customer_side "Yeah, I needed to see Jun so we met there."
    "Shay barks out a laugh and shakes her head."
    Rival happy "Still managed to make a mess though. Typical Blake.  Well, my boring day off has been redeemed because I was able to witness this."
    "Shay finishes up making her drink. Marllie remains standing near the door. She’s not entirely sure what to do in this situation, with a person she’s heard so much about but never met."
    Rival "Can I get you anything? I’m afraid we don’t have much right now; it’s Blake’s turn to go shopping this week and she hasn’t yet."
    Customer_side "No, I’m good. Thank you."
    Rival "Alright then."
    "Shay brings her mug over to the sofa and drops down, sipping at it with a satisfied sigh."
    Rival "You can sit if you want, you know. I’m not going to bite."
    Customer_side "Um. Okay."
    "Marllie gingerly sits at the other side. She tries not to sit too far away that it would be obvious that she's uncomfortable, but not too close either. Shay sets her mug down on the table."
    Rival "So. You're her."
    "Marllie blinks."
    Customer_side "I... what? You mean Blake's friend? Yes."
    "Shay lets out an undignified snort."
    Rival "Come on, don't play dumb. We both know you want to be way more than 'friends'."
    "Marllie feels herself going red all the way up to her ears. It had been bad enough with Asher’s teasing, but their denials were technically the truth."
    Customer_side "{i}It's like she's looking straight into my soul somehow. Ugh.{/i}"
    Rival "Listen. I'm going to say all this once and I'll know if you're lying to me. Got it?"
    "Marllie can only nod her head."
    Rival "Okay. I care about Blake. She's like the sister I never had. An immature and annoying sister who makes me want to tear my hair out, but still my family."
    Rival "I just want to make sure you care. If it was just sex, whatever, but I can tell Blake wants more than that. She's shit at hiding it."
    "Marllie's breath catches. She can only latch onto one part of all that."
    Customer_side "She likes me?"
    "Shay actually throws her hands in the air in exasperation."
    Rival "Seriously? Oh, my God. You're both useless at this."
    Customer_side "I... I do care about her. I don't want just a fling. That's not me. "
    "Marllie reddens further."
    Customer_side "And we’re not… you know. Sleeping together."
    Rival "At this point, I’m begging you to fuck. Please. For my sake. I don’t know how much more of her doe eyes I can handle."
    "Marllie tries her best to look anywhere but at Shay, finding a sudden interest in the hands that are folded on her lap. She hears Shay sigh."
    Rival "Ugh, I hate this… she does like you, Marllie. You seem to spend every waking moment texting each other when she isn’t working and she cares about you too. Just ask her. She’ll say yes and I can retain some of my sanity. I just wanted to make sure you weren’t leading her on."
    Customer_side "N-no. I want more."
    Customer_side "{i}I do want more. That was… easier to admit out loud than I thought it would be.{/i}"
    Rival "Okay, we're cool then."
    Customer_side "Yeah, we are."
    "There’s a comfortable silence for a few moments as they just sit next to each other."
    Rival "So… Do you want to see Blake with a mullet and braces?"    
    jump j_sceneb9
    
    
    
    
    
    
    
    
    
    
    
    
    