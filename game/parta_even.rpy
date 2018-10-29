label scene_a2:
    scene bg_fallsidewalk with fade
    "Blake shivers in the wind."
    CW_side sad "Jesus, what's with the sudden cold snap?"
    show rival
    Rival hips1 "Why didn’t you bring a jacket? I told you before we left."
    CW_side sad "Thought it was warmer. We’ll be out of the wind soon anyway."
    show rival distressed
    "Shay tuts disapprovingly."
    Rival "That’s what you said last time and you caught a cold for like, a week. You are atrocious to deal with when you’re sick."
    CW_side neutral "Pot, meet kettle."
    Rival "At least I don’t claim that I’m actually dying."
    CW_side sad "Well I felt like I was."
    Rival "If you get sick again I'm staying at a friend's for the week."
    CW_side happy "That's almost tempting."
    Rival angry "Rude."
    CW_side happy "Uh huh."
    hide rival
    play sound bg_car
    scene bg_busystreet with fade
    "They stop at a busy road. Shay's workplace is even closer and Blake can just make it out now behind all the passing cars."
    show rival
    Rival "I won’t be home for dinner. The girls and I are going to try that fancy new Italian place near the train station. "
    CW_side sad "Aw, where was my invite?"
    show rival happy
    "Shay raises an eyebrow at Blake."
    show rival chin1 with dis
    Rival "You sure you want to do that after what happened last time?"
    "Blake winces at the memory. After the sauce incident, she still can’t show her face in front of most of Shay’s friends."
    CW_side neutral "Okay, yeah. Maybe next time."
    hide rival with fade
    "They soon come to a stop outside Shay’s workplace."
    CW_side happy "Have a terrible day at work, bitch."
    stop music fadeout 2.0
    "Shay flips her off over her shoulder as she walks inside."
    show rival happy hips1
    Rival "You too, ho."
    hide rival
    stop sound fadeout 1.0
    jump j_scenea3
label scene_a4:
    scene bg_shop with fade
    play music nameless loop fadein 2.0
    "The morning has been going well so far. A little trouble, but Maya has been here to help each time. Blake's even managed to sell most of the banana bread. Jun will be happy."
    "She's actually starting to feel more confident."
    "The bell above the door rings and Blake’s head snaps up, ready to greet the new customer. Her newfound confidence evaporates when she sees who it is. "
    CW_side "Oh my God, I forgot to check the clock. Fuck, she’s here again. Please help." #panic TODO
    show mc annoyed with dissolve
    MC "What are you-"
    hide mc
    "The new customer walks up to the counter. Blake knows exactly who she is and she plasters on a tight smile, internally preparing herself for whatever convoluted order she’s about to receive."
    CW_side happy "Good morning! What can I get for you this morning?"
    show customer
    Marrlley "Can I please get a quad, non-fat, extra hot caramel macchiato, upside down?"
    CW_side "{i}What... the... Fuck?{/i}" #panic TODO
    CW_side "{i}Upside down???? Who is this girl?{/i}"
    "Blake keys the order into the register and repeats it. Marrlley nods in confirmation."
    CW_side happy "Sure thing. Anything else? We’ve just put out some new banana bread. It’s made with a different recipe. "
    "Marrlley ponders this for a moment. She opens her wallet to take out another bill."
    Marrlley "Sure, why not."
    CW_side "No worries. That’ll be $7.25 in total."
    "Marrlley pays and heads off to her usual table. Blake waits until she’s busy taking out her things before turning to Maya."
    hide customer
    show mc order1 neutral
    CW_side sad "You gotta help me."
    "Maya finishes rinsing out some equipment and turns to Blake."
    MC "Of course. Something with the order?"
    "Blake holds up the ticket in lieu of an explanation. She watches as Maya’s expression shifts from neutral to confused, both eyebrows furrowing."
    MC annoyed "Uh okay, that’s new."
    CW_side "All her orders are like this, I swear."
    "Maya scratches her chin in thoughtfulness. She takes the ticket and picks up one of the milk frothing jugs."
    MC -annoyed hips1 "Good practice, I guess? I think i know what she means. Here, I'll show you."
    CW_side "I wouldn’t object to a few easy ones in the morning though."
    hide mc
    play sound espresso
    "Luckily, there are no new customers to attend to. It takes two attempts, and both Maya and Blake working together to complete the order properly. The mug of coffee sits on the counter as Blake waits for the bread to come out of the toaster. "
    show mc
    MC "What do you think she does?"
    CW_side neutral "What do you mean?"
    MC "Well, she’s here almost every day and for a couple of hours. Always on her computer. "
    CW_side "I dunno. Student, maybe? It's quiet here. I know I’d work better without the distractions at home. My video games would be crying out to me."
    MC "Maybe, but her clothes look too fancy. She might be working for one of those corporations in those offices close by. "
    CW_side "She looks a bit young, though. Maybe just baby-faced. "
    MC "Maybe she just graduated then."
    CW_side "Do you usually do this? Like... people watch, I mean?"
    MC "It passes time. She is one of the regulars though; she's been coming here every day since we re-opened. "
    "A few seconds later and the bread is done. Blake sets it nicely on a plate with a knife and butter, and then sets it aside for a moment to grab a pen. She furrows brows."
    "MARRLLEY"
    "She calls out the name and misses her coworker cocking an eyebrow at her spelling, though Maya doesn't say anything."
    "Marrlley leaves her laptop at the table. She looks at her drink, looks at Blake, at Maya, back at Blake, and Blake's never felt so scrutinized in her life even though she lives with Shay. She finally leaves, seemingly satisfied"
    "Blake lets out a breath she didn't know she was holding."
    stop music fadeout 3.0
    MC happy hips1 "See. We got it."
    CW_side happy "Yeah. We did."
    "Maya offers a high five. Blake slaps her hand against her’s gratefully."
    hide mc
    pause 2.0
    jump j_scenea5
