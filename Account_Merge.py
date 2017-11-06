# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a list accounts, each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name,
# and the rest of the elements are emails representing emails of the account, in sorted order.
# Now, we would like to merge these accounts.
# Two accounts definitely belong to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name,
# they may belong to different people as people could have the same name.
# A person can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the format they were given:
# the first element of each account is the name, and the rest of the elements are emails in sorted order.
# The accounts themselves can be returned in any order.
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
# ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order,
# for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].


# 49 / 49 test cases passed.
# Status: Accepted
# Runtime: 379 ms
import collections
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        def dfs(i, emails):
            if accounts_visited[i]:
                return
            accounts_visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for account in email_accounts_map[email]:
                    dfs(account, emails)

        accounts_visited = [False] * len(accounts)
        email_accounts_map = collections.defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                email_accounts_map[email].append(i)
        for i, account in enumerate(accounts):
            emails = set()
            name = account[0]
            dfs(i, emails)
            if emails:
                res.append([name] + sorted(emails))
        return res


# Union Fing Algorithm
# 49 / 49 test cases passed.
# Status: Accepted
# Runtime: 272 ms
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        def get_parent(node):
            if parent[node] == node:
                return node
            parent[node] = get_parent(parent[node])
            return parent[node]

        def union(node_a, node_b):
            root_a = get_parent(node_a)
            root_b = get_parent(node_b)

            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        rank = collections.defaultdict(int)
        parent = {}
        owner = {}
        result = collections.defaultdict(list)
        emails_set = set()

        for i, account in enumerate(accounts):
            name, emails = account[0], account[1:]
            for email in emails:
                emails_set.add(email)
                owner[email] = name
                if email not in parent:
                    parent[email] = email

            for email in emails[1:]:
                union(emails[0], email)

        for email in emails_set:
            result[get_parent(email)].append(email)
        return [[owner[email]] + sorted(result[email]) for email in result]


if __name__ == '__main__':
    # print(Solution().accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]))
    # print(Solution().accountsMerge([["Kevin","Kevin1@m.co","Kevin5@m.co","Kevin2@m.co"],["Bob","Bob3@m.co","Bob1@m.co","Bob2@m.co"],["Lily","Lily3@m.co","Lily2@m.co","Lily0@m.co"],["Gabe","Gabe2@m.co","Gabe0@m.co","Gabe2@m.co"],["Kevin","Kevin4@m.co","Kevin3@m.co","Kevin3@m.co"]]))
    # print(Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
    print(Solution().accountsMerge([["David","David5@m.co","David8@m.co"],
                                    ["David","David1@m.co","David1@m.co","David8@m.co"],
                                    ["David","David0@m.co","David0@m.co","David5@m.co"]]))
