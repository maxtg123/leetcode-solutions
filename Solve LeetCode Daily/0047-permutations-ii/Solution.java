class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums); // Sắp xếp để nhận biết phần tử trùng
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
            // Bỏ qua phần tử đã dùng
            if (used[i]) continue;

            // Bỏ qua phần tử trùng nhau nếu phần tử trước chưa được dùng
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;

            temp.add(nums[i]);
            used[i] = true;
            backtrack(nums, temp, used, res);
            used[i] = false;
            temp.remove(temp.size() - 1);
        }
    }
}
