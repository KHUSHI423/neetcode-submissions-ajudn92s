class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        WordSet = set(wordList)
        queue = deque([(beginWord,1)])
        while queue:
            word,step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i] + c + word[i+1:]
                    if newword in WordSet:
                        queue.append((newword,step+1))
                        WordSet.remove(newword)
        return 0


        
        