label scene_a6:
    scene bg_shop with fade
    play music happy loop fadein 3.0
    play sound bg_coffeeshop
    "Friday morning rolls around quickly. It's been busier today, with more than a few exhausted parents and college students."
    "Blake finds herself watching the clock with growing trepidation, because she knows that girl with the impossible order is going to come in at about 10AM and it's already 9:50AM and what the fuck is it going to be today?"
    "Sure enough, she's just refilling the napkin dispenser when Marrlley trots into the shop. It’s summer, yet somehow Marrlley is sporting a coat and her hair is still down."
    "Apparently, she isn't feeling the heat on quite the same level."
    show customer
    stop sound fadeout 3.0
    "Blake takes a deep breath."
    CW_side happy "Hi! What can I get you today?"
    "Marrlley brushes her hair out of her eyes and shifts her computer case into her other hand, eyeing the menu. Blake can almost feel the sweat droplets forming on her forehead."
    Marrlley "Hm, I’ll have a extra large latte, four shots."
    "Blake exhales, disbelieving. Four shots is a little much, but this order is so simple and straightforward that there has to be a catch."
    CW_side "Of course. Will that be all?"
    Marrlley "Actually…"
    CW_side sad"{i}No, please. Why did I ask? A normal order for once, please.{/i}"
    show customer sad
    "Marrlley actually looks a tiny bit apologetic."
    Marrlley -sad "Actually, can you put two decaf shots at the bottom, milk, two normal shots on top and minimal foam? Also extra hot milk."
    "Blake fights to keep her expression neutral. She can feel the herculean effort she’s exerting to stop her left eye from twitching." #panicface TODO
    CW_side neutral "You betcha. Extra large latte, four shots with milk as hot as it will go without it exploding in my face, coming right up."
    show customer happy
    "Marrlley smiles, looking relieved."
    Marrlley "As long as it’s not too much trouble."
    CW_side happy "…None at all."
    "Marrlley watches her as Blake scribbles her name onto the cup, money ready in hand."
    "The rest of the transaction thankfully goes smoothly, and Marrlley shoots her another small smile before she turns to head to her favourite table."
    hide customer with dissolve
    CW_side "{i}Maybe I can dunk my face in the sink and drown. Or maybe the milk actually will explode. Grant me mercy.{/i}"
    "She can only hope."
    "The first two shots of decaf are in the cup when Asher slides up to her, a tray of dirty cups in his hands."
    show bestie with dissolve
    Bestie "What is it today?"
    "Blake merely grunts and tilts her head towards the ticket, eyes not leaving the thermometer so she doesn’t actually get a faceful of boiling milk. Asher peers at the ticket, letting out a snort."
    Bestie "I swear it’s always just you."
    CW_side sad "GOD, I know! It’s like she enjoys watching my suffering."
    Bestie "Well…"
    CW_side "Go away, I didn’t ask you."
    "Asher laughs before he continues into the kitchen."
    Bestie happy "Just think of it as field experience!"
    hide bestie with dissolve
    "Blake grumbles under her breath. The milk is finally ready. Blake is ready for this to be over."
    "Finally, the order is done. She wipes her sweaty hands on her apron and snaps a lid onto the cup."
    CW_side happy "Order for Marrlley!"
    show customer neutral
    "Marrlley is up at the counter in a flash. She takes the coffee with another thank you and glides away. She sweeps her hair over on shoulder as she retreats, and it uncovers the back of the jacket."
    "{b}MARLLIE{/b}"
    "Blake’s eyes widen before she remembers what she had written on the cup. "
    "{b}Marrlley{/b}"
    "She has a dramatic flashback to every other time she’s written Marllie’s name and she’s more than certain none of them were correct."
    CW_side "{i}Her name was right there. God damn it. That’s embarrassing.{/i}"
    "She leans on the countertop and covers her face with her hands just as Asher walks back out."
    hide customer with dissolve
    show bestie with dissolve
    "Asher makes a sympathetic noise while Blake just lets out a long groan."
    Bestie happy "Aw, did you have to it again?"
    CW_side sad "No, worse."
    Bestie -happy "What do you mean?"
    CW_side "I’ve kind of sort of been spelling her name wrong the entire time that I’ve worked here. So like, I’m going to take my break now so I can throw myself off the bridge."
    Bestie "You can’t do that. It’s too busy."
    CW_side "Wow, thanks for the sympathy. "
    show bestie happy
    "Asher flashes her a charming smile."
    Bestie "You’re welcome! "
    "He laughs again, lightly patting her on the back."
    Bestie happy "Really though, I spell names wrong on purpose. Some customers find it funny. Others are just assholes. She hasn’t thrown a fit so I wouldn’t worry about it. "
    "Blake’s voice is muffled in her hands."
    CW_side happy "Really?"
    Bestie -happy "Yeah. But you still have to make her drinks, so..."
    "Asher’s eyes glint with amusement as Blake lets out a long, distressed noise."
    Bestie "Enjoy your break!"
    hide bestie
    stop music fadeout 3.0
    jump j_scenea7
