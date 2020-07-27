# Daily Notes



# 12th, July

### 1st

lgbm, basic version

코드 공유에서 lgbm 모델을 사용한 사람의 코드를 기본적으로 사용

rmse가 낮길래 기대했으나, 실제 점수는 별로라 파라미터 튜닝이 필요해 보임

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_1.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_2.png">

HDLY_0712(1) score = 6.6072841989 

<hr>

### 2nd

lgbm, parameter tuned

파라미터 값들을 검색한 내용들 위주로 바꿔서 진행해 봄

하지만 rmse 값이 너무 높아서, 아마도 점수가 좋지 않을 듯 하여 제출은 하지 않음

(1일 3회 최대 제출 너무 야박하다)

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_3.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_4.png">

score = not sumbitted

<hr>

### 3rd

lgbm, metric : rmse -> custom(with rmsle function)

rmse 대신 rmsle 구하는 함수를 작성해서 적용

학습 횟수도 1,000에서 20,000으로 올리고 진행

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_5.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_6.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0712_7.png">

HDLY_0712(2) score = 6.9135767409

<hr>



# 13th, July

### 1st

lgbm, metric=custom(rmsle_1 function), boosting=gdbt

부스팅은 기본인 gdbt로 설정하고, metric은 rmsle_1으로 설정했지만

굉장히 점수가 낮음

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_1.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_2.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_3.png">

HDLY_0713 score = 7.2448565177

<hr>

### 2nd

lgbm, parameter tuned

boosting : dart

objective : li

metric : custom(rmsle_1)

train : 20000, eval=100, earlystopping=1000

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_4.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_5.png">

score = not sumbitted

<hr>

### 3rd

lgbm, parameter tuned

boosting : dart

objective : multiclass

metric : softmax

train : 20000, eval=100, earlystopping=100

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_6.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_7.png">

predict 과정에서 에러 남

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_8.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_9.png">

클래스 수는 41개로 학습 시켰는데,  AMT 하나만 예측하려고 하니까 에러나는 듯?

일단은.... 모델 저장 시켜두고, 내일 논의하기로

model svae & load 까지 구현

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0713_10.png">

<hr>

+

추가)

4월 점수를 기준으로 보드에 올라가고, 7월은 나중이지만.

가채점 점수가 낮으면(좋으면) 그냥 그걸 4월 데이터라고 가져가서

시계열로 7월을 판단하면 안되나?

-> 7월 28일에 4월 데이터 공개 예정



<hr>

# 15th, July

### 1st

독립 변수들에 대한 전처리 진행

1. 계절 추가 : 봄1 여름2 가을3 겨울4
2. 결제 지역과 거주지 기준으로 여행객0, 거주자1로 구분
3. 결제 건수를 20가지 범위로 나눠서 0~19로 카테고리 화
4. 코로나 영향이 있는 업종들은 따로 표시

위 4가지 컬럼을 추가해서 진행

총 11개 독립변수

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_1.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_2.png">



모델은 기본 lgbm 으로 진행

boosting : gbdt

objective : tweedie

metric : custom(rmsle_1)

train : 1000 epochs

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_3.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_4.png">

예측 템플릿 부분 코드 추가

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_5.png">

....

temp 만들다가 죽어버림

<hr>

### 

# 17th, July

### 1st

독립 변수들에 대한 전처리 진행

1. 계절 추가 : 봄1 여름2 가을3 겨울4
2. 결제 지역과 거주지 기준으로 여행객0, 거주자1로 구분
3. 결제 건수를 20가지 범위로 나눠서 0~19로 카테고리 화
4. 코로나 영향이 있는 업종들은 따로 표시

위 4가지 컬럼을 추가해서 진행

총 11개 독립변수

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_1.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_2.png">

모델은 기본 lgbm 으로 진행

boosting : gbdt

objective : tweedie

metric : custom(rmsle_1)

train : 20,000 epochs

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_1.png">

예측 템플릿 부분 코드 추가

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_5.png">

....

temp 만들다가 죽어버림, 그래서 다른 컴퓨터로 해봄

1) KJH RAM 32G, 메모리 터짐...

2) 친구 연구실 컴퓨터 RAM 16G, 메모리 터짐...

<hr>

### 2nd

