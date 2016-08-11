
# coding: utf-8

# Name       : Brion Mallon
# 
# Student no : 1756894 
# 
# C A 1      : Choose an input file and apply various statistical processes 
# 
# Input      : Use a songs metadata file contains a 10,000 record subset of http://labrosa.ee.columbia.edu/millionsong/
# 
# Process    : Apply the following actions 
# 
#            - Matplotlib Scatterplot two of the attributes against each other.
#            - Including titles, headings etc for all plots
#            - Calculate summary statistics for each of 2 attributes (mean, median, variance or similar)
#            - Take a numerical attribute, and bin it into categories, and plot it somehow.
# 
# Songs file : this file contains 10,000 entries with track, artist, year and other attributes  
# 

# Start By importing required packages, get input songs file ( save numeric values in correct format, for speed when doing calculations)

# In[36]:

get_ipython().magic(u'matplotlib inline')
import matplotlib as plt
import pandas as pd
import numpy as np


# In[37]:

songs = pd.read_csv("songs.csv",  dtype={'artist_familiarity': float,'artist_hotttnesss': float, 'year': int})  


# In[23]:

songs.head(10)


# After reviewing the file above, there are several ID fields not required for this process, rewrite DataFrame without these columns
# 
# Remove following 
# Track_id
# song_id
# artist_id
# artist_mbid
# 
# Also, only select tracks from last 50 years 
# 

# In[48]:

songs = songs[['title','release','artist_name','duration','artist_familiarity','artist_hotttnesss','year']]

songs = songs[(songs['year'] >= 1965)]

songs.head(10)


# Now, describe the contents of the file

# In[30]:

songs.describe()


# Create a scatter plot with columns artist familiarity and hotttnesss (thats a term from the music industry i think)

# In[28]:

plot1 = songs.plot.scatter(x='artist_familiarity',y='artist_hotttnesss')

plot1.set(title='Plot Familiarity and Hotttnesss ',xlabel="Artist familiarity",ylabel="Artist hotttnesss")


# The above plot shows a positive linear association between artist familiarity and hotttnesss 
# 
# Now, get summary stats for 2 columns (artist_familiarity, artist_hotttnesss)
# list of Stats 
#     mean
#     median
#     variance 
#     StD

# In[42]:

print songs['artist_familiarity'].mean()
print songs['artist_hotttnesss'].mean()


# In[43]:

print songs['artist_familiarity'].median()
print songs['artist_hotttnesss'].median()


# In[45]:

print songs['artist_familiarity'].std()
print songs['artist_hotttnesss'].std()


# In[46]:

print songs['artist_familiarity'].var()
print songs['artist_hotttnesss'].var()


# Now, create a Plot showing total duration (music time) in mins for each year  (duration in seconds, sum to min)

# In[77]:

Durations = songs.groupby('year').agg({'duration': sum }).apply(lambda x: x/60)

plot2 = Durations.plot(kind='bar',figsize=(15, 4),legend=None)
plot2.set(title="Total Recording time (mins) Per Year",xlabel="Year",ylabel="Totals Songs duration in Mins")
 


# In[ ]:



