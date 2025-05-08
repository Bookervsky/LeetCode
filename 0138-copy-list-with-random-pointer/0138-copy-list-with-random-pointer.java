/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {    
        if (head == null) {
            return head;
        }
        Map<Node, Node> cache = new HashMap<>();
        Node cur = head;
        while (cur != null) {
            cache.put(cur, new Node(cur.val));
            cur = cur.next;
        }
        cur = head;
        while (cur != null) {
            cache.get(cur).random = cache.get(cur.random);
            cache.get(cur).next = cache.get(cur.next);
            cur = cur.next;
        }
        return cache.get(head);
    }
}