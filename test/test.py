import time
from selenium import webdriver # Seleniumにあるwebdriver機能を取り込む

driver = webdriver.Chrome() # Chromeに接続(ここでウィンドウが開く)
driver.set_window_size(1440, 720) # ウィンドウサイズを調整
driver.get('https://shrouded-cove-30909.herokuapp.com/') # get(URL)で特定サイトにアクセス
time.sleep(1) # ページ表示を待つ

button = driver.find_element_by_id('exec')
button.click()
time.sleep(1)
output = driver.find_element_by_id('output')
try:
  assert output.text == 'Hippopotamus'
finally:
  driver.quit() # 終了

