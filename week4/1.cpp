#include "edx-io.hpp"

int week4_1() {
    char operation;
    auto stack = new int[1000000];
    int n;
    io >> n;

    for (int i = 0; i < n; i++) {
        io >> operation;
        if (operation == '-') {
            io << *(--stack) << '\n';

        }
        else {
            io >> *(stack++);
        }
    }

    return 0;
}


