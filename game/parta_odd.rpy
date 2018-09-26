#Scene 1 a
label scene_a1:
    $ snooze = 0
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
                if snooze < 2:
                    $snooze += 1
                    scene black with fade
                    pause
                    jump .alarm2
                else:
                    scene black with fade
                    pause
                    jump .get_up

    label .get_up:
        if snooze < 1:
            scene bg_cobedroom
            "There's a heavy series of knocks against the door."
            pause
            show rival
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
            CW_side -angry "Five minutes?"
            Rival "How many times have you said that to yourself this morning?"
            CW_side sad "It’s too early for you to call me out like that."
            Rival "Your shift is in half an hour.  You're going to be late. Get up or I'll throw ice water on you and then leave without you anyway."

            "Blake groans. Time for another day at work."

            "Ten minutes later, Blake stumbles out of her room, hat perched haphazardly on her head. Shay is already halfway out the door."
            Rival "Finally. I thought you’d slipped and hit your head or something."
            CW_side -sad "Yeah yeah, you’re hilarious. Let’s go."

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
    CW_side -happy " Yes, ma’am."

    "Jun sets down the tray, leaves them with some instructions and heads off into the back. Blake waits until she's out of earshot and turns to Maya."
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

    show bestie at left
    hide mc
    show mc at right
    Bestie "There was an accident at the intersection. I had to get off the bus and walk."
    MC "That’s okay. Just get to grinding the coffee beans, I’m still on newbie duty."
    Bestie "No problem. You holding up okay, Blake?"
    CW_side "Getting the hang of it I hope."
    MC "You're doing fine."
    Bestie "Yeah, you’re keeping up with that one girl who orders something new and ridiculous everyday."

    "Blake groans."

    CW_side sad "Yeah, how the hell does she come up with these things? It’s actually a new one every single day."
    Bestie "Dunno, at least she hasn’t asked you to make a frappuccino with no ice,  and then yell at you when it predictably comes out a disaster."
    CW_side "...Has that happened to you?"
    Bestie "Yup, on my second day too."
    MC "I had someone yell at me because their ice was melting in their drink. Said I gave them the wrong ice cubes because they were supposed to stay big."
    CW_side -sad "What."
    MC "My fourth day."
    Bestie "People are dumb. You’ll become numb to it soon, I promise. Come and join us in the “dead inside at work” club!"
    CW_side "You guys are the worst at being reassuring. You’re like an awkward dad trying to reassure his teenager’s angst."
    Bestie "Well, they don’t call me daddy for nothing."

    "Maya makes a noise of disgust."

    MC "Stop. No one calls you that. I don’t want to know if your boyfriend calls you that either, so don’t tell me."

    "Asher merely bites his lip and winks at her. Maya makes another disgusted noise."

    MC "Stop scarring me and the newbie and go and do your job."
    hide bestie with dissolve
    hide mc
    show mc
    "Asher laughs as he disappears into the storeroom. Maya rubs her eyes tiredly."

    CW_side "This conversation took a turn I wasn’t prepared for."
    MC "Welcome to the family. You’ll get used to it soon."

    jump j_scenea4

