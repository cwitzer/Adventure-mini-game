
import time 
import pygame, sys, time



pygame.init()
music_file = "music.exe/Music/Harvest Dawn.mp3" #
music_file2 = "music.exe/Music/Pokemon RedBlue Opening.mp3"#
transition_effect = "SoundEffects.exe/Sound effects/Video Game Start Sound Effect.mp3" #
typingsound_effect = "SoundEffects.exe/Sound effects/typing sound effect .mp3"# 
walking_effect = "SoundEffects.exe/Sound effects/walking noise.mp3" #
bushsound_effect = "SoundEffects.exe/Sound effects/Bush.wav" #
click_sound = "SoundEffects.exe/Sound effects/Pokemon (A Button) - Sound Effect (HD).mp3" #
woodswalking = "SoundEffects.exe/Sound effects/Walking In The Woods Outdoors (Free Sound Effect Download).mp3" #
sword = "SoundEffects.exe/Sound effects/sword drawn.mp3" #
wolf_attack_sound = "SoundEffects.exe/Sound effects/wolf sound.mp3" #
battle_music = "music.exe/Music/Let the Battles Begin! - Super Smash Bros. Ultimate.mp3" #
stabbing_sound = "SoundEffects.exe/Sound effects/stabbing.mp3" #
path2_sound = "music.exe/Music/path2background music.mp3" #
stranger_sound = "SoundEffects.exe/Sound effects/Stranger noise.mp3" #
meme_music = "music.exe/Music/Undertale OST_ 023 - Shop.mp3" #
meme_music2 = "music.exe/Music/Kirby dream land theme song.mp3" #
finding_princess = "music.exe/Music/Hollow Knight OST - Hornet.mp3" #
entering_sound = "SoundEffects.exe/Sound effects/Hollow Knight OST - Hornet.mp3" #
you_failed = "SoundEffects.exe/Sound effects/You Failed!.mp3" #
YAY_sound= "SoundEffects.exe/Sound effects/YAYYY.mp3" #
oh_sound = "SoundEffects.exe/Sound effects/OHHH.mp3" #
traveling_speech = "SoundEffects.exe/Sound effects/SPEECH .mp3" #
entering_the_smash = "music.exe/Music/Super Smash Bros. 4_ Main Theme.mp3" #
RUNNING_sound = "SoundEffects.exe/Sound effects/Sonic Running Sound Effect.mp3" #
door_opening = "SoundEffects.exe/Sound effects/door opening.mp3" #
evil_laugh = "SoundEffects.exe/Sound effects/Evil Laugh Sound Effect.mp3" #
help_me_sound = "SoundEffects.exe/Sound effects/HELP ME SOUND .mp3" #
battle_putin = "music.exe/Music/Pokémon Red, Blue & Yellow - Trainer Battle Music (HQ).mp3" #
removing_coat = "SoundEffects.exe/Sound effects/removing coat .mp3" #
putin_sword = "SoundEffects.exe/Sound effects/drawling sword.mp3" #
finalboss_putin = "music.exe/Music/Pokémon Red, Blue & Yellow - Trainer Battle Music (HQ).mp3" #
pound_effect_1 = "SoundEffects.exe/Sound effects/pound_effect_1.mp3" #
pound_effect_2 = "SoundEffects.exe/Sound effects/pound_effect_2.mp3" #
pound_effect_3 = "SoundEffects.exe/Sound effects/pound_effect_3.mp3" #
dash = "SoundEffects.exe/Sound effects/Zoro Dash Sound Effect FX.mp3" #
swordclash1 = "SoundEffects.exe/Sound effects/swordclash1.mp3" #
swordclash2 = "SoundEffects.exe/Sound effects/swordclash2.mp3" #
walkingin_castle = "SoundEffects.exe/Sound effects/Anime School Shoes Walking Sound Effect.mp3" #
running_sound_putin = "SoundEffects.exe/Sound effects/hallway running.mp3" #
final_scenemusic = "music.exe/Music/Gunman Clive OST - Desert.mp3" #
ALRIGHt_final = "SoundEffects.exe/Sound effects/alright!!!.mp3" #
ending_final_music = "music.exe/Music/zelda theme.mp3" #
###################

