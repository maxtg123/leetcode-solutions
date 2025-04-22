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
    public ListNode reverseKGroup(ListNode head, int k) {
        // Kiểm tra nếu còn ít hơn k node
        ListNode node = head;
        for (int i = 0; i < k; i++) {
            if (node == null) return head;
            node = node.next;
        }

        // Đảo ngược k node đầu tiên
        ListNode prev = null, curr = head, next = null;
        for (int i = 0; i < k; i++) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Đệ quy xử lý phần còn lại
        head.next = reverseKGroup(curr, k);

        return prev; // prev là node đầu tiên sau khi đảo ngược
    }
}
