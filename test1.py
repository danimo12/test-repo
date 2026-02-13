from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        # 브라우저 실행 (headless 모드로 실행됨)
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # 1. 존재하지 않는 이상한 주소로 접속 시도
        page.goto('https://www.g00000gle.con') 
        
        # 2. 구글 검색창의 ID는 'q'인데, 말도 안 되는 ID로 검색 시도
        # 이 부분에서 에러가 발생하여 멈출 것입니다.
        page.fill('#this-is-wrong-id', 'AI Agent')
        
        # 3. 버튼 클릭도 잘못된 선택자 사용
        page.click('button[type="invalid"]')
        
        print("검색 완료!")
        browser.close()

if __name__ == "__main__":
    test_google_search()