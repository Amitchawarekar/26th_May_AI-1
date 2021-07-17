#!/usr/bin/env python
# coding: utf-8

# #### Build custom generator function

# In[ ]:


def table(n):
    for i in range(1,11):
    yield n*i


# In[ ]:


def mygen(n):
    yield n*2
    yield n*3


# In[2]:


t=(i*6 for i in range(1,11))


# In[3]:


t


# In[5]:


for i in t:
    print(i)


# #### Object Oriented Programming

# In[37]:


class Abc():
    a=10
    b=30
    print(a+b)
    def show(self):
        print(self.a,self.b)
        self.onemore()
    def onemore(self):
        print('wow')


# In[41]:


y=Abc()


# In[42]:


y.show()


# In[30]:


x.a


# In[31]:


x.b


# In[32]:


Abc.a


# In[43]:


class Pqr():
    def __init__(self,m=0,n=0):
        self.a=m
        self.b=n
        print("Object Created")
    def show(self):
        print("its showtime")
        print(self.a,self.b)
    def __del_(self):
        print("object deleted")
    def __call__(self):
        print("Its objects calling")
    def __str__(self):
        return self.b
    def __getitem__(self,ind):
        return self.b[ind]
    def __len__(self):
        return len(self.b)
    def __It__(self,obj):
        return len(self.b) <len(str(obj))
        
        
        


# In[44]:


print(y)


# In[45]:


y=Pqr(4,'hi')


# In[46]:


print(y)


# In[48]:


x=Pqr()


# In[51]:


x.show()


# ### Inheritance

# In[54]:


class Xyz():
    a=10
    def show(self):
        print('wow')
        


# In[55]:


class Mno(Xyz):
    def another(self):
        print('from PQR')


# In[56]:


k = Mno()


# In[57]:


k.another()


# In[58]:


k.show()


# In[59]:


k.a


# #### Data Hiding

# In[66]:


class Acb():
    a=10
    def show(self):
        print(self.__a)
        


# In[67]:


a =Acb()


# In[68]:


a


# In[69]:


a.a


# In[ ]:




