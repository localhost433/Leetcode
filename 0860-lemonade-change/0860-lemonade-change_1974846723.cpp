class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int n = bills.size();
        int v = 0, x = 0;
        for (int bill: bills) {
            if (bill == 5) {
                v++;
            } else if (bill == 10) {
                if (v == 0) return false;
                x++;
                v--;
            } else {
                if (x > 0 && v > 0) {
                    x--;
                    v--;
                } else if (v >= 3) {
                    v -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};