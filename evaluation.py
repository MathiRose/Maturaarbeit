from randomStr import randomStr
from human import humanStr
from Minimax import MinimaxStr
from QLearning import QLearningStr, QTrained, QTable, Exploration
import time
import pickle


def play(str1, str2, games = 100):

    wins = 0
    losses = 0
    average_times = [0, 0]  # List to store average time for each player

    for i in range(games):          #play games between the two strategies
        result = timed_game(str1, str2)
        
        if result[0] == 'win':
            if result[1] == 1:  
                wins += 1
            else:
                losses += 1

        average_times[0] += result[2][0]
        average_times[1] += result[2][1]

    winrate = wins / games
    average_times = [time / games for time in average_times]  # Calculate average time for each player

    return wins, losses, average_times


def timed_game(str1, str2):

    game = True
    player = 1
    board = [[0] * 6 for _ in range(7)]
    player_times = [0, 0]  # List to store total time for each player
    turn_amount = 0  # Counter for the number of turns taken
    
    while True:
        turn_amount += 1  
        
        if player == 1:
            start_time = time.perf_counter()    #startzeit
            state = str1(board, 1)
            end_time = time.perf_counter()      #endzeit
            player_times[0] += end_time - start_time
            if type(state) == str:
                average_times = list(map(lambda x: x / (turn_amount//2), player_times)) #there is some issue with dividing by (turn_amount//2) when turn_amount is odd, but it should be a good enough approximation for now
                return [state, 1, average_times]
            
            board, player = state
            
        else:
            start_time = time.perf_counter()    #startzeit
            state = str2(board, 2)  
            end_time = time.perf_counter()      #endzeit
            player_times[1] += end_time - start_time
            if type(state) == str:
                average_times = list(map(lambda x: x / (turn_amount//2), player_times)) #WIP
                return [state, 2, average_times]
            
            board, player = state

play(QLearningStr, randomStr, 1)