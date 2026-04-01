int strStr(char* haystack, char* needle) {
    if (needle[0] == '\0') return 0;
    for (int i = 0; haystack[i] != '\0'; ++i) {
        int tmp = i;
        int j = 0;
        while (haystack[tmp] == needle[j] && needle[j] != '\0'){
            tmp++;
            j++;
        }
        if (needle[j] == '\0') {
            return i;
        }
    }
    return -1;
}