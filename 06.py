
# coding: utf-8

# ## 중심적 경향 측정
# "평균"이 평균인가?

# In[1]:

import pandas as pd


# In[4]:

get_ipython().magic('matplotlib inline')


# In[5]:

연령 = pd.read_excel('share/data/ages.xlsx')
연령[:5]


# In[8]:

연령.mean()


# 45세 미만의 연령대만 선택

# In[13]:

연령[연령 < 45].mean()


# In[15]:

(연령['연령'] < 45).value_counts()


# ## 중앙값 
# 전체 자료를 딱 절반으로 나누는 기준값

# In[17]:

연령.median()


# In[19]:

수영강습생 = pd.read_excel('share/data/swim_class.xlsx')


# 이 강좌 내가 들어도 될까?
# 

# In[21]:

수영강습생.mean()


# In[23]:

수영강습생.median()


# In[25]:

수영강습생.hist()


# ## 최빈값
# 가장 빈번하게 등장하는 값

# In[27]:

수영강습생.mode()


# ## 중심적 경향의 변화
# 평균 연봉과 연봉인상

# In[29]:

연봉 = pd.read_excel('share/data/salary.xlsx')


# In[32]:

연봉[:3]


# In[38]:

연봉.hist(bins=30)


# In[37]:

연봉.mean()


# In[40]:

연봉.median()


# In[42]:

연봉.mode()


# In[44]:

연봉.max()


# In[46]:

연봉.min()


# 평균연봉 15%인상안

# In[48]:

(연봉 * 1.15).mean()


# In[50]:

(연봉 * 1.15).median()


# In[58]:

(연봉 * 1.15).mode()


# In[59]:

(연봉 * 1.15).max()


# 1000 만원 인상

# In[54]:

(연봉 + 1000).mean()


# In[56]:

(연봉 + 1000).median()


# In[60]:

(연봉 + 1000).mode()


# In[62]:

(연봉 + 1000).max()


# # 분포와 범위

# In[63]:

게임당점수 = pd.read_excel('share/data/player_stats.xlsx')


# In[64]:

게임당점수


# In[66]:

게임당점수.mean()


# In[68]:

게임당점수.median()


# In[72]:

def 범위구하기(수치) :
    return 수치.max() - 수치.min()


# In[73]:

게임당점수.apply(범위구하기)

