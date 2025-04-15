public class Solution {
    public String intToRoman(int num) {
        // Bảng ánh xạ giá trị số và ký hiệu La Mã
        int[] values =    {1000, 900, 500, 400, 100,  90,  50,  40,  10,   9,   5,   4,   1};
        String[] symbols ={"M", "CM","D", "CD","C", "XC","L", "XL","X", "IX","V", "IV","I"};

        StringBuilder result = new StringBuilder();

        // Duyệt qua từng giá trị từ lớn đến bé
        for (int i = 0; i < values.length && num > 0; i++) {
            while (num >= values[i]) {
                result.append(symbols[i]);
                num -= values[i];
            }
        }

        return result.toString();
    }
}
