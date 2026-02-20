import java.util.*;

class Solution {
    static final class Node {
        int p, t;
        Node(int p, int t) { this.p = p; this.t = t; }
        double gain() { return ((double)(t - p)) / (t * (t + 1.0)); }
        void addOne() { p++; t++; }
        double ratio() { return (double) p / t; }
    }

    public double maxAverageRatio(int[][] classes, int extra) {
        PriorityQueue<Node> pq = new PriorityQueue<>(
            (a, b) -> Double.compare(b.gain(), a.gain())
        );
        for (int[] c : classes) pq.offer(new Node(c[0], c[1]));

        while (extra-- > 0) {
            Node x = pq.poll();
            x.addOne();
            pq.offer(x);
        }

        double sum = 0.0;
        for (Node x : pq) sum += x.ratio();
        return sum / classes.length;
    }
}
