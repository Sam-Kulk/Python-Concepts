'''
range(): This function is used to specify the range

Different options avaiable with range()
-----------------------------------------
1. range(10): This means range starts from 0 & ends at 10
2. range(1, 10): This means range starts from 1 & ends at 10-1 = 9
3. range(2,10,2): Here start point is 2, every time 2 will be incremented & the
numbers considred will be 2, 4, 6, 8 (10 will be excluded)
4. range(-10,-5): [-10,-9,-8,-7,-6]
5. range(-10,-5,2): [-10,-8,-6]

Note:
1. To print i can use print(list(range(1,10,2))) & output will be [1, 3, 5, 7, 9]
2. if i specify only one number, then starting point will be 0 & autoincrement will
be by +1
3. if i dont specify increment value, by default it will be +1

LOOPS
-----
1. The loop is used to execute a statement or a block of statements for n number of times
2. There are two types of loops i,e for & while
3. while loop has to be used when i want to execute the set of statements until a
condition fails, wherein i dont know usually how many times the statements will be
executed.
4. In while loop statement, i need to specify three things i,e initialization(start point)
then condition & then incrementation/decrementation
5. for loop has to be used when i know how many times i want to execute the block of
statements
6. In for loop i need to use range function, where start, end & increment/decrement
will be specified
'''

# while loop
# printing numbers in descending order
i = 10 # Initialization
while i>=1: # Condition
    print(i)
    i = i-1 # Incrementation/Decrementation
print("Done!!!")

# for loop
# printing odd numbers between 1 to 10
for i in range(1,11,2): # Every iteration i will be assigned with one value by in keyword
    print(i)
print("Done!!!")