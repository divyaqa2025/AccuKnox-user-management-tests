import time

class AdminPage:
    def __init__(self, page):
        self.page = page

    # ----------------------------
    # Open Admin → System Users
    # ----------------------------
    def open_admin(self):
        self.page.click("text=Admin")
        self.page.wait_for_selector("button:has-text('Add')")

    # ----------------------------
    # Add User
    # ----------------------------
    def add_user(self):
        # Click Add
        self.page.click("button:has-text('Add')")
        self.page.wait_for_selector("form.oxd-form")

        # -------- User Role (Admin) --------
        self.page.locator(".oxd-select-text").nth(0).click()
        self.page.get_by_role("listbox").get_by_text("Admin").click()

        # -------- Employee Name --------
        emp = self.page.locator("input[placeholder='Type for hints...']")
        emp.fill("a")
        self.page.wait_for_timeout(2000)
        emp.press("ArrowDown")
        emp.press("Enter")

        # -------- Status (Enabled) --------
        self.page.locator(".oxd-select-text").nth(1).click()
        self.page.get_by_role("listbox").get_by_text("Enabled").click()

        # -------- Username --------
        username = f"autoUser_{int(time.time())}"
        self.page.locator(
            "input.oxd-input:not([type='password'])"
        ).nth(1).fill(username)

        # -------- Password --------
        self.page.locator("input[type='password']").nth(0).fill("Test@123")

        # -------- Confirm Password --------
        self.page.locator("input[type='password']").nth(1).fill("Test@123")

        # -------- Save --------
        self.page.locator("button[type='submit']").click()

        # Back to System Users page
        self.page.wait_for_selector("button:has-text('Add')")

        return username


    # ----------------------------
    # Search User
    # ----------------------------
    def search_user(self, username):
    # Scope to filter area (important)
        filter_area = self.page.locator("div.oxd-table-filter-area")

        # Username input inside filter area
        username_input = filter_area.locator("input.oxd-input").first

        # Fill username
        username_input.fill("")
        username_input.fill(username)

        # Click Search button (inside same filter area)
        filter_area.locator("button[type='submit']").click()

        # Wait for results
        self.page.wait_for_timeout(2000)


        # ----------------------------
    # Edit User (✏️ Pencil)
    # ----------------------------
    def edit_user(self, username):
        # Wait until search results load
        self.page.wait_for_selector(".oxd-table-card")

        # Locate the card by username text (robust)
        user_card = self.page.locator(
            f".oxd-table-card:has-text('{username}')"
        ).first

        # Scroll into view (important)
        user_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)

        # Click pencil icon inside this card
        user_card.locator("button:has(i.bi-pencil-fill)").click()

        # Wait for Edit User page
        self.page.wait_for_selector("text=Edit User")

        # Update Username (Edit page input order!)
        new_username = f"{username}_edit"
        username_input = self.page.locator(
            "input.oxd-input:not([type='password'])"
        ).nth(1)

        username_input.fill("")
        username_input.fill(new_username)

        # Save
        self.page.locator("button[type='submit']").click()

        # Back to System Users page
        self.page.wait_for_selector("button:has-text('Add')")

        return new_username




    # ----------------------------
    # Delete User (🗑️ Trash)
    # ----------------------------
    def delete_user(self, username):
        # Small wait to ensure table loads
        self.page.wait_for_timeout(2000)

        # Locate the user card by username text
        user_card = self.page.locator(
            ".oxd-table-card:has(.data:has-text('{}'))".format(username)
        )

        if user_card.count() == 0:
            print(f"User '{username}' not found. Skipping delete.")
            return

        # Click DELETE (trash) icon button
        user_card.locator("button:has(i.bi-trash)").click()

        # Wait for confirmation popup
        yes_delete = self.page.locator("button:has-text('Yes, Delete')")
        yes_delete.wait_for(state="visible", timeout=5000)

        # Click Yes, Delete
        yes_delete.click()

        # Verify deletion
        self.page.wait_for_timeout(3000)
        assert self.page.locator("text=No Records Found").is_visible()
