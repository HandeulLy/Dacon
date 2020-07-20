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





