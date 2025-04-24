# - This solution builds a Trie from the root words and replaces words in the sentence with the shortest matching root prefix found in the Trie.
# - For each word in the sentence, we walk through the Trie and replace it with the first root we encounter that marks the end of a word.
# - Time Complexity: O(N + M), Space Complexity: O(N), where N is the total number of characters in the dictionary, and M is the number of characters in the sentence.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()

        # Build the Trie from the dictionary
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        # Replace each word in the sentence with the shortest root
        def replace(word):
            node = root
            prefix = ""
            for ch in word:
                if ch not in node.children:
                    return word
                prefix += ch
                node = node.children[ch]
                if node.is_end:
                    return prefix
            return word

        return ' '.join(replace(word) for word in sentence.split())
