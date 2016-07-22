
# coding: utf-8

# 통계와 그래프

# In[2]:

import pandas as pd


# In[4]:

get_ipython().magic('matplotlib inline')


# 그래프 노트북 출력 설정
# 

# In[35]:

월간재무 = pd.read_excel('share/data/profit.xlsx')


# In[36]:

월간재무 = 월간재무.rename(columns={'월':'month', '이익':'benefit'})


# In[27]:

월간재무.plot()


# In[28]:

월간재무.set_index('month').plot()


# 글씨체 설정
# 

# In[29]:

''' python
import matplotlib as mpl
mpl.rcParams['font.family']='batang'
'''


# In[37]:

월간재무 = 월간재무.set_index('month')
월간재무.plot(ylim=(0.0, 2.5))


# In[42]:

게임사용자 = pd.read_excel('share/data/game_users.xlsx')


# In[ ]:




# In[43]:

게임사용자 = 게임사용자.set_index('장르')


# In[45]:

게임사용자


# In[47]:

게임사용자['누적사용자수'].plot(kind='pie', subplots=True)


# In[51]:

게임사용자['만족도'].plot(kind='barh')


# 비교는 절대값 뿐만 아니라 도수가 중요합니다.

# In[52]:

만족도수 = 게임사용자['누적사용자수'] * 게임사용자['만족도']


# In[54]:

만족도수.plot(kind='barh')


# ## 도수와 평균
# 

# In[55]:

평점 = pd.read_excel('share/data/ratings.xlsx')


# In[57]:

평점[:3]


# In[58]:

len(평점)


# 구간에 따라 데이터 분류

# In[59]:

구간구분 = [0, 20, 40, 60, 80, 100]


# In[62]:

평점분류 = pd.cut(평점['평점'], 구간구분)


# In[67]:

평점도수 = 평점분류.value_counts()


# In[70]:

평점도수 = 평점도수.sort_index()


# In[75]:

평점도수.plot(kind='bar')


# ## 히스토그램
# 도수분포표

# In[77]:

평점.hist(bins=5)


# In[79]:

게임시간 = pd.read_excel('share/data/playtime.xlsx')
게임시간[:5]


# In[81]:

게임시간.hist()


# 히스토그램을 비율로 표현하기

# In[82]:

게임시간.hist(normed=True)