click_sound = pygame.mixer.Sound(click_sound)
typingsound_effect = pygame.mixer.Sound(typingsound_effect)
bushsound_effect = pygame.mixer.Sound(bushsound_effect)
walking_effect = pygame.mixer.Sound(walking_effect)
woodswalking = pygame.mixer.Sound(woodswalking)
sword = pygame.mixer.Sound(sword)
wolf_attack_sound = pygame.mixer.Sound(wolf_attack_sound)
transition_effect = pygame.mixer.Sound(transition_effect)
stabbing_sound = pygame.mixer.Sound(stabbing_sound)
stranger_sound = pygame.mixer.Sound(stranger_sound)
entering_sound = pygame.mixer.Sound(entering_sound)
you_failed = pygame.mixer.Sound(you_failed)
YAY_sound = pygame.mixer.Sound(YAY_sound)
oh_sound = pygame.mixer.Sound(oh_sound)
traveling_speech = pygame.mixer.Sound(traveling_speech)
RUNNING_sound = pygame.mixer.Sound(RUNNING_sound)
door_opening = pygame.mixer.Sound(door_opening)
evil_laugh = pygame.mixer.Sound(evil_laugh)
help_me_sound = pygame.mixer.Sound(help_me_sound)
removing_coat = pygame.mixer.Sound(removing_coat)
putin_sword = pygame.mixer.Sound(putin_sword)
pound_effect_1 = pygame.mixer.Sound(pound_effect_1)
pound_effect_2 = pygame.mixer.Sound(pound_effect_2)
pound_effect_3 = pygame.mixer.Sound(pound_effect_3)
dash = pygame.mixer.Sound(dash)
swordclash1 = pygame.mixer.Sound(swordclash1)
swordclash2 = pygame.mixer.Sound(swordclash2)
walkingin_castle = pygame.mixer.Sound(walkingin_castle)
running_sound_putin = pygame.mixer.Sound(running_sound_putin)
ALRIGHt_final = pygame.mixer.Sound(ALRIGHt_final)
############################################
pygame.mixer.music.load(music_file2)
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

# Set buffer size (smaller buffer can reduce latency but might cause choppy audio)

import sys
narrator = "[Narrator]: "
width = 40
Stranger = "[Stranger]:"
cut_line  = """
\n-----------------------------------------------------------------------"""
Princess = "[Princess Anay]:"
Evil_PUtin = "[Evil Putin]:"


## Intro into the adventure story
#1
def intro(): 
    typingsound_effect.play(-1)
    message = f"""
{narrator}
Welcome future Knight!
Before we get started we need a username! """
    for char in message:
        print(char,end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()

### Getting their username information 
def get_username():
    typingsound_effect.play(-1)
    prompt = ("\n\nEnter a username: ")
    typingsound_effect.stop()
    user_input = input(prompt)
    click_sound.play()
    return user_input

# Defining the storyline 
def story_line(username):
    typingsound_effect.play(-1)
    problem = f"\n{narrator}\nSir {username},\nThe beautiful Princess has been taken by Evil Putin\nWE NEED YOUR HELP!!"
    for a2 in problem:
        print(a2,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(1)
    beginning(username)
######## Princess's intro---------------------------------------------
def beginning(username):
    while True:
        typingsound_effect.play(-1)
        message_two = (f"\n\n{Princess}\nSir {username}\nI've been trapped here and I can't get out!\nWill you rescue me?(y/n): ")
        for a2 in message_two:
            print(a2,end="",flush=True)
            time.sleep(0.0300)
        typingsound_effect.stop()
        question_one = input()
        if question_one.lower() == "y":
            click_sound.play()
            time.sleep(1)
            YAY_sound.set_volume(3)
            YAY_sound.play()
            typingsound_effect.play(-1)
            waiting = f"\n{Princess}\nI'll be waiting for you ;)"
            for a3 in waiting:
                print(a3, end="",flush=True)
                time.sleep(0.0400)
            typingsound_effect.stop()
            print(str(cut_line))
            act_one(username)
            break
        elif question_one.lower() == "n":
            click_sound.play()
            time.sleep(0.9)
            pygame.mixer.music.stop()
            oh_sound.play()
            time.sleep(0.5)
            you_failed.play()
            typingsound_effect.play(-1)
            no = (f"\n{Princess}\nWEll Well well! Guess somebody doesn't wanna save me....FINE THEN I'll GET SOMEONE ELSE!\n\nGAME OVER")
            for no_a in no:
                print(no_a,end="",flush=True)
                time.sleep(0.0500)
            typingsound_effect.stop()
            time.sleep(5)
            sys.exit()
        else:
            click_sound.play()
            typingsound_effect.play(-1)
            print("Invalid answer, Try again")
            typingsound_effect.stop()
            

time.sleep(1)
###### ACTI ONE INTRO
def act_one(username):
    walking_effect.play(-1)
    message_2 = f"\n*** {username} enters the starting point ****\n"
    for a3 in message_2:
        print(a3,end="", flush=True)
        time.sleep(0.0800)
    walking_effect.stop()
    welcome_user(username)

time.sleep(1)

def welcome_user(username):
    while True:  # Use a loop to handle user input until a valid choice is made
        typingsound_effect.play(-1)
        message_3 = f"""
{narrator}
Welcome to the small Kingdom of Adobe,\nJust across the river of Greenland in Ireland there are two paths that we can travel to.\nBoth are a long distance to the princess:\n\n1. Path of the hidden woods (Filled with traps and wolves)
2. The safe path creek of Greenland(May encounter a trickster villager) """
        for a4 in message_3:
            print(a4, end="", flush=True)
            time.sleep(0.0200)
        typingsound_effect.stop()
        typingsound_effect.play(-1)
        question_12 = f"""
Which number(1/2): """
        
        for answer_123 in question_12:
            print(answer_123, end="", flush=True)
            time.sleep(0.0500)
        typingsound_effect.stop()
        answer_1 = input() 
        if answer_1 == "1":
            click_sound.play()
            print(str(cut_line))
            path1(username)
            break

        elif answer_1 == "2":
            click_sound.play()
            print(str(cut_line))
            path2(username)
            break
        else:
            print("invalid Answer")
        
####PATH1 STORYLINE ACT I#####------------------------------------------------
def path1(username):
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music_file)  # Load the new music file
    pygame.mixer.music.play(-1)  # Start playing the new track
    typingsound_effect.play(-1)
    transition_effect.play()
    
    message_5 = f"""
*** Entering the hidden woods ***
    """
    for a6 in message_5:
        print(a6,end="",flush=True)
        time.sleep(0.0800)
    typingsound_effect.stop()
    typingsound_effect.play(-1)
    message_6 = f"""
{narrator}
Welcome Sir {username}
This is the Hidden Woods,
It's a long walk but it will do for now, definitely better than the "Safe path" option
*COUGH COUGH**
"""
    for b in message_6:
        print(b,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()

    time.sleep(0.0500)

    typingsound_effect.play(-1)
    time.sleep(1)
    message_j = f"""
anyways...
 """
    for c in message_j:
        print(c,end="",flush=True)
        time.sleep(0.0900)
    typingsound_effect.stop()
    time.sleep(0.0500)
    typingsound_effect.play(-1)
    message_n =f"""
{narrator}
Shall we venture into the forest.....?\n """
    for answering_message in message_n:
        print(answering_message, end="", flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    into_thewoods(username)

def into_thewoods(username):
    walking_effect.play(-1)
    typingsound_effect.play(-1)
    begin_message = f"""
\n*** Begins walking into the forest***\n"""
    for acs in begin_message:
        print(acs, end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    walking_effect.stop()


    typingsound_effect.play(-1)
    begin_message2 = f"""

{narrator}
What you see before you may seem like mere empty groves, yet they hold secrets in their silent depths.
During the daylight, these woods are mostly safe, a sanctuary of serene greenery, 
but as dusk falls the shadows whisper tales of mystery and danger.\n"""
    for aa in begin_message2:
        print(aa, end="", flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(1)
    typingsound_effect.play(-1)
    message_m = f"""
Oh!
I should probaly tell you about the princess while we are at it,
The Princess was captive during the fierce conflict between our noble Adobe Kingdom and the fierce warriors of Ireland.
She got captured from the evil Putin during the battle when the stakes were high,
and now the air is thick with uncertainty—is our princess still alive......

{narrator}
Quick!
Lets step softly but swiftly into the embrace of these woods—the quest for our princess and the soul of our kingdom begins now!
"""
    for ab in message_m:
        print(ab, end="", flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()

    time.sleep(3)
    typingsound_effect.play(-1)
    woodswalking.play(-1)
    message_7 = f"\n\n*** AIMLESSLY WALKING ***"
    for a8 in message_7:
        print(a8,end="", flush=True)
        time.sleep(0.0500)
    woodswalking.stop()
    typingsound_effect.stop()
    pygame.mixer.music.stop()
    time.sleep(2)


    bushsound_effect.play(-1)
    message_8 = f"\n***CRACKLE SOUND FROM THE RIGHT!!!***\n"
    for a9 in message_8:
        print(a9,end="", flush=True)
        time.sleep(0.0300)
    bushsound_effect.stop()

    typingsound_effect.play(-1)
    message_9 = f"\n{narrator}\nWhat..... what was that???\n"
    for a10 in message_9:
        print(a10,end="", flush=True)
        time.sleep(0.0900)
    typingsound_effect.stop()
    question_11actIII(username)

def question_11actIII(username):
    while True:
        typingsound_effect.play(-1)
        messageabc = """
1. It's nothing to worry about 
2. Let's be on guards
Which number(1/2): """
        for answer1221 in messageabc:
            print(answer1221, end="", flush=True)
            time.sleep(0.0500)
        typingsound_effect.stop()
        answer123 = input()
        if answer123 == "1":
            click_sound.play()
            answer1(username)
            break
            
        elif answer123 == "2":
            click_sound.play()
            answer2(username)
            break
        
        else:
            print("invalid answer")
            question_11actIII(username)

###### function for anwer 1 in messageabc #### 
def answer1(username):
    typingsound_effect.play(-1)
    message1_actII = f"""
{narrator}
Ok....
*Laughs nervously*
Maybe it was my imagination
.........
"""
    for message_AII in message1_actII:
        print(message_AII, end="", flush=True)
        time.sleep(0.0900)
    typingsound_effect.stop()
    time.sleep(2)
    wolve_1(username)       

def answer2(username):
    typingsound_effect.play(-1)
    message2_actII = f"""
{narrator}
Ok let's do it!
"""
    for message2_AII in message2_actII:
        print(message2_AII,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    wolve_1(username)


def wolve_1(username):
    pygame.mixer.music.load(battle_music)
    pygame.mixer.music.play(-1)
    wolf_attack_sound.play()
    wolve_attack = f"""
{narrator}
{username} WATCH OUT!!!!!!!
WOLVE ATTACK!!!!!!\n""" 
    for ATT in wolve_attack:
        print(ATT,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.play(-1)
    wolf_attack_sound.play()
    battle_1 = f"""
QUICK!!
TAKE COVER!!\n

** [{username}] takes cover**\n """
    for battle in battle_1:
        print(battle, end="", flush=True)
        time.sleep(0.0400)
    typingsound_effect.stop()
    time.sleep(2)
    wolve_2(username)

def wolve_2(username):
    wolf_attack_sound.play()
    typingsound_effect.play(-1)
    message_wolve_2 = f"""
**{narrator}dodges the wolves **\n

{narrator}
Woah that was too close......\n"""
    for wolve_attack2 in message_wolve_2:
        print(wolve_attack2, end="", flush=True)
        time.sleep(0.0400)
    typingsound_effect.stop()
    time.sleep(2)
    answer2_fight2(username)
    

def answer2_fight2(username):
    wolf_attack_sound.play()
    sword.play()
    time.sleep(0.500)
    typingsound_effect.play(-1)
    fight_answer2 = f"""

*** [Narrator] kills a wolf **\n"""
    for fighting_scene in fight_answer2:
        print(fighting_scene, end="", flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    stabbing_sound.play()
    time.sleep(2)
    decision_1(username)

def decision_1(username): 
    typingsound_effect.play(-1)
    decision = f"""
{narrator}
{username} are you ok? 


[{username}]:
Yeah I'm fine......\n

{narrator}
Ok good, it looks like we are out numbered, 
I think we need to get the heck out of here\n
        
[{username}]:
Ok,
Sounds good to me\n """
    for acs in decision:
        print(acs,end="",flush=True)
        time.sleep(0.0600)
    typingsound_effect.stop()
    typingsound_effect.play(-1)
    time.sleep(1)

    running_away = f"""
*** {username} RUNS AWAY *** 
""" 
    for run_option in running_away:
        print(run_option,end="",flush=True)
        time.sleep(0.0300)
    print(str(cut_line))
    typingsound_effect.stop()
    act_II(username)



####END OF PATH1 STORYLINE#####-------------------------------------



####START OF PATH2  STORYLINE####----------
#Now going to be working on Path2 storyline###
def path2(username):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path2_sound) 
    pygame.mixer.music.play(-1)
    transition_effect.play()
    typingsound_effect.play(-1)
    message_101 = f"""
***Entering the safe path creek of Greenland***\n"""
    for path_safe in message_101:
        print(path_safe,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)

    typingsound_effect.play(-1)
    talking_message = f"""
{narrator}
Well, here we are. It's not a bad choice you made.
Normally, I would have been a bit nervous about this path, but we should be fine. They usually don't come out at this time of day.

**Begins to walk into the path **
""" 
    for lets_talk in talking_message:
        print(lets_talk,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2.5)

    typingsound_effect.play(-1)
    responding = f"""
{username}:
Who do you mean by "they"?\n"""
    for question012 in responding:
        print(question012,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)

    typingsound_effect.play(-1)
    talking_message2 = f"""
\n
{narrator}
Oh... um, well, you see, there are some folks we might run into. They are interesting, to say the least.
I should probaly tell you about the princess while we are at it,
The Princess was captive during the fierce conflict between our noble Adobe Kingdom and the fierce warriors of Ireland.
She got captured from the evil Putin during the battle when the stakes were high,
and now the air is thick with uncertainty—is our princess still alive......

{narrator}
Quick!
Lets step softly but swiftly into the embrace of these woods—the quest for our princess and the soul of our kingdom begins now!"""
    for question0123 in talking_message2:
        print(question0123,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(3)

    typingsound_effect.play(-1)
    stranger_sound.play()
    message_10123 = f"""\n
{Stranger}
Hello there...\n"""
    for asc_answer in message_10123:
        print(asc_answer,end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(1)

    typingsound_effect.play(-1)
    question_mark123 = f"""
[{username}]:
uhhh hello.... can we help you?\n"""
    for dwDi2 in question_mark123:
        print(dwDi2,end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(1)
    question_1923(username)

def question_1923(username):
    while True:     
        typingsound_effect.play(-1)
        stranger_sound.play()
        message_1923 = f"""
{Stranger}
Hey...
I know you you are looking for the princess, I think I can help with that....
Let's just say I know a way....
Continue(y): """
        for asc_answer2 in message_1923:
            print(asc_answer2,end="",flush=True)
            time.sleep(0.0300)
        typingsound_effect.stop()
        answer_10232 = input()
        if answer_10232 == "y":
            click_sound.play()
            question_10100(username)
            break
        else:
            print("Invalid Answer, try again")
    
def question_10100(username):
    typingsound_effect.play(-1)
    message_111230 = f"""
[{username}]
You can???
That would be helpfull actually...
\n"""
    for path_safe101 in message_111230:
        print(path_safe101,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    answer_23844(username)

def answer_23844(username):
    typingsound_effect.play(-1)
    stranger_sound.play()
    message_22323 = f"""
{Stranger}
Excellent!
My path is better and faster, let's head to the woods!!
...\n
{narrator}
Wait Stranger can you give me and {username} a second.
.
.
.
Hey {username},
We should stick on focusing on heading to the kingdom and following the plan, I don't really trust this guy that much
I think we should try to dtich him\n"""
    for asd23_234 in message_22323:
        print(asd23_234,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    answer238466(username)


############STORYLINE PATH2 Decision################

def answer238466(username):
    while True: 
        typingsound_effect.play(-1)
        message_1923234 = f"""
1.Ok ditch him 
2.Give it some more time 
Answer(1/2): """
        for asc_answer122 in message_1923234:
            print(asc_answer122,end="",flush=True)
            time.sleep(0.0500)
        typingsound_effect.stop()
        answer_10102 = input()
        if answer_10102 == "1":
            click_sound.play()
            answer238445(username)
            time.sleep(1)
            break
        elif answer_10102 == "2":
            click_sound.play()
            answewr_2_334(username)
            time.sleep(1)
            break
        else:
            print("Invalid Answer")


######STORY FOR 1 answer IN ANSWER2384 DECISION#######
def answer238445(username): 
    pygame.mixer.music.stop()
    pygame.mixer.music.load(meme_music2) 
    pygame.mixer.music.play(-1)
    time.sleep(0.5)
    typingsound_effect.play(-1)
    stranger_sound.play()
    message_1923 = f"""
{Stranger}
NO WAIT!.....I mean
There is no need to.....
Listen the princess is doing fine, TRUST ME..
Besides if she was in that much danger the whole world would be looking for her, it's seriously not that big of a deal...\n"""
    for asd23_23231 in message_1923:
        print(asd23_23231,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    answer22311(username)


def answer22311(username):
    typingsound_effect.play(-1)
    message_12937 = f"""
{narrator}
Remember {username},
We knew ahead of time we might encounter a trickster\n"""
    for asd23_23231 in message_12937:
        print(asd23_23231,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    answer2384(username)


def answer2384(username):
    typingsound_effect.play(-1)
    message_192323 = f"""
[{username}]:
Mr Stranger, there something that popped up that we need to go.....\n
"""
    for asc_answer12 in message_192323:
        print(asc_answer12,end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(2)
    answer2384212(username)

def answer2384212(username):
    typingsound_effect.play(-1)
    message_192323 = f"""
*** {username} RUNS AWAY ****\n"""
    for asc_answer1223 in message_192323:
        print(asc_answer1223,end="",flush=True)
        time.sleep(0.0300)
    print(str(cut_line))
    typingsound_effect.stop()
    time.sleep(3)
    act_II(username)

######END STORY FOR 1 answer IN ANSWER2384 DECISION#######


######STORY FOR 2 answer IN ANSWER2384 DECISION#######
def answewr_2_334(username):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(meme_music) 
    pygame.mixer.music.play(-1)
    typingsound_effect.play(-1)
    message_123474 = f"""
{narrator}
Ok, lets give it some more time\n"""
    for asc_answer12232 in message_123474:
        print(asc_answer12232,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    comment_2123(username)

def comment_2123(username):
    typingsound_effect.play(-1)
    stranger_sound.play()
    message_12347454 = f"""
{Stranger}
Another thing is.....is the dangerous animals out here!
I don't think it's best for you too follow me instead...
TRUST ME.......\n """
    for asc_answer122321 in message_12347454:
        print(asc_answer122321,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2.5)
    answewr_2_3344(username)

def answewr_2_3344(username):
    typingsound_effect.play(-1)
    message_12347423 = f"""
{narrator}
OK! It's time to go!\n
*** {username} RUNS AWAY ****\n"""
    for asc_lol23 in message_12347423:
        print(asc_lol23,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    print(str(cut_line))
    time.sleep(2)
    pygame.mixer.music.stop()
    time.sleep(1)
    act_II(username)
###### END STORY FOR 2 answer IN ANSWER2384 DECISION#######



##Next Act, Act II Going to be where both storys come together to find the princess. 

def act_II(username):
    entering_sound.play()
    time.sleep(2)
    pygame.mixer.music.load(finding_princess)  # Load the new music file
    pygame.mixer.music.play(-1)  # Start playing the new track
    typingsound_effect.play(-1)
    message1223 = f"""
{narrator}
Keep Running!!
Don't stop, if we get caught we won't be able to save the Princess,
.
.
.
I forgot to tell you this but we are sorta on a time crunch 
See the Evil Putin said if we don't get her by the next day,
He will KILL HER!!!!!\n"""
    for asc_lol231 in message1223:
        print(asc_lol231,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message122323 = f"""
{username}:
OH CRAP!!!
How much time do we have left?


{narrator}
Less than 24 hours WE NEED TO HURRY!!!!\n"""
    for asc_lol2313 in message122323:
        print(asc_lol2313,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    ### ENTERING THE TRAVELING SCECE 
    entering_sound.play()
    time.sleep(1)
    traveling_speech.play()
    typingsound_effect.play()
    message_23241 = f"""\n
{narrator}
As they journeyed along the rugged coastline, 
their eyes fixed on the distant horizon, they were fueled by an unyielding passion. 
Each step brought them closer to the hidden kingdom where the captive princess awaited her saviors. 
The crashing waves echoed their determination, and the salty breeze carried their unspoken vows to rescue her at any cost."""
    for asc_lol231323 in message_23241:
        print(asc_lol231323,end="",flush=True)
        time.sleep(0.0400)
    typingsound_effect.stop()
    print(str(cut_line))
    pygame.mixer.music.stop()
    time.sleep(3)
    typingsound_effect.play(-1)
    message122324 = f"""\n
{narrator}
We made it.\n"""
    for asj2e2 in message122324:
        print(asj2e2,end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(1)
    typingsound_effect.play(-1)
    walking_effect.play()
    message122323432 = f"""
*** Walking towards the Kingdom ***\n"""
    for asj2e223in in message122323432:
       print(asj2e223in, end="",flush=True)
       time.sleep(0.0600)
    typingsound_effect.stop()
    pygame.mixer.music.load(entering_the_smash)
    pygame.mixer.music.play(-1)
    time.sleep(2)
    typingsound_effect.play(-1)
    message12232323 = f"""
{narrator}
Looks like we entered the entrance...
I think we should walk around to locate the princess...\n"""
    for asj2e223 in message12232323:
        print(asj2e223,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    pygame.mixer.music.stop()
    help_me_sound.play()
    help_me = f"""
{Princess}
HELP!!!!\n"""
    for asj2e22323 in help_me:
        print(asj2e22323,end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()

    time.sleep(2)

    typingsound_effect.play(-1)
    message657 = f"""
[{username}]:
Who said that??...\n"""
    for asj2e2232 in message657:
        print(asj2e2232,end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()

    time.sleep(2)

    typingsound_effect.play(-1)
    help_me2 = f"""
{Princess}
I'M UP HERE !!!!\n"""
    for asj2e223233 in help_me2:
        print(asj2e223233,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message122323 = f"""
{narrator}
HOLD ON Princess WE'RE COMING!! ..\n"""
    for asj2e22323323 in message122323:
        print(asj2e22323323,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(1)
    RUNNING_sound.play()
    typingsound_effect.play(-1)
    message1223234 = f"""
*** {narrator} & {username} RUNNING ***\n"""
    for asj2e22323233 in message1223234:
        print(asj2e22323233,end="",flush=True)
        time.sleep(0.0400)
    typingsound_effect.stop()
    RUNNING_sound.stop()
    time.sleep(1)
    pygame.mixer.music.stop()
    door_opening.play()
    time.sleep(2)
    evil_laugh.play()
    time.sleep(1)
    evil_putin(username)

def evil_putin(username):
    while True:
        typingsound_effect.play(-1)
        evil_putin = f"""
{Evil_PUtin}
Well Well Well..\n"""
        for message_231234 in evil_putin:
            print(message_231234,end="",flush=True)
            time.sleep(0.0500)
        typingsound_effect.stop()
        time.sleep(2)
        typingsound_effect.play(-1)
        evil_putin1523 = f"""
Look who made it
I knew you were coming Sir {username}....
Let me guess you are here for Princess aren't you...

Answer(y/n): """
        for asj2e2212323 in evil_putin1523:
            print(asj2e2212323,end="",flush=True)
            time.sleep(0.0300)
        typingsound_effect.stop()
        continue_it = input()
        if continue_it == "y":
            click_sound.play()
            evil_putin2(username)
            break
        else:
            print("Invalid Answer")

def evil_putin2(username):
    typingsound_effect.play(-1)
    message_231 = f"""
{Evil_PUtin}
Well if you really want her that bad {username} than..\n"""
    for asj2e221232323 in message_231:
        print(asj2e221232323,end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    removing_coat.play()
    putin_sword.play()
    time.sleep(2)
    option_213(username)

def option_213(username):
    while True:
        typingsound_effect.play(-1)
        message_23123 = f"""
{Evil_PUtin}
YOU WILL HAVE TO GO THROUGH ME THAN!!
Accept(y): """
        for asj2e21234 in message_23123:
                print(asj2e21234,end="",flush=True)
                time.sleep(0.0200)
        typingsound_effect.stop()
        answer_10232 = input()
        if answer_10232 == "y":
            click_sound.play()
            time.sleep(1)
            final_battle1(username)
            break
        else:
            click_sound.play()
            print("\nBRUH PLEASE JUST DO Y")
            time.sleep(2)

def final_battle1(username):
    pygame.mixer.music.load(finalboss_putin)
    pygame.mixer.music.play(-1)
    time.sleep(3)
    print(str(cut_line))
    time.sleep(1)
    pound_effect_1.play()
    message_2768 ="""\n
FINAL. 
    """
    print(message_2768)
    time.sleep(0.32)
    pound_effect_2.play()
    message_231244 ="""
    BATTLE."""
    print(message_231244)
    time.sleep(0.34)
    pound_effect_3.play()
    message_231234 = """
            BEGINS!!!\n"""
    print(message_231234)
    time.sleep(2)
    evil_laugh.play()
    typingsound_effect.play()
    message_2312332 = f"""
{Evil_PUtin}
YOU WILL LIVE TO REGRET THIS DAY!\nTHE PRINCESS IS MINE!!.......\n"""
    for asj2e21234 in message_2312332:
            print(asj2e21234,end="",flush=True)
            time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(1)
    typingsound_effect.play()
    message_23123321 = f"""
YOU WON'T TAKE HER AWAY FROM ME !!!!!\n"""
    for asj2e21234 in message_23123321:
            print(asj2e21234,end="",flush=True)
            time.sleep(0.0100)
    typingsound_effect.stop()
    time.sleep(2)
    entering_sound.play()
    sword.play(-1)
    message_231343 = f"""\n
{narrator}
BRING IT ON!!"""
    for awd2937 in message_231343:
        print(awd2937,end="",flush=True)
        time.sleep(0.0200)
    time.sleep(2)
    sword.stop()
    dash.play()
    time.sleep(0.5)
    messagegg123 = f"""\n
{Evil_PUtin}
TAKE THIS!!"""
    for asc2332 in messagegg123:
         print(asc2332, end="",flush=True)
         time.sleep(0.0010)
    typingsound_effect.stop()

    swordclash1.play()
    time.sleep(3)
    dash.play()
    time.sleep(1)
    swordclash2.play()
    time.sleep(5)
    typingsound_effect.play(-1)
    messagegg = f"""\n
{Evil_PUtin}
NOT BAD KIDO....."""
    for asc23 in messagegg:
         print(asc23, end="",flush=True)
         time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    messagegg2312 = f"""\n
{narrator}
QUICK!

{username} RUN I'll try to hold him off!!!\n"""
    for asc23123 in messagegg2312:
         print(asc23123, end="",flush=True)
         time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message2133 = f"""
[{username}]:
OK sounds good"""
    for asc231232113 in message2133:
         print(asc231232113, end="",flush=True)
         time.sleep(0.0500)
    typingsound_effect.stop()
    running_sound_putin.play(-1)
    time.sleep(2)
    entering_sound.play()
    pygame.mixer.music.stop
    pygame.mixer.music.load(final_scenemusic)
    pygame.mixer.music.play(-1)
    time.sleep(4)
    running_sound_putin.stop()
    typingsound_effect.play(-1)
    messagegg231223 = f"""\n
[{username}]:
I have to find her!"""
    for asc23123213 in messagegg231223:
         print(asc23123213, end="",flush=True)
         time.sleep(0.0500)
    typingsound_effect.stop()
    running_sound_putin.play()
    time.sleep(2)
    help_me_sound.play()
    time.sleep(4)
    help_me_sound.play()
    pygame.mixer.music.stop()
    time.sleep(1)
    typingsound_effect.play(-1)
    messagegg2312221 = f"""\n
[{username}]:
HOLD ON PRINCESS I AM ON MY WAY!!!"""
    for asc231123 in messagegg2312221:
         print(asc231123, end="",flush=True)
         time.sleep(0.0500)
    typingsound_effect.stop()
    running_sound_putin.play()
    time.sleep(3)
    door_opening.play()
    time.sleep(1)
    ALRIGHt_final.play()
    time.sleep(1)
    typingsound_effect.play(-1)
    message1232313 = f"""\n
{Princess}
{username} you mande it...
I can't believe it's happening!!!"""
    for asc2312313 in message1232313:
         print(asc2312313, end="",flush=True)
         time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message1323232 = f"""\n
{Princess}
Evil Putin has been keeping here captive against my will.
He's after my royal blood."""
    for asc2123123 in message1323232:
         print(asc2123123, end="",flush=True)
         time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(3)
    typingsound_effect.play(-1)
    message12123213 = f"""\n
[{username}]:
I'm sorry to hear that..."""
    for asc212223 in message12123213:
        print(asc212223, end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(1)
    typingsound_effect.play(-1)
    message12122345 = f"""\n
[{username}]:
But have no fear... I'm here, So LETS GO!
While we have the chance!"""
    for asc21123222 in message12122345:
        print(asc21123222, end="",flush=True)
        time.sleep(0.0300)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message11231223= f"""\n
{Princess}
Wait.....
I'm greatfull, but I am also nervous...."""
    for asc21324 in message11231223:
        print(asc21324, end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    messages0092 = f"""\n
[{username}]:
Why is that?"""
    for asc2992 in messages0092:
        print(asc2992, end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(1)
    typingsound_effect.play(-1)
    message00292 = f"""\n
{Princess}
I am just scared...
I've been trapped here for decades who knows .."""
    for asc823 in message00292:
        print(asc823, end="",flush=True)
        time.sleep(0.0400)
    typingsound_effect.stop()
    typingsound_effect.play(-1)
    message1112323= f"""\n
[{username}]:
Hey!"""
    for asc27364 in message1112323:
        print(asc27364, end="",flush=True)
        time.sleep(0.0200)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message002323 = f"""\n
*** {username} reaches out his hand **** """
    for asc82323112 in message002323:
        print(asc82323112, end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message02324223 = f"""\n
[{username}]:
Everything is gonna be ok."""
    for asc823 in message02324223:
        print(asc823, end="",flush=True)
        time.sleep(0.0400)
    typingsound_effect.stop()
    time.sleep(3)
    typingsound_effect.play(-1)
    message09977 = f"""\n
*** Princess Smiles ****"""
    for asc823123 in message09977:
        print(asc823123, end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(2)
    typingsound_effect.play(-1)
    message03214 = f"""\n
{Princess}
Ok then,
Let's go!""" 
    for asc822321 in message03214:
        print(asc822321, end="",flush=True)
        time.sleep(0.0500)
    typingsound_effect.stop()
    time.sleep(1)
    pygame.mixer.music.load(ending_final_music)
    pygame.mixer.music.play(-1)
    time.sleep(2)
    message09977 = """
                                                                                        *** CONGRATS ON SAVING THE PRINCESS!!! ****"""
    print(message09977)
    time.sleep(370)
## calling the functions 
intro()
#storing the get_useranme function in a variable called user_name to reuse it 
username = get_username()
#storing the story_lube function in a variable called story_message to reuse it 
story_line(username)
#than printing the story_message variable 

