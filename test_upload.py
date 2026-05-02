from playwright.sync_api import sync_playwright
import os

def test_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Step 1: Login first
        page.goto("http://10.20.1.102:5000")
        page.click("text=Login")
        page.fill("input[name='username']", "lara")
        page.fill("input[name='password']", "9961176854")
        page.click("button[type='submit']")
        page.wait_for_timeout(2000)
        print("✅ Logged in!")
        
        # Step 2: Go to Upload page
        page.goto("http://10.20.1.102:5000/upload_skin")
        page.wait_for_timeout(2000)
        print("✅ Upload page opened!")
        
        # Step 3: Check page title visible
        assert page.is_visible("text=AI Skin Type Detection")
        print("✅ Title visible!")
        
        # Step 4: Check Choose file button exists
        assert page.is_visible("input[type='file']")
        print("✅ Choose file button visible!")
        
        # Step 5: Check Analyze Skin button exists
        assert page.is_visible("text=Analyze Skin")
        print("✅ Analyze Skin button visible!")
        
        # Step 6: Check Back To Home button exists
        assert page.is_visible("text=Back To Home")
        print("✅ Back To Home button visible!")
        
        browser.close()
        print("TEST PASSED ✅")

test_upload()