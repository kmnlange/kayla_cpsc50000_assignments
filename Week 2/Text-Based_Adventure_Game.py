'''
Kayla Lange
01/31/2026
Text-Based_Adventure_Game.py

Description: 
This program uses variables, loops, conditional statements,
and user input to create a branching text-based adventure game
'''

#Enter Game

print('\nGame Title: Lost Cat of Moon Alley')

input('\nPress ENTER to view INTRO')


#Game Intro

print('\n ***Opening Scene*** \n')
print('''A flickering streetlight hums overhead \n
You startle awake, tail twitching, paws cold against the pavement.
The air smells like rain, metal, and something faintly familiar.''')
print('You are not home.')
print('''\nSomewhere beyond Moon Alley, a warm window waits- but the night isn't done with you yet. 
Choose carefully. Every step costs energy, and sunrise is still far away.''')

choice = input('\nNEXT [Press Enter]: ')

#User Guide

guide_text = ''' \n              ***GUIDE***\n
    -Choose an option by typing "a" or "b" 
    -Your energy reflects how tired or hungry you are.
    -Some choices will restore energy. Others will drain it. 
    -Type "s" at any time to check your Status.
    -Type "i" at any time to view your inventory
    -If your energy runs out, the journey ends. 
\n Press "h" at any time to view this again.'''

print(guide_text)

#Health Stats

energy = 6


def energy_check(energy):
    if energy > 7:
        return "Strong"
    elif energy >5:
        return "Steady"
    elif energy > 3:
        return "Low-Your movements feel slower than before."
    else:
        return "Critical- Every step takes effort. You can't keep this up much longer."

# Beginning Stats

stage = 1
Location = 'Moon Alley'
Mood = 'Disoriented, hungry'
Progress = 'Still searching for home'
Helping_Friend_Advantage = 0

Inventory = []

def use_inventory_if_needed():
    global energy

    if energy <= 2 and 'Scrap of Food' in Inventory:
        print('\nYou eat the scrap of food you saved earlier.')
        energy = energy + 2
        Inventory.remove('Scrap of Food')

# energy
def energy_Message():
    return f''' ***Current Status*** \n
Energy = {energy_check(energy)}\n
Location = {Location}\n
Mood = {Mood}\n
Progress = {Progress}'''





def choice_check(choice):
    if choice == 's':
        print(energy_Message())
        choice = input('\n Press Enter to resume:')
        return True
    if choice == 'h':
        print(guide_text)
        choice = input('\n Press Enter to resume:')
        return True
    if choice == 'i':
        if Inventory:
            print('\nInventory:')
            for item in Inventory:
                print(f'- {item}')
        else:
            print('\nYour inventory is empty.')
        choice = input('\n Press Enter to resume:')
        return True
    return False

choice = input('\nPress ENTER to begin game:')
choice_check(choice)



#Main Loop- runs until player reaches end or runs out of energy

while stage < 4 and energy > 0:
    use_inventory_if_needed()   #checkchoice_check inventory for help before each stage
    if stage == 1:
        stage_Intro = '''Stage 1: Waking in the Alley\n
        You stretch and look around.
        Your stomach tightens. A torn bag of food sits nearby, 
        but the alley stretches ahead- dark, quiet, and full of unknown sounds.'''
        Location = 'Moon Alley'
        Progress = 'Still searching for home'
        Mood = 'Disoriented, hungry'
    elif stage == 2:
        stage_Intro = '''Stage 2: The Alley Stranger\n
        A pair of glowing eyes appears in the darkness
        Another cat steps forward, watching you closely.
        It tilts its head, as if deciding whether to help you.'''
        Location = 'Moon Alley'
        Progress = 'Still Searching for home'
        Mood = 'Tension, Curiosity'
    elif  stage == 3:
        stage_Intro = '''Stage 3: The Final Stretch\n
        You freeze.
        You smell a familiar scent, your old neighborhood, 
        but one last obstacle blocks your way.
        The street ahead roars with headlights and noise.'''
        Location = 'Moon Alley'
        Progress = 'Still searching for home'
        Mood = 'Urgency, Hope'

    print(f'\nEntering stage {stage}: {energy_Message()}')
    choice = input('\nPress ENTER to continue')
    if choice_check(choice):
        continue
    print(f'\n {stage_Intro}')

    if stage == 1:
        choice = input('''\n How do you proceed?
                         (a) Scavenge for food \n
                         (b) Slip through the shadows \n
            Enter your Choice: ''').strip().lower()
        if choice_check(choice):
            continue
        if choice == 'a':
            print('\n You tear into the bag, eating quickly before anything else notices.')
            Inventory.append('Scrap of Food')
            print('\nScrap of Food has been added to your inventory')
            energy = energy + 2
            stage = stage + 1
            choice = input('\nPress ENTER to continue down the alley:').strip().lower()
            if choice_check(choice):
                continue
        elif choice == 'b':
            print('\nYou stay low and quiet, every sound making your ears twitch.')
            energy = energy - 2
            stage = stage + 1
            if energy <= 0:
                print("\nYour strength fades, and the night claims you.")
                break
            choice = input('\nPress ENTER to keep moving silently:').strip().lower()
            if choice_check(choice):
                continue
        else: 
            print("""This doesn't feel like the path you should take. \n
            Try one of the listed choices.""")
            continue
    elif stage == 2:
        choice = input('''\n What will you do?
                         (a) Approach the stranger \n
                         (b) Keep your distance \n
            Enter your Choice: ''').strip().lower()
        if choice_check(choice):
            continue
        if choice == 'a':
            print('\nThe stray studies you for a moment, then turns-expecting you to follow.')
            Inventory.append('Alley Companion')
            print('\nYou have gained an alley companion')
            energy = energy - 1
            stage = stage + 1
            Helping_Friend_Advantage = 1
            if energy <= 0:
                print("\nYour strength fades, and the night claims you.")
                break
            choice = input('\n Press ENTER to follow:').strip().lower()
            if choice_check(choice):
                continue
        elif choice == 'b':
            print('\nYou move on alone, the feeling of being watched fading behind you')
            energy = energy - 1 
            stage = stage + 1
            Helping_Friend_Advantage = 0
            if energy <= 0:
                print("\nYour strength fades, and the night claims you.")
                break
            choice = input('\n Press ENTER to keep walking:').strip().lower()
            if choice_check(choice):
                continue
        else: 
            print("""\nYou hesitate, unsure what to do. \n
            Choose one of the options shown.""")
            continue
    elif stage == 3:    
        if 'Alley Companion' in Inventory:
            print('\nThe stray cat pads up beside you, steadying your steps.\n')
            energy = energy + 1
            Inventory.remove('Alley Companion')
        choice = input('''\nHow do you proceed?
                         (a) Make a run for it
                         (b) Wait and look for another way \n
                Enter your Choice: ''').strip().lower()
        if choice_check(choice):
            continue
        if choice == 'a':
            print('\nYou gather your strength and bolt forward, heart pounding.')
            energy = energy -2
            stage = stage + 1
            if energy <= 0:
                print("\nYour strength fades, and the night claims you.")
                break
            choice = input('\n Press ENTER to keep running:').strip().lower()
            if choice_check(choice):
                continue
        elif choice == 'b':
            print('\nYou sit still, tail curled tight, watching the street carefully.')
            energy = energy + 2 
            stage = stage + 1
            choice = input('\n Press ENTER to dash when the street is calm:').strip().lower()
            if choice_check(choice):
                continue
        else: 
            print("""\nThe night waits patiently. \n
            Choose one of the options...""")
            continue


if stage > 3 and energy > 2:
    print('''\nYou curl up somewhere warm as the sky begins to lighten.
    \nThe alley is behind you now, you made it home.''')
    progress = 'Finally Home.'
    Mood = 'Safety, Content'
    Location = 'Home'
elif stage > 3 and energy <= 2 and Helping_Friend_Advantage == 1:
    print(''' \nYour legs give out, and the sounds of the city blur together...
          But right as you don't think you can take one more step, 
          the stray cat emerges from the shadows, pushing their body against yours
          You both complete the final stretch of the journey.
          \n You curl up somewhere warm as the sky begins to lighten, 
          The alley is behind you now, you made it home.''')
elif stage > 3 and energy <= 2:
    print(''' \nYour legs give out, and the sounds of the city blur together.
      \nThe night was too long, and you didn't have the strength  to finish the journey.''')  
    

choice = input('\nPress ENTER to view your final game status:')
print(f'Final Status: \n {energy_Message()}')

print("\nThanks for playing Lost Cat of Moon Alley.")
