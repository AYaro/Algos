#include <deque>
#include "edx-io.hpp"

using namespace std;

int main() {
    auto heap = new int[1000000];
    bool flag = true;
    int n;
    io >> n;

    for (int i = 0; i < n; i++) {
        io >> heap[i];
    }
    for (int i = 1; i <= n / 2; i++) {
        if (heap[i - 1] > heap[2*i - 1]) {
            flag = false;
            break;
        } else if (2 * i + 1 <= n && heap[i - 1] > heap[(2 * i + 1) - 1]) {
            flag = false;
            break;
        }
    }
    io << (flag ? "YES" : "NO");

    return 0;
}

