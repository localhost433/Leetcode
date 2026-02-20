int factorial(int n) {
    long long ret = 1;
    for (int j = 2; j <= n; j++) {
        ret = ret * j % 1000000007;
    }
    return (int) ret;
}

int countPermutations(int* complexity, int complexitySize) {
    for (int i = 1; i < complexitySize; i++) {
        if (complexity[i] <= complexity[0]) {
            return 0;
        }
    }
    return factorial(complexitySize - 1);
}