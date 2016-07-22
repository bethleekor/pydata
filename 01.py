
# coding: utf-8

# In[8]:

hello = 'hello world'
print (hello)


# In[9]:

hello += ' nice to meet to you'
print(hello)

### 경로 파일 읽어서 한줄씩 출력
1. 각 줄의 필드는 쉼표로 구분되어 이다. 각 줄의 두번째 필드의 값만 출력
# In[10]:

location = 'share/data/geeks.csv'


# In[11]:

file = open(location, 'r', encoding='utf-8')


# In[12]:

for line in file :
    print(line)
file.close()


# In[ ]:

file = open(location, 'r', encoding='utf-8')

for line in file :
    columns = line.split(',')
    print(columns[1])
file.close()


# ### 커널

# In[ ]:

trueLove = True
while trueLove:
    pass


# In[ ]:



