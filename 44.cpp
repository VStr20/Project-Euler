// Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

// 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

// It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

// Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; 
// what is the value of D?

#include <iostream>
#include <cmath>
#include <vector>

int main() {
    std::vector<int> min_diff;

    for (int n = 1; n < 10000; ++n) {
        for (int m = 1; m < n; ++m) {
            double k = (1 + std::sqrt(1 + 12 * (3 * n * n - n + 3 * m * m - m))) / 6;
            double p = (1 + std::sqrt(1 + 12 * (3 * n * n - n - 3 * m * m + m))) / 6;

            if (std::floor(k) == k) {
                if (std::floor(p) == p) {
                    min_diff.push_back(p * (3 * p - 1) / 2);
                }
                else {
                    continue;
                }
            }
            else {
                continue;
            }
        }
    }

    std::cout << "min_diff: ";
    for (int i : min_diff) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    int min = min_diff[0];
    for (int i : min_diff) {
        if (i < min) {
            min = i;
        }
    }
    std::cout << "Minimum: " << min << std::endl;

    return 0;
}

// n(3n-1)/2 + m(3m-1)/2 = k(3k-1)/2  sum

// n(3n-1)/2 - m(3m-1)/2 = p(3p-1)/2  difference

// finding roots of quadratic in k and p

// k = (1 + math.sqrt(1 + 12*(3*n*n-n+3*m*m-m)))/6
// p = (1 + math.sqrt(1 + 12*(3*n*n-n-3*m*m+m)))/6

// for the sum and difference to be pentagonal numbers k and p have to be integers
// hence the condition if((int(k) == k) and (int(p) == p))

// We coukd also use the condition math.sqrt(1 + 12*(3*n*n-n+3*m*m-m)) mod 6 =5 5 and math.sqrt(1 + 12*(3*n*n-n-3*m*m+m)) mod 6 ==5
// Anyways