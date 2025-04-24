public class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;

        // Bước 1: tìm điểm mà nums[i] < nums[i+1]
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            // Bước 2: tìm phần tử lớn hơn nums[i] để swap
            int j = nums.length - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }

            // Hoán đổi
            swap(nums, i, j);
        }

        // Bước 3: đảo ngược đoạn sau i
        reverse(nums, i + 1);
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int[] nums, int start) {
        int end = nums.length - 1;
        while (start < end) {
            swap(nums, start++, end--);
        }
    }
}
