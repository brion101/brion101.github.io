
# coding: utf-8

# The following are SQL type commands in pandas. the following has mostly been copied from 
# 
# http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
# 
# Have added the imput file in the following cell, copy this and add to a file called tips.csv

# totalbill,tip,sex,smoker,day,time,size
# 16.99,1.01,Female,No,Sun,Dinner,2
# 10.34,1.66,Male,No,Sun,Dinner,3
# 21.01,3.5,Male,No,Sun,Dinner,3
# 23.68,3.31,Male,No,Sun,Dinner,2
# 24.59,3.61,Female,No,Sun,Dinner,4
# 25.29,4.71,Male,No,Sun,Dinner,4
# 8.77,2.0,Male,No,Sun,Dinner,2
# 26.88,3.12,Male,No,Sun,Dinner,4
# 15.04,1.96,Male,No,Sun,Dinner,2
# 14.78,3.23,Male,No,Sun,Dinner,2
# 10.27,1.71,Male,No,Sun,Dinner,2
# 35.26,5.0,Female,No,Sun,Dinner,4
# 15.42,1.57,Male,No,Sun,Dinner,2
# 18.43,3.0,Male,No,Sun,Dinner,4
# 14.83,3.02,Female,No,Sun,Dinner,2
# 21.58,3.92,Male,No,Sun,Dinner,2
# 10.33,1.67,Female,No,Sun,Dinner,3
# 16.29,3.71,Male,No,Sun,Dinner,3
# 16.97,3.5,Female,No,Sun,Dinner,3
# 20.65,3.35,Male,No,Sat,Dinner,3
# 17.92,4.08,Male,No,Sat,Dinner,2
# 20.29,2.75,Female,No,Sat,Dinner,2
# 15.77,2.23,Female,No,Sat,Dinner,2
# 39.42,7.58,Male,No,Sat,Dinner,4
# 19.82,3.18,Male,No,Sat,Dinner,2
# 17.81,2.34,Male,No,Sat,Dinner,4
# 13.37,2.0,Male,No,Sat,Dinner,2
# 12.69,2.0,Male,No,Sat,Dinner,2
# 21.7,4.3,Male,No,Sat,Dinner,2
# 19.65,3.0,Female,No,Sat,Dinner,2
# 9.55,1.45,Male,No,Sat,Dinner,2
# 18.35,2.5,Male,No,Sat,Dinner,4
# 15.06,3.0,Female,No,Sat,Dinner,2
# 20.69,2.45,Female,No,Sat,Dinner,4
# 17.78,3.27,Male,No,Sat,Dinner,2
# 24.06,3.6,Male,No,Sat,Dinner,3
# 16.31,2.0,Male,No,Sat,Dinner,3
# 16.93,3.07,Female,No,Sat,Dinner,3
# 18.69,2.31,Male,No,Sat,Dinner,3
# 31.27,5.0,Male,No,Sat,Dinner,3
# 16.04,2.24,Male,No,Sat,Dinner,3
# 17.46,2.54,Male,No,Sun,Dinner,2
# 13.94,3.06,Male,No,Sun,Dinner,2
# 9.68,1.32,Male,No,Sun,Dinner,2
# 30.4,5.6,Male,No,Sun,Dinner,4
# 18.29,3.0,Male,No,Sun,Dinner,2
# 22.23,5.0,Male,No,Sun,Dinner,2
# 32.4,6.0,Male,No,Sun,Dinner,4
# 28.55,2.05,Male,No,Sun,Dinner,3
# 18.04,3.0,Male,No,Sun,Dinner,2
# 12.54,2.5,Male,No,Sun,Dinner,2
# 10.29,2.6,Female,No,Sun,Dinner,2
# 34.81,5.2,Female,No,Sun,Dinner,4
# 9.94,1.56,Male,No,Sun,Dinner,2
# 25.56,4.34,Male,No,Sun,Dinner,4
# 19.49,3.51,Male,No,Sun,Dinner,2
# 38.01,3.0,Male,Yes,Sat,Dinner,4
# 26.41,1.5,Female,No,Sat,Dinner,2
# 11.24,1.76,Male,Yes,Sat,Dinner,2
# 48.27,6.73,Male,No,Sat,Dinner,4
# 20.29,3.21,Male,Yes,Sat,Dinner,2
# 13.81,2.0,Male,Yes,Sat,Dinner,2
# 11.02,1.98,Male,Yes,Sat,Dinner,2
# 18.29,3.76,Male,Yes,Sat,Dinner,4
# 17.59,2.64,Male,No,Sat,Dinner,3
# 20.08,3.15,Male,No,Sat,Dinner,3
# 16.45,2.47,Female,No,Sat,Dinner,2
# 3.07,1.0,Female,Yes,Sat,Dinner,1
# 20.23,2.01,Male,No,Sat,Dinner,2
# 15.01,2.09,Male,Yes,Sat,Dinner,2
# 12.02,1.97,Male,No,Sat,Dinner,2
# 17.07,3.0,Female,No,Sat,Dinner,3
# 26.86,3.14,Female,Yes,Sat,Dinner,2
# 25.28,5.0,Female,Yes,Sat,Dinner,2
# 14.73,2.2,Female,No,Sat,Dinner,2
# 10.51,1.25,Male,No,Sat,Dinner,2
# 17.92,3.08,Male,Yes,Sat,Dinner,2
# 27.2,4.0,Male,No,Thur,Lunch,4
# 22.76,3.0,Male,No,Thur,Lunch,2
# 17.29,2.71,Male,No,Thur,Lunch,2
# 19.44,3.0,Male,Yes,Thur,Lunch,2
# 16.66,3.4,Male,No,Thur,Lunch,2
# 10.07,1.83,Female,No,Thur,Lunch,1
# 32.68,5.0,Male,Yes,Thur,Lunch,2
# 15.98,2.03,Male,No,Thur,Lunch,2
# 34.83,5.17,Female,No,Thur,Lunch,4
# 13.03,2.0,Male,No,Thur,Lunch,2
# 18.28,4.0,Male,No,Thur,Lunch,2
# 24.71,5.85,Male,No,Thur,Lunch,2
# 21.16,3.0,Male,No,Thur,Lunch,2
# 28.97,3.0,Male,Yes,Fri,Dinner,2
# 22.49,3.5,Male,No,Fri,Dinner,2
# 5.75,1.0,Female,Yes,Fri,Dinner,2
# 16.32,4.3,Female,Yes,Fri,Dinner,2
# 22.75,3.25,Female,No,Fri,Dinner,2
# 40.17,4.73,Male,Yes,Fri,Dinner,4
# 27.28,4.0,Male,Yes,Fri,Dinner,2
# 12.03,1.5,Male,Yes,Fri,Dinner,2
# 21.01,3.0,Male,Yes,Fri,Dinner,2
# 12.46,1.5,Male,No,Fri,Dinner,2
# 11.35,2.5,Female,Yes,Fri,Dinner,2
# 15.38,3.0,Female,Yes,Fri,Dinner,2
# 44.3,2.5,Female,Yes,Sat,Dinner,3
# 22.42,3.48,Female,Yes,Sat,Dinner,2
# 20.92,4.08,Female,No,Sat,Dinner,2
# 15.36,1.64,Male,Yes,Sat,Dinner,2
# 20.49,4.06,Male,Yes,Sat,Dinner,2
# 25.21,4.29,Male,Yes,Sat,Dinner,2
# 18.24,3.76,Male,No,Sat,Dinner,2
# 14.31,4.0,Female,Yes,Sat,Dinner,2
# 14.0,3.0,Male,No,Sat,Dinner,2
# 7.25,1.0,Female,No,Sat,Dinner,1
# 38.07,4.0,Male,No,Sun,Dinner,3
# 23.95,2.55,Male,No,Sun,Dinner,2
# 25.71,4.0,Female,No,Sun,Dinner,3
# 17.31,3.5,Female,No,Sun,Dinner,2
# 29.93,5.07,Male,No,Sun,Dinner,4
# 10.65,1.5,Female,No,Thur,Lunch,2
# 12.43,1.8,Female,No,Thur,Lunch,2
# 24.08,2.92,Female,No,Thur,Lunch,4
# 11.69,2.31,Male,No,Thur,Lunch,2
# 13.42,1.68,Female,No,Thur,Lunch,2
# 14.26,2.5,Male,No,Thur,Lunch,2
# 15.95,2.0,Male,No,Thur,Lunch,2
# 12.48,2.52,Female,No,Thur,Lunch,2
# 29.8,4.2,Female,No,Thur,Lunch,6
# 8.52,1.48,Male,No,Thur,Lunch,2
# 14.52,2.0,Female,No,Thur,Lunch,2
# 11.38,2.0,Female,No,Thur,Lunch,2
# 22.82,2.18,Male,No,Thur,Lunch,3
# 19.08,1.5,Male,No,Thur,Lunch,2
# 20.27,2.83,Female,No,Thur,Lunch,2
# 11.17,1.5,Female,No,Thur,Lunch,2
# 12.26,2.0,Female,No,Thur,Lunch,2
# 18.26,3.25,Female,No,Thur,Lunch,2
# 8.51,1.25,Female,No,Thur,Lunch,2
# 10.33,2.0,Female,No,Thur,Lunch,2
# 14.15,2.0,Female,No,Thur,Lunch,2
# 16.0,2.0,Male,Yes,Thur,Lunch,2
# 13.16,2.75,Female,No,Thur,Lunch,2
# 17.47,3.5,Female,No,Thur,Lunch,2
# 34.3,6.7,Male,No,Thur,Lunch,6
# 41.19,5.0,Male,No,Thur,Lunch,5
# 27.05,5.0,Female,No,Thur,Lunch,6
# 16.43,2.3,Female,No,Thur,Lunch,2
# 8.35,1.5,Female,No,Thur,Lunch,2
# 18.64,1.36,Female,No,Thur,Lunch,3
# 11.87,1.63,Female,No,Thur,Lunch,2
# 9.78,1.73,Male,No,Thur,Lunch,2
# 7.51,2.0,Male,No,Thur,Lunch,2
# 14.07,2.5,Male,No,Sun,Dinner,2
# 13.13,2.0,Male,No,Sun,Dinner,2
# 17.26,2.74,Male,No,Sun,Dinner,3
# 24.55,2.0,Male,No,Sun,Dinner,4
# 19.77,2.0,Male,No,Sun,Dinner,4
# 29.85,5.14,Female,No,Sun,Dinner,5
# 48.17,5.0,Male,No,Sun,Dinner,6
# 25.0,3.75,Female,No,Sun,Dinner,4
# 13.39,2.61,Female,No,Sun,Dinner,2
# 16.49,2.0,Male,No,Sun,Dinner,4
# 21.5,3.5,Male,No,Sun,Dinner,4
# 12.66,2.5,Male,No,Sun,Dinner,2
# 16.21,2.0,Female,No,Sun,Dinner,3
# 13.81,2.0,Male,No,Sun,Dinner,2
# 17.51,3.0,Female,Yes,Sun,Dinner,2
# 24.52,3.48,Male,No,Sun,Dinner,3
# 20.76,2.24,Male,No,Sun,Dinner,2
# 31.71,4.5,Male,No,Sun,Dinner,4
# 10.59,1.61,Female,Yes,Sat,Dinner,2
# 10.63,2.0,Female,Yes,Sat,Dinner,2
# 50.81,10.0,Male,Yes,Sat,Dinner,3
# 15.81,3.16,Male,Yes,Sat,Dinner,2
# 7.25,5.15,Male,Yes,Sun,Dinner,2
# 31.85,3.18,Male,Yes,Sun,Dinner,2
# 16.82,4.0,Male,Yes,Sun,Dinner,2
# 32.9,3.11,Male,Yes,Sun,Dinner,2
# 17.89,2.0,Male,Yes,Sun,Dinner,2
# 14.48,2.0,Male,Yes,Sun,Dinner,2
# 9.6,4.0,Female,Yes,Sun,Dinner,2
# 34.63,3.55,Male,Yes,Sun,Dinner,2
# 34.65,3.68,Male,Yes,Sun,Dinner,4
# 23.33,5.65,Male,Yes,Sun,Dinner,2
# 45.35,3.5,Male,Yes,Sun,Dinner,3
# 23.17,6.5,Male,Yes,Sun,Dinner,4
# 40.55,3.0,Male,Yes,Sun,Dinner,2
# 20.69,5.0,Male,No,Sun,Dinner,5
# 20.9,3.5,Female,Yes,Sun,Dinner,3
# 30.46,2.0,Male,Yes,Sun,Dinner,5
# 18.15,3.5,Female,Yes,Sun,Dinner,3
# 23.1,4.0,Male,Yes,Sun,Dinner,3
# 15.69,1.5,Male,Yes,Sun,Dinner,2
# 19.81,4.19,Female,Yes,Thur,Lunch,2
# 28.44,2.56,Male,Yes,Thur,Lunch,2
# 15.48,2.02,Male,Yes,Thur,Lunch,2
# 16.58,4.0,Male,Yes,Thur,Lunch,2
# 7.56,1.44,Male,No,Thur,Lunch,2
# 10.34,2.0,Male,Yes,Thur,Lunch,2
# 43.11,5.0,Female,Yes,Thur,Lunch,4
# 13.0,2.0,Female,Yes,Thur,Lunch,2
# 13.51,2.0,Male,Yes,Thur,Lunch,2
# 18.71,4.0,Male,Yes,Thur,Lunch,3
# 12.74,2.01,Female,Yes,Thur,Lunch,2
# 13.0,2.0,Female,Yes,Thur,Lunch,2
# 16.4,2.5,Female,Yes,Thur,Lunch,2
# 20.53,4.0,Male,Yes,Thur,Lunch,4
# 16.47,3.23,Female,Yes,Thur,Lunch,3
# 26.59,3.41,Male,Yes,Sat,Dinner,3
# 38.73,3.0,Male,Yes,Sat,Dinner,4
# 24.27,2.03,Male,Yes,Sat,Dinner,2
# 12.76,2.23,Female,Yes,Sat,Dinner,2
# 30.06,2.0,Male,Yes,Sat,Dinner,3
# 25.89,5.16,Male,Yes,Sat,Dinner,4
# 48.33,9.0,Male,No,Sat,Dinner,4
# 13.27,2.5,Female,Yes,Sat,Dinner,2
# 28.17,6.5,Female,Yes,Sat,Dinner,3
# 12.9,1.1,Female,Yes,Sat,Dinner,2
# 28.15,3.0,Male,Yes,Sat,Dinner,5
# 11.59,1.5,Male,Yes,Sat,Dinner,2
# 7.74,1.44,Male,Yes,Sat,Dinner,2
# 30.14,3.09,Female,Yes,Sat,Dinner,4
# 12.16,2.2,Male,Yes,Fri,Lunch,2
# 13.42,3.48,Female,Yes,Fri,Lunch,2
# 8.58,1.92,Male,Yes,Fri,Lunch,1
# 15.98,3.0,Female,No,Fri,Lunch,3
# 13.42,1.58,Male,Yes,Fri,Lunch,2
# 16.27,2.5,Female,Yes,Fri,Lunch,2
# 10.09,2.0,Female,Yes,Fri,Lunch,2
# 20.45,3.0,Male,No,Sat,Dinner,4
# 13.28,2.72,Male,No,Sat,Dinner,2
# 22.12,2.88,Female,Yes,Sat,Dinner,2
# 24.01,2.0,Male,Yes,Sat,Dinner,4
# 15.69,3.0,Male,Yes,Sat,Dinner,3
# 11.61,3.39,Male,No,Sat,Dinner,2
# 10.77,1.47,Male,No,Sat,Dinner,2
# 15.53,3.0,Male,Yes,Sat,Dinner,2
# 10.07,1.25,Male,No,Sat,Dinner,2
# 12.6,1.0,Male,Yes,Sat,Dinner,2
# 32.83,1.17,Male,Yes,Sat,Dinner,2
# 35.83,4.67,Female,No,Sat,Dinner,3
# 29.03,5.92,Male,No,Sat,Dinner,3
# 27.18,2.0,Female,Yes,Sat,Dinner,2
# 22.67,2.0,Male,Yes,Sat,Dinner,2
# 17.82,1.75,Male,No,Sat,Dinner,2
# 18.78,3.0,Female,No,Thur,Dinner,2
# 

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

tips = pd.read_csv("C:\\Users\\conmallon\\Documents\\tips.csv") 


# In[3]:

tips.head(10)


# In[4]:

#    Folllow SQL can be written as below
#SELECT 'time', 'tip','smoker','day'
#FROM tips
#LIMIT 5;
 
tips[['time','tip','smoker','day']].head(5)


# In[5]:

#SELECT *
#FROM tips
#WHERE time = 'Dinner'
#LIMIT 5;

# sql in pandas 
tips[tips['time'] == 'Dinner'].head(5)


# In[6]:

is_dinner = tips['time'] == 'Dinner'  

is_dinner.value_counts()

tips[is_dinner].head(10)


# In[7]:

# tips of more than $5.00 at Dinner meals
# SELECT *
# FROM tips
# WHERE time = 'Dinner' AND tip > 5.00;

tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)].head(10)


# In[8]:

# tips by parties of at least 5 diners OR tip was more than $5.5
# SELECT *
# FROM tips
# WHERE size >= 5 OR total_bill > 45;

tips[(tips['size'] >= 5) | (tips['tip'] > 5.5)].head(10)


# In[9]:

# GROUP BY
#
# SELECT sex, count(*)
# FROM tips
# GROUP BY sex;
#

tips.groupby('sex').size()


# Notice that in the pandas code we used size() and not count(). This is because count() applies 
# the function to each column, returning the number of not null records within each.

# In[11]:

tips.groupby('sex').count() 


# In[15]:

#Alternatively, we could have applied the count() method to an individual column: 
tips.groupby('sex')['tip'].count()
    


# Multiple functions can also be applied at once. For instance, say we’d like to see how tip
# amount differs by day of the week - agg() allows you to pass a dictionary to your grouped 
# DataFrame, indicating which functions to apply to specific columns.

# In[16]:

# SELECT day, AVG(tip), COUNT(*)
# FROM tips
# GROUP BY day;

tips.groupby('day').agg({'tip': np.mean, 'day': np.size})


# In[17]:

#SELECT smoker, day, COUNT(*), AVG(tip)
#FROM tips
#GROUP BY smoker, day;
tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})


# JOIN
# 
# JOINs can be performed with join() or merge(). By default, join() will join the
# DataFrames on their indices. Each method has parameters allowing you to specify
# the type of join to perform (LEFT, RIGHT, INNER, FULL) or the columns to join on 
# (column names or indices).
# 

# In[18]:

#  create 2 dataframes (these will be used in sample joins)
#

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],'value': np.random.randn(4)})
df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],'value': np.random.randn(4)})


# In[19]:

# INNER JOIN

# SELECT *
# FROM df1
# INNER JOIN df2
#  ON df1.key = df2.key;