label scene_a5:
    scene bg_apartment
    "It’s late when Blake arrives home. She fiddles with her earphones, shoving them back in her pocket in a tangled heap, and throws open the door. Stumbling in tiredly, she tosses her bag on to the sofa and drops down with a groan, throwing her arm across her eyes"
    show rival
    "Shay's sitting comfortably in a chair reading, having gotten home first. As expected, she spares Blake no attention."
    "So Blake groans again. Louder this time."
    Rival "Do you require medical attention?"
    CW_side "Aren’t you going to care? Ask me about my day?"
    "Shay lets out a long-suffering sigh and sets her book page-down on the chair arm."
    Rival "Go on. Let it out."
    CW_side "Work was fine. How are you?"
    Rival "That’s it? I was expecting some drama or tragedy."
    CW_side "The tragedy is that I had to get out of bed this morning, but alas it must happen."
    Rival "I consider getting you up to be my morning workout at this point."
    "Blake sits up and wiggles her eyebrows at Shay suggestively. Shay makes a noise of disgust and throws a nearby cushion at her face."
    Rival "No. Absolutely not. Ever."
    CW_side "My feelings are hurt."
    Rival "Idiot."
    "Blake throws the cushion back and Shay catches it out of the air. Despite her protests, there is a tiny smile playing at the edge of her lips."
    Rival "Oh, there was a parcel that came for you. New game?"
    "Blake sits up quickly. Shay tuts."
    Rival "You really can’t do that in a morning?"
    CW_side "Nope. Where is it?"
    "Shay gestures towards the dining table, uncluttered and a flower in the middle thanks to Shay’s efforts. Blake flies off the sofa and dives at the box. Shay is stands behind her, arms folded across her chest. She attempts to glance over her roommate’s shoulder. The height difference makes it difficult, however."
    Rival "That’s not a game"
    CW_side "Package from Dad."
    "She tips the box over the surface and lets everything fall out in a pile (she misses Shay’s distressed twitching at the mess)."
    Rival "That’s the second one this month."
    CW_side "Yeah, he’s in a different location now. Look."
    "Blake picks up some photos and a couple of packets of different candies. She grins."
    CW_side "From Germany to Japan. Bit of a culture difference, I’d say. Wanna try some?"
    Rival "If you’re offering."
    CW_side "Of course."
    "Shay sits while Blake ruffles through the selection. Probably would help if any of the packaging was written in English, but it’s always cool to try new things, Blake thinks. She finds a letter, scans it quickly, then refolds it and shoves it into her back pocket for later."
    CW_side "There’s a bear on this one. Let’s start with that."
    "They tear into them and half an hour later they’ve tried at least half the new foods. And caught up on their days."
    Rival "I need some kale. We’ve had so much sugar that my tongue is sticking to the roof of my mouth."
    CW_side "I’m probably going to crash in like, half an hour."
    Rival "Joy of joys."
    CW_side "Hey, my package, my rules."
    "Shay rolls her eyes and stands from her chair. The coffee machine whirs to life. Shay leans on the counter while she waits."
    Rival "Have you told him about your new job?"
    "Blake makes an affirmative noise around yet another mouthful of candy."
    Rival "Did you tell him you’re taking a break from college?"
    CW_side "Yeah. He says he’s okay with it but I know he thinks I’m wasting my time."
    Rival "He’s not the one in school though."
    CW_side "No, but he’s the one paying the bills."
    Rival "You have to do what’s right for you, Blake. If he says it’s okay, then it’s okay."
    CW_side "Yeah…"
    "Blake looks unsure. Shay hesitates for a moment before walking back over to the dining table where Blake is slumped. She lays a hand on Blake’s shoulder."
    Rival "You’ll figure it out. There’s time, and your parents aren’t going to stop supporting you. They’re actually the nicest people I know."
    "Blake smiles appreciatively, but she can’t help but make a joke."
    CW_side happy "Are we having a moment?"
    Rival "Not now you’ve ruined it."
    "There’s laughter behind Shay as she heads back to pour her coffee. Blake begins packing up the box again to take to her room; she’s definitely going to crash soon."
    CW_side -happy "Are you still working on your group assignment?"
    "Shay wordlessly lifts her mug in assent."
    Rival "I had to duck out of work early to deal with someone not pulling their weight. We were supposed to have three sections done by today."
    CW_side "Ugh."
    Rival "We still have plenty of time. It’s just frustrating that the person said they’d have it completed but they didn’t."
    CW_side "Are you being graded as a group?"
    Rival "No. Or I’d be far more pissed off."
    CW_side "I’ll bring us something home tomorrow so you can at least suffer with something nice."
    Rival " I might even put up with your crappy reality TV if you do."
    CW_side "Don’t you dare talk shit about the Bachelor."
    "Shay hides her smirk behind another swig of her coffee. She makes to retrieve the book she left earlier, setting it aside neatly beside her laptop."
    Rival "Close your door so I don’t have to work over your snoring."
    CW_side "Yeah, yeah. Will do. G’night, Shay."
    jump j_scenea6

label scene_a7:

    "It’s later in the afternoon and past lunch-hour, so the coffee shop is particularly quiet. There has only been a handful of customers in the past several hours and Blake is frankly bored out of her mind. She almost wishes Marllie would order something just to give her something to do."

    "Almost."

    $ bClean1 = True
    $ bClean2 = True
    $ bClean3 = True
    $ bClean4 = True
    label .clean_menu1:
        menu:
            "Look around" if bClean1:
                $bClean1 = False
                "There are two customers in right now. One man who looks about done with his coffee but is currently entranced in a book, and Marllie still tapping away on her computer. Asher’s on his break and Maya’s cleaning the coffee machine, and Jun’s in the kitchen baking fresh cakes ready for the influx of people who need a fix after a long day at work."
            "Clean the front counter." if bClean2:
                $bClean2 = False
                CW_side "{i}Eh, I think I’ve cleaned it twice already in the… past half an hour? Goddamn, time is passing slowly.{/i}"
            "Sweep the floor." if bClean3:
                $bClean3 = False
                CW_side "{i}Oh right, Asher swept before his break already. Damn that man’s efficiency.{/i}"
            "Wipe the tables." if bClean4:
                $bClean4 = False
                CW_side "{i}Well, gotta at least look busy. Might as well do the tables again.{/i}"
                jump .after_clean_menu1
        jump .clean_menu1

    label .after_clean_menu1:
    "She takes her time but not slow enough that she looks like she’s wasting it. She meticulously straightens up the condiments on each table, ignoring the guy’s corner table lest she disturb his reading. Marllie pauses her frantic typing to take a sip at her drink without her eyes leaving the screen and now Blake’s a little bit closer, she can make out a few words."

    "She’s been working here a few weeks now and despite how much time she’s technically been in Marllie’s company, it occurs to her she has no idea what the regular is actually doing. She does vaguely recall the speculating she and Maya had done in her first days. She has to admit she’s curious."

    CW_side "{i}Huh, I wonder if I can sneak a look. Never did find out what she’s doing while in here.{/i}"

    "Blake makes her way as nonchalantly as she can to the table behind Marllie. She feels a bit like a creep but she sprays the table a couple of times anyway and starts casually cleaning."

    "Unfortunately, she can't see around Marley's head, damn it. She shifts to the side a little..."
    show customer with dissolve
    Customer "You know, you could just ask me what I'm doing."

    "Blake just about jumps out of her skin and knocks the bottle on the floor. She stammers some incoherent apologies as Marllie leans back in her chair to stare at her, and she once again considers telling Asher she’s going to jump off a bridge today so can he please clean the coffee machine later in her place, thanks."

    Customer "You’re not very stealthy."
    CW_side "Oh, my God."
    Customer "You were almost leaning  over my shoulder. You even stopped wiping the table at one point."
    CW_side sad up1 "I’m so sorry."

    show customer happy
    "Marllie bursts into a fit of giggles. Blake is dumbfounded, but… she figures Marllie isn’t actually mad, then? Man, is she bad at being discreet. Really, she should have known her capabilities better from all the times Shay’s caught her doing something she shouldn’t have been doing."

    CW_side -sad -up1 "You’re not upset?"
    Customer "No. It’s okay."
    CW_side happy "Okay. Okay, good."
    Customer "…"
    CW_side "…"
    show customer -happy
    Customer "Do you... want to sit?"

    "The offer breaks the awkward silence. Blake glances back at the register and considers its safety, but they'd be sitting fairly close, the shop's empty, and Asher will be back from his break in a little over ten minutes."

    "Blake pulls out the chair across the table and plonks herself down. She’s got a good view of the counter and the entrance from here so she lets herself relax."

    CW_side -happy "So… You said I could ask what you’re doing?"

    "Marllie stops typing to take another sip of her coffee. She inclines her head towards the mess on the table."

    Customer "Take a guess."

    "Blake casts her gaze down onto the table. Loose pages full of what look to be lecture notes, textbooks."

    CW_side " Er… english major?"

    Customer "Close. Journalism."

    CW_side " Oh. Cool."
    $ bStudy =  True
    $ bHere =  True

    label q1_menu:
        if (bStudy == False) and (bHere == False):
            jump after_q1
        else:
            menu:
                "How long have you been studying?" if bStudy:
                        $bStudy = False
                        Customer "I’m about a year into it. It’s a 20 month course, so halfway done, I guess."
                "You’re here a lot." if bHere:
                        $bHere = False
                        Customer "The coffee is good, the atmosphere is good, and there’s free wifi. What’s there not to love?"
        jump q1_menu

    label after_q1:

    CW_side "You come here during your free periods?"

    Customer "Yeah. And the professors don’t mind us not showing up as long as we catch up in our own time. I just watch the lecture video later and review the notes here. Like I said, I like the atmosphere."

    "There’s a bit of an awkward pause. Blake internally cringes at how bad she is at small talk."

    Customer "What about you? You haven’t been here that long."
    CW_side "I just moved in with a friend from high school not that long ago. I used to tutor too, but I’m kinda too far away from my students now."
    Customer "You used to tutor?"
    CW_side  "Yeah, biology and maths."
    Customer "Are you in school too?"

    "Blake shakes her head."

    CW_side "I’m taking a break for a semester or two. I think. I don’t really know what I wanna do but I don’t want to move all the way back in with my mom yet in case I change my mind, so I’m just here."

    "She sighs a little wistfully."

    CW_side "I do miss the dogs, though. And my family too, of course."

    "Marllie’s entire being perks up."
    show customer hips1 happy with dissolve
    Customer "You have dogs?"

    "Blake is already reaching for her phone before the question is even fully posed to her. She clicks through her phone and into the library of images she has stored away."

    CW_side happy "Yeah, three."

    "She pulls up a picture with all three sitting in the living room and points each one out."

    CW_side "The big one is Ein. The oldest one too. Astro is the Shiba, and David’s the Pomeranian mix. We got him not long before I moved out."

    "Marllie’s eyes light up as she looks at them. She cups a hand over her mouth."

    Customer happy "They’re so adorable!"
    CW_side "I know, right? I’m thinking about getting another. I miss having a dog around and I know my roommate would be more than okay with it. Just waiting until the right time when I have some money saved. I’m walking other people's’ dogs right now for a bit of side money and it helps fill the hole a bit."
    Customer "If you do, I’d love to meet them. I’ve never had a pet before."
    CW_side -happy "Really? Never?"
    Customer sad "Yeah… my parents didn’t really have time to take care of them and they don't really trust me to take care of one on my own. Maybe someday. Studying takes up a lot of time."

    "Blake flashes her a smile."

    CW_side happy "Yeah, you’ll want to be able to spoil them. If or when I do get one, I promise I’ll bring them in so you can meet them."
    Customer happy "I’d love that."

    "Blake notices Asher gesturing to her from the register, back from his break. She offers Marllie an apologetic grin."

    CW_side "Back to the grind, I guess. Good luck with your studying."
    Customer "Thanks. I might need a new coffee soon to keep awake."

    "Blake winces, but hides it well. She pushes herself up with the table."

    CW_side -happy "No problem. Just let me know."

    jump j_scenea8

label scene_a9:
    scene bg_shop
    "Maya had left early for home not long after, having started an earlier shift anyway that day. She’d seemed… off, Blake thought, but had claimed to be okay and Blake didn’t want to press. Or appear rude for prying."
    "So she decided to do her usual thing at this time when everything else had been taken care of: stare at the clock until she could go home."
    scene bg_busystreet
    "Shay met her outside. She was leaning with one foot against the wall, scrolling through her phone. Her eyes flicked upwards, noticing Blake, and she slipped her phone back in her front pocket and fell into step beside her roommate."
    show rival
    CW_side "How was your day?"
    Rival "I got stuck training the newbies. Plural. They progressed to making cold drinks today so it was pretty chaotic."
    CW_side "Eh, go easy on them. I can’t imagine that people getting coffee at a big chain store are any less picky."
    Rival "Ugh, don’t remind me."
    scene bg_fallsidewalk
    "They fall into a comfortable silence. Blake is making a list of takeaway places that they can get dinner from in her head when they pass a bus stop. A colourful advertisement that flashes across across a screen catches her eye."
    CW_side happy "{b}{i}Thai. Gonna get some Thai food for dinner. Hell yeah.{/i}{/b}"
    "She turns her head to tell Shay, ask her if she wants anything too, but a familiar silhouette makes her stop dead."
    CW_side -happy "Hey, why don’t you go on ahead and I’ll meet you at home. I’ll pick up some food for us instead."
    show rival
    Rival "Everything okay?"
    CW_side "Yeah. Everything’s cool. I’ll just see you soon, okay?"
    "Shay looks suspicious, but she bobs her head once. They bicker like enemies sometimes but she appreciates that Shay backs her up in her own way for things like this."
    Rival "No problem. Don’t be too long."
    "\"Or I’ll get worried\" is the unspoken finish. Shay’s out of sight a moment later and Blake does an about face back to the bus stop."
    hide rival disolve
    CW_side "Marllie?"
    show customer
    "The other girl startles. Blake catches a glimpse of her wet cheeks and red eyes before Marllie whips her head back around."
    Customer "Uh, hey! What are you doing here?"
    CW_side "I was on my way home. Are you okay?"
    "Marllie hesitates briefly, then puffs out a sigh and shakes her head. She roughly scrubs at her eyes with the back of her hand."
    Customer "I will be. It was... stupid. Stupid feelings."
    CW_side "What-"
    "The sudden realisation makes Blake want to slap herself. She’s equally as incoherent around girls she likes, after all. And Maya leaving early… fuck, Maya never leaves early."
    CW_side sad "Shit. I’m an idiot."
    "Marllie looks confused for a second."
    Customer sad "What, no! You didn’t do anything wrong."
    CW_side "I put you on the spot. I’m sorry."
    Customer "You didn’t know. And it would have happened eventually anyway. I was going to bail so you actually did me a favour. At least this ripped the bandaid off."
    CW_side "I’m still sorry. Sorry you’re hurting, I mean. "
    Customer "I’m not… sad. Well I am, but it wasn’t that serious. I’m more embarrassed than anything. I come in everyday… so that’s going to be awkward now."
    CW_side "Maya’s professional. It won’t affect her service."
    Customer "I hope not. It’s still going to feel weird for a while."
    "She sniffles once. Blake precariously snakes an arm around Marllie’s shoulders, unsure if the contact would be welcomed. To her relief, Marllie doesn’t mind."
    CW_side -sad "Maybe. But not forever."
    "The reassurance seems to help a little. Marllie leans into the embrace, apparently grateful for it to Blake’s relief."
    CW_side "Can I help? Do you need anything? Would a Triple, Venti, Half Sweet, Non-Fat, Caramel Macchiato make you feel better? "
    "A quiet snort escapes Marllie. There’s even a small smile. Blake counts it as a win."
    Customer -sad "You’d just make it wrong."
    CW_side "You wound me."
    "There’s another laugh. Marllie sniffles and swipes at her cheeks again."
    Customer "Really though, I should get home to finish off my paper. But, uh… thank you. For talking to me."
    CW_side "It’s not a problem. Let me give you my number. Text me when you get home so I know you made it safely. And, you know, I’ve got no plans tonight and no work tomorrow, so I’ll be around if you change your mind."
    Customer "I will. But I’ll probably want to be on my own for now… get over the embarrassment."
    "She manages a smile."
    Customer happy "But… thanks."
    CW_side happy "Anytime."
    "They exchange numbers silently. She notices Marllie add a little dog emoji at the end of her name and laughs."
    CW_side -happy "I should get going. I’m supposed to be getting takeout for my roommate and I."
    Customer -happy "I’ll see you later then."
    CW_side "Get home safely!"
    Customer "You, too."
    hide customer
    "Blake leaves, but as slowly as possible. She doesn’t feel too comfortable leaving Marllie alone so she’s relieved when the bus shows up."
    "She waits until Marllie climbs on and only leaves when the other girl waves at her from the window. She heads off to grab her and Shay’s dinner, vowing to shoot Marllie a text before bed."
    jump j_scenea10

