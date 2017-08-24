class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        from collections import defaultdict
        front, back = defaultdict(list), defaultdict(list)

        front[beginWord].append([beginWord])
        back[endWord].append([endWord])

        wordSet.discard(beginWord)
        ab = 'abcdefghijklmnopqrstuvwxyz'
        size = len(beginWord)

        forward, result = True, []
        while front:
            nextSet = defaultdict(list)
            for word, paths in front.items():
                for s in set([word[:i] + c + word[i + 1:] for i in range(size) for c in ab]) & wordSet:
                    if forward:
                        nextSet[s].extend([path + [s] for path in paths])
                    else:
                        nextSet[s].extend([[s] + path for path in paths])
            front = nextSet
            common = set(front) & set(back)
            if common:
                if not forward:
                    front, back = back, front
                result.extend([head + tail[1:] for word in common for head in front[word] for tail in back[word]])
                return result
            if len(front) > len(back):
                front, back, forward = back, front, not forward
            wordSet -= set(front)
        return []
