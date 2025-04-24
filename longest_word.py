# - This solution builds a Trie from the list of words and performs DFS to find the longest word where every prefix is also a valid word.
# - During DFS, it only continues down paths where the current node marks the end of a word, ensuring all prefixes exist.
# - Time Complexity: O(N * M + N log N), Space Complexity: O(N * M), where N is number of words and M is max word length.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        # Insert all words into the Trie
        def insert(word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        for word in words:
            insert(word)

        result = ""

        def dfs(node, path):
            nonlocal result
            if node != root and not node.is_end:
                return  # If prefix is not a word, stop

            if len(path) > len(result) or (len(path) == len(result) and path < result):
                result = path

            for ch in sorted(node.children.keys()):  # Lexicographical order
                dfs(node.children[ch], path + ch)

        dfs(root, "")
        return result
