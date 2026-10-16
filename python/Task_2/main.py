from solutions import word_frequency

# Test Q1
n = "python is easy and python is powerful"
print("Q1:", word_frequency(n))

from solutions import char_freq
#Test Q2
n="banana"
print("Q2:", char_freq(n))

from solutions import non_repeat
#Test Q3
n="swiss"
print("Q3:", non_repeat(n))

from solutions import anagram
#Test Q4
s1="listen"
s2="silent"
print("Q4:",anagram(s1,s2))

from solutions import first_repeating
#Test Q5
n="programming"
print("Q5:",first_repeating(n))

from solutions import move_0
#Test Q6
n=[0, 3, 0, 1, 2, 0, 4]
print("Q6:",move_0(n))

from solutions import second_high
#test Q7
n=[10, 20, 40, 30, 40, 20]
print("Q7:",second_high(n))

from solutions import remove_dups
#test Q8
n=[4, 2, 4, 5, 2, 7, 5]
print("Q8:",remove_dups(n))

from solutions import missing_num
#test Q9
num=[1, 2, 4, 5, 6]
n=6
print("Q9:",missing_num(num,n))

from solutions import two_sum
#test Q10
n = [2, 7, 11, 15]
target = 9
print("Q10:",two_sum(n,target))

from solutions import clos_to_zero
#test Q11
n=[-8, -3, 2, 5, -2]
print("Q11:",clos_to_zero(n))

from solutions import common_elements
#test Q12
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("Q12:", common_elements(list1,list2))

from solutions import rotate_right
#test Q13
n= [1, 2, 3, 4, 5]
K = 2
print("Q13:",rotate_right(n,K))

from solutions import consecutive_sum
#test Q14
n=[4, 7, 2, 9, 5]
print("Q14:",consecutive_sum(n))

from solutions import pairs_sum
#test Q15
n = [2, 4, 3, 5, 7, 8, 1]
target = 9
print("Q15:",pairs_sum(n,target))


