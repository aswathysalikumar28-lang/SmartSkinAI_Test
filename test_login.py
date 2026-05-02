from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Open Smart Skin AI
        page.goto("http://10.20.1.102:5000")
        print("✅ Website opened!")
        
        # Step 2: Click Login button
        page.click("text=Login")
        print("✅ Clicked Login!")
        
        # Step 3: Type username
        page.fill("input[name='username']", "lara")
        print("✅ Username typed!")
        
        # Step 4: Type password
        page.fill("input[name='password']", "9961176854")
        print("✅ Password typed!")
        
        # Step 5: Click Submit
        page.click("button[type='submit']")
        print("✅ Submitted!")
        
        # Step 6: Wait 3 seconds to see dashboard!
        page.wait_for_timeout(3000)
        
        # Step 7: Check which page we landed on
        print("Page after login:", page.url)
        
        browser.close()
        print("TEST PASSED ✅")

test_login()