독립 변수들에 대한 전처리 진행

1. 계절 추가 : 봄1 여름2 가을3 겨울4
2. 결제 지역과 거주지 기준으로 여행객0, 거주자1로 구분
3. 결제 건수를 20가지 범위로 나눠서 0~19로 카테고리 화
4. 코로나 영향이 있는 업종들은 따로 표시

위 4가지 컬럼을 추가해서 진행

총 11개 독립변수

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_1.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0715_2.png">

모델은 기본 lgbm 으로 진행

boosting : gbdt

objective : tweedie

metric : custom(rmsle_1)

train : 20,000 epochs

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_1.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_2.png">

예측 템플릿 부분 코드 추가

여기서 12개를 10개로 줄여서 시도해봄(HOM_SIDO_NM, FLC 두개 삭제)

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_3.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_4.png">

터짐...

<hr>


### 3rd

main code 변경 : [Main_0717_10fors.ipynb] => [Main_0717_10combinations.ipynb]

일단, 변수를 줄이고 for 반복 횟수를 줄여야 한다고 생각

따라서 KMH님이 그래프를 통해 feature importance를 확인한 것을 이용해서 비중 없는 변수는 삭제하기로 함

모델을 학습시키는 흐름은 이전이랑 거의 동일

- 먼저, 컬럼을 추가 함 : 계절, 거주/여행, 결제 건수, 코로나 ...

- 이렇게 4개를 추가해서, 총 12개의 독립변수로 1차 모델 학습 시킴
- 모델 학습 파라미터 동일, 학습 횟수 20000번으로 동일

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_5.png">

- 여기서 feature 비중을 그래프로 그려서 확인해 봄

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_6.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_7.png">

- 위 그래프를 보면 알 수 있듯이, 추가한 변수  [CNT_Category, season, covid, visitor]는 큰 영향력이 없음
- 그러면..... 추가한 변수들을 그냥 버려야 하는 것인가?
- 아니면, for 문을 도는 그 부분의 시스템 부하를 좀 줄일 수 있는 방법이 있는가?

변수를 버리기보다는 for 문을 수정해보기로 함

12중 for loops 는 매우 부담되기 때문에, 리스트에서 조합 찾는 방법을 생각해봄

코드 참고 링크 : https://ourcstory.tistory.com/414

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_8.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0717_9.png">

역시나 터짐

그러면 변수를 줄여야 하는데, 추가한 4개 없이 그대로 가면. 기존 베이스 라인 그대로니까...

이미 모델은 12개 변수로 학습을 진행했고, 만약 temp 생성하는 단계에서는 4개 없이 8개로만 진행하면?

그럼 for loop에 부담도 줄어들고, 모델 학습은 진행 했고. 가중치가 있으니까 진행해도 되지 않을까 했지만.

아닌것 같다.

결국에는 '예측'하는 단계에서 그 변수를 써야 의미가 잇는 것이다.

어렵다.

변수를 더 생각해보자.

일단 그나마 제일 영향력 없는 변수 2개(CNT_Category, COVID) 제외하고 진행해보고자 함

총 10개의 fors.



<hr>


# 20th, July

새로운 feature 발견을 위해 데이터를 이해해보고자 함.



### 1st

성별과 가족 구성원에 대해 살펴봄

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0720_1.png">



1인 가구의 증가가 소비 패턴에 영향이 있지 않을까? 생각하여

2019년에서 2020년의 구성원 비율에 변화가 있는지 살펴봄

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0720_2.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0720_3.png">



하지만, 숫자들과 그래프를 통해서 구성원 비율에 대한 변화는 크게 없음을 확인했다.

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0720_4.png">





# 22th, July

새로운 feature 발견을 위해 데이터를 이해해보고자 함.



### 1st

나이 대 별 변화 추이를 살펴 봄

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_1.png">



위 그래프는 달 수 에 따라 달라졌다고 생각함

즉, 19년은 총 12개월인 반면, 20년은 3개월이기 때문에 비중 차이가 발생함

이를 해결하기 위해 년-월의 컬럼을 추가



<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_2.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_3.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_4.png">



큰 차이는 없어보이지만, 전체적으로 20년 2~3월에 낮은 수치, 19년 9월에 높은 수치를 보임

