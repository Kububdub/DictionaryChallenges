####Cha 1
##def count_freqs(arr):
##    word_freq = {}
##    for item in arr:
##        if item in word_freq:
##            word_freq[item] += 1
##
##        else:
##            word_freq[item] = 1
##
##    return word_freq
##
##print(count_freqs(["apple", "banana", "apple", "orange", "banana", "apple"]))

####Cha 2
##student_grades = {
## "Alice": [85, 90, 78],
## "Bob": [92, 88, 84],
## "Charlie": [70, 75, 80]
##}

##print(student_grades.get("Alice"))
##def average_grades(dic):
##    avg_grades = {}
##    for student in dic:
##        total = 0
##        for score in dic.get(student):
##            total += score
##        avg = total / len(dic.get(student))
##        avg_grades[student] = avg
##
##    return avg_grades
##
##print(average_grades(student_grades))

####Cha 3
##original_dict = {"a": 2, "b": 3, "c": 4}

##
##def square_values(dic):
##    squared = {}
##    for item in dic:
##        squared[item] = (dic.get(item))**2
##    return squared
##
##print(square_values(original_dict))


# ##Cha 4
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 3, "c": 4, "d": 5}

# def merge_dicts(dict1, dict2):
#     merged = {}
#     for item1 in dict1:
#         if item1 in dict2:
#              for item2 in dict2:
#                  if item1 == item2:
#                      merged[item1] = dict1.get(item1) + dict2.get(item2)
#         else:
#             merged[item1] = dict1.get(item1)

#     for item in dict2:
#         if item not in dict1:
#             merged[item] = dict2.get(item)

#     return merged

# print(merge_dicts(dict1, dict2))

# ##Cha 5
# data = {
#  "fruit": ["apple", "banana", "orange"],
#  "colour": ["red", "yellow", "orange"]
# }

# def transform_data(data):
#     list1 = []
#     for item in data:
#         for value in data.get(item):
#             list1.append({item:value})
#     return list1

# print(transform_data(data))

# ##Cha 6
# data = {"a": 1, "b": 2, "c": 3}

# def remove_and_return(data,value):
#     out = data.get(value)
#     data.pop(value)
#     return out

# print(remove_and_return(data, "b")) # Output: 2
# print(data) # Output: {'a': 1, 'c': 3}

# ##Cha 7
# data = {"x": 10, "y": 20, "z": 30}

# def pop_all_values(data):
#     out = []
#     for item in data:
#         out.append(data.get(item))

#     while len(data)>0:
#         data.popitem()
    
#     return(out)

# print(pop_all_values(data)) # Output: [10, 20, 30]
# print(data) # Output: {}

# ##Cha 8
# data = {"p": 5, "q": 15, "r": 25}

# def pop_and_sum(data,values):
#     sum = 0
#     for item in data:
#         if item in values:
#             sum += data.get(item)
    
#     for item in values:
#         if item in data:
#             data.pop(item)

#     return sum

# print(pop_and_sum(data, ["p", "r"])) # Output: 30
# print(data) # Output: {'q': 15}

# ##Cha 9
# data = {"m": 7, "n": 14}

# def pop_with_default(data,value,default):
#     if value in data:
#         out = data.get(value)
#         data.pop(value)
#         return out

#     else:
#         return default

# print(pop_with_default(data, "n", 0)) # Output: 14
# print(pop_with_default(data, "o", 0)) # Output: 0
# print(data) # Output: {'m': 7}

##Cha10 (ALMOLST DONE!!)
data = {"a": 1, "b": 2, "c": 3, "d": 4}

def pop_and_create_new(data, values):
    newdict = {}
    for item in data:
        if item in values:
            newdict[item] = data.get(item)

    for item in values:
         if item in data:
             data.pop(item)

    return newdict
    

print(pop_and_create_new(data, ["b", "d"])) # Output: {'b': 2, 'd': 4}
print(data) # Output: {'a': 1, 'c': 3}