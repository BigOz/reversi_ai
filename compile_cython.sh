echo 'compiling with cython...';
cython -3 util.pyx -o util.c;
cython -3 game/reversi.pyx -o game/reversi.c;
cython -3 game/board.pyx -o game/board.c;
cython -3 agents/monte_carlo_agent.pyx -o agents/monte_carlo_agent.c;
cython -3 agents/handicapped_agent.pyx -o agents/handicapped_agent.c;

echo 'removing old .so files...';
rm *.so agents/*.so game/*.so;

echo 'compiling .c files with gcc...'
gcc -shared -I/usr/include/python3.5m -fPIC -pthread -fwrapv -O3 -Wall -fno-strict-aliasing util.c -o util.so;
gcc -shared -I/usr/include/python3.5m -fPIC -pthread -fwrapv -O3 -Wall -fno-strict-aliasing game/reversi.c -o game/reversi.so;
gcc -shared -I/usr/include/python3.5m -fPIC -pthread -fwrapv -O3 -Wall -fno-strict-aliasing game/board.c -o game/board.so;
gcc -shared -I/usr/include/python3.5m -fPIC -pthread -fwrapv -O3 -Wall -fno-strict-aliasing agents/monte_carlo_agent.c -o agents/monte_carlo_agent.so;
gcc -shared -I/usr/include/python3.5m -fPIC -pthread -fwrapv -O3 -Wall -fno-strict-aliasing agents/handicapped_agent.c -o agents/handicapped_agent.so;

echo 'removing .c files...';
rm *.c agents/*.c game/*.c;

echo 'done.';

