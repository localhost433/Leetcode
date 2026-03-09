char* findDifferentBinaryString(char** nums, int numsSize) {
    char* ret = malloc(numsSize + 1);
    if (!ret) {return NULL;}
    for (int i = 0; i < numsSize; i++) {
        ret[i] = (nums[i][i] == '0') ? '1' : '0';
    }
    ret[numsSize] = '\0';
    return ret;
}