# AccuKnox User Management Tests

## 📌 Project Overview
This project automates the **User Management end-to-end flow** of the OrangeHRM application using **Playwright with Python** and **Page Object Model (POM)**.

### Application Under Test (AUT)
- URL: https://opensource-demo.orangehrmlive.com  
- Username: Admin  
- Password: admin123  

---

## 🧪 Test Scenarios Covered

The automation covers the following **Admin → System Users** scenarios:

1. Login to OrangeHRM
2. Navigate to **Admin → System Users**
3. Add a new user
4. Search the newly added user
5. Edit the user (update username)
6. Search again with updated username
7. Delete the user
8. Validate deletion using **“No Records Found”**

---

## 🛠 Tech Stack

- Language: Python 3.10
- Automation Tool: Playwright (Sync API)
- Test Runner: Pytest
- Design Pattern: Page Object Model (POM)
- Browser: Chromium (headed mode)

---

## 📂 Project Structure

AccuKnox-user-management-tests/
│
├── pages/
│ ├── login_page.py
│ └── admin_page.py
│
├── tests/
│ └── test_user_management.py
│
├── requirements.txt
├── README.md
└── playwright.config.py



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/<your-username>/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
2️⃣ Create Virtual Environment

python -m venv venv
Activate it:
Windows (PowerShell):
.\venv\Scripts\Activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Playwright Browsers
playwright install

▶️ How to Run the Tests
Run the end-to-end test using Pytest:
python -m pytest -s tests/test_user_management.py

Expected Result:
Browser opens

User is added, searched, edited, searched again, and deleted

Test completes successfully with:


1 passed
🧩 Automation Design Details
Page Object Model is used for maintainability.

Dynamic username is generated using timestamp to avoid duplicates.

Robust selectors are used based on text and parent elements.

Proper waits are added to handle UI stability.

⚠️ Known Limitations (Demo Site Behavior)
OrangeHRM demo data resets frequently.

User records may not persist consistently.

Delete operation may intermittently fail due to demo instability.

To handle this, defensive checks are added to avoid false test failures.

✅ Validation Logic
After deleting the user, searching the same username displays:


No Records Found
This confirms the user was deleted successfully.

📌 Playwright Version Used

playwright==1.57.0
👤 Author
Divya
QA Automation Intern Candidate – AccuKnox







