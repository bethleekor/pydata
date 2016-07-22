
# coding: utf-8

# In[1]:

import pandas as pd


# In[4]:

ncgames = pd.read_excel('share/data/ncgames.xlsx')
ncgames


# ## Series
# 
# 일련의 값을 담은 자료구조
# 

# In[7]:

제목 = ncgames['제목'] # ncgames[['제목']]
제목


# In[8]:

type(제목)


# In[9]:

type(ncgames)


# In[10]:

제목[0]


# In[11]:

제목.index


# In[12]:

제목.values


# In[13]:

ncgames


# In[16]:

ncgames = ncgames.set_index('제목')


# In[17]:

ncgames['장르']


# 색인화된 열은 더이상 열이 아님

# In[18]:

ncgames.set_index('제목')


# In[21]:

장르 = ncgames['장르']
장르


# 시리즈 생성
# 
# 1. 데이터프레임의 단일 열 또는 행 선택
# 1. 직접생성

# In[22]:

ncgames[['장르', '플랫폼']]


# In[23]:

pd.Series({'블레이드 앤 소울' : 'MMORPG'})


# #### 연습
# 
# ncgames 장르 열의 값을 직접 시리즈로 생성

# In[24]:

내장르 = pd.Series({'리니지':'MMORPG', '리니지2': 'MMORPG'})
내장르


# In[25]:

pd.Series(['MMORPG']*5, 
          index=['리니지', '리니지2', '히어로', '길드워', '블소'])


# In[26]:

장르['리니지']


# In[27]:

장르[['리니지', '아이온']]


# In[28]:

장르[:]


# 정수 색인이 아닌 라벨 색인도 범위 선택이 가능

# In[29]:

장르['리니지':'아이온']


# 라벨 색인이 설정되어도 기본 정수 색인을 계속 활용할수 있음

# In[31]:

장르[:5]


# In[32]:

장르['리니지']


# In[33]:

장르[0]


# #### 연습
# 
# 식당 주문 기록 식당.xlsx (이전 자료가 없으면 share/data/food_order.xlsx)에 대해 수행
# 
# 1. 메뉴 열을 선택
# 1. 메뉴, 코너의 형식으로 시리즈 구성

# In[35]:

식당 = pd.read_excel('식당.xlsx')
식당[:3]


# In[42]:

식당['메뉴'][:3]
#pd.Series(식당['코너'], index=식당['메뉴'])


# In[43]:

식당['코너'][:3]


# In[44]:

식당.set_index('메뉴')[:3]


# In[45]:

식당.set_index('메뉴')['코너'][:3]


# 각 열을 꺼내서 직접 시리즈로 생성하는 것도 가능

# In[51]:

#원본 데이터 변경없이 시리즈 생성 가능
pd.Series(식당['코너'].values, index=식당['메뉴'].values)


# ## 데이터프레임
# 
# "그러니까 ... 표"

# In[53]:

ncgames 


# In[55]:

pd.DataFrame({'장르': ['MMORPG']*5, '플랫폼': ['PC']*5})


# #### 연습
# 
# 사용자 정보는 이름. 이메일. 게임명 세 가지 정보로 구성됨
# 임의의 사용자 2명 이상의 정보를 데이터 프레임으로 구성
# 
# 1. 이메일 열을 색인으로 설정
# 1. 게임명을 색인으로 설정

# In[84]:

사용자정보 = pd.DataFrame({'이름' : ['박명수', '유재석', '정형돈'], 
                      '이메일': ['ms@test.net', 'js@test.net', 'jung@test.net'], 
                      '게임명': ['와우', '리니지', '']})


# In[69]:

사용자정보


# In[58]:

사용자정보.set_index('이메일')


# In[59]:

사용자정보.set_index('게임명')


# In[74]:

사용자정보.reset_index()
사용자 = 사용자정보.set_index('이메일')

사용자.reset_index()
#사용자
사용자 = 사용자.set_index('게임명')
사용자


# In[81]:

pd.DataFrame([{'이름' : '좌니', '이메일': 'lee', '게임명': '리니지'},
              {'이름' : '와니', '이메일': 'wee', '게임명': '리니지'},
              {'이름' : '오니', '이메일': 'oee'}
             ])


# #### 색인과 열 선택

# In[87]:

ncgames['장르']['리니지']


# In[89]:

ncgames.ix['리니지']


# 두개 이상의 색인 선택

# In[90]:

ncgames.ix[['리니지', '아이온']]


# 단일한 색인을 선택하면서, 시리즈가 아닌데 데이터프레임(~표) 형식으로 만들기

# In[91]:

ncgames.ix[['리니지']]


# .T는 행과 열을 바꾸는 기능

# In[94]:

pd.DataFrame(ncgames.ix['리니지'])


# In[95]:

pd.DataFrame(ncgames.ix['리니지']).T


# In[97]:

ncgames.index


# In[98]:

ncgames.columns


# In[99]:

ncgames.values


# In[100]:

ncgames['장르']


# In[102]:

ncgames[['장르', '플랫폼']]


# 데이터프레임의 열의 순서를 무작위로 바꾸기

# In[103]:

from random import shuffle

nums = [1,2,3,4]
shuffle(nums)
nums


# In[111]:

ncgames.columns


# In[109]:

열목록 = list(ncgames.columns)
shuffle(열목록)
열목록


# In[110]:

ncgames[열목록]


# ### 색인과 열 동시 선택
# 

# 데이터프레임 색인 선택 --> 시리즈 --> 시리즈 색인 선택

# In[119]:

ncgames.ix['리니지']['출시']


# In[120]:

ncgames.ix['리니지', '출시']


# In[121]:

