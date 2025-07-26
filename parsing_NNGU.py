from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time
from tqdm import tqdm
from urls import URLS


def get_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def load_html(url, driver, wait_time=3):
    driver.get(url)
    time.sleep(wait_time)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')[1:]
    data = [
        ["+" if col.find('i', class_='fa-check') else col.get_text(strip=True) for col in row.find_all(['td', 'th'])]
        for row in rows
    ]
    return data


def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def process_url(filename, url, driver, wait_time=3):
    data = load_html(url, driver, wait_time)
    write_file(filename, data)
    return filename


def process_all(urls, driver, wait_time=3):
    return [process_url(filename, url, driver, wait_time) for filename, url in tqdm(urls.items(), desc="Загрузка таблиц")]


def main(headless=True, wait_time=3):
    driver = get_driver(headless)
    try:
        processed_files = process_all(URLS, driver, wait_time)
        print("Файлы обновлены:", processed_files)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

