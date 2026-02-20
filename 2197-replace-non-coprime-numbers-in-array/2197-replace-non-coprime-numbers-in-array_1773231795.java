class Solution {
    public long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }

    public List<Integer> replaceNonCoprimes(int[] nums) {
        ArrayList<Long> ret = new ArrayList<>(nums.length);
        for (int x: nums) {
            long cur = x;
            ret.add(cur);
            int i = ret.size() - 1;
            while (i > 0) {
                long a = ret.get(i - 1);
                long b = ret.get(i);
                long g = gcd(a, b);
                if (g == 1) break;
                long m = a / g * b;
                ret.set(i - 1, m);
                ret.remove(i);
                i--;
            }
        }
        List<Integer> ans = new ArrayList<>(ret.size());
        for (Long l: ret) {
            ans.add(l.intValue());
        }
        return ans;
    }
}