label scene_a8:
    scene bg_shop with fade
    play music happy loop fadein 2.0
    play sound bg_coffeeshop
    "It takes another few weeks for Blake and Marllie to establish their own little routine during the quieter hours of the day."
    "As long as someone’s keeping an eye out for potential customers and everything’s tidy and prepared, Jun doesn’t really mind if they stand around for a bit."
    "Work can get boring sometimes. So can studying. They keep other company, it's a good arrangement"
    show customer
    stop sound fadeout 3.0
    "It’s almost evening now, though, and Marllie is only just slinking in. She looks a bit haggard."
    CW_side neutral "You’re here late."
    Customer "One of my classes got swapped around. And I’m going to be pulling an all-nighter, I think."
    CW_side sad "Ouch. Definitely don’t miss those. Well, ones caused by actual work, that is."
    "Blake start preparing Marllie’s order. It’s thankfully quite tame, so Blake allows herself to zone out for a bit. She scribbles the name on the cup and sketches a cute little dog face on the side. It earns her a happy, if tired grin."
    Customer happy "You know I’m going to expect those every time now."
    CW_side happy "Not going to lie, that’s the only thing I can draw."
    Customer "I mean, it’s cute!"
    "Blake lets out a small chuckle. She finishes up the drink and pops the lid on."
    CW_side "You want that same dog every time? Sure, I can do that. "
    Customer "Good."
    "The smaller girl wraps another napkin around her coffee and grabs a couple of sugars to take back to her table. She makes to leave, but she pauses."
    Customer neutral "So. Uh…  are you the only one here?"
    CW_side "Hm? Oh, uh, no. Maya and Jun are doing boring adult paperwork in the back somewhere. Just me to close up today. "
    "Marllie fiddles with the packets in her hands. She glances at the door to the back room and back at Blake. Blake tilts her head quizzically."
    CW_side neutral "Everything alright?"
    Customer "Yeah. Everything’s good."
    "Blake eyes her suspiciously."
    Customer "Totally fine. I don’t know why you would think I wasn’t."
    "Blake cocks an eyebrow. She opens her mouth to say it’s okay, but Marllie continues to babble."
    Customer "I was just wondering, you know?"
    CW_side "Right…"
    Customer "Yeah…"
    "There’s a highly awkward silence. Marllie’s still eyeing the door."
    CW_side "Erm, do you… want me to go and get her for you? I think they’re going to call it a day soon too. There’s only so much taxes you can do in one day. She’s probably ready to tear her hair out. I know I would be."
    Customer angry "No! Uh. No. I wouldn’t want to intrude on important business."
    "Marllie covers her face with her hands, blushing furiously."
    Customer "God. And I said you weren’t stealthy. I’m useless at this."
    CW_side "Hey now. Be nice. I don’t need to live that embarrassment again."
    Customer sad "Sorry."
    CW_side "{i}What the hell is going on?{/i}" #confused face TODO
    Customer angry "I’m… going to go to my table. I have to work on an assignment. You know how it is. I’ll just-"
    "The door to the back room opens. Maya, looking tired and disheveled, trudges out and sighs."
    hide customer with dissolve
    show mc order1 annoyedclosed
    MC "You know, I didn’t think I’d be doing taxes when I joined up."
    "Maya leans against the counter tiredly. Blake half-shrugs, a mug in hand that she’s now cleaning."
    CW_side "You’re the one who offered to help."
    MC annoyed "Please don’t remind me."
    show mc happy with dis
    "Maya notices the customer. She offers her her patented Customer Service Worker smile, slipping back into the role easily."
    show mc at right with moveinright
    show customer at left with moveinleft #panic TODO
    MC "Oh, hey Marllie! You’re here late."
    "Marllie looks like a deer in headlights. Her mouth opens and closes several times, trying and failing to find words."
    CW_side "Weren’t you looking for Maya? I didn’t even have to interrupt them."
    MC "Oh? What can I do for you?"
    stop music fadeout 3.0
    "With Marllie still quiet, Maya pushes herself off the counter and gestures towards the front door."
    MC "We can talk outside if you want? If it’s easier."
    "Marllie nods, looking slightly panicked. She throws a glance at Blake before following Maya out the door."
    hide mc with dissolve
    hide customer with dissolve
    CW_side "{i}Huh. Weird.{/i}"
    jump j_scenea9
