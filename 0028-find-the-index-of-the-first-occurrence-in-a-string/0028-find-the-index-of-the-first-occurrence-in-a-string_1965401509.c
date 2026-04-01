int strStr(char* haystack, char* needle) {
    int n = strlen(haystack);
    int m = strlen(needle);

    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && needle[j] == haystack[(i + j)]) {
            j++;
            if (j == m) {return i;}
        }
    } return -1;
}