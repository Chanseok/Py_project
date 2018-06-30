# * https://www.youtube.com/watch?v=n0PUuYVB90o&index=8&list=PL9mhQYIlKEhf0DKhE-E59fR-iu7Vfpife

# 인터파크 투어 사이트에서 여행지 입력 후 검색 --> 잠시 후 --> 결과
# 로그인 시 PC 웹 사이트 처리가 어려우면 --> 모바일 로그인 진입
# 모듈 가져오기 - pip install selenium
from selenium import webdriver as wd

# 사전 설정 => DB or file or shell or batch
main_url = "http://tour.interpark.com/"
# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 고려사항 -> 옵션 부여해서 ( 프록시, 에이전트 조작, 이미지 파일 배제)
# More 크롤링 More 임시파일 => 정기적으로 flush

# 사이트 접속 (get )
driver.get(main_url)

# 검색창 찾아서 검색어 입력
# 검색버튼 클릭
# 잠시 대기 => 페이지 로드
#