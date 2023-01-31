from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Browser Action 1 > Open Web
driver.get("https://www.google.com/")
sleep(1)

# # Browser Action 2 > Title
# windows_title = driver.title
# print(windows_title)

# # Browser Action 3 > Back
# driver.get("https://www.wikipedia.org/")
# sleep(3)
# driver.back()
# sleep(3)

# # Browser Action 4 > forward
# driver.forward()
# sleep(3)

# # Browser Action 5 > Refresh
# driver.refresh()
# sleep(3)

# # Browser Action 6 > Open new window and switch to it(Tab)
# driver.switch_to.new_window('tab')
# sleep(3)

# # Browser Action 7 > Open new window and switch to it(Window)
# driver.switch_to.new_window('window')
# driver.get('https://yahoo.com')
# sleep(3)

# Browser Action 8 > Current window
# yahoo_window = driver.current_window_handle

# # Browser Action 9 > All windows
# all_handle = driver.window_handles

# # Browser Action 10 > Switch
# driver.switch_to.window(all_handle[0])
# sleep(3)

# # Browser Action 11 > Close current open tap
# driver.close()
# sleep(3)

# # Browser Action 12 > Quit session
# driver.quit()

# # Browser Action 13 > Window Size
# window_size = driver.get_window_size()  # {'width': 1050, 'height' 796}
# print(window_size)

# # Browser Action 14 > Set window size
# driver.set_window_size(512, 512)
# sleep(3)
# size = driver.get_window_size()
# assert size['width'] == 512

# Browser Action 14 > Get windows Position
# current_position = driver.get_window_position()
# print(current_position)

# Browser Action 16 > Set window position
# driver.set_window_position(x=500, y=200)

# Browser Action 17 > Maximize
driver.minimize_window()
sleep(2)

# Browser Action 18 > Maximize
driver.maximize_window()
sleep(2)

# Browser Action 19 > Full screen window
driver.fullscreen_window()
sleep(2)


driver.quit()
