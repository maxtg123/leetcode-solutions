public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            // Rút gọn prefix đến khi nào còn là tiền tố của strs[i]
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);

                // Nếu không còn gì để so sánh nữa
                if (prefix.isEmpty()) return "";
            }
        }

        return prefix;
    }
}
