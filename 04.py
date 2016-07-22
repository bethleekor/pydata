
# coding: utf-8

# ### 분석사례 3
# "어떤 코너와 메뉴를 어떤 날씨에 더 선호할까?"

# In[2]:

import pandas as pd


# In[4]:

식당 = pd.read_excel('share/data/food_order.xlsx')
식당[:3]


# In[6]:

식당 = pd.read_excel('식당.xlsx')
식당[:3]


# In[8]:

날씨 = pd.read_excel('share/data/weather.xlsx')
날씨[:3]


# ### 연습
# 날씨 자료에서 다음을 수행하고, 결과를 '날씨.xlsx' 파일로 저장
# 
# 1. 'date', 'location', 'avgTemp', 'weather' 열 선택
# 2. 열 제목을 적절한 한국어 명칭으로 교체
# 

# In[19]:

정리컬럼 = ['date', 'location', 'avgTemp', 'weather']
날씨정리 = 날씨[정리컬럼]
날씨정리[:3]

정리날씨 = 날씨정리.rename(columns={'date': '날짜', 'location':'지역', 'avgTemp':'일평균온도', 'weather':'기상속성'})
정리날씨.to_excel('날씨.xlsx')

날씨 = 정리날씨


# In[23]:

날씨 = pd.read_excel('날씨.xlsx')
날씨[:3]


# "날씨에 다라 코너의 인기도가 달라질까?"

# In[26]:

수원날씨 = 날씨[날씨.지역 == 'suwon']
수원날씨[:3]


# 식당과 날씨 자료를 합치자

# In[29]:

식당날씨 = pd.merge(식당, 날씨, left_on='date', right_on='날짜')


# In[31]:

식당날씨[:3]


# 날씨에 따른 코너별 주문수량 집게

# In[34]:

식당날씨.pivot_table('주문수량', index='기상속성', columns='코너')


# In[36]:

식당날씨.pivot_table('주문수량', index='코너', columns='기상속성')

기상속성이 여전히 많으니까 눈비 여부로 나누자
# In[64]:

눈비여부 = 식당날씨.기상속성.str.contains('비|눈|소나기')
눈비여부[:3]


# In[65]:

눈비여부 = 눈비여부.replace({True:'rain snow', False:'not rain snow'})


# In[66]:

눈비여부.value_counts()


# In[67]:

코너별눈비별_주문평균 = 식당날씨.pivot_table('주문수량', index='코너', columns=눈비여부)


# In[59]:

get_ipython().magic('matplotlib inline')


# In[69]:

코너별눈비별_주문평균.plot(kind='barh')


# "기상에 따라 코너에 대한 선호도가 유의미하게 바뀔까?"
# 
# ===> 일단 각 코너의 주문량을 백분율로 만들어서 봐야겠다

# In[70]:

코너별눈비별_주문평균


# In[73]:

코너별합계 = 코너별눈비별_주문평균.sum(axis=1)
코너별합계


# In[76]:

코너별눈비별_주문비율 = 코너별눈비별_주문평균.div(코너별합계, axis=0)


# In[78]:

코너별눈비별_주문비율


# In[81]:

코너별눈비별_주문비율.plot(kind='barh', stacked=True)


# 기상에 따른 코너별 상대적 선호도를 (꼭) ㅇㄹ아야겠다면
# 눈비 오는 날 상대적으로 더 선호하는 코너?
# 

# In[85]:

비율평균 = 코너별눈비별_주문비율['rain snow'].mean()


# In[87]:

비율차 = 코너별눈비별_주문비율['rain snow'] - 비율평균


# In[90]:

비율차.sort_values().plot(kind='barh')


# In[92]:

식당날씨[:3]


# ### 연습
# 
# 날씨에 따라 야근 비율이 달라질까?
# --> 전체 코너의 저녁시간 주문량 평균을 날씨에 따라 구하고 비율을 비교

# In[120]:

식당날씨2 = pd.merge(식당, 날씨, left_on='date', right_on='날짜')
식당날씨2[:3]


# In[155]:

#식당날씨2 = 식당날씨.pivot_table('주문수량', index='시간대', columns=눈비여부)
#식당날씨2.plot(kind='barh')
#저녁여부 = 식당날씨.시간대.str.contains('dinner')
#시간대별 = 식당날씨2.set_index('시간대').groupby(눈비여부)


# In[159]:

시간대별눈비별_주문평균 = 식당날씨.pivot_table('주문수량', index='시간대', columns=눈비여부)
시간대별눈비별_주문평균.div(시간대별눈비별_주문평균.sum(1), axis=0)


# 요일에 따른 식당 이용율

# In[139]:

요일별 = 식당날씨.set_index('date').groupby(lambda 날짜: 날짜.weekday())

요일별[['주문수량']].mean().rename({0:'mon', 1:'tue', 2:'wed', 3:'thr', 4:'fri', 5:'sat', 6:'sun'}).plot()

