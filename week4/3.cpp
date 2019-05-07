#include <string>
#include "edx-io.hpp"
using namespace std;

int main() {
    auto stack = new char[1000000];
    int ptr;
    int n;
    io >> n;

    string str;
    for (int i = 0; i < n; i++) {
        ptr = -1;
        io >> str;
        bool isWrong = false;
        int len = str.length();
        if (len % 2 == 1)
            isWrong = true;
        for (int j = 0; j < len && !isWrong; ++j) {
            if (str[j] == '(' || str[j] == '['){
                ptr++;
                stack[ptr] = str[j];
            } else {
                if (ptr == -1){
                    isWrong = true;
                }
                else {
                    if (str[j] == ')'){
                        stack[ptr] == '(' ? (ptr--) : isWrong = true;
                    } else{
                        stack[ptr] == '[' ? (ptr--) : isWrong = true;
                    }
                }

            }
        }

        isWrong = isWrong || ptr > -1;
        io << (isWrong ? "NO\n" : "YES\n");
    }

    return 0;
}

