def count_substring(string, sub_string):
    len_substring = len(sub_string)
    c=0
    for i in range(len(string)):
        if string.count(sub_string, i, i + len_substring) >= 1:
            c+=1
    return c
    
string = input('whats your string').strip()
sub_string = input('what are you looking for?').strip()

count = count_substring(string, sub_string)
print(count)