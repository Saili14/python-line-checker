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

Demo

**Sample Input (`input.csv`):**
