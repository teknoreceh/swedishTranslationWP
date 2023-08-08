from selenium import webdriver
from selenium.webdriver.common.by import By

# Inisialisasi webdriver
driver = webdriver.Chrome()  # Anda dapat menggunakan driver browser lain seperti Firefox, Edge, dll.

# Buka halaman web
driver.get("https://www.contoh.com")

# Cari elemen berdasarkan ID menggunakan By.ID
elemen_berdasarkan_id = driver.find_element(By.ID, "id-elemen")
print("Elemen berdasarkan ID:", elemen_berdasarkan_id.text)

# Cari elemen berdasarkan nama kelas menggunakan By.CLASS_NAME
elemen_berdasarkan_kelas = driver.find_element(By.CLASS_NAME, "nama-kelas")
print("Elemen berdasarkan kelas:", elemen_berdasarkan_kelas.text)

# Cari elemen berdasarkan selector CSS menggunakan By.CSS_SELECTOR
elemen_berdasarkan_css = driver.find_element(By.CSS_SELECTOR, "selector-css")
print("Elemen berdasarkan selector CSS:", elemen_berdasarkan_css.text)

# Cari elemen berdasarkan XPath menggunakan By.XPATH
elemen_berdasarkan_xpath = driver.find_element(By.XPATH, "ekspresi-xpath")
print("Elemen berdasarkan XPath:", elemen_berdasarkan_xpath.text)

# Cari elemen berdasarkan nama kelas menggunakan By.CLASS_NAME
elemen_berdasarkan_kelas = driver.find_elements(By.CLASS_NAME, "nama-kelas")
for elemen in elemen_berdasarkan_kelas:
    print("Elemen berdasarkan kelas:", elemen.text)

# Cari elemen berdasarkan selector CSS menggunakan By.CSS_SELECTOR
elemen_berdasarkan_css = driver.find_elements(By.CSS_SELECTOR, "selector-css")
for elemen in elemen_berdasarkan_css:
    print("Elemen berdasarkan selector CSS:", elemen.text)

# Cari elemen berdasarkan XPath menggunakan By.XPATH
elemen_berdasarkan_xpath = driver.find_elements(By.XPATH, "ekspresi-xpath")
for elemen in elemen_berdasarkan_xpath:
    print("Elemen berdasarkan XPath:", elemen.text)

# Tutup jendela browser
driver.quit()
