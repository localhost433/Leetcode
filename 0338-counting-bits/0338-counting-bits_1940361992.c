/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* ans = (int*)malloc((*returnSize) * sizeof(int));
    ans[0] = 0;
    for (int i = 1; i <= n; i++){
        ans[i] = 1 + ans[i & (i - 1)];
    }
    return ans;
}