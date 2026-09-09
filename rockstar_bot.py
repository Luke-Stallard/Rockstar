import random
 
def choose_move(history):
    beats = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
   
    rounds_played = len(history)
   
    if rounds_played == 0:
        return random.choice(["Rock", "Paper", "Scissors"])
   
    counter_move = beats[history[-1]["opponent"]]
   
    if rounds_played == 1:
        return counter_move
   
    if rounds_played == 2:
        if random.random() < 0.5:
            return counter_move
        else:
            return random.choice(["Rock", "Paper", "Scissors"])
           
    return random.choice(["Rock", "Paper", "Scissors"])
 
 
history = [
    {
        "round": 1,
        "player": "Rock",
        "opponent": "Paper",
        "round_winner": "Opp"
    },
    {
        "round": 2,
        "player": "Scissors",
        "opponent": "Paper",
        "round_winner": "Player"
    }
]
 
next_move = choose_move(history)
print("ROCKSTAR DOES: " + next_move)