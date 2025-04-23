class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int n = nums.length;

        while (i < n) {
            if (nums[i] == val) {
                // Gán phần tử cuối vào vị trí hiện tại và giảm n
                nums[i] = nums[n - 1];
                n--;
            } else {
                i++;
            }
        }

        // Độ dài mới là n
        return n;
    }
}