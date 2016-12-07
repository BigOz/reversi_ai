# reversi_ai_testbed
A platform built to test various agents of game AI. 

The ultimate goal was to create a platform where a monte carlo player could compete against a handicapped monte carlo player. This platform could then be used to test various parameters through experiments.

The handicapped monte carlo player has three parameters that can be tweaked:
- number of gameplay simulations permitted before a choice of move must be made
- number of seconds the player is permitted to think before a choice of move must be made
- the number of times in 100 a player will choose a random legal move rather than an intelligent legal move

To run, use run_game.py. An example shell script has been included that outlines some of the parameters that can be controlled via the command line, including substituting a human or random player into the game, changing the board size, etc.

Scripts have also been included to allow critical game files to be compiled using Cython. My testing has shown the compiled code can complete 2-4 times more simulations in the same timeframe as the regular Python interpreter.

### Credits
The base implementation of this program was forked from Andy Salerno's excellent reversi_ai (check out his web page detailing the development of the project). It has been hacked, torn apart, and mutilated for my specific needs.