class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_words = {}

        for word in strs: 
            parsed_word = "".join(sorted(word))

            if parsed_word not in grouped_words:
                grouped_words[parsed_word] = []
            grouped_words[parsed_word].append(word)
    
        return list(grouped_words.values())