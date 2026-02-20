class Solution {
    private static int maskOf(String s) {
        int m = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ('a' <= c && c <= 'z') m |= 1 << (c - 'a');
        }
        return m;
    }

    public int canBeTypedWords(String text, String brokenLetters) {
        int brokenMask = maskOf(brokenLetters);
        int count = 0;
        for (String w : text.split("\\s+")) {
            int m = maskOf(w);
            if ( (m & brokenMask) == 0 ) count++;
        }
        return count;
    }
}