label scene_a11:
    scene bg_apartment
    "It’s the weekend and Blake’s lying on the couch texting, with one of her shows blaring from the television and a half-eaten sandwich resting on her chest. Shay, having decided to stay home to study, is taking a break. She eyes Blake and seems to consider threatening her if she makes a mess, but Blake picks up the sandwich and somehow shove the entirety of it in her mouth instead."
    show rival
    Rival "Why."
    "Blake garbles unintelligibly  around the food. Shay curls her lip in disgust."
    Rival "Seriously."
    "The responded apology is barely heard and pointless on the basis that she’s still doing what she’s apologising for. Shay shifts so she’s facing the other way and shoves her nose back into her book in an attempt to ignore Blake’s antics. Blake finishes and tries again."
    CW_side "Sorry."
    Rival "Go away."
    "Blake’s phone flashes again for what has to be the dozenth time in a ten minute period. She answers, letting out a soft snort of laughter as she reads the message. Blake texts back rapidly with a reply before putting her phone down again. Shay peers at her suspiciously."
    Rival "Who are you texting? You’re grinning."
    CW_side "You remember that one customer who kept ordering ridiculous things?"
    Rival "That doesn't narrow it down, Blake."
    CW_side "Okay, you're right. Upside down macchiato. Small blonde. Can't spell her name for shit."
    Rival "Ah, yes. I remember the stories."
    CW_side "She’s babysitting some kids and they’re engrossed in a movie right now. We’re just talking about stuff."
    "Shay squints at her, looking between Blake and the phone. She puts her book down."
    Rival "You like her."
    "Blake’s smile disappears immediately."
    CW_side "What’re you talking about?"
    Rival "You like her. I remember this from your last ex. It’s the same dopey look."
    CW_side "Psh, what? Nah. It’s actually not. I barely know her."
    Rival "It actually is."
    CW_side "Is not."
    Rival "Is too."
    CW_side "Is not."
    Rival "I’m not doing this with you. You’re deflecting."
    CW_side "She’s a customer! A new friend, nothing more. I’ll admit that she’s… cute. But that’s it."
    Rival "You’re also blushing."
    CW_side "Am not."
    "Shay rolls her eyes again."
    Rival "Whatever. You should just ask her out if you like her. Save me from the pining from last time. I beg of you. I really don’t need you lying on my floor whimpering about how pretty you think a girl is again."
    CW_side "Didn’t you listen to a word I just said?"
    Rival "I did. And I’m still choosing to believe that you’re an idiot."
    CW_side "Eh, what’s new."
    Rival "Fair point."
    "Shay picks up reading from where she left off. Blake feels beyond awkward on her phone now, though, and she notes Shay’s side eye when another text message comes through. She takes a moment to casually turn up the volume on the TV and then she’ll text back as nonchalantly as possible."
    "The phone flashes again."
    "Blake gives up."
    CW_side "I’m gonna go take a nap. Didn’t sleep until 4AM, so…"
    Rival "Uh huh. Right."
    CW_side "I’ll see you in a couple of hours."
    Rival "Or tomorrow morning. I know how your naps are."
    "Blake is sure \‘naps\’ would be in air quotations if Shay could be bothered to put her book down, but she’ll take it."
    CW_side "Yeah yeah. See ya."
    hide rival
    scene bg_cobedroom
    "She leaves to her room as quickly as possible without it looking like she’s actually fleeing."
    CW_side "{b}{i}And I’m not, right? I just don’t wanna talk about my love life with Shay. Not that there is one. We’re just friends and she’s pretty cool, that’s all.{/i}{/b}"
    "Blake does take a nap, in fact. But she makes certain she texts back first."
    jump j_scenea12
