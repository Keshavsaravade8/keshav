#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


get_ipython().system('pip install --upgrade pip')


# In[3]:


get_ipython().system('pip install pandas')


# In[4]:


get_ipython().system('pip install matplotlib')


# In[5]:


get_ipython().system('pip install seaborn')


# In[6]:


get_ipython().system('pip install numpy')


# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random


# # Task 2 – Generate random data for the social media data

# To generate some random tweet data to analyze.There are many ways to generate random data in Python, but some are more convenient than others. Inthis case, you may use pandas date range to choose a pseudo-random date within a range, the random
# module’s choice to create a choice from a list, and numpy’s random to create a random integer.
# First of all you need to define a list of categories for the social media experiment. The list may include
# the following, for example:Food, Travel, 'Fashion, Fitness, Music, Culture, Family, and Health
# Next, generate a Python data dictionary with fields Date, Category, and number of likes, all with random
# data. You will need the data to align, so the ‘Date’ dictionary entry should be n periods long, The
# Category should be a list of random choices n entries long and the Likes category should be random
# integers in the range 0 to lets say 10000 also with size equal to n. For example, if n is equal to 500:
# data = {'Date': pd.date_range('2021-01-01', periods=500),
#  . . .
# … Now Use the random method called choice to gather a random category.
# 'Category': [random.choice(categories) for _ in range(500)]
# … Then Use numpy’s random randint() to form a random integer for the number of likes.
# 'Likes': np.random.randint(0, 10000, size=500)

# In[8]:


categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']


# In[9]:


categories


# In[10]:


n = 500

data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}
df = pd.DataFrame(data)

print(df)


# # Task 3 – Load the data into a Pandas DataFrame and Explore the data

# The next step is to load the randomly generated data into the pandas dataframe and print the data.
# To do so, you need to use the DataFrame method of the pandas object and pass the data to it.
# Then, print the dataframe head, the dataframe information, and the dataframe description.
# Finally, print the count of each ‘Category’element.

# In[ ]:





# In[11]:


df.head()


# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


df["Category"].value_counts()


# # Task 4 – Clean the data

# An important aspect of processing data is to move invalid data points so you can effectively perform
# statistics and visualize valid data. The pandas dataframe has built-in functionality to clean the data.
# First, remove all the null data using the appropriate dataframe drop method. Next, you may want to
# also remove duplicate data from the dataframe. Use a dataframe method to do so.
# To appropriately display the data field, convert the dataframe field to a datetime format using the
# pandas object (not the dataframe). Hint: you pass the dataframe’s ‘Date’ field to the pandas conversion
# method.
# Next, convert the dataframe ‘Likes’ data to an integer.
# 

# In[ ]:


df.dropna()


# In[ ]:


df.dropna().sum()


# In[ ]:


df.dropna()


# In[ ]:


df.drop_duplicates()


# In[ ]:


df["Date"]=pd.to_datetime(df["Date"])


# In[ ]:


df


# In[ ]:


df["Likes"]=df["Likes"].astype(int)


# In[ ]:


df["Likes"]


# # Task 5– Visualize and Analyze the data 

# First, visualize the data using the plotly module in a histogram plot of the Likes. This is accomplished
# using the method histogram, passing in the dataframe field ‘Likes’ as in x.
# In order to have the histogram show up in the output.

# In[ ]:


get_ipython().system('pip install plotly')
import plotly.express as px


# First, visualize the data using the plotly module in a histogram plot of the Likes. This is accomplished
# using the method histogram, passing in the dataframe field ‘Likes’ as in x.
# In order to have the histogram show up in the output, use the MathPlotLib.pyplot’s show merthod.

# In[ ]:


fig=px.histogram(df,x="Likes",nbins=20,barmode="group",hover_data="Category",title="Histogram plot of the Likes")
fig.show()


# In[ ]:


Second, visualize the same graph:data using the matplotlib module in a histogram plot of the Likes. This is accomplished
using the method histogram, passing in the dataframe field ‘Likes’ as in x.
In order to have the histogram show up in the output.