pd.merge(df1, df2, on='key')


# merge() also offers parameters for cases when you’d like to join one DataFrame’s column 
# with another DataFrame’s index.

# In[20]:

indexed_df2 = df2.set_index('key')
pd.merge(df1, indexed_df2, left_on='key', right_index=True)


# In[21]:

# LEFT OUTER JOIN
# show all records from df1
# SELECT *
# FROM df1
# LEFT OUTER JOIN df2
#  ON df1.key = df2.key;

pd.merge(df1, df2, on='key', how='left')


# FULL JOIN
# 
# pandas also allows for FULL JOINs, which display both sides of the dataset,
# whether or not the joined columns find a match. As of writing, FULL JOINs are not 
# supported in all RDBMS (MySQL).
# 

# In[22]:

# show all records from both tables
# SELECT *
# FROM df1
# FULL OUTER JOIN df2
#  ON df1.key = df2.key;

pd.merge(df1, df2, on='key', how='outer')


# UNION
# 
# UNION ALL can be performed using concat().
# 

# In[23]:

df1 = pd.DataFrame({'city': ['Chicago', 'San Francisco', 'New York City'],'rank': range(1, 4)})
   
df2 = pd.DataFrame({'city': ['Chicago', 'Boston', 'Los Angeles'],'rank': [1, 4, 5]})
 


# In[25]:

# SELECT city, rank
# FROM df1
# UNION ALL
# SELECT city, rank
# FROM df2;

pd.concat([df1, df2])

#use drop_duplicates() to remove duplicates 
# pd.concat([df1, df2]).drop_duplicates()


# In[27]:

#Top N rows per group
#
#
# -- Oracle's ROW_NUMBER() analytic function
# SELECT * FROM (
#  SELECT
#    t.*,
#    ROW_NUMBER() OVER(PARTITION BY day ORDER BY tip DESC) AS rn
#  FROM tips t
# )
# WHERE rn < 3
# ORDER BY day, rn;

(tips.assign(rn=tips.sort_values(['tip'], ascending=False)
                      .groupby(['day'])
                      .cumcount() + 1)
                      .query('rn < 3')
                      .sort_values(['day','rn'])
 )


# In[28]:

# UPDATE

# UPDATE tips
# SET tip = tip*2
# WHERE tip < 2;
tips.loc[tips['tip'] < 2, 'tip'] *= 2

 


# In[29]:

# DELETE

# DELETE FROM tips
# WHERE tip > 9;

tips = tips.loc[tips['tip'] <= 9]


# In[ ]:



