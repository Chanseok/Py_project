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
## 세 번째 Log 2018-07-18, 수요일
Jupyter Notebook으로 연결하는 경우에는 아래 경로가 실행이 되고
    C:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_64
PC의 환경 변수 Path 상으로는 아래 경로가 실행이 되어서
    C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64
pip 명령어를 어느 위치에서 실행시켰나에 따라 엉뚱한 결과가 나올 수 있네요. 

## 두 번째 Log 2018-07-??, ?요일


## 첫번째 Log ~ 2018-06-30, 토요일
StudyLog.md 파일을 생성하고 어떻게 학습한 내용을 정리할 지 전체적인 틀, 초안을 만들었습니다. 
- - -
