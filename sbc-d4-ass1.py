from random import randint

while True:
    # Generate a list of 3 random numbers between 0 and 2
    random_num = [randint(0, 2) for randnum in range(3)]
    
    # Get the user's bet, split it into a list of strings ex.['1', '2', '3'], map each to an int 1 ' ' 2 ' ' 3, and convert to a list [1, 2, 3]
    bet = list(map(int, input("Enter Bet(ex. 1 2 3): ").split()))
    
    # Print the user's bet and the randomly generated numbers and convert the list to string separated by space using(' '.join(map()))
    # ex. random_num is `[1, 2, 3]` when map() it's `'1', '2', '3'`. when ' '.join is become `1 2 3`
    print(f"Your Bet: {' '.join(map(str, bet))}\nThe Result: {' '.join(map(str, random_num))}")
    
    # Determine the outcome and print it
    print(f"{'You Win' if bet == random_num else 'Ramble Win' if sorted(bet) == sorted(random_num) else 'You lose'}")
