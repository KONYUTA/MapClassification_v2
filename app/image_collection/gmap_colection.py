import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

print('地図の収集をはじめます(´･ω･`)\n')
index = 1
with open('../../data/bussoxn_h29_r2.csv') as f_in:
    time.sleep(1)
    for line in f_in:
        if(index>29378):
            coord = line.split(',')
            # File Name
            FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data/image/"+str(index)+".png")

            #オプションの設定
            options = Options()
            options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            options.add_argument('--headless')

            # set driver and url
            driver = webdriver.Chrome(options=options)
            url = 'https://google.co.jp/maps/@'+coord[0]+','+coord[1]+',20z?hl=ja'

            # set window size
            driver.set_window_size(350,350)
            driver.get(url)
            time.sleep(0.5)
            script = """
                elements = document.getElementsByClassName("NaMBUd")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("m6QErb")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("gb_3a")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("scene-footer")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("lTfMvb")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("JLm1tf")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("Hk4XGb")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("top-center-stack")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                elements = document.getElementsByClassName("app-viewcard-strip")
                elements = Array.from( elements )
                elements.forEach(element => element.remove())
                """
            try:
                driver.execute_script(script)
                time.sleep(0.5)

                # Get Screen Shot
                #driver.save_screenshot('../../data/image/'+str(index)+'.png')
                png = driver.find_element_by_id('scene').screenshot_as_png
                with open('../../data/image/'+str(index)+'.png', 'wb') as f:
                        f.write(png)
                #png = driver.find_element_by_class_name('id-scene').screenshot_as_png
            except selenium.common.exceptions.NoSuchElementException:
                index -= 1

            driver.quit()
            print(str(index)+'番目の地点周辺マップを保存しましたよ(´・ω・)',end="\r")
        index+=1
print('(´・ω・)(´･ω･`)(´・ω・)(´・ω・)\n終わりますよ(´・ω・)')
