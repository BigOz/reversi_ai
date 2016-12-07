python3 run_game.py \
    BlackAgent="monte_carlo" \
    WhiteAgent="human" \
    hc_sim_time=5 \
    hc_max_sim=10000 \
    hc_wrong=0 \
    mc_sim_time=5 \
    silent=False \
    amount=10 \
    record=False \
    filename="example_file.txt" \
    size=8
    # sets the agent for white and black, options are handicapped, monte_carlo,
    # random, or human
    # sets the simulation time permitted for the handicapped agent
    # sets the max number of simulations permitted for the handicapped agent
    # sets the number of times in 100 the handicapped agent will make a wrong
    # move
    # sets the simulation time permitted for the monte_carlo agent
    # True to keep console silent, False to show gameply on console
    # The number of games to run
    # True if results should be appended to file, False otherwise
    # The filename results should be appended to
    # Size of the game board


