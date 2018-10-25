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
    
    
    
    
    
    