// Using sliding window:


// - Since the length of each word is fixed (wordLen)

// - The total length of the substring to be considered is wordLen * words.length

// - Iterate through the string s, at each position, check if the substring of length windowLen contains
// the correct words in words (use HashMap to count the frequency of words)




class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || words == null || words.length == 0) return result;

        int wordLen = words[0].length();
        int numWords = words.length;
        int windowLen = wordLen * numWords;

        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words)
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);

        for (int i = 0; i <= s.length() - windowLen; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            while (j < numWords) {
                int wordStart = i + j * wordLen;
                String word = s.substring(wordStart, wordStart + wordLen);
                if (!wordCount.containsKey(word)) break;

                seen.put(word, seen.getOrDefault(word, 0) + 1);
                if (seen.get(word) > wordCount.get(word)) break;
                j++;
            }

            if (j == numWords) result.add(i);
        }

        return result;
    }
}
