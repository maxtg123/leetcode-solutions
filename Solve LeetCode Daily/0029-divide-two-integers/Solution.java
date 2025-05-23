class Solution {
    public int divide(int dividend, int divisor) {
        // Xử lý tràn số nguyên
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        // Lưu dấu kết quả
        boolean negative = (dividend < 0) ^ (divisor < 0);

        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);
        int result = 0;

        while (dvd >= dvs) {
            long temp = dvs;
            int multiple = 1;
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            result += multiple;
        }

        return negative ? -result : result;
    }
}
