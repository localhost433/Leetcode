class Solution {
    public int countPermutations(int[] complexity) {
        for (int i = 1; i < complexity.length; i++) {
            if (complexity[i] <= complexity[0]) return 0;
        }
        return factorial(complexity.length - 1);
    }

    public int factorial(int n) {
        long res = 1;
        for (int i = 2; i <= n; i++) {
            res = res * i % 1000000007;
        }
        return (int) res;
    }
}