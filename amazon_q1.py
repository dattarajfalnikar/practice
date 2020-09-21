
def merge_sublist(new_string, start_index, new_char):
    updated_list = []
    new_sub_string=''
    for i in range(0, start_index):
        updated_list.append(new_string[i])

    for i in new_string[start_index: len(new_string)]:
        new_sub_string +=i
        
    new_string = updated_list + [new_sub_string + new_char]
    return new_string

def check_presence(ch, s, new_string):
   # print new_string
    if new_string:
        len_of_list = len(new_string)
        for index, i in enumerate(new_string):
            for sublist in i:
                if ch in sublist and index <= (len_of_list - 1):
                        return merge_sublist(new_string, index, ch)
                
        return new_string + [ch]               
    else:
        return [ch]
    
def count_shots(s):
    new_string = []
    for i in s:
        new_string = check_presence(i, s, new_string)
    return [len(i) for i in new_string]


a=['a','a','b','c','a','a','c','c','b','a','d']
print 'input::', a
print 'output::', count_shots(a)
a=['a','b','c','a']
print 'input::', a
print 'output::', count_shots(a)
a=['a','b','c']
print 'input::', a
print 'output::', count_shots(a)

a=['a','b','a','b','c','b','a','c','a','d','e','f','e','g','d','e','h','i','j','h','k','l','i','j',]
print 'input::', a
print 'output::', count_shots(a)
