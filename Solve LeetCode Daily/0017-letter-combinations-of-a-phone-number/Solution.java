class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> ans = new LinkedList<>();
        if (digits.isEmpty()) return ans;

        String[] mapping = new String[] {
            "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        ans.add("");
        for (int i = 0; i < digits.length(); i++) {
            int digit = digits.charAt(i) - '0';
            int size = ans.size();

            for (int j = 0; j < size; j++) {
                String prefix = ans.remove(0);
                for (char c : mapping[digit].toCharArray()) {
                    ans.add(prefix + c);
                }
            }
        }
        return ans;
    }
}
