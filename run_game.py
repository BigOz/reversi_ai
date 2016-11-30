#!/usr/bin/env python3
from sys import argv
import time
from game.reversi import Reversi
from agents import random_agent, monte_carlo_agent, human_agent, handicapped_agent
from util import *
from prop_parse import prop_parse

prop_names = {
        # agent names. if user passes BlackAgent=human, becomes human_agent.Hu...
        # 'q_learning': q_learning_agent.QLearningAgent,
        'monte_carlo': monte_carlo_agent.MonteCarloAgent,
        'random': random_agent.RandomAgent,
        'human': human_agent.HumanAgent,
        'handicapped': handicapped_agent.HandicappedAgent,
        }


def main(**kwargs):

    input_args = prop_parse(argv)
    input_args.update(kwargs)

    if len(argv) <= 1 and len(kwargs) <= 1:
        print('necessary inputs:')
        print('  BlackAgent=')
        print('  WhiteAgent=')
        print('choices:')
        print('  q_learning')
        print('  monte_carlo')
        print('    mc_sim_time=(seconds to think)')
        print('  random')
        print('  human')
        print('  handicapped')
        print('    hc_sim_time=(seconds to think)')
        print('    hc_depth=(how many layers deep to search)')
        print('    hc_wrong=(how many times in 100 to make a random move)')
        print('optional inputs:')
        print('size=(board size)')
        print('amount=(#games)')
        print('silent=(True/False)')
        print('record=(True/False)')
        print('filename=(file to write results to)')
        quit()

    for k, v in input_args.items():
        # convert 'human' to human_agent.HumanAgent, etc
        if v in prop_names:
            input_args[k] = prop_names[v]
        elif v == 'q_learning':
            from agents import q_learning_agent
            input_args[k] = q_learning_agent.QLearningAgent

    amount = input_args.get('amount', 1)
    make_silent(input_args.get('silent', False))
    make_record_data(input_args.get('record', False))
    make_filename(input_args.get('filename', "test_file.txt"))

    print('About to run {} games, black as {}, white as {}.'.format(
        amount, input_args['BlackAgent'].__name__, input_args['WhiteAgent'].__name__)
        )

    summary = []
    white_wins = 0
    black_wins = 0
    reversi = Reversi(**input_args)
    start = time.time()
    for t in range(1, amount + 1):
        info('starting game {} of {}'.format(t, amount))
        winner, white_score, black_score = reversi.play_game()
        if winner == WHITE:
            white_wins += 1
        elif winner == BLACK:
            black_wins += 1
        info('game {} complete.'.format(t))
        message = '{} wins! {}-{}'.format(
                color_name[winner], white_score, black_score)
        info(message)
        record_data(black_score - white_score)
        summary.append(message)

    seconds_spent = time.time() - start
    ms_per_game = (seconds_spent / amount) * 1000
    print('time: {0:.2f} minutes ({0:.2f}ms per game)'.format(
        seconds_spent / 60, ms_per_game))
    print('summary: {} games played'.format(len(summary)))
    for each in summary:
        info(each)
    wins = {'Black': black_wins / (black_wins + white_wins) *
            100, 'White': white_wins / (black_wins + white_wins) * 100}
    print('Black won {}%'.format(wins['Black']))
    print('White won {}%'.format(wins['White']))

    return wins

if __name__ == '__main__':
    main()
