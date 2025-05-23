// Difficulty: Easy
// Solved on: 2025-04-11
// https://leetcode.com/problems/longest-substring-without-repeating-characters



import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if (map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }

            map.put(nums[i], i);
        }

        // If no solution is found
        return new int[]{};
    }
}


