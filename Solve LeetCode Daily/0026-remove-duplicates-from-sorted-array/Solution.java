class Solution {
    public int removeDuplicates(int[] nums) {
        // Edge case: mảng rỗng
        if (nums == null || nums.length == 0) {
            return 0;
        }

        // i giữ vị trí phần tử duy nhất gần nhất
        int i = 0;

        for (int j = 1; j < nums.length; j++) {
            // Nếu nums[j] khác với phần tử cuối cùng duy nhất -> giữ lại
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j]; // cập nhật phần tử mới vào vị trí tiếp theo
            }
        }

        // Độ dài mảng không trùng là i + 1
        return i + 1;
    }
}
