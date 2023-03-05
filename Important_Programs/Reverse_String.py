# Method 1
s = 'Python'
rev_str = ''
for i in s: # It will start assigning values from P i.e.first character
    rev_str = i+rev_str
print(rev_str)

# Method 2
rev_str = s[::-1]
print(rev_str)
'''start index = 0
end index, since not provided, it will consider all indexes i.e. 7
so i am saying print from index 0 to 7 in reverse order '''
