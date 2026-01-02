import sys
import os
from playwright.sync_api import sync_playwright

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_user_management_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open application
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Login
        login = LoginPage(page)
        login.login("Admin", "admin123")

        # Admin page
        admin = AdminPage(page)
        admin.open_admin()

        # Add User
        # Add User
        # Add User
        username = admin.add_user()

        # Search newly added user
        admin.search_user(username)

        # Edit User (username changes)
        username = admin.edit_user(username)

        # 🔑 MUST search again after edit
        admin.search_user(username)

        # Delete User
        admin.delete_user(username)

        # 🔑 OPTIONAL: search again to confirm deletion
        admin.search_user(username)


        browser.close()
