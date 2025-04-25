/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0); // node giả
        dummy.next = head;

        ListNode fast = dummy;
        ListNode slow = dummy;

        // Bước 1: Di chuyển fast n+1 bước
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        // Bước 2: Di chuyển fast và slow đến cuối
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // Bước 3: Xóa node
        slow.next = slow.next.next;

        return dummy.next;
    }  
}
    