
# coding: utf-8

# # 분석 사례 1
# 
# NCSOFT 사내 식당 주문 기록
# "어느 코너에 줄을 서야 할까?"
# 

# In[1]:

import pandas


# 식당 주문 기록 엑셀파일 읽어오기

# In[19]:

restaurant = pandas.read_excel('share/data/food_order.xlsx')


# In[20]:

restaurant[:3]


# In[7]:

restaurant[-3:]


# In[8]:

type(restaurant)


# 주문 기록에서 특정한 날짜나 날짜 범위를 선택하고 싶다면?
# 예) 2014년 9월

# In[22]:

restaurant = restaurant.set_index('date')


# In[25]:

restaurant2014 = restaurant.ix['2014']


# In[26]:

restaurant2014.to_excel('식당 주문 2014.xlsx')


# 열이 너무 많다! 원하는 열만 선택하기

# In[39]:

columnSelect = ['menu', 'corner', 'dine_type', 'use_count']
restaurant = restaurant[columnSelect]


# In[68]:

restaurant[:3]


# In[71]:

restaurant[['메뉴', '코너']]


# 열 제목 변경
# 

# In[46]:

columnName = {'menu': '메뉴', 'corner':'코너', 'use_count': '주문수량', 'dine_type': '시간대'}


# In[47]:

restaurant.rename(columns=columnName)[:3]


# In[50]:

restaurant = restaurant.rename(columns=columnName)


# In[52]:

restaurant[:3]


# 정리한 결과가 마음에 든다면 중간 결과를 저장해 두는 것이 도움이 됨! (엑셀이나 파일 등으로)

# In[57]:

restaurant.to_excel('식당.xlsx')


# In[84]:

restaurant = pandas.read_excel('식당.xlsx')
restaurant[:3]


# In[63]:

test =restaurant.set_index(['date', '메뉴'])


# In[74]:

test.ix[['2014']['판모밀정식']]


# In[85]:

restaurant = restaurant.set_index('date')
restaurant[:3]


# 어느 코너가 어느 시간에 인기가 많을 까?
# 
# 1. 각 코너별 시간대별 주문수량의 평균
# 

# In[87]:

restaurant.pivot_table('주문수량', index='코너', columns='시간대')


# In[90]:

코너별시간대별_주문평균 = restaurant.pivot_table('주문수량', index='코너', columns='시간대')


# aggfunc= 집계함수

# In[108]:

restaurant.pivot_table('주문수량', index='코너', columns='시간대', aggfunc='std')


# 코너별 합계가 궁금할때!

# In[97]:

열선택 =['breakfast', 'lunch', 'dinner']
코너별시간대별_주문평균 = 코너별시간대별_주문평균[열선택]


# 각 시간대별 합계

# In[99]:

코너별시간대별_주문평균.sum() # default 열단위


# In[101]:

코너별시간대별_주문평균.sum(axis=1) # 줄단위


# In[103]:

코너별시간대별_주문평균['합계'] = 코너별시간대별_주문평균.sum(axis=1)


# In[104]:

코너별시간대별_주문평균


# In[105]:

코너별시간대별_주문평균.sort_values(by='합계')


# In[109]:

코너별시간대별_주문평균.sort_values(by='합계', ascending=False)


# 그래프로 출력해서 보면 더 잘보임

# In[110]:

get_ipython().magic('matplotlib inline')


# In[116]:

열선택 =['breakfast', 'lunch', 'dinner']
코너별시간대별_주문평균[열선택].plot(kind='bar', stacked=True)
코너별시간대별_주문평균[열선택].plot(kind='barh')
코너별시간대별_주문평균[열선택].plot(kind='barh', stacked=True)


# In[118]:

코너별시간대별_주문평균.to_excel('코너별시간대별_주문평균.xlsx')


# In[120]:

restaurant.reset_index()


# In[122]:

restaurant.set_index(['date', '메뉴'])

