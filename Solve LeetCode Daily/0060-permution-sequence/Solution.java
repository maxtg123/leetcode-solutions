

class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> numbers = new ArrayList<>();
        int fact = 1;
        
        // Create list of numbers and calculate factorial
        for (int i = 1; i <= n; i++) {
            numbers.add(i);
            fact *= i;
        }
        
        // Convert k to 0-based index
        k--;
        
        StringBuilder result = new StringBuilder();
        
        // Generate permutation
        for (int i = n; i > 0; i--) {
            fact /= i;
            int index = k / fact;
            result.append(numbers.remove(index));
            k %= fact;
        }
        
        return result.toString();
    }
}