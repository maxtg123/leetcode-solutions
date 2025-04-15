public class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanMap = Map.of(
            'I', 1, 'V', 5, 'X', 10,
            'L', 50, 'C', 100, 'D', 500, 'M', 1000
        );

        int total = 0;

        for (int i = 0; i < s.length(); i++) {
            int curr = romanMap.get(s.charAt(i));
            int next = (i + 1 < s.length()) ? romanMap.get(s.charAt(i + 1)) : 0;

            if (curr < next) {
                total -= curr;
            } else {
                total += curr;
            }
        }

        return total;
    }
}
