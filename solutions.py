# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(n):
    words=n.split()
    freq= {}
    for i in words:
        freq[i]=len(i)
    return freq

# Q2.  Write a Python program to count how many times each character appears in a given word and store the result in a dictionary.

def char_freq(n):
    freq={}
    for i in n:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

#Q3. Write a Python program to find the first character that appears only once in a given word. If no such character exists, return None.

def non_repeat(n):
    freq={}
    for i in n:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in n:
        if freq[i]==1:

            return i
    return None

#Q4. Check Whether Two Strings Are Anagrams

def anagram(s1, s2):
    if len(s1)!=len(s2):
        return False
    freq1 = {}
    freq2={}
    for i in s1:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i]=1
    for i in s2:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
    return freq1==freq2
    
#Q5. Find the First Repeating Character in a String

def first_repeating(n):
    Frepeat = []
    for i in n:
        if i in Frepeat:
            return i
        Frepeat.append(i)
    return None

#Q6. Move All Zeros to the End of a List

def move_0(n):
    non_zeros=[]
    zeros=[]
    
    for num in n:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
            
    return non_zeros + zeros

# Q7. Find the Second Highest Distinct Number in a List
def second_high(n):
    unique_num = sorted(list(set(n)), reverse=True)
    if len(unique_num) < 2:
        return None
    return unique_num[1]

# Q8. Remove Duplicates Without Changing the Original Order
def remove_dups(n):
    result = []
    for i in n:
        if i not in result:
            result.append(i)
    return result

# Q9. Find the Missing Number from 1 to N
def missing_num(num, n):
    expected_sum = 0
    for i in range(1, n + 1):
        expected_sum += i
        
    actual_sum = 0
    for i in num:
        actual_sum += i
        
    return expected_sum - actual_sum

# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(n, target):

    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == target:
                return [n[i], n[j]]
    return []

# Q11. Find the Number Closest to Zero
def clos_to_zero(nums):
    closest = nums[0]
    
    for num in nums:
       #abs = it takes any number and removes its negative sign if it has one, turning it into a positive number.
        if abs(num) < abs(closest):
            closest = num
            
        #If it's the exact same distance, prefer the positive number
        elif abs(num) == abs(closest):
            if num > closest:
                closest = num
                
    return closest

# Q12. Find Common Elements Between Two Lists (Shorter version)
def common_elements(list1, list2):
    result = []
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result

# Q13. Rotate a List to the Right by K Positions
def rotate_right(n, k):
    if not n:
        return n
    k = k % len(n)
    # Slice the list and swap them
    return n[-k:] + n[:-k]

# Q14. Find the Maximum Sum of Two Consecutive Elements

def consecutive_sum(n):
    max_sum = n[0] + n[1]
    for i in range(len(n) - 1):
        s = n[i] + n[i + 1]
        if s > max_sum:
            max_sum = s
    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def pairs_sum(n, target):
    pairs = []
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == target:
                # Sort the pair so the small number come first
                p = [n[i], n[j]] if n[i] < n[j] else [n[j], n[i]]
                if p not in pairs: #check if it already exist in our list to avoid dups
                    pairs.append(p) #add if its new
    return sorted(pairs)     #sort the final list and return the list                                                                                                                                                        