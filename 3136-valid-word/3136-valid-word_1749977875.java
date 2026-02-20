class Solution {
    public boolean isValid(String word) {
        String VOWELS = "aeiou";
        String w = word.toLowerCase();
        int n = w.length();
        if (w == null || n < 3) return false;
        if (!w.matches("[a-z0-9]+")) return false;
        boolean v = false, c = false;
        for (int i = 0; i < n; i++) {
            char ch = w.charAt(i);
            if (Character.isDigit(ch)) continue;
            if (VOWELS.indexOf(ch) >= 0) v = true;
            else c = true;
        }
        return (v && c);
    }
}