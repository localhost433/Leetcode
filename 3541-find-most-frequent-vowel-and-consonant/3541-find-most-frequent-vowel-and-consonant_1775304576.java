class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    
    public int maxFreqSum(String s) {
        int vowelMax = 0;
        int consMax = 0;
        Map<Character, Integer> freq = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for (Map.Entry<Character, Integer> e : freq.entrySet()) {
            char c = e.getKey();
            int f = e.getValue();
            if (isVowel(c)) vowelMax = Math.max(vowelMax, f);
            else consMax = Math.max(consMax, f);
        }
        return vowelMax + consMax;
    }
}