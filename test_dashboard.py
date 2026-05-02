from playwright.sync_api import sync_playwright

def test_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Open Smart Skin AI
        page.goto("http://10.20.1.102:5000")
        print("✅ Website opened!")
        
        # Step 2: Login first
        page.click("text=Login")
        page.fill("input[name='username']", "lara")
        page.fill("input[name='password']", "9961176854")
        page.click("button[type='submit']")
        print("✅ Logged in!")
        
        # Step 3: Wait for dashboard
        page.wait_for_timeout(3000)
        
        # Step 4: Check we are on dashboard
        print("Current page:", page.url)
        
        # Step 5: Check dashboard elements
        assert page.is_visible("text=Your Skin Progress")
        print("✅ Dashboard loaded!")
        
        assert page.is_visible("text=Total Entries")
        print("✅ Total Entries visible!")
        
        assert page.is_visible("text=Average Sleep")
        print("✅ Average Sleep visible!")
        
        assert page.is_visible("text=Average Water")
        print("✅ Average Water visible!")
        
        browser.close()
        print("TEST PASSED ✅")

test_dashboard()