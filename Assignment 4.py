#!/usr/bin/env python
# coding: utf-8

# In[2]:


#  1. A = { 55, 6, 8, 9, 11} , B = {44, 55, 89,54} apply set union.
A = { 55, 6, 8, 9, 11}
B = {44, 55, 89,54}
print('Appling union ' , A | B)


# In[9]:


# 2. Which data type not allow duplicate item. Give an example.
# Set and Dictionary data typye dose not allow duplicate values such as
Set = {1,1,2,2,3,3}
print(type(Set))
print(Set)
# --------------
Dic = {'Name ': 'Shorif', 'Roll': 1,'Name ': 'Shorif', 'Roll': 1}
print(type(Dic))
print(Dic)


# In[12]:


# 3. B={‘Django’: 16, ‘Project’: 8, ‘Students’: 20} print keys.
B={'Django': 16, 'Project': 8, 'Students': 20} 
showB =B.keys()
print(showB)


# In[15]:


# 4. Create a function & call the function.
def my_function():
    print('This is my firs fuction! ')
my_function()


# In[18]:


# 5. Create Class & Object.
class FirstClass:
    x = 4
Class1 = FirstClass()
print(Class1.x)


# In[20]:


# 6. Give an example of Inheritance.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



x = Person("Shoriful", "Alam")
x.printname()


# In[ ]:




