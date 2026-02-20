class Solution {
    public int[] finalPrices(int[] prices) {
        int num = prices.length;
        int[] updated = new int[num];
        for(int i = 0; i < num; i++) {
            updated[i] = prices[i] - discount(i, prices);
        }
        return updated;
    }

    public int discount(int pos, int[] prices) {
        int disc = 0;
        int num = prices.length;
        for (int p = pos + 1; p < num; p++) {
            if (prices[p] <= prices[pos]) {
                return prices[p];
            } 
        }
        return 0;
    }
}