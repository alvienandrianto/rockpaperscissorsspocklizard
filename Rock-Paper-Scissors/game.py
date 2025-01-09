

def RPSgame(Play1, Play2):
    Player1 = Play1
    Player2 = Play2

    #print(Player1)
    #print(Player2)

    win_cases = {
        "Rock": ["Scissors", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Paper", "Spock"],
        "Spock": ["Scissors", "Rock"]
    }
    
    #Check
    if Player2 in win_cases[Player1]:
        print(f"Player1 input: {Player1}")
        print(f"Player2 input: {Player2}")
        return {'Player1': 'win', 'Player2': 'loss'}
    else:
        print(f"Player1 input: {Player1}")
        print(f"Player2 input: {Player2}")
        return {'Player1': 'loss', 'Player2': 'win'}