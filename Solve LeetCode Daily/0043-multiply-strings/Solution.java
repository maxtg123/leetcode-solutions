class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";
        
        int[] result = new int[num1.length() + num2.length()];
        
        for (int i = num1.length() - 1; i >= 0; i--) {
            for (int j = num2.length() - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int sum = mul + result[i + j + 1];
                
                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int r : result) {
            if (!(sb.length() == 0 && r == 0)) {
                sb.append(r);
            }
        }
        
        return sb.toString();
    }
}
