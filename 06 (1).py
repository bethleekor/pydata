
# coding: utf-8

# ## 중심적 경향 측정
# "평균"이 평균인가?

# In[4]:

import pandas as pd


# In[5]:

get_ipython().magic('matplotlib inline')


# In[6]:

연령 = pd.read_excel('share/data/ages.xlsx')
연령[:5]


# In[7]:

연령.mean()


# 45세 미만의 연령대만 선택

# In[8]:

연령[연령 < 45].mean()


# In[9]:

(연령['연령'] < 45).value_counts()


# ## 중앙값 
# 전체 자료를 딱 절반으로 나누는 기준값

# In[10]:

연령.median()


# In[11]:

수영강습생 = pd.read_excel('share/data/swim_class.xlsx')


# 이 강좌 내가 들어도 될까?
# 

# In[12]:

수영강습생.mean()


# In[13]:

수영강습생.median()


# In[14]:

수영강습생.hist()


# ## 최빈값
# 가장 빈번하게 등장하는 값

# In[15]:

수영강습생.mode()


# ## 중심적 경향의 변화
# 평균 연봉과 연봉인상

# In[16]:

연봉 = pd.read_excel('share/data/salary.xlsx')


# In[17]:

연봉[:3]


# In[18]:

연봉.hist(bins=30)


# In[19]:

연봉.mean()


# In[20]:

연봉.median()


# In[21]:

연봉.mode()


# In[22]:

연봉.max()


# In[23]:

연봉.min()


# 평균연봉 15%인상안

# In[24]:

(연봉 * 1.15).mean()


# In[25]:

(연봉 * 1.15).median()


# In[26]:

(연봉 * 1.15).mode()


# In[27]:

(연봉 * 1.15).max()


# 1000 만원 인상

# In[28]:

(연봉 + 1000).mean()


# In[29]:

(연봉 + 1000).median()


# In[30]:

(연봉 + 1000).mode()


# In[31]:

(연봉 + 1000).max()


# # 분포와 범위

# In[32]:

게임당점수 = pd.read_excel('share/data/player_stats.xlsx')


# In[ ]:




# In[33]:

게임당점수


# In[34]:

게임당점수.mean()


# In[35]:

게임당점수.median()


# In[40]:

def 범위구하기(수치) :
    return 수치.max() - 수치.min()


# 함수가 각 열에 대해서 적용됩니다.

# In[41]:

게임당점수.apply(범위구하기)


# 특이한 값 하나를 설정해 보겠습니다.

# In[42]:

게임당점수.ix[10, '이성주'] = 50
게임당점수[-2:]


# 이상치가 포함되면 범위가 크게 달라진다.

# In[44]:

게임당점수.apply(범위구하기)


# ## 사분범위
# 
# 전체를 균등하게 4개로 나누어, 중앙의 두 개만 취해 이상치를 제거하는 표준화된 방법
# 
# "이상한 값입니다."
# "왜?"
# "사분범위 밖이니까요"
# 

# In[55]:

print(pd.qcut(게임당점수['이성주'], 4))

사분위수 = pd.qcut(게임당점수['이성주'], 4).value_counts().sort_index()
사분위수


# In[52]:

사분범위 = 사분위수.index[1:-1]
사분범위


# In[53]:

범위여부 = pd.qcut(게임당점수['이성주'], 4).isin(사분범위)
범위여부


# In[56]:

사분범위내점수 = 게임당점수['이성주'][범위여부]
사분범위내점수


# In[57]:

사분범위내점수.mean()


# In[58]:

사분범위내점수.median()


# In[59]:

범위구하기(사분범위내점수)


# In[60]:

게임당점수.plot(kind='box')


# In[61]:

게임당점수.plot(kind='box', vert=False)


# 연습
# 
# 기상청의 날씨 데이터는 /share/data/weather.xlsx에 담겨 있다.
# 
# 1. 서울과 수원의 일 평균 온도의 중앙값 산출
# 2. 서울과 수원의 일 평균 온도의 범위 산출 (max - min)
# 

# In[ ]:




# In[62]:

날씨 = pd.read_excel('share/data/weather.xlsx')


# In[63]:

날씨[:3]


# In[69]:

날씨색인 = 날씨.set_index('location')


# In[95]:

서울날씨 = 날씨색인.ix['seoul']


# In[96]:

서울날씨['avgTemp'].median()


# In[86]:

지역 = 날씨['location']
지역[:3]


# In[88]:

서울여부 = 지역 == 'seoul'


# In[97]:

서울일평균 = 날씨[서울여부]['avgTemp']
서울일평균.median()


# In[98]:

서울일평균.max() - 서울일평균.min()


# In[74]:

수원날씨 = 날씨색인.ix['suwon']


# In[75]:

수원날씨['avgTemp'].median()


# In[99]:

수원여부 = 지역 == 'suwon'


# In[102]:

수원일평균 = 날씨[수원여부]['avgTemp']
수원일평균.median()


# In[103]:

수원일평균.max() - 수원일평균.min()


# In[78]:

pd.qcut(서울날씨['avgTemp'], 4).value_counts()


# In[79]:

pd.qcut(수원날씨['avgTemp'], 4).value_counts()


# 연습
# 
# 사용자의 연령대 데이터는 share/data/ages.xlsx에 대해 다음을 수행
# 1. 범위산출
# 2. 평균과 사분범위내 평균 비교

# In[80]:

연령 = pd.read_excel('share/data/ages.xlsx')


# In[81]:

연령[:3]


# 분산과 표준편차

# In[104]:

게임당점수.var()


# In[105]:

게임당점수.std()


# ## 표준 점수
# 
# "평소에 비해 얼마나 잘한 걸까?"
# 
# $$표준점수 Z = \frac{x-\mu}-{\sigma}, \mu:평균, \sigma: 표준편차

# In[111]:

게임표준점수 = (게임당점수 - 게임당점수.mean()) / 게임당점수.std() #열별로 계산됨


# In[112]:

게임표준점수


# 0 늘하던대로, - 하던것 보다 못함, + 하던것보다 잘함
# 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[106]:

게임당점수


# In[ ]:




# In[ ]:




# In[ ]:



