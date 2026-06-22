class Solution {
    public int maxNumberOfBalloons(String text) {
        char[] arr = text.toCharArray();
        int[] count = new int[5];
        for (char c: arr) {
            switch (c) {
                case 'b':
                    count[0]++;
                    break;
                case 'a':
                    count[1]++;
                    break;
                case 'l':
                    count[2]++;
                    break;
                case 'o':
                    count[3]++;
                    break;
                case 'n':
                    count[4]++;
                    break;
                default:
                    break;
            }
        }
        count[2] /= 2;
        count[3] /= 2;
        Arrays.sort(count); 
        return count[0];
    }
}