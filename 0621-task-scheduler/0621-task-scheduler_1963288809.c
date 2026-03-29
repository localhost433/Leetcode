int leastInterval(char* tasks, int tasksSize, int n) {
    int counts[26] = {0};
    int max = 0;
    int c = 0;
    for (int i = 0; i < tasksSize; i++) {
        counts[tasks[i] - 'A']++;
        max = fmax(counts[tasks[i] - 'A'], max);
    }
    for (int i = 0; i < 26; i++) {
        if (counts[i] == max) {
            c++;
        }
    }
    return fmax((max - 1) * (n + 1) + c, tasksSize);
}