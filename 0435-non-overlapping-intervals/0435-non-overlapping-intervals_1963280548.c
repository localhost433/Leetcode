int compare(const void* a, const void* b) {
    int* intervalA = *(int**)a;
    int* intervalB = *(int**)b;
    return intervalA[1] - intervalB[1];
}

int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    if (intervalsSize <= 1) return 0;
    qsort(intervals, intervalsSize, sizeof(int*), compare);
    int count = 1;
    int last = intervals[0][1];
    for (int i = 0; i < intervalsSize; ++i) {
        if (intervals[i][0] >= last){
            count++;
            last = intervals[i][1];
        }
    }
    return intervalsSize - count;
}