label scene_a13:
    scene bg_park
    "Blake is waiting near the gate when Marllie arrives. One of the two dogs is whining and tugging at his lead, almost strangling himself in his attempt to enter the park faster. Blake gently scolds him and demands he sit, which he does… albeit very reluctantly. The other smaller dog, at least, waits patiently."
    show customer
    Customer "Sorry I’m late! "
    "She notices the dogs and squeals."
    Customer happy "They’re so cute! What are their names? Would they be okay with me petting them?"
    CW_side happy "The big one is Cookie and the well-behaved one is Alfredo. They’re friendly."
    "As if to emphasise it, Cookie is no longer trying to get into the park but instead pulling to get to Marllie. Alfredo’s tail beats against the pavement at the sight of a new friend."
    "Marllie crouches down to fuss them both equally, Cookie’s affectionate licks making her giggle. Alfredo whoofs as if demanding he gets a turn, too, so Marllie leans down further to scratch behind the smaller dog’s ears."
    CW_side "Sorry, I know Cookie can be a bit overwhelming. He almost knocked me down when I showed up to walk him for the first time."
    Customer "I love them. It’s already making me want a dog of my own."
    "She stands after giving them both an extra scratch. It’s evening, so there are plenty of people walking their pets after work or school. It’s also a particularly lovely day outside. They start walking together."
    Customer "I enjoyed your company at the restaurant last night. I know I can talk a lot when it’s something I’m interested in…"
    CW_side "I didn’t mind. I can tell you’re passionate about your studies. That’s a good thing."
    "Marllie looks bashful."
    Customer "That’s sweet of you to say..."
    "They chatter some more about their respective days, Blake regaling (what is probably) an exaggerated story of a ridiculously demanding customer. Marrlie has tears in her eyes from laughing so hard."
    CW_side -happy "So I had to add sixteen more pumps of caramel with what I’d already added and she was still insisting it wasn’t sweet enough. I watched her, with my own two eyes, add more of that artificial sweetener that we keep on the tables. Who needs that much sugar? Just because she had almond milk, doesn’t make it \"healthy\"."
    Customer angryopen "I don’t believe you. That can’t be real."
    CW_side "No, it gets better. I offered her one of Jun’s muffins after for that promo we’re having and she said -- you wouldn’t believe it -- \"oh, no, I’m on a diet. I have to watch my figure!\""
    Customer neutral "Pretty sure eighteen pumps of caramel is like, three days worth of sugar intake."
    CW_side "My head hurts just thinking about it."
    Customer "My teeth hurt just thinking about it."
    CW_side "One of my ex’s actually, her usual order was a caramel macchiato with six extra pumps. She had one basically everyday. I tried it once and nearly spat it all over her. I mean I have a sweet tooth, but oh my God."
    "Marllie’s eyes widen and she blurts out the question before she can stop herself."
    Customer "\"Her\"?"
    CW_side "Oh, yeah. You didn’t know? Shay always says I dress like a walking stereotype but I guess you haven’t seen me outside my work clothes."
    Customer "I guess she’s right. No offense, but you do look like a walking stereotype right now."
    CW_side "Wow."
    Customer "Don’t be like that. I… like it."
    CW_side happy "You like it, huh?"
    "Marllie blushes. She quickly changes the subject and soon they’re talking away again, and soon an hour’s passed and the little dog is trailing along at a slower, tired speed. Blake leans down to ruffle his fur."
    CW_side -happy "Aw, are you getting sleepy, buddy?"
    Customer "You’d better get him home. I’d better get going, too, actually..."
    "She whips out her phone and calls a cab. There’s one close by, so Blake heads off to wait with her."
    CW_side "You know… as long as I’m with them, you’re more than welcome to come along when I’m walking some dogs. I wouldn’t mind the company."
    show customer happy
    "Marllie pauses as she approaches into the uber, a slow, beaming smile spreading across her lips. Blake isn’t sure if she’s mistaking the faint sheen of colour on the other girl’s face."
    Customer "That would be wonderful."
    "Marllie leans down to give both dogs a goodbye scratch. She straightens up again, hesitates for a second before wrapping her arms around Blake’s shoulders for a quick hug. The sudden, unexpected contact and hands too full of dog leashes stops Blake from hugging back."
    "It’s brief, but Blake’s heart is pounding out of her chest anyway. Marllie has to lean up on her tiptoes and she's so warm and her perfume smells so nice and-"
    "Blake bites back an embarrassing noise of protest when Marllie pulls away. There’s a lump stuck in her throat as Marllie waves, pink-faced, and climbs into the waiting cab."
    hide customer disolve
    "As the vehicle drives away, Blake grips the leads tightly and starts to tug the dogs home. She resists the urge to watch the car turn to the next street."
    CW_side angry "{b}{i}Oh Jesus, I am so fucked.{/i}{/b}"
    jump j_scenea14
