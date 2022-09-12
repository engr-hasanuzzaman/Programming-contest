class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

class GfG {
    // Function to find the data of nth node from the end of a linked list.
    int getNthFromLast(Node head, int n) {
        Node cur = head;

        while (n > 0 && cur != null) {
            cur = cur.next;
            n -= 1;
        }

        if (n > 0) {
            return -1;
        }

        Node ans = head;
        while (cur != null) {
            cur = cur.next;
            ans = ans.next;
        }

        return ans.data;
    }
}