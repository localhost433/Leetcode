class Solution {
    public boolean isVowel(char c) {
        return "aeiouAEIOU".indexOf(c) >= 0;
    }

    public String sortVowels(String s) {
        char[] arr = s.toCharArray();
        ArrayList<Character> vowels = new ArrayList<>();
        for (char c: arr) {
            if (isVowel(c)) {
                vowels.add(c);
            }
        }
        Collections.sort(vowels);
        int idx = 0;
        for (int i = 0; i < arr.length; i++) {
            if (isVowel(arr[i])) {
                arr[i] = vowels.get(idx++);
            }
        }
        return new String(arr);
    }
}