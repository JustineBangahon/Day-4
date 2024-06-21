from random import randint
while True:
    # the player input and choose 'fold' or 'unfold'
    player = 'fold' if int(input("1: Fold | 2: Unfold: ")) == 1 else 'unfold'

    #It randomly generate 'fold' or 'unfold' for both computer 1 and 2
    computer1, computer2 = ['fold' , 'unfold'][randint(0,1)], ['fold' , 'unfold'][randint(0,1)]

    #print player choice and computer random generated choices
    print(f"PLayer    : {player}\nComputer 1: {computer1}\nComputer 2: {computer2}\n")

    # Determine the winner based on choices
    if player not in (computer1, computer2):
        print("You Win")
        break
    print(f"{'Computer 1 win' if computer1 != player and computer1 != computer2 else 'Computer 2 wins' if computer2 != computer1 and computer2 != player else 'Draw'}")