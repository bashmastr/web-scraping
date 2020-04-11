#!/usr/bin/env python
# coding: utf-8

# # Installation

# In[2]:


get_ipython().system('pip install lxml # parser html, laxml and so on')
get_ipython().system('pip install requests  #package for request urls')

#BeautifulSoup4
get_ipython().system('pip install beautifulsoup4')


# In[50]:


#show packages
get_ipython().system('pip list  #conda list ')


# # Import packages
# 

# In[51]:


import requests
from bs4 import BeautifulSoup
import json
import time 
from bs4 import UnicodeDammit


# # Extract the HTML into text

# In[52]:



req = requests.get('https://www.imdb.com/title/tt0071853/')
print(req.text)

r_unparsed = req.text


# ##### Now make some Soup using Beautiful Soup and XML parser

# In[54]:


b = BeautifulSoup(r_unparsed, 'lxml')
start = time.time()
b = BeautifulSoup(r_unparsed,'lxml')
end = time.time()
print(end - start)


# ##### extract the title and save it into a variable
# you can use some specific methods of Beautiful Soup or follow the tree
# 

# In[57]:


title = b.title.text
# print(title)

print(b.find('h1').text)


# if there was more than one title it would have to be
# 

# In[77]:


title = b.find_all('title')
print(title)


# ##### extract the description 

# In[78]:


desc = b.find('div','summary_text').text.strip()
print(desc)


# ### extract the Rating eg: R and save into a variable
# 

# In[36]:


print(b.find('div','subtext').text.strip()[0:2])


# # Find Actors

# In[74]:


actors = json.loads(b.find('script', type='application/ld+json').text)['actor']
# print(actors)

actors_list = []

for actor in actors:
    actors_list.append(actor)
print(actors_list)


# create function for repeatation
def actors(x):
    actors_list = []
    actors = json.loads(x.find('script', type='application/ld+json').text)['actor']
    for actor in actors:
        actors_list.append(str(actor['name']))
    return actors_list

print(actors(b))


# ### Create a function that extracts this information of any IMDB movie of your choosing

# In[80]:



def movie_info(id):
    r = requests.get('https://www.imdb.com/title/{0}/'.format(id))
    b = BeautifulSoup(r.text,'lxml')
    movie_dict = {}
    movie_dict[id] = {}
    movie_dict[id]['title'] = b.title.text
    movie_dict[id]['desc'] = b.find('div','summary_text').text.strip()
    movie_dict[id]['rating'] = json.loads(b.find('script', type='application/ld+json').text)['contentRating']
    movie_dict[id]['actors'] = actors(b)
    # movie_dict[id]['directors'] = directors(b)
    return movie_dict


Adrift = movie_info('tt6751668')

print(Adrift)


# In[ ]:





# In[ ]:




