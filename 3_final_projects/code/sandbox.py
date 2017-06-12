
# coding: utf-8

# ##### meta

# <span style="color:red">word</span>
# <span style="color:red"></span>

# # Required Modules

# In[112]:

import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# # <span style="color:green">Load file Data</span>

# In[51]:

# 441.8 MB
all_loan_data = pd.read_csv("../assets/lending-club-loan-data/loan.csv"
                            ,low_memory=False)


# In[53]:

# 21 KB
data_dictionary = pd.read_excel("../assets/lending-club-loan-data/LCDataDictionary.xlsx")


# # <span style="color:blue">Basic Explorations</span>

# In[54]:

all_loan_data.head()


# In[55]:

all_loan_data.shape


# ### above shows 800k+ rows with 74 columns

# In[56]:

all_col_list = ' '.join(all_loan_data.columns).split(' ')
for col_name in all_col_list:
    if all_col_list.index(col_name) % 4 == 0:
        print (col_name,'\n',end='')
    else:
        print (col_name,end='   ')


# In[57]:

a1000 = ' '.join(all_loan_data.columns).split(' ')
a1000 = sorted(a1000)
# print (a1000)

for col_name in a1000:
    if a1000.index(col_name) % 4 == 0:
        print (col_name,'\n',end='')
    else:
        print (col_name,end='   ')


# ## below shows data dictionary contents

# In[58]:

data_dictionary


# In[59]:

pd.set_option("display.width",500)
pd.set_option("max_colwidth",500)
pd.set_option("max_rows",200)
data_dictionary.sort_values('LoanStatNew')


# ## Interesting columns
# 
# annual_inc,   annual_inc_joint,   application_type
# delinq_2yrs,   desc,   dti,   dti_joint,   earliest_cr_line,   emp_length,   emp_title
# funded_amnt,   grade,   home_ownership,   installment
# ### int_rate,   loan_amnt,   loan_status
# mths_since_last_delinq,   open_acc,   out_prncp,   purpose,   revol_bal
# #### revol_util  <-- utilization rate is a misleading percentage
# sub_grade,   term,   total_acc,   total_rec_late_fee,   total_rec_prncp

# In[60]:

print(all_loan_data.iloc[4096])


# In[61]:

pd.set_option("max_colwidth",80)
pd.set_option("max_rows",60)


# In[62]:

all_loan_data['loan_status'].unique()


# In[63]:

loan_status_list = ','.join(all_loan_data['loan_status'].unique()).split(',')
loan_status_list


# ## What is the difference between Default and Charge-off?

# http://www.lendacademy.com/the-difference-between-a-default-and-a-charge-off-at-lending-club/
# 
# <h3> At Lending Club a loan moves from late into default before it is charged off whereas at Prosper there is no intermediate category, notes just go from late to charged off.
# <br><br>
# Why is there this intermediate category at Lending Club? When I asked this question they provided this as an official response:
# </h3>
# <blockquote cite="http://www.lendacademy.com/the-difference-between-a-default-and-a-charge-off-at-lending-club/">
# In general, a note goes into Default status when it is 121 or more days past due.  When a note is in Default status, Charge Off occurs no later than 150 days past due (i.e. No later than 30 days after the Default status is reached) when there is no reasonable expectation of sufficient payment to prevent the charge off.  However, bankruptcies may be charged off earlier based on date of bankruptcy notification.
# </blockquote>
# 
# 

# In[64]:

all_loan_data[all_loan_data['loan_status']=='Fully Paid']


# <h3>
# <span style="color:#0099ff"> Above, we have around 25% (200k+) observations where the loan was paid in full.
# <br>This is the outcome we want to predict.
# </span>

# ## <span style="color:green">Let's get distinct values for all of our interesting columns
# </span>
# 
# ## Interesting columns
# 
# annual_inc,   annual_inc_joint,   application_type
# delinq_2yrs,   desc,   dti,   dti_joint,   earliest_cr_line,   emp_length,   emp_title
# funded_amnt,   grade,   home_ownership,   installment
# ### int_rate,   loan_amnt,   loan_status
# mths_since_last_delinq,   open_acc,   out_prncp,   purpose,   revol_bal
# #### revol_util  <-- utilization rate is a misleading percentage
# sub_grade,   term,   total_acc,   total_rec_late_fee,   total_rec_prncp

