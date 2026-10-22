import numpy as np
import random
actions=[0,1,2]   #0-->rock ; 1-->paper ; 2-->scissors


def collect_rewards(player,opponent):
    if player == opponent:
        return 0
    elif (player == actions[0]  and opponent == actions[2]) or (player == actions[2] and opponent == actions[1]) or (player == actions[1] and opponent == actions[0]):
        return 1
    else:
        return -1
    
Q=np.zeros((3,3))
alpha = 0.5   
gamma = 0.9  
epsilon=0.2
episode=1000

for ep in range(episode):
    if random.uniform(0, 1) < epsilon:
        player_action=random.choice(actions)
    else:
        player_action = np.argmax(np.mean(Q, axis=1)) 

    opponent_action=random.choice(actions)

    reward = collect_rewards(player_action, opponent_action)

    Q[player_action, opponent_action] = Q[player_action, opponent_action] + alpha * (reward + gamma * np.max(Q[opponent_action]) - Q[player_action, opponent_action])

def play_game():
    print("Choose your move: 0=Rock, 1=Paper, 2=Scissors")
    player_action = int(input())
    opponent_action = np.argmax(np.mean(Q, axis=1))  
    print(f"You chose: {actions[player_action]}")
    print(f"Agent chose: {actions[opponent_action]}")
    reward = collect_rewards(player_action, opponent_action)
    if reward == 1:
        print("Agent wins!")
    elif reward == -1:
        print("You win!")
    else:
        print("It's a tie!")

while True:
    play_game()
    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        break
