
# coding: utf-8

# ### 분석사례2
# "날씨가 어떤가요"

# In[2]:

import pandas as pd


# In[8]:

날씨 = pd.read_excel('share/data/weather.xlsx')


# In[10]:

날씨[:3]


# In[12]:

len(날씨)


# In[14]:

날씨.info()


# 열에 들어 있는 값들의 종류와 등장하는 횟수, 즉 도수 집계

# In[16]:

지역 = 날씨['location']


# In[18]:

지역.value_counts()


# 지역별로 날씨 자료선택

# In[20]:

지역[:3]


# In[22]:

서울인가 = 지역 == 'seoul'


# In[24]:

서울날씨 = 날씨[서울인가]


# In[25]:

서울날씨[-3:]


# In[26]:

서울날씨['location'].value_counts()


# 수원 지역 날씨만 선택하여 수원날시에 저장

# In[27]:

수원인가 = 지역 == 'suwon'


# In[28]:

수원날씨 = 날씨[수원인가]


# In[29]:

수원날씨[-3:]


# In[31]:

수원날씨['location'].value_counts()


# In[49]:

수원평균 = 수원날씨.sum()
수원평균
#수원일평균온도 = 수원날씨['avgTemp']
#수원더운날 = 수원일평균온도 > 수원평균
#수원더운날씨 = 수원날씨[수원더운날]
#수원더운날씨[:3]
#수원더운날씨 = 수원날씨[수원날씨['avgTemp']> 수원평균]


# 요일별 지역별 날씨

# 요일별 지역별 일평균기온의 (평균)

# In[44]:

날씨.pivot_table('avgTemp', index='weekDay', columns='location')


# In[45]:

요일별지역별_평균온도 = 날씨.pivot_table('avgTemp', index='weekDay', columns='location')


# In[46]:

get_ipython().magic('matplotlib inline')


# In[47]:

요일별지역별_평균온도.plot()


# 그런데 만약 요일 정보를 다음 열이 없었다면?

# In[50]:

날씨.date[:3]


# In[55]:

요일알아내기 = lambda 날짜: 날짜.weekday()
요일 = 날씨.date.map(요일알아내기)


# In[54]:

요일[:3]


# In[69]:

def 요일알아내기(날짜):
    return 날짜.weekday()

요일 = 날씨.date.map(요일알아내기)


# In[70]:

요일[:3]


# In[71]:

요일매핑 = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}


# In[72]:

요일 = 요일.map(요일매핑)


# 추출한 요일 정보를 추출하고, 분류의 기준으로 활용하기

# In[74]:

날씨.pivot_table('avgTemp', index=요일, columns='location')


# ### 연습
# 2016-07-15와 같은 형식의 날짜에 대해 다음을 수행
# 1. 연도별 지역별 평균 기온
# 2. 월별 지역별 평균기온
# 3. 연도별월별 지역별 평균기온

# In[75]:

def 연도추출(날짜):
    return 날짜.year


# In[82]:

첫날 = 날씨.date[0]
첫날.year


# In[83]:

첫날.month


# In[86]:

연도 = 날씨.date.map(연도추출)

연도별지역별_평균기온 = 날씨.pivot_table('avgTemp', index=연도, columns='location')
연도별지역별_평균기온[:3]


# In[88]:

def 월추출(날짜) :
    return 날짜.month


# In[90]:

월 = 날씨.date.map(월추출)

월별지역별평균기온 =  날씨.pivot_table('avgTemp', index=월, columns='location')
월별지역별평균기온[:3]


# In[113]:

def 연도월추출(날짜) :
    return '{}-{:02d}'.format(날짜.year, 날짜.month)


# In[116]:

연도월 = 날씨.date.map(연도월추출)

연도별월별지역별평균기온 =  날씨.pivot_table('avgTemp', index=연도월, columns='location')
연도별월별지역별평균기온[:3]


# In[118]:

날씨[:3]


# In[122]:

날씨['weather'][:3]


# In[124]:

날씨.weather[:3] #컬럼명에 띄어쓰기가 없는 경우에 가능


# In[128]:

기상서술도수 = 날씨.weather.value_counts()


# In[127]:

get_ipython().magic('matplotlib inline')


# In[131]:

기상서술도수[:5].plot(kind='barh')


# "눈비가 온 날과 그렇지 않은 날로 딱 두개로 분류했으면 좋겠는데 ..."

# In[136]:

눈비여부 = 날씨.weather.str.contains('비|눈|소나기')
눈비여부[:3]


# In[140]:

눈비도수 = 눈비여부.value_counts()
눈비도수


# In[143]:

눈비비율 = 눈비도수[True]/눈비도수.sum()*100
눈비비율


# 눈비 온 날과 그렇지 않은 날 지역별 평균 기온

# In[147]:

지역별눈비여부별_평균기온 = 날씨.pivot_table('avgTemp', index='location', columns=눈비여부)
지역별눈비여부별_평균기온 = 지역별눈비여부별_평균기온.rename(columns={False:'안옴', True:'눈비'})


# In[149]:

지역별눈비여부별_평균기온


# In[150]:

지역별눈비여부별_평균기온.plot(kind='bar')

