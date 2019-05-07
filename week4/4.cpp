#include <deque>
#include "edx-io.hpp"

using namespace std;

int man() {
    char operation;
    auto queue = new long[1000000];
    int startPtr = 0;
    int endPtr = -1;
    int n;
    io >> n;

    deque<long> deque;

    for (int i = 0; i < n; i++) {
        io >> operation;
        if (operation == '-') {
            if (deque.front() == queue[startPtr]){
                deque.pop_front();
            }
            startPtr++;
        }
        else if (operation == '+'){
            endPtr++;
            io >> queue[endPtr];
            while (!deque.empty() && deque.back() > queue[endPtr]) {
                deque.pop_back();
            }
            deque.push_back(queue[endPtr]);
        }
        else {
            io << to_string(deque.front()) << '\n';
        }
    }

    return 0;
}

