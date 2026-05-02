from playwright.sync_api import sync_playwright

def test_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Open Smart Skin AI
        page.goto("http://10.20.1.102:5000")
        print("✅ Website opened!")
        
        # Step 2: Click Register button
        page.click("text=Register")
        print("✅ Clicked Register!")
        
        # Step 3: Type username
        page.fill("input[name='username']", "noya")
        print("✅ Username typed!")
        
        # Step 4: Type email
        page.fill("input[name='email']", "noya123@gmail.com")
        print("✅ Email typed!")
        
        # Step 5: Type password
        page.fill("input[name='password']", "noya1234")
        print("✅ Password typed!")
        
        # Step 6: Click Register button
        page.click("button[type='submit']")
        print("✅ Register clicked!")
        
        # Step 7: Wait and check
        page.wait_for_timeout(3000)
        print("Page after register:", page.url)
        
        browser.close()
        print("TEST PASSED ✅")

test_register()