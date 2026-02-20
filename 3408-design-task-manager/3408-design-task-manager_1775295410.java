import java.util.*;

class TaskManager {

    static class Node {
        final int taskId;
        final int userId;
        final int priority;
        final int version;

        Node(int taskId, int userId, int priority, int version) {
            this.taskId = taskId;
            this.userId = userId;
            this.priority = priority;
            this.version = version;
        }
    }

    private final Map<Integer, Node> cur = new HashMap<>();

    private final PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> {
        if (a.priority != b.priority) return Integer.compare(b.priority, a.priority);
        return Integer.compare(b.taskId, a.taskId);
    });

    private final Map<Integer, Integer> ver = new HashMap<>();

    public TaskManager(List<List<Integer>> tasks) {
        for (List<Integer> t : tasks) {
            int userId = t.get(0);
            int taskId = t.get(1);
            int priority = t.get(2);
            add(userId, taskId, priority);
        }
    }

    public void add(int userId, int taskId, int priority) {
        int v = ver.getOrDefault(taskId, 0) + 1;
        ver.put(taskId, v);
        Node live = new Node(taskId, userId, priority, v);
        cur.put(taskId, live);
        pq.add(live);
    }

    public void edit(int taskId, int newPriority) {
        Node old = cur.get(taskId);
        if (old == null) return;
        int v = old.version + 1;
        ver.put(taskId, v);
        Node live = new Node(taskId, old.userId, newPriority, v);
        cur.put(taskId, live);
        pq.add(live);
    }

    public void rmv(int taskId) {
        cur.remove(taskId);
    }

    public int execTop() {
        while (!pq.isEmpty()) {
            Node top = pq.peek();
            Node live = cur.get(top.taskId);
            if (live == null || live.version != top.version) {
                pq.poll();
                continue;
            }
            pq.poll();
            cur.remove(top.taskId);
            return top.userId;
        }
        return -1;
    }
}
