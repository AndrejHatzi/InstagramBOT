from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
driver = webdriver.Firefox()

class Pessoa:
	def __init__(proprio, email, password, hashtag):
		proprio.email = email
		proprio.password = password
		proprio.hashtag = hashtag
		
	def login_to_instagram(proprio):
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
		
	def scrap_comments(proprio):
		for elem in driver.find_elements_by_xpath('.//span'):
			texto_em_span = elem.text
			with open('trash' , 'a') as f:
				try:
					f.write(texto_em_span + '\n')
				except:
					pass
					
	def procurar_fotos(proprio):
		driver.get('https://www.instagram.com/explore/tags/' + proprio.hashtag + '/?hl=pt')
		time.sleep(1.67)
		for i in range(4, 6):
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
					actions = ["Gosto", "Seguir", "Nada", "Comentar"]
					x = random.choice(actions)
					print(x)
					if x == "Gosto":
						driver.find_element_by_link_text("Gosto").click()
						time.sleep(t)
					if x == "Seguir":
						yo = driver.find_element_by_xpath("/html/body/span/section/main/div/div/article/header/div[2]/div[1]/div[2]/span[2]/button")
						yo.click()                     
						time.sleep(t)
					if x == "Comentar":
						with open('trash', 'r', encoding='utf-8') as m:
							try:
								comment_hashtags = m.read()
							except:
								pass
					
						comment_hashtags = comment_hashtags                        
						z = [x for x in comment_hashtags.split() if x.startswith('#')]
				
						with open('processed.byhash', 'a') as mine:
							for i in range(len(z)):
								try:
									mine.write(str(z[i]) + '\n')
								except:
									pass
								
						with open('processed.byhash', 'r', encoding='utf-8') as p:
							current_comment = p.read()
							
						current_comment = current_comment.splitlines()
						indice_comm = random.randint(0, len(current_comment))
						next_comment = current_comment[indice_comm]  
						time.sleep(2)
						el = driver.find_element_by_xpath("/html/body/span/section/main/div/div/article/div[2]/section[3]/form/textarea")
						time.sleep(1)
						el.send_keys(next_comment)
						actions = ActionChains(driver)
						actions = actions.send_keys(Keys.ENTER)
						actions.perform()
						print(next_comment)
						time.sleep(t)
					if x == "Nada":
						time.sleep(t - 2)
						pass   
				except Exception as e:
					time.sleep(2)
		
		
maria = Pessoa('youremail@gmail.com', 'yourpassword', 'yourtag')
maria.login_to_instagram()
maria.procurar_fotos()