# In[65]:

col_of_interest = ['annual_inc',   'annual_inc_joint',   'application_type',
'delinq_2yrs',   'desc',   'dti',   'dti_joint',
'earliest_cr_line',   'emp_length',   'emp_title',
'funded_amnt',   'grade',   'home_ownership',   'installment',
'int_rate',   'loan_amnt',   'loan_status',
'mths_since_last_delinq',   'open_acc',   'out_prncp',   'purpose',   'revol_bal',
'sub_grade',   'term',   'total_acc',   'total_rec_late_fee',   'total_rec_prncp']

distinct_dictionary = {}


# In[66]:

for col in col_of_interest:
    findu = all_loan_data[col].unique()
    # print ("*** {} *** :\t {}".format(col,findu))
    findu = [str(x) for x in findu]
    makeulist = ','.join(list(findu)).split(',')
    distinct_dictionary[col] = makeulist

#a = all_loan_data['annual_inc'].unique()
#b = ','.join(a).split(',')


# In[67]:

print (distinct_dictionary.keys())


# In[125]:

kn = list(distinct_dictionary.keys())
k0 = kn[0]
k1 = kn[1]
k2 = kn[2]
k3 = kn[3]
k4 = kn[4]
k5 = kn[5]
k6 = kn[6]
k7 = kn[7]
k8 = kn[8]
k9 = kn[9]
k10 = kn[10]
k11 = kn[11]
k12 = kn[12]
k13 = kn[13]
k14 = kn[14]
k15 = kn[15]
k16 = kn[16]
k17 = kn[17]
k18 = kn[18]
k19 = kn[19]
k20 = kn[20]
k21 = kn[21]
k22 = kn[22]
k23 = kn[23]
k24 = kn[24]
k25 = kn[25]
k26 = kn[26]


# In[126]:

distinct_dictionary[k4]


# In[127]:

len (distinct_dictionary.keys())


# In[128]:

# print (k0,'\n',sorted(distinct_dictionary[k0]),'\n')
inted = [float(string_number) for string_number in distinct_dictionary[k0]]
inted2 = [int(x) for x in inted]
inted2 = sorted(inted2)
#print(sorted(distinct_dictionary[k0]))
intedf = pd.DataFrame(inted2)
intedf.describe()


# In[129]:

intedf.head()


# In[130]:

intedf.tail()


# In[ ]:




# In[133]:

print (k1,'\n',distinct_dictionary[k1],'\n')

print (k2,'\n',distinct_dictionary[k2],'\n')

print (k3,'\n',distinct_dictionary[k3],'\n')

print ('{},\n,distinct_dictionary[{}],\n'.format(k4,distinct_dictionary[k4]))


# In[132]:

for x in [.2,.4,.6,.8,1]:
    print (intedf.quantile(x))


# In[1]:

intedf.plot(kind='box')


# In[119]:

k14 = list(distinct_dictionary.keys())[0]
k15 = list(distinct_dictionary.keys())[1]
k16 = list(distinct_dictionary.keys())[2]
k17 = list(distinct_dictionary.keys())[3]
k18 = list(distinct_dictionary.keys())[4]
k19 = list(distinct_dictionary.keys())[5]
k20 = list(distinct_dictionary.keys())[6]
k21 = list(distinct_dictionary.keys())[7]
k22 = list(distinct_dictionary.keys())[8]
k23 = list(distinct_dictionary.keys())[9]
k24 = list(distinct_dictionary.keys())[10]
k25 = list(distinct_dictionary.keys())[11]
k26 = list(distinct_dictionary.keys())[12]
k27 = list(distinct_dictionary.keys())[13]

print ('{},\n,distinct_dictionary[{}],\n'.format(k4))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



