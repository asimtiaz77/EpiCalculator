#!/usr/bin/env python
# coding: utf-8

# In[12]:


# prevalence
population = int(input("Population: "))
existingcases = int(input("Existing cases: "))
prevalence = existingcases/population
print(prevalence)
print(prevalence * 100000)

"Population: 1780000"
"Existing Cases: 99"
5.5617977528089886e-05
5.561797752808989


# In[10]:


# incidence
newcases = int(input("New cases: "))
population = int(input("Population: "))
incidence = newcases / population
print(incidence)
print(incidence * 100000)

"New cases= 19"
"Population= 1780000"
1.0674157303370787e-05
1.0674157303370786


# In[13]:


# mortality rate
dead  =int(input("Number of those who died: "))
segment =int(input("Number of those who had the disease: "))
mortalityrate = dead / segment 
print(mortalityrate)
print(mortalityrate * 100000)

"Number of those who died = 2"
"Number of those who had the disease = 99"
0.020202020202020204
2020.2020202020203


# In[15]:


# years of potential life lost
lifeexpectancy = 77
ages = [64, 74]
print(lifeexpectancy - ages[0])
print(lifeexpectancy - ages[1])
13
3


# In[14]:


lifelost = [13, 3]
yppl = sum(lifelost) / len(lifelost)
print(yppl)
8.0


# In[17]:


# prevalence
population = int(input("Population: "))
existingcases = int(input("Existing cases: "))
prevalence = existingcases / population 
print(prevalence)
print(prevalence * 100000)

"Population = 2660000"
"Existing cases = 1459"
0.0005484962406015038
54.849624060150376


# In[31]:


# incidence
newcases - int(input("New cases: "))
population - int(input("Population: "))
incidence - newcases / population
print(incidence)
print(incidence * 100000)

"New cases: 248"
"Population: 2660000"
1.0674157303370787e-05
1.0674157303370786


# In[20]:


# mortality rate
dead - int(input("Number of those who died: "))
segment - int(input("Number of those who had the disease: "))
mortalityrate - dead / segment 
print(mortalityrate)
print(mortalityrate * 100000)

"Number of those who died: 1"
"Number of those who had the disease: 1459"
0.020202020202020204
2020.2020202020203


# In[24]:


# prevalence
population = int(input("Population: "))
existingcases = int(input("Existing cases: "))
prevalence = existingcases / population 
print(prevalence)
print(prevalence * 100000)

"Population = 100000"
"Existing cases = 3000"
0.03
3000.0


# In[25]:


# incidence
newcases - int(input("New cases: "))
population - int(input("Population: "))
incidence - newcases / population
print(incidence)
print(incidence * 100000)

"New cases: 2500"
"Population: 100000"
1.0674157303370787e-05
1.0674157303370786


# In[27]:


# mortality rate
dead - int(input("Number of those who died: "))
segment - int(input("Number of those who had the disease: "))
mortalityrate - dead / segment 
print(mortalityrate)
print(mortalityrate * 100000)

"Number of those who died: 1"
"Number of those who had the disease: 3000"
0.020202020202020204
2020.2020202020203


# In[28]:


# prevalence
population = int(input("Population: "))
existingcases = int(input("Existing cases: "))
prevalence = existingcases / population 
print(prevalence)
print(prevalence * 100000)

"Population = 1780000"
"Existing cases = 15000"
0.008426966292134831
842.6966292134831


# In[29]:


# incidence
newcases - int(input("New cases: "))
population - int(input("Population: "))
incidence - newcases / population
print(incidence)
print(incidence * 100000)

"New cases: 3000"
"Population: 1780000 "
1.0674157303370787e-05
1.0674157303370786


# In[33]:


# mortality rate
dead = int(input("Number of those who died: "))
segment = int(input("Number of those who had the disease: "))
mortalityrate - dead / segment 
print(mortalityrate)
print(mortalityrate * 100000)

"Number of those who died: 5"
"Number of those who had the disease: 15000"
0.020202020202020204
2020.2020202020203


# In[6]:


# years of potential life lost
lifeexpectancy = 77
ages = [32, 45, 28, 37, 52]
print(lifeexpectancy - ages[0])
print(lifeexpectancy - ages[1])
print(lifeexpectancy - ages[2])
print(lifeexpectancy - ages[3])
print(lifeexpectancy - ages[4])
45
32
49
40
25

