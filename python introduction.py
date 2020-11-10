#!/usr/bin/env python
# coding: utf-8

# In[3]:


print ('welcome to the first class of python')


# In[4]:


print(2+3)


# In[19]:


#list
scores=[67,54,98,91,76,59,69,99]

type(scores)

scores[0] #accesing an element of a list using its index

scores[3:]

scores[:4]

scores[2:6] #list slicing

scores.append(100) #append a new element to the list

scores.extend([80,81]) #append multiple elements to the list

scores.insert(3,66)# inserting a new element at specifying index

scores.remove(100)

scores


# In[5]:


#Dictionary
pizza_info={'pizza_type':['veg','non-veg'],
           'base_type':['hand_tossed','pan_based','thin_crust'],
           'toppings':['capsicum','olives','jalapenos','paneer'],
           'payment_mode':['debit','credit','gpay']
           }
type(pizza_info)

pizza_info['pizza_type'] #accesing values from a dictionary using key

pizza_info['base_type'].append('cheese_burst')
pizza_info


# In[ ]:





# In[12]:


#tuple

dog_breeds=('german shepherd','labrador','american bully','golden retriver','husky')

dog_breeds

dog_breeds[3] #accessing elements using index

dog_breeds[-1]  #negative indexing

dog_breeds.append('puppy')
god_breed.remove('husky')


# In[13]:


#list is muatable, tuple is immutable

pubs=[('autumn leaf',36),('zero 40',10),('tiki shak',36),('fat pigeon',45)]

pubs[1]


# In[14]:


#sets

scores_set={34,34,34,65,69,87,69,34,56,97,90,34,90,56,69}
scores_set


# In[15]:


9**3


# In[20]:


a_list=[1,2,3,4,5,6,7,8]

#loop 

squares_list=[] #empty list

for ele in a_list:
    squares_list.append(ele**2)

squares_list


# In[21]:


sq_list=[ele**2 for ele in a_list] #list comprehension

sq_list 


# In[24]:


for ele in a_list :
    if ele>5:
        print (ele)
        
grt_5=[ ele for ele in a_list if ele>5] #list comprehension
 
grt_5


# In[27]:


#functions

#reusability / modularity of code

def add(x,y): #x and y are the inputs
    return x+y

add(2,32)


# In[31]:


#WAPF that takes a list of integers and returns the squares of them.

def squares_list(demo_list):
    for ele in demo_list:
        print (ele**2)
squares_list([1,2,34,5,656,354,5,6,7787,12])
squares_list([2,3,6,77,88,98])


# In[ ]:





# In[32]:


#WAPF that takes a list of integers and returns the squares of them.

def squares_list(x):
    return [ele**2 for ele in x] #list comprehension
squares_list([1,2,3,4,5,6])


# In[44]:


#WAPF that tales a list of integers and reorders the elements in the following fasion.

#sample_input=[-98,43,23,12,67,32,-69,21,9,-100,-21,-63,-43,99]
#sample_output=[-98,-69,-100,-21,-63,-43,43,23,12,67,32,69,21,9,99]


def rlist(x):
    n_list=[]
    p_list=[]
    for ele in x:
        if(ele<0):
            n_list.append(ele)
        if(ele>0):
            p_list.append(ele)
    return n_list+p_list

rlist([-98,43,23,12,67,32,-69,21,9,-100,-21,-63,-43,99])
        
    


# In[45]:


def rlist(x):
    return[ele for ele in x if ele<0]+[ele for ele in x if ele>0]
rlist([-98,43,23,12,67,32,-69,21,9,-100,-21,-63,-43,99])


# In[46]:


#sort

samp_list=[1,33,49,34,65,78,66,12,3,44,5,66]

samp_list.sort()

samp_list


# In[47]:


#WAPF that takes a list of numbers and returns the smallest and largest numbers from the list

def sllist(x):
    x.sort()
    
    return x[0],x[-1]

sllist([23,43,23,12,46,676,356,57,76,86,3546,68,67,4567,69])


# In[3]:


list(range(1,10))

for ele in range(1,10):
    print(ele)


# In[6]:


#WAPF that takes a number and returns the factorial of it.

#fact of 6= 6*5*4*3*2*1

def factorial(x):
    fact=1
    
    for ele in range (1,x+1):
        fact=fact*ele
    return fact

factorial(5)
        


# In[7]:


list(range(1,20,3))


# In[9]:


#strings

food='pizza'
type(food)

for char in food:
    print (char)


# In[10]:


food='pizza is from italy'

for char in food.split():
    print(char)


# In[11]:


'Data'+"_"+'Science'


# In[13]:


#Wapf to revert a string

def reverse(string):
    rev=''
    for char in string:
        rev=char+rev
    return rev
reverse ('pizza')

'Pizza'[::-1] #shortcut to reverse a string
        


# In[34]:


#WAPF that take a list and a number(n) and divides elements into chunks(each chunk containing n elements) in the below fasion.


#sample_input=[1,2,3,4,5,6,7,8,9],n=4

#sample_output=[1,2,3,4],[5,6,7,8],[9]

l=[1,2,3,4,5,6,7,8,9]
n=4
x=[l[i:i + n] for i in range(0, len(l), n)]
print(x)

    


# In[ ]:




