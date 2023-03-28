#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np


# In[31]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# # 1
# How many negative numbers are there?

# In[7]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a <0)


# In[8]:


# this breaks out the list of negatives
a[a < 0]


# In[9]:


# this counts the list
len(a[a < 0])


# # 2 
# How many positive numbers are there?
# 
# 
# 
# 

# In[10]:


# this breaks out the list of positives
a[a > 0]


# In[11]:


# this counts the list
len(a[a > 0])


# # 3
# How many even positive numbers are there?
# 

# In[12]:


# this breaks out the list of positives
a[a > 0]


# In[13]:


# this breaks out the evens
b = a[a>0]
b[b % 2 == 0] 


# In[14]:


# counts the positve even
len(b[b % 2 == 0] )


# In[ ]:





# # 4
# If you were to add 3 to each data point, how many positive numbers would there be?
# 

# In[20]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# add 3 to array
c = a + 3
print(c)


# In[22]:


# break out the positives
d = c [c>0]
print(d)


# In[23]:


len(d)


# In[ ]:





# # 5
# If you squared each number, what would the new mean and standard deviation be?

# In[33]:


g=a**2
print(g)


# In[36]:


# this is the mean
np.mean(g)


# In[37]:


# this is the standard deviation

np.std(g)


# # 6
# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
# 
# subtract the std from every value in the set

# In[38]:


a- (np.std(a))


# # 7
# 
# Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# #### Z=x-μ/σ
# where:
# 
# X is a single raw data value
# μ is the population mean
# σ is the population standard deviation
# 

# In[45]:


x = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[47]:


# STD
o=np.std(x)
print(o)


# In[48]:


#Mean
m=np.mean(x)
print(m)


# In[57]:


z= (x-m)/o

print(z)


# In[ ]:





# 