label scene_a10:
    scene bg_shop with fade
    play music water loop fadein 1.0
    play sound bg_coffeeshop
    "Blake is dealing with a customer complaint when Marllie walks in. The other girl raises her eyebrows upon hearing the customer’s tantrum and Blake’s desperate retort."
    show rando
    CW_side happy "Ma’am, no offense, but we primarily serve coffee… I don’t understand-"
    Rando "But I don’t like coffee! Why would you serve me this? I want a refund. Get me your manager-!" with vpunch
    "Blake rapidly counts to ten in her head."
    CW_side "I’ll get my boss."
    hide rando disolve
    "Blake pinches her nose once her back is to the customer and heads off into the back, aware of the customer’s eyes staring daggers into the back of her head and Marllie watching sympathetically. She comes back with Jun a moment later and leaves her to deal with it while she takes her place back behind the counter."
    show customer
    CW_side neutral "Hi. What can I get you?"
    Customer "What on earth was that about?"
    stop music fadeout 5.0
    "They glance at Jun talking animatedly with the lady and said lady storming out in a huff… without her refund. Jun looks like she’s just aged ten years in their brief encounter."
    CW_side "She ordered a mocha and insisted it should taste like chocolate, not coffee, because she doesn’t like coffee. "
    Customer "Wow."
    hide customer
    show boss
    "Jun walks past them to get back to her own duties, but not before giving them a completely baffled look."
    Boss "I’ve worked far too long in this industry."
    hide boss disolve
    play music happy fadein 5.0
    show customer
    "Free of crazy customers (mostly), Blake turns back to Marllie and warily recites her spiel."
    CW_side happy "So what can I get you? Jun made some amazing new muffins if you’d like to try one. Salted caramel. I’d highly recommend them."
    Customer "I’d love one. And you’ve been through enough. Just give me a latte."
    "Marllie scrunches her face up and puts on a poor imitation of the lady’s posh accent, splaying a hand on her hip."
    Customer angryopen "And can you, like, make it not taste like coffee? I can’t stand coffee!"
    CW_side "Not you too. That’ll be $6.25. I’ll have your not-coffee ready ASAP."
    "The regular giggles."
    Customer happy "Really though, thank you. I know my orders can be a little much on occasion but you’ve always made them drinkable."
    CW_side "Drinkable, huh?"
    Customer "Edible. Drinkable. No wait, I mean that it’s never terrible tasting."
    CW_side "Thanks?"
    Customer "I’m not doing a very good job at saying this, am I?"
    CW_side "Luckily for you, I’m regularly even more awkward than you are so I get what you’re trying to say."
    "It takes a moment for Blake to realise how that sounds when said out loud. A look of horror clouds over her face"
    CW_side "{i}No no no no{/i}" #panic
    CW_side sad "N-not that I’m saying you’re awkward, I mean- "
    Customer neutral "Point taken."
    "Marllie doesn’t seem too offended."
    CW_side "I’ll go and get your order ready before I can put my foot further in my mouth now. "
    Customer happy "Thanks. Remember, I don’t want it to taste like coffee."
    CW_side "Sorry, I suddenly don’t speak english."
    stop music fadeout 5.0
    "Marllie laughs and retreats to her usual table, setting her laptop case on the table and already retrieving her books. Blake finds herself smiling as she gets to work."
    jump j_scenea11
label scene_a12:
    scene bg_shop with fade
    play music nameless loop fadein 1.0
    "The lunch rush is over, so the amount of people in the store is slowly dwindling. Blake's already had her break and popped by the deli next door for a sandwich, so at least she's not constantly tempted by the smell of Jun's fresh baking."
    "She finishes up dealing with the queue that's formed and then there's only one guy left, dressed smartly for his... office job? Or whatever. She takes his order and hands him his change."
    "The coffee he wants is simple and Blake’s hands work on autopilot, her attention free to roam around the shop."
    "There are a few people milling about. Marllie is here in her usual seat, work spread out over the table. She’s tapping away on her laptop, pen between her teeth and completely absorbed in her own work."
    CW_side "{i}Okay fine. Maybe she’s… endearing. And more than a little cute. Maybe. Maybe.{/i}"
    CW_side "{i}Shay must never know I even thought that.{/i}"
    "Blake finishes up the order, snapping the cap onto the to-go cup."
    CW_side happy "Order for Chester! "
    "The man takes his order gratefully and thanks her again. Blake sets to work rinsing out the milk jug."
    "Out of the corner of her eye, she notices as the same customer she served before hovers around Marllie, unsubtly peering at the papers on the table."
    "He adjusts his collar, smooths his hand through his hair before plastering on a charming smile. Blake groans internally, immediately understanding what he’s about to do."
    "Predictably, he approaches Marllie’s table and drops into the empty seat opposite her without preamble. The sound of the action startles her out of her reverie. She looks up at him, the tip of the pen falling out her mouth as she regards him with a blank stare for a few moments."
    "Another customer sidles up to the counter and Blake takes their order, still half paying attention to Marllie. Thankfully, it’s another simple order."
    "The man opposite to Marllie is still there, coffee rested on the table and relaxed into the seat. He’s talking animatedly, hands flying around as he gestures into a story he’s telling, but Blake pays him little mind."
    "Instead, her attention is on Marllie and the increasingly uncomfortable expression on her face. She’s almost retreated into herself, legs and arms crossed and clearly trying to find an opening to get a word in. She obviously has no idea who this man is, and wants out of this situation badly."
    "Blake finishes up quickly, pushing it into the waiting hands of the customer at the counter. She barely waits until their back is turned before she spins around, tapping Maya on the shoulder."
    CW_side neutral "Hey, I’m going for my break."
    "Maya shrugs, grunting in response and Blake wastes no time in untying her apron and tossing it over her shoulder. She snags her water bottle from its hiding place on the counter and jogs as casually as possible over to Marllie’s table."
    scene bg_cs_lounge with fade
    show customer
    CW_side happy "Hey babe, sorry about the wait. I-- oh, hello. Who’s your friend?"
    "Both heads whip up to look at Blake. Blake shoots Marllie her best, subtle “just go with it” face before shuffling over behind her, placing one hand on her shoulder and taking a swig out of her bottle."
    "Marllie stiffens slightly under her hand for a moment before relaxing. She covers Blake’s hand with her own. She tilts her head, smiling up at her. Blake returns the expression and squeezes her shoulder gently."
    Customer "He was just telling me about his new play. Something about bears?"
    "Blake watches as the man’s gaze shifts from her face to their hands. He chews on the inside of his cheek for a moment before standing from the chair. He grumbles something under his breath before turning and exiting the shop without another word."
    "Blake’s inward sigh is mirrored out loud, Marllie letting out a relieved breath and dropping the hand from her shoulder."
    Customer "Thank you so much for stepping in."
    CW_side "No problem, he didn’t seem like he was getting the message."
    Customer "I was obvious enough for you, apparently."
    CW_side "I feel like there was a dig at me in there somewhere."
    stop music fadeout 5.0
    "Marllie ducks her head and smiles shyly."
    Customer happy "Not at all."
    CW_side "Good. I uh… well, I’m on my break now. I’ll stay with you. You know, in case he comes back."
    Customer folded1 "I’d like that."
    CW_side "Cool, cool."
    "Blake sits at the offered chair, glad to be off her feet for the time being. She takes the time to pull off her apron and down half the bottle in one go."
    play music happy fadein 5.0
    Customer neutral "Honestly don’t know how you can stand for that many hours a day, most days of the week. That lunch rush was busier than usual."
    CW_side "You get used to it."
    "They sit in comfortable silence for a while as Marllie taps away on her computer. She’s always so busy, but Blake swears there’s a few less stress lines on her forehead than there had been. "
    CW_side "Correct me if I’m wrong, but you seem a hell of a lot less tense than you were yesterday."
    Customer "Been watching me, have you?"
    "Blake winces."
    CW_side "Be cool, Blake. Be cool."
    CW_side "Okay, definitely didn’t mean for it to sound so creepy."
    "Marllie laughs."
    Customer happy "I’m only joking. I’ve been working on an assignment for the past week and a half, the deadline was yesterday. I’m just finishing up my pre-tutorial readings for tomorrow right now, so there’s no stress."
    CW_side "What was the assignment about?"
    Customer "We’re supposed to write three big articles throughout the semester and that was the second one."
    CW_side "Fancy."
    Customer "Most of the time I was just researching. Interviewing people and collecting all that information and all that."
    CW_side "What did you write about?"
    Customer neutral crossed1 "Students who were having difficulties paying their tuition. "
    CW_side -happy "That’s a heavy topic."
    Customer "Yeah. I was a bit apprehensive when it was assigned to me at first but I think it was a… learning experience. "
    "Blake takes another swig of her bottle."
    CW_side "Why is that?"
    "Marllie shrugs and rests her chin on her hand."
    Customer neutral "My parents are quite well off. They’re paying for my degree, among other things, so I guess I didn’t fully appreciate how difficult it is for other people. I had to interview some people in my class, and I can’t imagine having two jobs and doing this too. Full time classes and one job is taking up almost all my free time as is."
    CW_side neutral "Yeah, I can’t imagine. I took a break so I’d be in a better financial position if I go back to studying. What else do you do?"
    Customer "I do a bit of babysitting sometimes. Just for friends of my parents so they pay me well."
    CW_side "Kids are exhausting though; that’s not an easy job."
    Customer "I know. Still…"
    "They sit talking for the rest of Blake’s break, Blake waving her arms around in animated conversation. She only notices the time when Jun calls her name. She curses under her breath. Marllie stops her as Blake makes to stand."
    Customer "Hey, before you go back…"
    "Marllie suddenly looks nervous. She’s staring at a spot slightly beside Blake’s head, fingers picking aimlessly at a sticker on her laptop’s keyboard."
    CW_side happy "What’s up? Want more coffee?"
    Customer "No. I mean yes. I mean… yes to more coffee."
    CW_side "Okay, what would you like?"
    Customer "I’ll come up and order in a second. I wanted to ask you… my last class of the day is in an hour. I was planning to come back here, do some reading and go to my favourite Vietnamese restaurant for dinner. I was wondering if you’d like to come with me?"
    CW_side neutral "..."
    Customer "I just… I like talking with you. And eating dinner alone is something I’ve been doing more often lately."
    "Blake hesitates for a second. Is it normal to be friends with a customer? Hang out with them outside working hours? She shakes the thoughts away."
    CW_side happy "I would love to."
    "There’s a hint of pink in Marllie’s cheeks at Blake’s agreement. Blake tries not to think about it too much."
    Customer happy "I’ll come back and wait for you to close then."
    CW_side "How did you know I’m closing today?"
    Customer "Today is Wednesday, isn’t it? I’m here enough to notice."
    CW_side hips1 "Fair point. So I’ll… see you tonight then."
    stop music fadeout 2.0
    "Marllie smiles widely, cutely twirling her hair around her fingers. Blake tries not to think about that too much, either… even if she wants to."
    Customer "See you tonight."
    scene black with fade
    jump j_scenea13