ncgames.ix['리니지', ['출시', '장르']]


# #### 연습
# 
# ncgames에서 아이온, 리니지의 플랫폼, 장르를 제시된 순서로 선택

# In[129]:

ncgames.ix[['아이온', '리니지'],['플랫폼', '장르']]


# 범위선택

# 편의상, 범위 선택은 색인에 대해 수행됨

# In[130]:

ncgames[:2]


# In[131]:

ncgames.ix[:2]


# In[132]:

ncgames['리니지':'아이온']


# In[133]:

ncgames['리니지']


# "그럼 열 범위 선택은 어떻게?"

# In[136]:

ncgames2 = ncgames.T
ncgames2


# In[137]:

ncgames2['리니지':'아이온']


# In[142]:

ncgames2.ix[:]


# 열선택 : (모든 색인을 선택하고) 그리고 지정된 열 범위를 선택
# 
# DataFrame.ix[:, 열범위]

# In[150]:

ncgames2.ix[:, '리니지':'아이온']


# 위 아래 동일

# In[146]:

ncgames2['리니지']


# In[148]:

목록 = [1,2,3,4,5]
복사본 = 목록[:]
복사본


# #### 연습
# 
# 식당자료 'share/data/food_order.xlsx'에 대해 다음을 수행
# 1. 처음 10줄과 마지막 10줄 선택
# 1. 두번째 열부터 마지막에서 두번째 열까지 선택
# 1. 처음 10줄과 처음 5열 선택

# In[152]:

식당 = pd.read_excel('share/data/food_order.xlsx')
식당[:10]


# In[154]:

식당[-10:]


# In[161]:

식당.ix[:, 1:-1][:3]


# In[163]:

식당.ix[:10, :5]


# 조건에 따라 선택
# 21세기에 출시된 게임 자료 선택

# In[165]:

출시2k = ncgames.출시 > 2000
ncgames[출시2k]


# In[169]:

ncgames[ncgames.출시 > 2000 ]


# #### 연습
# 
# 어떤 사용자는 NCSOFT 게임에 대해 호불호가 있다. 해당 사용자는 다음과 같은 선호도를 갖는다고 한다.
# 
#     - 리니지: 호
#     - 리니지: 호
#     - 히어로: 불
#     - 길드워: 불
#     - 아이온: 호
# 
# 1. 사용자의 취향을 시리즈로 표현
# 1. 사용자의 취향에 맞는 게임자료만 ncgames에서 선택

# In[207]:

#취향 = pd.Series([True, True, False, False, True, True], index=['리니지', '리니지2', '히어로', '길드워', '아이온', '리이털'])
취향 = pd.Series([True, True, False, False, True, True])


# In[189]:

ncgames.index


# In[205]:

ncgames[취향.values]


# In[208]:

취향 = pd.Series([True, True, False, False, True, True], index= ncgames.index)


# In[209]:

ncgames[취향]


# In[210]:

날씨 = pd.read_excel('날씨.xlsx')
날씨[:3]


# In[211]:

서울 = 날씨.지역 == 'seoul'
서울[:3]


# 색인이 일치하지 않아서 에러가 발생

# In[213]:

날씨.set_index('날짜')['서울']


# 열의 값을 기반으로 선택

# In[214]:

날씨[날씨.지역 == 'seoul'][:3]


# 대상 열을 색은으로 만든 다음, 색인 선택 활용

# In[216]:

날씨.set_index('지역').ix['seoul'][:3]


# #### 연습
# 
# 식당.xlsx를 읽어들여 생성한 데이터프레임에 대해 다음을 수행
# 
# 1. rice & soup 1코너 자료 선택
# 1. rice & soup 1,2 자료 선택
# 1. 주문 수량이 200 이상인 자료만 선택

# In[218]:

식당 = pd.read_excel('식당.xlsx')
식당[:3]


# In[239]:

식당[식당['코너'] == 'rice & soup 1'][:3]


# In[240]:

식당.set_index('코너').ix['rice & soup 1'].reset_index()[:3]


# 두 개 이상의 조건을 합쳐서 불리언 필터 생성

# In[257]:

한식코너 = (식당['코너'] == 'rice & soup 1') | (식당['코너'] == 'rice & soup 2')
식당[한식코너][:3]


# 필터 적용후 한식이 제대로 선택 되었는지 확인

# In[250]:

식당[한식코너].코너.value_counts()


# In[254]:

식당.set_index('코너').ix[['rice & soup 1', 'rice & soup 2']][:10]


# In[255]:

식당[식당.주문수량 >= 200][:3]


# In[259]:

ncgames['장르'] = '대규모 롤플레잉'
ncgames[:3]


# 데이터 잘 선택하면 고치기 쉬움

# In[264]:

ncgames.ix[['리니지', '리니지2'], '장르'] = 'MMORPG'


# In[265]:

ncgames[:3]


# 여러 열 정보 한번에 바꾸기 = > 여러 열이니까 series
# 전체 열이 통채로 바뀜

# 

# In[267]:

ncgames.ix['리니지'] = pd.Series({'장르': 'RPG', '플랫폼': '윈도우'})
ncgames[:3]


# 1. 원본 자료를 근거로 새로운 시리즈 생성
# 1. 시리즈의 정보를 원하는 대로 수정
# 

# In[274]:

리니지 = ncgames.ix['리니지'].copy()
리니지['출시'] = 1998


# In[270]:

리니지


# 시리즈를 대상에 색인 또는 열에 할당해 갱신

# In[273]:

ncgames.ix['리니지'] = 리니지
ncgames[:3]


# In[275]:

ncgames.ix[['리니지', '리니지2']] = 리니지


# In[ ]:



