# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are similar.
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
# if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
# Note that the similarity relation is transitive. For example,
# if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.
# Similarity is also symmetric. For example,
# "great" and "fine" being similar is the same as "fine" and "great" being similar.
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
# pairs = [] are similar, even though there are no specified similar word pairs.
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
# Note:
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].

import collections


# Union Find. Tutorial link:http://www.ganbinwen.com/2017/11/06/%E8%81%94%E5%90%88-%E6%9F%A5%E6%89%BE%E7%AE%97%E6%B3%95/
# 117 / 117 test cases passed.
# Status: Accepted
# Runtime: 422 ms
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        def find(word):
            if word not in parent:
                return False
            if parent[word] == word:
                return parent[word]
            parent[word] = find(parent[word])
            return parent[word]

        def union(word1, word2):
            parent1 = find(word1)
            parent2 = find(word2)
            if rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
            else:
                parent[parent2] = parent1
                rank[word2] += 1

        parent = {}
        rank = collections.defaultdict(int)

        for pair in pairs:
            word1, word2 = pair
            if word1 not in parent:
                parent[word1] = word1
            if word2 not in parent:
                parent[word2] = word2
            union(word1, word2)

        for word1, word2 in zip(words1, words2):
            if word1 != word2 and find(word1) != find(word2):
                print(word1, word2)
                print(parent)
                return False
        return True


# Whenever we see a list of pairs as input, one probable approach will be to treat that as a list of edges and model
# the question as a graph. In this question, the idea here is to connect words to their similar words, and all
# connected words are similar. In each connected component of a graph, select any word to be the root word and
# then generate a mapping of word to root word. If two words are similar, they have the same root word.
# 117 / 117 test cases passed.
# Status: Accepted
# Runtime: 269 ms
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        words, similar_words = collections.defaultdict(set), {}
        [(words[word1].add(word2), words[word2].add(word1)) for word1, word2 in pairs]

        def dfs(word, root_word):
            if word in similar_words:
                return
            similar_words[word] = root_word
            [dfs(w, root_word) for w in words[word]]

        [dfs(word, word) for word in words]
        return all(similar_words.get(w1, w1) == similar_words.get(w2, w2) for w1, w2 in zip(words1, words2))


if __name__ == '__main__':
    print(Solution().areSentencesSimilarTwo(['great', 'acting', 'skills'],
                                            ['fine', 'drama', 'talent'],
                                            [["great", "good"], ['fine', 'good'], ["acting", "drama"],
                                             ["skills", "talent"]]))
    test_method = Solution().areSentencesSimilarTwo
    print(
        Solution().areSentencesSimilarTwo(
            ["this", "summer", "thomas", "get", "really", "very", "rich", "and", "have", "any", "actually", "wonderful",
             "and", "good", "truck", "every", "morning", "he", "drives", "an", "extraordinary", "truck", "around",
             "the", "nice", "city", "to", "eat", "some", "extremely", "extraordinary", "food", "as", "his", "meal",
             "but", "he", "only", "entertain", "an", "few", "well", "fruits", "as", "single", "lunch", "he", "wants",
             "to", "eat", "single", "single", "and", "really", "healthy", "life"],
            [
                "this", "summer", "thomas", "get", "very", "extremely", "rich", "and", "possess", "the", "actually",
                "great", "and", "wonderful", "vehicle", "every", "morning", "he", "drives", "unique", "extraordinary",
                "automobile", "around", "unique", "fine", "city", "to", "drink", "single", "extremely", "nice", "meal",
                "as", "his", "super", "but", "he", "only", "entertain", "a", "few", "extraordinary", "food", "as",
                "some", "brunch", "he", "wants", "to", "take", "any", "some", "and", "really", "healthy", "life"],
            [["good", "wonderful"], ["nice", "well"], ["fine", "extraordinary"], ["excellent", "good"], ["wonderful",
                                                                                                         "nice"], [
                 "well", "fine"], ["extraordinary", "excellent"], ["great", "wonderful"], ["one", "the"], ["a",
                                                                                                           "unique"], [
                 "single", "some"], ["an", "one"], ["the", "a"], ["unique", "single"], ["some", "an"], ["any", "the"], [
                 "car", "wagon"], ["vehicle", "car"], ["auto", "vehicle"], ["automobile", "auto"], ["wagon",
                                                                                                    "automobile"], [
                 "truck", "wagon"], ["have", "have"], ["take", "take"], ["eat", "eat"], ["drink", "drink"], [
                 "entertain", "entertain"], ["meal", "food"], ["lunch", "breakfast"], ["super", "brunch"], ["dinner",
                                                                                                            "meal"], [
                 "food", "lunch"], ["breakfast", "super"], ["brunch", "dinner"], ["fruits", "food"], ["own", "own"], [
                 "have", "have"], ["keep", "keep"], ["possess", "own"], ["very", "very"], ["super", "super"], ["really",
                                                                                                               "really"],
             [
                 "actually", "actually"], ["extremely", "extremely"]]
        )
    )
