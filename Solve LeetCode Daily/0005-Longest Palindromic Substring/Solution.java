class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
    if (n == 0) return "";

    boolean[][] dp = new boolean[n][n];
    String res = "";

    for (int len = 1; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;

            if (s.charAt(i) == s.charAt(j)) {
                if (len <= 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    if (len > res.length()) {
                        res = s.substring(i, j + 1);
                    }
                }
            }
        }
    }

    return res;
    }
}