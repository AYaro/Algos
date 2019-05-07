#include "edx-io.hpp"

int main(){
    char operation;
    auto queue = new int[1000000];
    int endPtr = 0;
    int startPtr = 0;
    int n;
    io >> n;

    for (int i = 0; i < n; i++) {
        io >> operation;
        if (operation == '-') {
            io << queue[startPtr] << '\n';
            startPtr++;
        }
        else {
            io >> (queue[endPtr]);
            endPtr++;
        }
    }

    return 0;
}

