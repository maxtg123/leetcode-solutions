class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
         // Result list to store all valid combinations
        List<List<Integer>> res = new ArrayList<>(); 
        backtrack(candidates, target, new ArrayList<>(), res, 0, 0);
        return res;
    }

    private void backtrack(int[] candidates, int target, List<Integer> current,                 List<List<Integer>> res, int sum, int start) {
        if (sum > target) {
            return; // Sum next target on the return
        }
        
        if (sum == target) {
            res.add(new ArrayList<>(current)); // True target auto save
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            current.add(candidates[i]); // select element
            backtrack(candidates, target, current, res, sum + candidates[i], i); // Call back (i), because it is reselected
            current.remove(current.size() - 1); // Backtrack, remove selected element
        }
    }
}