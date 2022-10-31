#include <stdlib.h>
#include <stdio.h>


void matrix_calc(int* a, int* b, int* c, int n, int k, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            c[i * n + j] = 0;
            for (int l = 0; l < k; l++) {
                c[i * m + j] += a[i * k + l] * b[l * m + j];
            }
        }
    }
}
