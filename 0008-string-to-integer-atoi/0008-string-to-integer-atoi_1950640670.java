class Solution {
    public int myAtoi(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int i = 0;
        
        while (i < n && s.charAt(i) == ' ') i++;
        if (i == n) return 0;
        
        int sign = 1;
        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = (s.charAt(i++) == '-') ? -1 : 1;
        }

        long num = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            num = num * 10 + (s.charAt(i++) - '0');    
            if (num * sign >= Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (num * sign <= Integer.MIN_VALUE) return Integer.MIN_VALUE;
        } return (int) (num * sign);
    }
}