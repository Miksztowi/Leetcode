# -*- encoding:utf-8 -*-
# __author__=='Gan'



Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.



15 / 15 test cases passed.
Status: Accepted
Runtime: 1095 ms
Your runtime beats 79.71 % of mysql submissions.

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1

