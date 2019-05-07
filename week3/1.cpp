#include <wrl.h>
#include "edx-io.hpp"

void radixsort(long *A, unsigned int n, unsigned int max)
{
    auto *B = new long[n];
    auto *C = new long[256];

    for (int power = 0; 1LL << power <= max; power += 8)
    {
        memset(C, 0, sizeof(unsigned int) * 256);

        for (int i = 0; i < n; i++)
        {
            C[(A[i] >> power) & 255]++;
        }

        for (int i = 1; i < 256; i++)
        {
            C[i] += C[i - 1];
        }

        for (int i = n - 1; i >= 0; i--)
        {
            B[C[(A[i] >> power) & 255] - 1] = A[i];
            C[(A[i] >> power) & 255]--;
        }

        for (int i = 0; i < n; i++)
        {
            A[i] = B[i];
        }
    }
    delete[] B;
    delete[] C;
}

int first() {
    int n, m;
    unsigned int max = 0;
    io >> n >> m;
    unsigned int len = (unsigned int)n * m;

    auto *A = new int[n];
    auto *B = new int[m];
    auto *C = new long[len];

    for (int i = 0; i < n; i++) {
        io >> A[i];
    }
    for (int i = 0; i < m; i++) {
        io >> B[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            long value = A[i] * B[j];
            C[i * m + j] = value;
            max = max > value ? max : value;
        }
    }

    radixsort(C, len, max);

    unsigned long long sum = 0;

    for (int i = 0; i<len; i=i+10){
        sum = sum + C[i];
    }

    io << sum;

    return 0;
}

