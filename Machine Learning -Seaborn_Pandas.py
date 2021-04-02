#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as njoki
import seaborn as sbn
#Machine Learning Assignment
#1: Load the data file attached (chidata_for_assignment_5) using pandas
#df = njoki.read_csv(r"C:\Users\User\Downloads\chidata_for_assignment_5.csv")
#df = njoki.read_csv(r'C:\\Users\User\Downloads\chidata_for_assignment_5.csv')
df = njoki.read_csv('C:\\Users\\User\\Downloads\\chidata_for_assignment_5.csv')


# In[5]:


df


# In[6]:


#2: Display Column names
df.columns


# In[7]:


#Print/Display the Column Information
df.shape


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


#Print/Display the Column Information
df.info()


# In[12]:


#Generates a seaborn count plot of the gender
gender_count = njoki.DataFrame(df)
gender_count = sbn.countplot(x="Gender", data=df)
#Adding appropriate Chart Title
gender_count.set_title("Categories for Gender difference in Health")


# In[13]:


#Adding appropriate Chart Title
gender_count.set_title("Categories for Gender difference in Health")


# In[14]:


#Generate a count for Insurance
gender_count = njoki.DataFrame(df)
gender_count = sbn.countplot(x="Insurance", data=df)
#Adding appropriate Chart Title
gender_count.set_title("Categories for Gender difference in Health")


# In[15]:


#Adding the title to the Chart
gender_count.set_title("Category for Insurance")


# In[16]:


#Contigency cross table of the two data fields
#A contingency table, sometimes is called a two-way 
#frequency table. It is a tabular mechanism with at 
#least two rows and two columns used in statistics 
#to present categorical data in terms of frequency counts.
emily = njoki.crosstab(df.Gender, df.Insurance, margins=True, margins_name="Totals")
emily


# In[17]:


#10: Create a heatmap fo the contingency cross table
gender_count = sbn.heatmap(emily)
gender_count.set(title='Insurance (M/F)', xlabel='Insurance Results', ylabel='Gender')


# In[28]:


#Examples with Matplotlib
#import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[29]:


#prepare the data
nancy = np.linspace(0, 10, 100)


# In[30]:


#Plot the data
plt.plot(nancy, nancy, label='linear')


# In[33]:


#Add a legend
plt.legend(['linear'])


# In[ ]:


dx = pd.DataFrame({'c0':range(5), 'c1':range(5,10)})
dx.set_index('c0').plot(marker='o', )


# In[ ]:




