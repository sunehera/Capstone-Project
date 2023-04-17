#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import csv


# In[2]:


import nest_asyncio
nest_asyncio.apply()


# In[3]:


import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log
import pandas as pd
import numpy as np
import re


# In[ ]:


consumer_key = "d1GQM32qnALmxQmhc5A7eW4kU"
consumer_secret = "WKNXA0QUt2A4vZccO5tEaMxd1XQlUtz7YvRhU0LzDVNVpMW1aP"
access_token = "1646197650620833792-U3ldssA9IZ20lfd43g9EjTfu4iH0Og"
access_token_secret = "CaTMccY8fkJ3iNPJhjfOQqDNYmBhjUhhPETVKz3mSmiM0"


# In[4]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# In[5]:


api = tweepy.API(auth, wait_on_rate_limit=True)


# In[6]:


try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")
    print(e)


# In[7]:


tags = ["#happiness","#blessed", "#thankful","grateful", "#goodvibes", "happiness", "happy", "thankful", "#joy"]


# In[8]:


date_since = "2021-03-01"


# In[9]:


csv_file = open('/Users/suneherahasib/Desktop/capstone/tweets3.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)


# In[10]:


csv_writer.writerow(['tweet_id', 'text'])
    


# In[ ]:


for tag in tags:
    # Define search query
    search_query = tag + " -filter:links -filter:retweets"
    
    # Perform search using Tweepy Cursor
    for tweet in tweepy.Cursor(api.search_tweets,
                               q=search_query,
                               lang='en',
                               since_id=date_since,
                               tweet_mode='extended').items():
        # Clean text by removing URLs, mentions, and special characters
        cleaned_text = re.sub(r'http\S+', '', tweet.full_text)
        cleaned_text = re.sub(r'@\S+', '', cleaned_text)
        csv_writer.writerow([tweet.id_str, cleaned_text])

# Close CSV file
csv_file.close()


# In[ ]:


df1 = pd.read_csv('/Users/suneherahasib/Desktop/capstone/tweets2.csv')
df2 = pd.read_csv('/Users/suneherahasib/Desktop/capstone/tweets3.csv')

# Concatenate the two data frames into a single data frame
combined_df = pd.concat([df1, df2], axis=0)

# Shuffle the rows of the combined data frame
shuffled_df = combined_df.sample(frac=1, random_state=42)

# Save the shuffled data frame as a new file
shuffled_df.to_csv('tweets4f.csv', index=False)

