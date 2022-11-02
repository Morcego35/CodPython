import random 

D20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
D6 = [1,2,3,4,5,6]


def roll(dado):
    i = random.randint(0, len(dado))
    if (i == 0):
        print(i+1)
    else:
        print(i)
        
roll(D20)