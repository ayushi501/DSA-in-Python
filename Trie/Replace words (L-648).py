

class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def getNode(self):
        return TrieNode()

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        crawler = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if not crawler.children[idx]:
                crawler.children[idx] = self.getNode()
            crawler = crawler.children[idx]
        crawler.isEnd = True

    def search(self, word):
        crawler = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if not crawler.children[idx]:
                return word
            crawler = crawler.children[idx]
            if crawler.isEnd:
                return word[:i+1]
        return word


class Solution:
    def __init__(self) -> None:
        self.trie = Trie()

    def replaceWords(self, dictionary, sentence):
        for word in dictionary:
            self.trie.insert(word)

        result = []
        for word in sentence.split():
            result.append(self.trie.search(word))

        return " ".join(result)
