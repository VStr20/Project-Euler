// The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

// There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

// How many circular primes are there below one million?

function isPrime(a) {
    for (let i = 2; i < a; i++) {
        if (a % i === 0) {
            return false;
        }
    }
    return true;
}

let primeNumbers = [2];
for (let k = 3; k < 1000000; k += 2) {
    if (isPrime(k)) {
        primeNumbers.push(k);
    }
}

function numContainsEven(b) {
    for (let p of String(b)) {
        if (parseInt(p) % 2 === 0) {
            return true;
        }
    }
    return false;
}

let prime = [];
let prime1 = [];
let sumAns = 0;
let answer = 0;
for (let num = 11; num < 1000000; num += 2) {
    let count = 1;
    let temp = num;
    if (numContainsEven(num)) {
        continue;
    } else {
        if (prime.includes(num)) {
            continue;
        } else {
            if (primeNumbers.includes(temp)) {
                for (let m = 0; m < String(num).length - 1; m++) {
                    temp = (temp % 10) * Math.pow(10, String(num).length - 1) + Math.floor(temp / 10);
                    if (primeNumbers.includes(temp)) {
                        count += 1;
                    }
                }
            }
            if (count === String(num).length) {
                answer += 1;
                prime1.push(num);
                for (let m = 0; m < String(num).length; m++) {
                    temp = (temp % 10) * Math.pow(10, String(num).length - 1) + Math.floor(temp / 10);
                }
                prime.push(temp);
            }
        }
    }
}

let x = [...new Set([...prime, ...prime1])];
console.log(x.sort());
console.log(x.length + 4); // +4 for including numbers 2, 3, 5, 7

// 2
// 3
// 5
// 7
// 11
// 13
// 17
// 31
// 37
// 71
// 73
// 79
// 97
// 113
// 131
// 197
// 199
// 311
// 337
// 373
// 719
// 733
// 919
// 971
// 991
// 1193
// 1931
// 3119
// 3779
// 7793
// 7937
// 9311
// 9377
// 11939
// 19391
// 19937
// 37199
// 39119
// 71993
// 91193
// 93719
// 93911
// 99371
// 193939
// 199933
// 319993
// 331999
// 391939
// 393919
// 919393
// 933199
// 939193
// 939391
// 993319
// 999331