# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
# determine if two sentences are similar.
# For example, "great acting skills" and "fine drama talent" are similar,
# if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar,
# and "fine" and "good" are similar, "great" and "good" are not necessarily similar.
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
# pairs = [] are similar, even though there are no specified similar word pairs.

# LeetCode Contest 60.
# 49 / 49 test cases passed.
# Status: Accepted
# Runtime: 32 ms
import collections
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        words = collections.defaultdict(set)
        for word1, word2 in pairs:
            words[word1].add(word2)
            words[word2].add(word1)
        for word1, word2 in zip(words1, words2):
            if word1 != word2 and word2 not in words[word1]:
                return False

        return True




if __name__ == '__main__':
    print(Solution().areSentencesSimilar(['great', 'acting', 'skills'],
                                         ['fine', 'drama', 'talent'],
                                         [["great", "fine"], ["acting", "drama"], ["skills", "talent"]]))


    # print(Solution().areSentencesSimilar(["an", "extraordinary", "meal"],
    #                                      ["a", "good", "dinner"],
    #                                      [["great", "good"], ["extraordinary", "good"], ["well", "good"],
    #                                       ["wonderful", "good"], ["excellent", "good"], ["fine", "good"],
    #                                       ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"],
    #                                       ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"],
    #                                       ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"],
    #                                       ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"],
    #                                       ["take", "have"], ["fruits", "meal"], ["brunch", "meal"],
    #                                       ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"],
    #                                       ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"],
    #                                       ["have", "own"], ["extremely", "very"], ["actually", "very"],
    #                                       ["really", "very"], ["super", "very"]]))
