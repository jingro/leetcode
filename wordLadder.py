class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ab = 'abcdefghijklmnopqrstuvwxyz'
        size = len(beginWord)
        length = 2
        front, back = set(beginWord), set(endWord)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordSet.discard(beginWord)
        while front:
            front = (set(word[:index] + ch + word[index + 1:] for word in front
                         for index in range(size) for ch in ab)) & wordSet
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            wordSet -= front
        return 0
