class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder ans = new StringBuilder();
        for (String word: words) {
            int s = 0;
            for (int i = 0; i < word.length(); i++) {
                s += weights[(int) (word.charAt(i) - 97)];
            }
            s %= 26;
            ans.append((char) (122 - s));
        }
        return ans.toString();
    }
}