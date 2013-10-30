Task 1: number of minutes in a week

>>> 60 * 24 * 7
10080

####################################################################

Task 2: find the remainder of 2304811 divided by 47 without using modulo

>>> 2304811 - 47*(2304811//47)
25

####################################################################

Task 3: enter a boolean expression to test whether the sum of 673 and 909 is divisible by 3

>>> (673 + 909)%3 == 0
False

####################################################################

Task 4: assign the value of -9 to x and 1/2 to y. Predict the value of the following expression, tehn enter it to check your prediction:
2**(y+1/2) if x + 10 < 0 else 2 ** (y -1/2)
1

>>> x = -9
>>> y = 1/2
>>> 2**(y+1/2) if x + 10 < 0 else 2 ** (y-1/2)
1.0

####################################################################

Task 5: write a comprehension over {1,2,3,4,5} whose value is the set consisting of the squares of the first five positive integers

>>> {x**2 for x in {1,2,3,4,5}}
{16, 1, 4, 25, 9}

####################################################################

Task 6: write a comprehension over {0,1,2,3,4} whose value is the set consisting of teh first five powers of 2 starting with 2^0

>>> {2**x for x in {0,1,2,3,4}}
{8, 1, 2, 4, 16}

####################################################################

Task 7: the value of the previous comprehension, {x*y for x in {1,2,3} for y in {2,3,4}} is a seven-element set. Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set

>>> {x*y for x in {2,3,5} for y in {7,11,13}}
{33, 35, 65, 39, 14, 21, 22, 55, 26}

####################################################################

Task 8: replace {1,2,3} and {2,3,4} in the previous comprehension with two disjoint (i.e. non-overlapping) three-element sets so that the value becomes a five-element set.

>>> {x*y for x in {2,4,8} for y in {16,32,64}}
{512, 256, 128, 64, 32}

####################################################################

Task 9: Assign 10 to the variable base. Assign the set {0,1,2,3,4,5,6,7,8,9} to the variable digits. now write an expression using a comprehension and base and digits whose value is the set of all at-most-three-digit numbers.

>>> {d1*base**2 + d2*base**1 + d3*base**0 for d1 in digits for d2 in digits for d3 in digits}

{0,1,2,...998,999}

####################################################################

Task 10: Assume that S and T are assigned sets. Without using the intersection operator &, write a comprehension over S whose value is the intersection of S and T. Test on S = {1,2,3,4} and T = {3,4,5,6}

>>> {x for x in S for y in T if x - y == 0}
{3, 4}

>>> {x for x in S if x in T}
{3, 4}

####################################################################

Task 11: Write an expression whose value is the average of the elements of the list [20, 10, 15, 75]

>>> x = [20, 10, 15, 75]
>>> avg = sum(x)/len(x)
>>> avg
30.0

####################################################################

Task 12: Assign to the variable LofL, the list of lists [[.25, .75, .1],[-1, 0],[4,4,4,4]]. Using a comprehension, write an expression involving LofL that returns the sum of all the numbers in all three lists.

>>> sum([sum(subtotal) for subtotal in LofL])
16.1

####################################################################

Task 13: Write a double list comprehension over the lists ['A','B','C'] and [1,2,3] whose value is the list of all possible two-element lists [letter, number]

>>> list1 = ['A','B','C']
>>> list2 = [1,2,3]
>>> [[x, y] for x in list1 for y in list2]
[['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]


####################################################################

Ungraded Task: Find out what happens if the length of the left-hand side list doesn not match the length of the right hand side list.

left > right:
>>> [a, b, c] = [3*1, 3*2]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    [a, b, c] = [3*1, 3*2]
ValueError: need more than 2 values to unpack

right < left:
>>> [d, e] = [5*1, 5*2, 5*3]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    [d, e] = [5*1, 5*2, 5*3]
ValueError: too many values to unpack (expected 2)

####################################################################

Task 14: Suppose S is a set of integers e.g. {-4, -2, 1, 2, 5, 0}. Write a triple comprehension whose value is a list of all the three element tuples (i, j, k) such that i, j, k are elements of S whose sum is 0.

>>> S = {-4, -2, 1,2,5,0}
>>> [(i, j, k) for i in S for j in S for k in S if i + j + k == 0]
[(0, 0, 0), (0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]

####################################################################

Task 15: Modify the comprehension of task 14 so that the resulting list does not include (0, 0, 0). Hint: add a filter.

>>> [(i, j, k) for i in S for j in S for k in S if i + j + k == 0 if i != 0 or j != 0 or k != 0]
[(0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]

####################################################################
 
Task 16: Further modify the comprehension of task 14/15 so that its value is not the list of all such tuples but is the first such tuple.

>>> [(i, j, k) for i in S for j in S for k in S if i + j + k == 0 if i != 0 if i <= j if j <= k]
[(-4, 2, 2), (-2, 0, 2), (-2, 1, 1)]

####################################################################


####################################################################


####################################################################


####################################################################


####################################################################


####################################################################


####################################################################


####################################################################


####################################################################


####################################################################


