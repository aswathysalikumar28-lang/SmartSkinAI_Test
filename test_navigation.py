from playwright.sync_api import sync_playwright

def test_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Login first
        page.goto("http://10.20.1.102:5000")
        page.click("text=Login")
        page.fill("input[name='username']", "lara")
        page.fill("input[name='password']", "9961176854")
        page.click("button[type='submit']")
        page.wait_for_timeout(2000)
        print("✅ Logged in!")
        
        # Test Profile page
        page.click("text=Profile")
        page.wait_for_timeout(2000)
        print("✅ Profile page:", page.url)
        page.go_back()
        page.wait_for_timeout(1000)
        
        # Test Skin Test page
        page.click("text=Skin Test")
        page.wait_for_timeout(2000)
        print("✅ Skin Test page:", page.url)
        page.go_back()
        page.wait_for_timeout(1000)
        
        # Test Track Daily Skin Habits
        page.click("text=Track Daily Skin Habits")
        page.wait_for_timeout(2000)
        print("✅ Track Daily Skin Habits page:", page.url)
        page.go_back()
        page.wait_for_timeout(1000)
        
        # Test Skin Pattern Tracker
        page.click("text=Skin Pattern Tracker")
        page.wait_for_timeout(2000)
        print("✅ Skin Pattern Tracker page:", page.url)
        page.go_back()
        page.wait_for_timeout(1000)
        
        # Test View Skin Data
        page.click("text=View Skin Data")
        page.wait_for_timeout(2000)
        print("✅ View Skin Data page:", page.url)
        page.go_back()
        page.wait_for_timeout(1000)
        
        # Test Upload Skin Image
        page.click("text=Upload Skin Image")
        page.wait_for_timeout(2000)
        print("✅ Upload Skin Image page:", page.url)
        page.go_back()
        page.wait_for_timeout(1000)
        
        browser.close()
        print("TEST PASSED ✅")

test_navigation()