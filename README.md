# 🧪 Smart Skin AI — Automation Test Suite

Automated end-to-end test suite for **Smart Skin AI**, 
a machine learning based skincare web application 
built with Python Flask, TensorFlow, and OpenAI.

## 📋 Tests Included

| Test File | What it Tests |
|---|---|
| test_login.py | User login functionality |
| test_register.py | New user registration |
| test_dashboard.py | Dashboard data and elements |
| test_navigation.py | All sidebar page navigation |
| test_upload.py | AI skin image upload page |

## 🛠️ Tools Used

- Python 3.14
- Playwright
- pytest
- pytest-html

## ✅ Test Results

- Total Tests: 5
- Passed: 5
- Failed: 0
- Pass Rate: 100%

## 🚀 How to Run Tests

Install dependencies:
pip install playwright pytest pytest-html
python -m playwright install

Run all tests:
py -m pytest

Generate HTML report:
py -m pytest --html=report.html

## 👩‍💻 Developer

Built and tested by Aswathy Salikumar
