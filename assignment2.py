#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
ans: 1.true 2.false
# In[1]:


s="ineuron"  


# In[2]:


s.startswith('i')


# In[3]:


s.endswith('r')


# 2. What are the three different types of Boolean operators?
ans: Arthimetic opareter
     Logical opareter
     Assignment opareter
# 3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate )

# In[ ]:





# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# In[1]:


(5>4)&(3==5)


# In[2]:


not (5 > 4)


# In[3]:


(5 > 4) or (3 == 5)


# In[4]:


not ((5 > 4) or (3 == 5))


# In[5]:


(True and True) and (True == False)


# In[6]:


(not False) or (not True)


# 5. What are the six comparison operators?
Ans: 1.less than(<),
     2.less than or equal to(<=)
     3.greater than(>)
     4.greater than or equal to(>=)
     5.equal to(==)
     6.not equal to(!=)
# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
Ans:
    '=' is the assignment operator that stores a value in a variable,
    '==' is the equal to operator that compares two values and evaluates to a Boolean.
    eg: if x=5 here we assign x as 5  
    if we compare x and 5 x==5,either true or false 
    here 5 equal to 5 is true
    
# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')

# In[19]:


print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# In[3]:


spam==input()
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings")


# 9.If your programme is stuck in an endless loop, what keys you’ll press?
Press CTRL-C to stop a program stuck in an infinite loop.
# 10. How can you tell the difference between break and continue?
The break statement will move the execution outside and just after a loop.
The continue statement will move the execution to the start of the loop.
# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and
range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.
# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[9]:


for i in range(1, 11):
    print(i)
i=1
while i >= 10:
    print(i)
i = i + 1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
This function can be called with spam.bacon().