낮은 이유는 코로나의 영향으로 그런 듯

10대와 70대는 시간 흐름에 큰 영향은 받지 않으나, 30~40대는 많은 영향이 있는 듯 보임



### 2nd

외부 데이터를 활용해보기 위해서 제주특별자치도관광협회 사이트 이용

- 링크 : http://www.visitjeju.or.kr/web/bbs/bbsList.do;jsessionid=xcJGAaPyYeKeViaOzdERrlI8o1tB1CmJQLIULFEDVgEUJXbZV7pKPN2NV1Dsshs2.DB_servlet_engine6?bbsId=TOURSTAT

여기서 월별 ''제주도 입도 현황'' 데이터를 사용함

19년 01월 ~ 20년 03월의 제주도 입도 데이터 컬럼을 추가

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_5.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_6.png">



### 3rd

이제 데이터를 정리해서 모델 학습시키고, 제출 파일 생성해봄

src code file : Main_0722_EDAs.ipynb



그동안 했던 변수들(계절, 거주자/여행자, 결제건수 카테고리, 코로나 영향)은 다 사용하지 않고

2개의 새로운 변수만 사용 : 단골 고객 여부 + 제주도 입도 현황

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_7.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_8.png">

여기서는 '결제된 시도' + '업종' + '거주지 시도' + 위의 2개 변수 만 사용하려 함

그 외 사용하지 않는 컬럼들은 drop

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_9.png">



모델 : boosting=dart , objectiv=tweedie

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_10.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_11.png">

20000번 학습 후, 0.02 수준으로 떨어졌는데, 모델을 학습시키기 전에 drop을 제대로 안함

독립변수가 9개인 상태로 모델이 생성되서 temp 만드는 부분에 for loop 돌다가 또 안됨

그래서 drop 제대로 다시 하고, 5개의 변수로만 모델 학습 다시 진행함

단, 여기서 24:00전에 제출하기 위해 dart 대신 gbdt로 학습함(이거 제대로 되면 dart로 진행해 볼 예정)

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_12.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_13.png">

그런데, 5개 변수로 했다고해서... temp 만들 때 year+month 7개까지 돌리면 안된다고 함.

그래서 다시 year + month 포함해서 시킴

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_14.png">

<img src="C:/Users/hande/Desktop/H/Git/Dacon/3_Jeju_Card/dailyNotes/img/0722_15.png">

HDLY_0722 : 7.54.... 매우 안좋음



-----------------------------



+

KJH(Captain) 아이디어

기간을 '계절' 기준으로 나눠서 시도해볼 아이디어 구상

4개의 모델을 만들어서, 짧은 기간의 데이터만 사용해서 학습해 볼 예정

전체 데이터를 학습하면 오히려 긴 기간이기 때문에 정확성이 안좋다고 판단

- 참고 링크 : https://www.kaggle.com/c/m5-forecasting-accuracy/discussion/163684

+

KMH(독수리) 아이디어

업종 별 코로나 영향도를 가중치로 사용해보면 어떨까

같은 업종, 전년 대비 AMT랑 추이를 계산에 사용하자

+

KMH(Cutie) 아이디어

어차피 소비하는 전체 금액은 동일할 것이다

예를 들어, 코로나 때문에 A업종의 소비가 줄었으면, 그 돈은 B업종에 쓸 것이다.

이용횟수 이용건수는 AMT랑 높은 관계가 있을 것으로 판단하여, 이 2개 기준으로 AMT를 예측

+

KJH() 아이디어

카드 사용처, 업종별, 년 월, 그 외(나머지)를 원-핫 인코딩해서 비율로 나타냄

이 비율들을 사용하려는 방법을 생각해야 함

어차피 결제가 발생하는 부분에 대한 예측이 우선되어야 하고, 그 뒤에 비율들을 사용하겠다

+

1) BC카드로 코로나 재난지원금 사용은 없을 것이다

2) 제주관광협회 참고 

- 링크 : http://www.visitjeju.or.kr/web/bbs/bbsList.do;jsessionid=xcJGAaPyYeKeViaOzdERrlI8o1tB1CmJQLIULFEDVgEUJXbZV7pKPN2NV1Dsshs2.DB_servlet_engine6?bbsId=TOURSTAT