import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def fetch_image_urls(query, max_links_to_fetch, wd, sleep_between_interactions=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    wd.get(search_url)
    time.sleep(2)  # Ensure the page loads

    image_urls = set()
    image_count = 0
    results_start = 0

    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # 🔴 DEBUG: Check if elements are being found
        thumbnail_results = wd.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
        print(f"🟢 Found {len(thumbnail_results)} image thumbnails.")

        for img in thumbnail_results[results_start:]:
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # Get full-size images
            actual_images = wd.find_elements(By.CSS_SELECTOR, "img.rg_i")
            for actual_image in actual_images:
                src = actual_image.get_attribute('src')
                if src and src.startswith("http"):
                    image_urls.add(src)

            image_count = len(image_urls)
            if image_count >= max_links_to_fetch:
                print(f"✅ Found {len(image_urls)} images. Downloading...")
                return image_urls

        results_start = len(thumbnail_results)

    return image_urls


def persist_image(folder_path, url, counter):
    try:
        image_content = requests.get(url).content
        file_path = os.path.join(folder_path, f"image_{counter}.jpg")

        with open(file_path, 'wb') as f:
            f.write(image_content)

        print(f"✅ Saved {url} as {file_path}")

    except Exception as e:
        print(f"❌ ERROR - Could not save {url}: {e}")


def search_and_download(search_term, driver_path, target_path='./images', number_images=10):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split()))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open in maximized mode for visibility
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Remove unnecessary logs

    service = Service(driver_path)
    wd = webdriver.Chrome(service=service, options=options)

    try:
        res = fetch_image_urls(search_term, number_images, wd, sleep_between_interactions=1)

        counter = 0
        for elem in res:
            persist_image(target_folder, elem, counter)
            counter += 1

    finally:
        wd.quit()  # Ensure browser closes properly


# 🔹 **Path to ChromeDriver**
DRIVER_PATH = r'D:\ML_model_Config\PYTHON_PROJECT\ImageScrapper\chromedriver.exe'

# 🔹 **Search term**
search_term = 'prabas'

# 🔹 **Start image scraping**
search_and_download(search_term=search_term, driver_path=DRIVER_PATH, number_images=5)
