import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums); // Sort to identify duplicate elements
        boolean[] used = new boolean[nums.length];
        backtrack(nums, new ArrayList<>(), used, res);
        return res;
    }

    private void backtrack(int[] nums, List<Integer> temp, boolean[] used, List<List<Integer>> res) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            // Skip used elements
            if (used[i]) continue;

            // Ignore duplicate elements if the previous element has not been used
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;

            temp.add(nums[i]);
            used[i] = true;
            backtrack(nums, temp, used, res);
            used[i] = false;
            temp.remove(temp.size() - 1);
        }
    }
}
