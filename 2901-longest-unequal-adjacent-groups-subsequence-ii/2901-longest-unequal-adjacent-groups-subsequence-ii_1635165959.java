import java.util.*;

class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        int[] dp = new int[n];
        int[] p = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(p, -1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] != groups[j]
                && words[i].length() == words[j].length()
                && Hamming(words[i], words[j])
                && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    p[i] = j;
                }
            }
        }
        int bestEnd = 0;
        for (int i = 1; i < n; i++) {
            if (dp[i] > dp[bestEnd]) bestEnd = i;
            
        }
        List<String> result = new ArrayList<>();
        for (int i = bestEnd; i != -1; i = p[i]) {
            result.add(words[i]);
        }
        Collections.reverse(result);
        return result;
    }

    public boolean Hamming(String a, String b){
        int dist = 0;
        for (int i = 0, m = a.length(); i < m; i++) {
            if (a.charAt(i) != b.charAt(i)){
                dist++;
                if (dist > 1) {
                    return false;
                }
            }
        }
        return dist == 1;
    }
}