## 1. Jupyter Notebook 설치와 VS Code 연동하기
vscode와 Jupyter notebook과 연동하는 방법을 만드느라고 시간을 꽤 소모했음..  
그런데 알고보니 Jupyter Notebook 실행 console에 아래와 같은 log가 있더군요.  
> Copy/paste this URL into your browser when you connect for the first time,  
     to login with a token:  
     http://localhost:8888/?token=31b930f617bbca08d14235671b5abf4da8774695a8f76667  

VS Code에서 아래 명령어를 실행하고 
> Jupyter: Enter the url of local/remote Jupyter Notebook  

token 정보까지 포함한 url을 넣으면 연동이 가능해지는군요 (약간 시간이 걸립니다.)  

## 2. 읽어 보기 / 익숙해지기 (1장 ~ 3장)
책 _파이썬으로 데이터주무르기_ 1장에서 3장까지 모두 한번 훑어 봤습니다.  

## 3. 구현 해보기 Part I (1장 ~ 3장)
이제 다시 1장으로 돌아와서 3장까지 예제 Code를 직접 작성 해봄으로써 내 것으로 만들어 보려고 합니다.   

### 1장  서울시 구별 CCTV 현황분석
#### Step 1. 데이타 준비하기 

* [서울시 정보소통광장](https://opengov.seoul.go.kr/ "서울시 정보소통광장")  
* [서울시 자치구 년도별 CCTV 설치현황](http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-2734&srvType=F&serviceKind=1)  
* [서울시 인구](http://data.seoul.go.kr/dataList/datasetView.do?serviceKind=2&infId=419&stcSrl=419&srvType=S)  

#### Step 2. 데이타 읽어들이기 
여기서 없는 파일이라는 Error가 계속 ... @.@ 
```python
pop_Seoul = pd.read_excel('01_PopulationInSeoul.xls', encoding='utf-8')
```
문제는 working directory를 설정하지 않아서였죠.  
현 script file로 working directory를 설정하지 않아서 한참 헤맸네요.
```python
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```
이렇게 해결했습니다. 


- - -
## 세 번째 Log 2018-07-06, 금요일
numpy의 polyfit과 같은 그래프 쓰는 법이 궁금해서 
아침에 출근하면서 오다가 읽은 글인데 정말 정리를 잘 해두셨네요
정리한 format인 Jupyter Notebook도 문서화 관점에서 엄청난 효용이 있는 걸 확인했고요 
* http://taewan.kim/post/numpy_cheat_sheet/  
정작 궁금했던 polyfit 관련 글은 읽어 보지 못했네요. (찾아만 두었습니다.)
* http://pinkwink.kr/1127  

## 두 번째 Log 2018-07-05, 목요일
그동안 pandas, numpy 기본 익히기에 해당하는 1장에 있는 절들을 code practice하다가
드디어 CCTV와 자치구별 인구수 데이터 분석하기로 다시 돌아왔습니다. 

## 첫번째 Log ~ 2018-06-30, 토요일
StudyLog.md 파일을 생성하고 어떻게 학습한 내용을 정리할 지 전체적인 틀, 초안을 만들었습니다. 
- - -