# In[ ]:


plt.hist(x="Likes",data=df,bins=20,color="skyblue",histtype='barstacked',label="Count",orientation="vertical")
plt.xlabel("Likes",color="r",size=12)
plt.ylabel("Counts",color="r",size=12)
plt.title("Histogram plot of the Likes",color="r",size=18)
plt.legend()
plt.show()


# To visualize the data using the plotly module in a box plot of the "Category" and "Likes". This is accomplished
# using the method box, passing in the dataframe field ‘Category’ as in x & 'Likes' as in y.
# In order to have the boxplot show up in the output.Now, create a boxplot with the x axis as ‘Category’, and the y axis as ‘Likes’.

# In[ ]:


fig=px.box(df,x="Category", y="Likes",color="Category",boxmode="overlay",title="Graph : Category vs Likes")
fig.show()


# In[ ]:


To visualize the data using the seaborn module in a box plot of the "Category" and "Likes". This is accomplished
using the method boxplot, passing in the dataframe field ‘Category’ as in x & 'Likes' as in y.
In order to have the boxplot show up in the output.Now, create a boxplot with the x axis as ‘Category’, and the y axis as ‘Likes’.


# In[ ]:


sns.boxplot(x="Category", y="Likes",data=df,notch=True)
plt.xlabel("Category",color="r",size=12)
plt.ylabel("Likes",color="r",size=12)
plt.title("Graph : Category vs Likes",color="r",size=18)
plt.show()


# Now perform some statistics on the data. First, print out the mean of the ‘Likes’ category.

# In[ ]:


print("The mean of the ‘Likes’ category  is :")
df["Likes"].mean()


# The dataframe’s groupby method to print out the mean of each Category ‘Likes’

# In[ ]:


print("The mean of each category Likes is : ")
df.groupby("Category")["Likes"].mean()


# # Task 5 – Describe Conclusions

# # Conclusion:
# 
# Throughout this portfolio project, I engaged in a comprehensive data analysis and visualization process, showcasing my critical thinking and problem-solving skills. I followed a structured approach to generate random data, clean and preprocess it, and then perform insightful visualizations and statistical analysis. The project allowed me to gain valuable insights into the dataset and present the findings effectively.
# 
# 

# # Key Findings:
# 
# Data Generation: By creating a synthetic dataset with random categories and likes, I was able to simulate social media data realistically. This process enabled me to perform meaningful analysis and draw relevant conclusions.
# 
# Data Cleaning: Ensuring data integrity was essential, and I effectively handled null values and duplicates. Converting the 'Date' field to a datetime format and 'Likes' to integers provided a solid foundation for further analysis.
# 
# Data Visualization: The use of Seaborn and Matplotlib allowed me to present the data through insightful histogram plots and boxplots. These visualizations revealed trends, patterns, and the spread of likes across different categories.
# 
# Statistical Analysis: Calculating the mean of 'Likes' provided an overall average, and the 'groupby()' method helped derive the mean of likes for each category. This statistical analysis shed light on the popularity of different categories in the dataset

# # Key Takeaways:
# 
# Through this project, I learned valuable skills in data manipulation, visualization, and analysis using Python. The combination of libraries like Pandas, NumPy, Seaborn, and Matplotlib allowed me to efficiently perform data analysis tasks and present results in a visually appealing manner.

# # What Sets This Portfolio Project Apart:
# 
# This portfolio project showcases my ability to handle synthetic data, clean and preprocess it for analysis, and perform in-depth visualizations and statistical computations. The inclusion of multiple data visualization techniques, such as histograms and boxplots, demonstrates my proficiency in presenting data insights clearly.
# 
# 

# # Improvements and Future Enhancements:
# 
# While the project serves as a strong foundation, there are areas for potential improvements and enhancements. For instance, incorporating interactive visualizations using libraries like Plotly could offer a more dynamic and engaging user experience. Additionally, conducting hypothesis testing or more advanced statistical analysis would allow for deeper insights into the data and its patterns.    how to ad these in jupyer notebook   same
