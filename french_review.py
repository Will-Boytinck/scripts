import random
def main():
    # all january = NOT DONE
    # feb 1 - done
    # feb 2 - done
    # feb 3 - 
    # feb 4 - 
    # feb 5 -
    # feb 6 - 
    # feb 7 -
    
    WORDBANK = {
        'mere' : 'mother',
        'pere' : 'father',
        'famille' : 'family',
        'parents' : 'parents',
        'proches' : 'relatives',
        'frere' : 'brother',
        'soeur': 'sister',
        'grand-pere' : 'grandfather',
        'grand-mere' : 'grandmother',
        "L'oncle": 'uncle',
        'tante': 'aunt',
        'cousin': 'cousin',
        'fils': 'son',
        'fille': 'daughter',
        'petit fils': 'grandson',
        'petit fille': 'granddaughter',
        "L'epoux" : 'spouse',
        'il y a' : 'there is',
        'quoi' : 'what',
        'qui' : 'who',
        'pourquoi' : 'why',
        'où' : 'where',
        'combien' : 'how much',
        'quand' : 'when',
        'comment' : 'how',
        'content' : 'happy',
        'triste' : 'sad', 
        'excite' : 'excited',
        'fatigue': 'tired',
        'en colere': 'angry',
        'preoccupe': 'worried',
        "s'ennyer" : 'bored',
        'confus': 'confused',
        'amoreux': 'in love',
        'avoir peur': 'scared',
        'etre effraye': 'frightened',
        'frustre': 'frustrated',
        'surpris': 'surprised',
        'malaise' : 'embarrassed',
        'timide': 'shy',
        'nerveux': 'nervous',
        'anxieux': 'anxious',
        'sentir' : 'to feel',
        'Je me sens': 'I feel',
        'Tu te sens': 'You feel',
        'il se sent': 'he feels',
        'nous sentons': 'we feel',
        'ils se sentent': 'they feel',
        'Comment vas-tu': 'how are you',
        'Comment te sens-tu': 'how do you feel',
        'ils sont en colere': 'they are angry',
    }
    
    while True:
        key, value = random.choice(list(WORDBANK.items()))
        test = input(f"What is the english word of: {key}: ")
        if test != value:
            print(f"That is not correct, the correct word is: {value}")
        else:
            print("That is correct!")


if __name__ == '__main__':
    main()
        

