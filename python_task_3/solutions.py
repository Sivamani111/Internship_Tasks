# Q1. Find the Frequency of Each Word in a Sentence

def frequency_word(Sentence):
    words = Sentence.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

print(frequency_word("python is easy and python is powerful"))



# Q2Find the Frequency of Each Character in a Word

def frequeny_char(Text):
    result={}
    for char in Text:
        if char in result:
            result[char]+=1
        else:
            result[char]=1
    return result

print(frequeny_char("banana"))


# Q3. Find the First Non-Repeating Character in a Word

def Non_Repeat_char(Text):
    result = {}
    for char in Text:
        if char in result:
            result[char]+=1
        else:
            result[char]=1
    for char in result:
        if result[char] == 1:
            return char
print(Non_Repeat_char("swiss"))

# Q4. Check Whether Two Strings Are Anagrams

def anagram_word(Text1,Text2):
    Text1 = Text1.lower()
    Text2 = Text2.lower()
    if sorted(Text1) ==sorted(Text2):
        return True
    else:
        return False
print(anagram_word("Silent","Listen"))

# Q5. Find the First Repeating Character in a String

def repeated_char(Text):
    result = {}
    for char in Text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    for char in result:
        if result[char] > 1:
            return char

    return None
print(repeated_char("programming"))

# Q6 Move All Zeros to the End of a List

def zeros(list1):
    list2 = []
    for i in list1:
        if i != 0:
            list2.append(i)
    for i in list1:
        if i == 0:
            list2.append(i)
    return list2
print(zeros([0, 3, 0, 1, 2, 0, 4]))

# Q7. Find the Second Highest Distinct Number in a List

def second_highest(list3):
    set1 = set()
    for i in list3:
        set1.add(i)
    list4 = sorted(set1,reverse=True)
    if len(list4)<2:
        return None
    return(list4[1])
print(second_highest([10, 20, 40, 30, 40, 20]))

# Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicates(list5):
    list6 = []
    for i in list5:
        if i not in list6:
            list6.append(i)
    return list6
print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))

# Q9. Find the Missing Number from 1 to N

def missing_value(nums,N):
    for i in range(1,N+1):
        if i not in nums:
            return i
print(missing_value([1, 2, 4, 5, 6],6))

# Q10 Find Two Numbers Whose Sum Equals a Target

def sum_equals(list7,target):
    for i in range(len(list7)):
        for j in range(i+1,len(list7)):
            if list7[i]+list7[j]==target:
                return [list7[i],list7[j]]
print(sum_equals([2, 7, 11, 15], 9))

# Q11. Find the Number Closest to Zero

def nearest_number(List8):
    if not List8:
        return None
    nearest = List8[0]
    for i in List8:
        if abs(i)<abs(nearest) or (abs(i) == abs(nearest)and i > nearest):
            nearest = i
    return nearest
print(nearest_number([-8, -3, 2, 5, -2]))

# Q12. Find Common Elements Between Two Lists

def commone_value(list9,list10):
    result = []
    for i in list9:
        for j in list10:
            if i == j:
                result.append(i)
    return result
print(commone_value([1, 2, 3, 4, 5],[3, 4, 5, 6, 7]))

# Q13. Rotate a List to the Right by K Positions

def rotate(List11,k):
    if len(List11) == 0:
        return List11
    k = k%len(List11)

    if k!=0:
        return List11[-k:] + List11[:-k]
    else:
        return List11
print(rotate([1, 2, 3, 4, 5],2))

# Q14. Find the Maximum Sum of Two Consecutive Elements

# [4, 7, 2, 9, 5]  
def max_sum(num):
    if len(num)<2:
        return None
    max = num[0]+num[1]
    for i in range(len(num)-1):
        total = num[i]+num[i+1]

        if total > max:
            max = total
    return max
print(max_sum([4, 7, 2, 9, 5]))

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def Pair_of_number(nums,target):
    result= []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                result.append((nums[i],nums[j]))
    return result
print(Pair_of_number([2, 4, 3, 5, 7, 8, 1],9))


