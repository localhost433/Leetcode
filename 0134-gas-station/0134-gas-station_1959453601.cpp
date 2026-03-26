class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int g = 0;
        int c = 0;
        int n = gas.size();
        for (int i = 0; i < n; ++i){
            g += gas[i];
            c += cost[i];
        }
        if (g < c){
            return -1;
        }
        int curr = 0;
        int index = 0;
        for (int i = 0; i < n; ++i) {
            curr += gas[i] - cost[i];
            if (curr < 0) {
                index = i + 1;
                curr = 0;
            }
        }
        return index;
    }
};