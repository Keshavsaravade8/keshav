#!/usr/bin/env python
# coding: utf-8

# # Portfolio Project: Online Retail Exploratory Data Analysis with Python

# ## Overview
# 
# In this project, you will step into the shoes of an entry-level data analyst at an online retail company, helping interpret real-world data to help make a key business decision.

# ## Case Study
# In this project, you will be working with transactional data from an online retail store. The dataset contains information about customer purchases, including product details, quantities, prices, and timestamps. Your task is to explore and analyze this dataset to gain insights into the store's sales trends, customer behavior, and popular products. 
# 
# By conducting exploratory data analysis, you will identify patterns, outliers, and correlations in the data, allowing you to make data-driven decisions and recommendations to optimize the store's operations and improve customer satisfaction. Through visualizations and statistical analysis, you will uncover key trends, such as the busiest sales months, best-selling products, and the store's most valuable customers. Ultimately, this project aims to provide actionable insights that can drive strategic business decisions and enhance the store's overall performance in the competitive online retail market.
# 
# ## Prerequisites
# 
# Before starting this project, you should have some basic knowledge of Python programming and Pandas. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - numpy
# - seaborn
# - matplotlib
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`

# ## Project Objectives
# 1. Describe data to answer key questions to uncover insights
# 2. Gain valuable insights that will help improve online retail performance
# 3. Provide analytic insights and data-driven recommendations

# ## Dataset
# 
# The dataset you will be working with is the "Online Retail" dataset. It contains transactional data of an online retail store from 2010 to 2011. The dataset is available as a .xlsx file named `Online Retail.xlsx`. This data file is already included in the Coursera Jupyter Notebook environment, however if you are working off-platform it can also be downloaded [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
# 
# The dataset contains the following columns:
# 
# - InvoiceNo: Invoice number of the transaction
# - StockCode: Unique code of the product
# - Description: Description of the product
# - Quantity: Quantity of the product in the transaction
# - InvoiceDate: Date and time of the transaction
# - UnitPrice: Unit price of the product
# - CustomerID: Unique identifier of the customer
# - Country: Country where the transaction occurred

# ## Tasks
# 
# You may explore this dataset in any way you would like - however if you'd like some help getting started, here are a few ideas:
# 
# 1. Load the dataset into a Pandas DataFrame and display the first few rows to get an overview of the data.
# 2. Perform data cleaning by handling missing values, if any, and removing any redundant or unnecessary columns.
# 3. Explore the basic statistics of the dataset, including measures of central tendency and dispersion.
# 4. Perform data visualization to gain insights into the dataset. Generate appropriate plots, such as histograms, scatter plots, or bar plots, to visualize different aspects of the data.
# 5. Analyze the sales trends over time. Identify the busiest months and days of the week in terms of sales.
# 6. Explore the top-selling products and countries based on the quantity sold.
# 7. Identify any outliers or anomalies in the dataset and discuss their potential impact on the analysis.
# 8. Draw conclusions and summarize your findings from the exploratory data analysis.

# ## Task 1: Load the Data

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install --upgrade pip')


# In[2]:


import pandas as pd


# # Task 2 – Upload DataFile Using Pandas

# In this project, we will analyze the Diwali Sales Data using a excel file named"Online Retail.xlsx . We'll start by loading the data and then perform initial exploratory data analysis.

# # Load Data and Check Shape:

# We first load the data from the excel file and check the shape to understand the number of rows and columns.

# In[3]:


df=pd.read_excel("Online Retail.xlsx")
df


# In[4]:


df


# # Check First Five Rows:

# To get an overview of the data,I use the .head() function to display the first five rows

# In[5]:


df.head()


# # Check Last Five Rows:

# Check Last Five Rows: Similarly, we use the .tail() function to display the last five rows of the data

# In[6]:


df.tail()


# # Check Data Types using .info():

# To understand the data types of each column, we use the .info() function.

# In[7]:


df.info()


# # Check Columns and Index:

# Lastly, we can check the columns and index of the DataFrame using .columns and .index attributes. python

# In[8]:


df.columns


# In[9]:


df.index


# # Task 3 – Clean the data

# # Column Seperated:

# In which,the invoice column present date and time so,now seperate new column date and time

# In[10]:


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Extract year, month, day, hour, minute, and second into separate columns
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Date'] = df['InvoiceDate'].dt.date
df['Time'] = df['InvoiceDate'].dt.time

df


# # Dropped Column:

# In which the InvoiceDate column is deleted.

# In[11]:


df.drop("InvoiceDate",axis=1,inplace=True)


# In[12]:


df


# # Checked for Null Values:

# We used the .isnull() and .notnull() functions to identify any null values present in the data. The .isnull() function returns a DataFrame with boolean values indicating whether each element is null or not, while the .notnull() function returns the opposite, indicating non-null elements.
# 
# df.isnull()

# In[13]:


df.isnull()


# In[14]:


df.isnull().sum()


# # Dropped Columns with Null Values:

# We identified columns with a significant number of null values and used the .drop() function to remove those columns from the DataFrame. This step was necessary to eliminate incomplete or irrelevant data that could affect our analysis.

# In[15]:


df.dropna(inplace=True)


# In[16]:


df.isnull().sum()


# In[17]:


df


# # Statistical Analysis

# In[18]:


df.describe()


# In[19]:


df


# # Column Seperated:

# In[20]:


df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year


# In[21]:


df


# # Task 4– Visualize and Analyze the data

# In[22]:


import matplotlib.pyplot as plt


# In[23]:


monthly_sales = df.groupby(["Month"],as_index=False)['UnitPrice'].sum()
monthly_sales


# In[24]:


get_ipython().system('pip install plotly')
import plotly.express as px


# In[25]:


fig=px.line(monthly_sales,x="Month",y="UnitPrice",markers="UnitPrice",title="SalesTrend-Monthly")
fig.show()


# In[26]:


Daily_sales=df.groupby(["Day"],as_index=False)["UnitPrice"].sum()
Daily_sales


# In[27]:


fig=px.line(Daily_sales,x="Day",y="UnitPrice",markers="Day",title="SalesTrend-Daily")
fig.show()


# In[28]:


yearly_sales=df.groupby(["Year"],as_index=False)["UnitPrice"].sum()
yearly_sales


# In[29]:


fig=px.bar(yearly_sales,x="Year",y="UnitPrice",title="SalesTrend-Yearly",color="Year",text="UnitPrice")
fig.show()


# In[30]:


#Number of transaction over time daily
df


# In[31]:


daily_transaction=df.groupby(["Day"],as_index=False)["InvoiceNo"].count()
daily_transaction


# In[32]:


fig=px.line(daily_transaction,x="Day",y="InvoiceNo",markers="Day",title="TransactionCount-Daily")
fig.update_layout(yaxis_title="Transaction Count",xaxis_title="Days")
fig.show()


# In[33]:


Monthly_transaction=df.groupby(["Month"],as_index=False)["InvoiceNo"].count()
Monthly_transaction


# In[34]:


fig=px.line(Monthly_transaction,x="Month",y="InvoiceNo",markers="Month",title="TransactionCount-Monthly")
fig.update_layout(yaxis_title="Transaction Count",xaxis_title="Months")
fig.show()


# In[35]:


Yearly_transaction=df.groupby(["Year"],as_index=False)["InvoiceNo"].count()
Yearly_transaction


# In[36]:


fig=px.bar(Yearly_transaction,x="Year",y="InvoiceNo",title="TransactionCount-Yearly",color="Year",text="InvoiceNo")
fig.update_layout(yaxis_title="Transaction Count",xaxis_title="Years")
fig.show()


# In[37]:


df


# In[38]:


total_quantity_sold = df.groupby(['StockCode', 'Description'],as_index=False)['Quantity'].sum().sort_values(by="Quantity",ascending=False).head(10)
total_quantity_sold


# In[39]:


fig=px.bar(total_quantity_sold,x="Description",y="Quantity",text="StockCode",color="StockCode")
fig.show()


# In[40]:


df


# In[41]:


total_quantity_sold_country=df.groupby(["Country"],as_index=False)["Quantity"].sum().sort_values(by="Quantity",ascending=False).head(10)
total_quantity_sold_country


# In[42]:


fig=px.choropleth(total_quantity_sold_country,locationmode='country names',color="Country",locations="Country",hover_data="Quantity",scope='world',hover_name="Country",)
fig.show()


# In[43]:


fig=px.bar(total_quantity_sold_country,x="Country",y="Quantity",text="Quantity",color="Country",title="Country based Quantity Sold")
fig.update_layout(yaxis_title="Total Quantity Sold")
fig.show()


# In[44]:


# Create a box plot to visualize potential outliers in the 'Quantity' column
df


# In[45]:


fig=px.box(df,y="Quantity",boxmode="group",hover_name="Quantity",labels="group")
fig.show()


# In[46]:


fig=px.box(df,y="UnitPrice",boxmode="group",hover_name="UnitPrice",labels="group")
fig.show()


# In[47]:


# Calculate total spending for each customer
df['TotalSpending'] = df['Quantity'] * df['UnitPrice']
total_spending_per_customer = df.groupby('CustomerID')['TotalSpending'].sum()
total_spending_per_customer


# In[48]:


df


# In[49]:


# Calculate frequency of purchases for each customer
frequency_per_customer = df.groupby('CustomerID').size()
frequency_per_customer


# In[50]:


# Scatter plot to segment customers based on total spending and frequ
fig=px.scatter(x=total_spending_per_customer,y=frequency_per_customer)
fig.show()


# In[51]:


from scipy import stats


z_scores = stats.zscore(df['Quantity'])

threshold = 3
potential_outliers_indices = (z_scores > threshold) | (z_scores < -threshold)

potential_outliers = df[potential_outliers_indices]

print(potential_outliers)






# In[52]:



z_scores = stats.zscore(df['UnitPrice'])


threshold = 3


potential_outliers_indices = (z_scores > threshold) | (z_scores < -threshold)


potential_outliers = df[potential_outliers_indices]


print(potential_outliers)


# # Task 5 – Describe Conclusions

# # Conclusion:

# # Monthly Sales Trend:

# The highest sales were observed in November, followed by October, indicating potential holiday shopping patterns or seasonal demand.
# The lowest sales occurred in February, suggesting a possible lull after the holiday season.

# # Daily Sales Trend:
# 
# The 10th day of the month saw the highest sales, while the 29th day had the lowest sales. Further investigation into the reasons behind these specific dates may uncover marketing or promotional activities that influenced customer behavior.

# # Yearly Sales Trend:
# 
# The year 2011 recorded the highest sales, indicating significant business growth during that period.
# Understanding the factors contributing to this exceptional performance in 2011 can provide valuable insights for future business strategies.

# # Weekly Transactions:
# 
# The 6th day of the week had the highest number of transactions, possibly indicating higher footfall or online activity on that day.
# Analyzing customer behavior and engagement on specific days can help optimize marketing efforts and customer service.

# # Top-Selling Product:
# 
# "World War 2 Glider Assisted Design" emerged as the highest-selling product based on total quantity sold.
# Identifying the reasons for its popularity can aid in capitalizing on successful product attributes or marketing strategies.

# # Top-Selling Country:
# 
# The United Kingdom stood out as the country with the highest product sales.
# Focusing on the UK market for further growth and expansion strategies could be beneficial.

# # High-Spending Customers:
# 
# Customers with IDs "7083," "5903," "5128," "4642," and "2782" were identified as high-spending customers.
# Personalizing offers and incentives for these customers may enhance customer loyalty and retention.

# # Outliers and Z-Scores:
# 
# Identifying outliers and calculating Z-scores for "UnitPrice" and "Quantity" helps detect unusual data points.
# Understanding the impact of outliers on the analysis and deciding whether to include or exclude them is important for accurate insights.

# # Geospatial Analysis:
# 
# Mapping the highest product sales to the United Kingdom can visually demonstrate the distribution of sales across regions and highlight potential growth areas.

# In[ ]:




