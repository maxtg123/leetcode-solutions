class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), res);
        return res;
    }

    void backtrack(int[] nums, List<Integer> temp, List<List<Integer>> res) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int num : nums) {
            if (temp.contains(num)) continue;
            temp.add(num);
            backtrack(nums, temp, res);
            temp.remove(temp.size() - 1);
        }
    }
}
