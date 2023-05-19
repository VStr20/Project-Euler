#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

std::vector<int> primeNumbers;

void SieveOfEratosthenes(int n) {
    std::vector<bool> isPrime(n + 1, true);
    int p = 2;

    while (p * p <= n) {
        if (isPrime[p] == true) {
            for (int i = p * p; i <= n; i += p) {
                isPrime[i] = false;
            }
        }
        p++;
    }

    for (int p = 2; p <= n; p++) {
        if (isPrime[p]) {
            primeNumbers.push_back(p);
        }
    }
}

int main() {
    SieveOfEratosthenes(7654321);

    std::vector<char> digits = { '1', '2', '3', '4', '5', '6', '7' };
    std::vector<int> answer;

    do {
        int res = std::accumulate(digits.begin(), digits.end(), 0,
            [](int sub, char ele) { return sub * 10 + (ele - '0'); });

        if (!((res % 10) % 2 == 0 || res % 10 == 5)) {
            if (std::binary_search(primeNumbers.begin(), primeNumbers.end(), res)) {
                answer.push_back(res);
            }
        }
    } while (std::next_permutation(digits.begin(), digits.end()));

    std::cout << *std::max_element(answer.begin(), answer.end()) << std::endl;

    return 0;
}
