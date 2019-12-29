from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
driver = webdriver.Firefox()

class Pessoa(object):
    def __init__(proprio, email, password, hashtag):
        proprio.email = email
        proprio.password = password
        proprio.hashtag = hashtag
        
    def comment(proprio):
        with open('trash', 'r') as f:
            comment_hashtags = f.read()
                    
        filtro = [hashtag for hashtag in comment_hashtags.split() if hashtag.startswith('#')]
        filtro = [i for i in filtro if len(i) <= 10]

        next_comm = random.choice(filtro)
        el = driver.find_element_by_xpath("/html/body/span/section/main/div/div/article/div[2]/section[3]/form/textarea").click()
        el.send_keys(next_comm)
        print(str(next_comm))
        time.sleep(5)
        actions = ActionChains(driver)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()
        
    def like(proprio):
        driver.find_element_by_link_text("Gosto").click()
        time.sleep(2)
    
    def follow(proprio):
        follow_button = driver.find_element_by_xpath("/html/body/span/section/main/div/div/article/header/div[2]/div[1]/div[2]/span[2]/button")
        follow_button.click()
        time.sleep(2)
    
    def nothing(proprio):
        pass
    
    
    def login(proprio):
        driver.get('https://www.instagram.com/?hl=pt')
        time.sleep(1)
        inputs = driver.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[1]/div/form/span/button")
        inputs.click()
        elem = driver.find_element_by_id("email")
        elem.send_keys(proprio.email)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(proprio.password)
        driver.find_element_by_id("loginbutton").click()
        time.sleep(8)
    
    def main_activity(proprio):
        driver.get('https://www.instagram.com/explore/tags/' + proprio.hashtag + '/?hl=pt')
        time.sleep(1.67)
        
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.37)
            hrefs = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
            pic_hrefs = [href for href in pic_hrefs if proprio.hashtag in href]
            print(proprio.hashtag + 'photos' + str(len(pic_hrefs)))
            
            for pic_href in pic_hrefs:
                t = random.randint(13, 25)
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                for elem in driver.find_elements_by_xpath('.//span'):
                    texto_em_span = elem.text
                    with open('trash' , 'a') as f:
                        try:
                            f.write(texto_em_span + '\n')
                        except:
                            pass
                    
                try:
                    t = random.randint(13, 25)
                    actions = ["Gosto", "Seguir", "Nada", "Comentar"]
                    next_mov = random.choice(actions)
                    print(next_mov)
                    
                    if next_mov == "Gosto":
                        proprio.like()
                        time.sleep(t)
                        
                    if next_mov == "Seguir":
                        proprio.follow()
                        time.sleep(t)
                                   
                    if next_mov == "Nada":
                        proprio.nothing()
                        time.sleep(t)
                        
                    if next_mov == "Comentar":
                        proprio.comment()
                        time.sleep(t)
                    
                except Exception as e:
                    time.sleep(2)
            
        


Maria = Pessoa('youremail@gmail.com', 'yourpassword', 'foodporn')
Maria.login()
Maria.main_activity()
time.sleep(1)
















'''
driver.get('https://www.instagram.com/p/Bje5gNulrwc/?taken-by=ricardo.jb.ferreira')
#Maria.like()
#time.sleep(30)
with open('trash', 'r') as f:
    comment_hashtags = f.read()               
filtro = [hashtag for hashtag in comment_hashtags.split() if hashtag.startswith('#')]
filtro = [i for i in filtro if len(i) <= 10]
next_comm = random.choice(filtro)
#el = driver.find_element_by_xpath("/html/body/span/section/main/div/div/article/div[2]/section[3]/form/textarea")
el = driver.find_element_by_class_name('Ypffh')
el.send_keys(next_comm)
print(str(next_comm))
actions = ActionChains(driver)
actions = actions.send_keys(Keys.ENTER)
actions.perform()
'''
