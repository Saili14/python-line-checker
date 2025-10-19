A Python tool to scan websites and detect backlinks to a target domain (`vijaypkaria.com`).  
Handles static and JavaScript-heavy pages, retries with Selenium, detects CAPTCHAs, and generates detailed CSV reports with summaries.

---

Features

- Reads a list of URLs from CSV or Excel.
- Checks each URL for a backlink to the target domain.
- Handles:
  - JS-heavy pages using Selenium
  - CAPTCHA detection (manual/automatic handling)
  - Retry logic for failed pages
- Logs results in a CSV file with:
  - URL
  - Status (Link found, Not found, JS page, CAPTCHA blocked)
  - Notes
- Displays a **colored terminal output** and summary report for quick analysis.

---

**Sample Input (`input.csv`):**
URL
https://vijaykariaofficial.blogspot.com/2025/05/leading-with-vision-and-values-story-of.html

https://telegra.ph/Vijay-P-Karia-The-Life-The-Legacy-The-Loop-08-07

https://visionary-leader-in-power-and-energy.hashnode.dev/about-vijay-p-karia

https://example.com



**Terminal Output:**
Starting Link Checker...
Checking (requests): https://vijaykariaofficial.blogspot.com/2025/05/leading-with-vision-and-values-story-of.html

❌ Link not found: https://vijaykariaofficial.blogspot.com/2025/05/leading-with-vision-and-values-story-of.html

Checking (requests): https://telegra.ph/Vijay-P-Karia-The-Life-The-Legacy-The-Loop-08-07

✅ Link found: https://telegra.ph/Vijay-P-Karia-The-Life-The-Legacy-The-Loop-08-07

Checking (requests): https://visionary-leader-in-power-and-energy.hashnode.dev/about-vijay-p-karia

Request failed: https://visionary-leader-in-power-and-energy.hashnode.dev/about-vijay-p-karia

Checking (requests): https://example.com

❌ Link not found: https://example.com

✅ Done! Results saved to 'results.csv'.

📊 Summary Report:

❌ Link not found: 2

✅ Link found: 1

Request failed: 1

Total URLs checked: 4

**Output CSV (`results.csv`):**
Original URL,Status,Notes
https://vijaykariaofficial.blogspot.com/2025/05/leading-with-vision-and-values-story-of.html,❌ Link not found,No link detected
https://telegra.ph/Vijay-P-Karia-The-Life-The-Legacy-The-Loop-08-07,✅ Link found,Found using requests
https://visionary-leader-in-power-and-energy.hashnode.dev/about-vijay-p-karia,Request failed,Status code: 403
https://example.com,❌ Link not found,No link detected

## Installation

Clone the repository:
git clone https://github.com/Saili14/python-link-checker.git

cd python-link-checker

Create a virtual environment 

python -m venv .venv

.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

Install dependencies:

pip install -r requirements.txt

If you don’t have requirements.txt, install manually:

pip install requests beautifulsoup4 selenium pandas openpyxl colorama

python link_checker.py

View results in results.csv and terminal summary.

**Technologies Used**
Python
Selenium
BeautifulSoup
Requests
Pandas
OpenPyXL
Colorama

Future Improvements
Automatic CAPTCHA solving via free APIs
Multi-threading for faster scanning
Enhanced HTML/JSON reports for easier analysis
