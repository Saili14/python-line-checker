import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

import time


# CONFIGURATION
TARGET_DOMAIN = "vijaypkaria.com"
INPUT_FILE = "input.csv"
OUTPUT_FILE = "results.csv"


# Function to check if link exists using Requests + BeautifulSoup
def check_with_requests(url):
    try:
        print(f"Checking (requests): {url}")
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return "Request failed", f"Status code: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            if TARGET_DOMAIN in link["href"]:
                return "✅ Link found", "Found using requests"
        return "❌ Link not found", "No link detected"
    except requests.exceptions.RequestException as e:
        if "captcha" in str(e).lower():
            return "⚠️ CAPTCHA blocked", "Blocked by CAPTCHA"
        return "🔄 JS page", f"Request error: {e}"


# Function to retry using Selenium for JS-heavy pages
def check_with_selenium(url):
    print(f"Retrying with Selenium: {url}")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(20)
        driver.get(url)
        time.sleep(5)  # Wait for JS to load

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            if TARGET_DOMAIN in link["href"]:
                driver.quit()
                return "✅ Link found", "Found using Selenium (JS page)"
        driver.quit()
        return "❌ Link not found", "JS page checked, no link"
    except WebDriverException as e:
        return "⚠️ CAPTCHA blocked", f"Selenium error: {e}"


# -------------------------------
# MAIN PROGRAM
# -------------------------------
def main():
    print("🔍 Starting Link Checker...")
    df = pd.read_csv(INPUT_FILE)

    results = []
    for url in df["URL"]:
        status, notes = check_with_requests(url)

        # Retry JS-heavy page with Selenium
        if status == "🔄 JS page":
            status, notes = check_with_selenium(url)

        results.append({"Original URL": url, "Status": status, "Notes": notes})

        # Print colored status in terminal
        if status == "✅ Link found":
            print(Fore.GREEN + f"{status}: {url}")
        elif status == "❌ Link not found":
            print(Fore.RED + f"{status}: {url}")
        elif "CAPTCHA" in status or "Request failed" in status:
            print(Fore.YELLOW + f"{status}: {url}")
        elif status == "🔄 JS page":
            print(Fore.BLUE + f"{status}: {url}")
        else:
            print(status + f": {url}")

    # Save results
    result_df = pd.DataFrame(results)
    result_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Done! Results saved to '{OUTPUT_FILE}'.")

    # -------------------------------
    # Colored summary report
    # -------------------------------
    summary = result_df["Status"].value_counts()
    print("\n📊 Summary Report:")
    for status, count in summary.items():
        if status == "✅ Link found":
            print(Fore.GREEN + f"{status}: {count}")
        elif status == "❌ Link not found":
            print(Fore.RED + f"{status}: {count}")
        elif "CAPTCHA" in status or "Request failed" in status:
            print(Fore.YELLOW + f"{status}: {count}")
        elif status == "🔄 JS page":
            print(Fore.BLUE + f"{status}: {count}")
        else:
            print(f"{status}: {count}")

    total = len(result_df)
    print(f"\nTotal URLs checked: {total}")

if __name__ == "__main__":
    main()
