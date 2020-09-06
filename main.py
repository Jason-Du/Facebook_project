from selenium import webdriver  #從library中引入webdriver

from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
from pyquery import PyQuery as pq
import os
# browser = webdriver.Chrome()    #開啟chrome browser
import time
class Click_more_comment():
	def __init__(self,
				 Btns_all_comment_path_input,
				 Btns_span_comment_path_s1input,
				 Btns_span_comment_path_s2input,
				 Btn_check_comment_input,
				 Btn_below_comment_input,
				 Btn_below_multiple_commemt_input,
				 post_num_input,
				 driver_input
				 ):
		self.Btns_all_comment_path=Btns_all_comment_path_input
		self.Btns_span_comment_path_s1=Btns_span_comment_path_s1input
		self.Btns_span_comment_path_s2=Btns_span_comment_path_s2input
		self.Btn_check_comment=Btn_check_comment_input
		self.Btn_below_comment=Btn_below_comment_input
		self.Btn_below_multiple_comment=Btn_below_multiple_commemt_input
		self.driver=driver_input
		self.post_num=post_num_input+1
	def Click_span_all_comment(self):
		pass
		for comment_index in range(1,self.post_num):
			try:
				Btns_all_comment = self.driver.find_element_by_xpath(self.Btns_all_comment_path.format(comment_index))
				Btns_all_comment.click()
				Btns_span_comment_s1 = self.driver.find_element_by_xpath(self.Btns_span_comment_path_s1.format(comment_index))
				Btns_span_comment_s1.click()
				print("Click_span_all_comment success 1 stage")
				time.sleep(1)
				Btns_span_comment_s2=self.driver.find_element_by_xpath(self.Btns_span_comment_path_s2)
				Btns_span_comment_s2.click()
				print("***************************************")
				print("Click_span_all_comment success 2 stage")
				print("***************************************")
				time.sleep(1)
			except:
				time.sleep(1)
				continue
	def Click_check_comment(self):
		pass
		for comment_index in range(1,self.post_num):
			try:
				print(self.Btn_check_comment.format(comment_index))
				Btn_check_comment=self.driver.find_element_by_xpath(self.Btn_check_comment.format(comment_index))
				print("ttttttttttttttttttttttttttttttttttttttttt")
				Btn_check_comment.click()
				print("***************************************")
				print("Click_check_comment success:{}".format(comment_index))
				print("***************************************")
				time.sleep(1)
			except:
				continue
			# try:
			# 	Btn_check_comment.send_keys("\n")
			# 	print("send_keys()succeses")
			# except:
			# 	pass
			# try:
			# 	Btn_check_comment.submit()
			# 	print("submit() success")
			# except:
			# 	continue


	def Click_comment_below(self):
		pass
		for comment_index in range(1,self.post_num):
			for respondent_index in range(20):
				try:
					Btn_below_comment=self.driver.find_element_by_xpath(self.Btn_below_comment.format(comment_index,respondent_index))
					Btn_below_comment.click()
					print("***************************************")
					print("Click_comment_below success")
					print("***************************************")
					time.sleep(1)
				except:
					pass
				try:
					Btn_below_comment=self.driver.find_element_by_xpath(self.Btn_below_multiple_comment.format(comment_index,respondent_index))
					Btn_below_comment.click()
					print("***************************************")
					print("Click_MULTIPLE_comment_below success")
					print("***************************************")
					time.sleep(1)
				except:
					continue
		htmltext= self.driver.page_source
		return htmltext
class Check_emoji():
	def __init__(self,
				 emoji_span_path_input,
				 emoji_user_path_input,
				 emoji_close_path_input,
				 post_num_input,
				 driver_input
				 ):
		self.emoji_span_path=emoji_span_path_input
		self.emoji_user_path=emoji_user_path_input
		self.emoji_close_path=emoji_close_path_input
		self.post_num = post_num_input+1
		self.driver=driver_input

	def emoji_user_check(self):
		respondent_list=[]
		pass
		for post_index in range(1,self.post_num):
			try:
				test = self.driver.find_element_by_xpath(self.emoji_span_path.format(post_index))
				test.click()
				time.sleep(1)
				print(post_index)
				print("***************************************")
				print("Click_span_emoji success 1 stage ")
				print("***************************************")
			except:
				continue
			for respondent_index in range(1,50):
				try:
					respondent = self.driver.find_element_by_xpath(self.emoji_user_path.format(respondent_index))
					print(respondent_index)
					print(respondent_index)
					print("***************************************")
					print("Click_span_emoji success 2 stage")
					print("***************************************")
					respondent_list.append(respondent.text)
				except:
					test_close = driver.find_element_by_xpath(self.emoji_close_path)
					test_close.click()
					time.sleep(1)
					break
		return respondent_list
class Check_comment():
	def __init__(self,htmltext_input,post_path_input,respondent_path_input,post_num_input):
		self.htmltext=htmltext_input
		self.post_path=post_path_input
		self.respondent_path=respondent_path_input
		self.post_num=post_num_input
		pass
	def comment_user_check(self):
		soup = BeautifulSoup(htmltext,
							 'html.parser'
							 )
		body = soup.find('body')
		respondent_list = []
		for post_index in range(self.post_num):
			try:
				posts = body.select(self.post_path)[post_index]
				for respondent_index in range(1, 20):
					respondent = posts.select(self.respondent_path)[respondent_index]
					print('success scratch the comment.{} respondent_index:{}'.format(post_index,respondent_index))
					respondent = str(respondent)
					respondent = respondent.split(">", 1)[1].split("<", 1)[0]
					respondent_list.append(respondent)
			except:
				continue
		return respondent_list


def data_analyze(comment_persons_list, emoji_persons_list):
	all_persons = list(set(comment_persons_list+emoji_persons_list))
	comment_times = []
	emoji_times = []
	for p in all_persons:
		emoji_times.append(comment_persons_list.count(p))
		comment_times.append(emoji_persons_list.count(p))

	data=[all_persons,comment_times,emoji_times]
	df=pd.DataFrame(dict(ID=all_persons,回復表情次數=emoji_times, 回覆留言次數=comment_times))
	df.to_csv('member_activity.csv', index=False,encoding="utf_8_sig")



if __name__ == '__main__':
	profile = webdriver.FirefoxProfile() # 新增firefox的設定
	profile.set_preference("dom.webnotifications.enabled", False) # 將頁面通知關掉
	profile.update_preferences() # 需要再更新目前firefox新的偏好設定
	driver = webdriver.Firefox(firefox_profile=profile)
	driver.get("http://www.facebook.com")
	time.sleep(2)
	driver.find_element_by_id("email").send_keys("") # 將USERNAME改為你的臉書帳號
	driver.find_element_by_id("pass").send_keys("") # 將PASSWORD改為你的臉書密碼
	driver.find_element_by_id("u_0_b").click()
	time.sleep(2)
	driver.get('https://www.facebook.com/2017%E4%B8%AD%E5%B1%B1%E9%9B%BB%E6%A9%9FX%E9%AB%98%E9%86%AB%E8%AD%B7%E7%90%86%E8%81%AF%E5%90%88%E5%AE%BF%E7%87%9Fx%E6%A9%9F%E4%B8%8D%E6%93%87%E9%A3%9F%E8%AD%B7%E6%80%95who-208102829724714')
	time.sleep(2)
	Test=Click_more_comment(Btns_all_comment_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]" \
							   "/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[1]/div/div[1]/div/div[2]",

							Btns_span_comment_path_s1input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]"
														   "/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]/div[2]/div",

							Btns_span_comment_path_s2input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/div[1]/div",

							Btn_check_comment_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]/div[4]/div/div[2]",
							# 						/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[21]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]/div[4]/div/div[2]

							Btn_below_comment_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]"
											   "/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]/ul/li[{}]/div[2]/div/div/div[2]",

							Btn_below_multiple_commemt_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]"
															 "/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]/ul/li[{}]/div[2]/div/div/div/div[2]",
							post_num_input=15,

							driver_input=driver
							)
	Test.Click_span_all_comment()
	driver.execute_script("window.scroll(0, 0);")
	time.sleep(1)
	# os.system("pause")
	Test.Click_check_comment()
	driver.execute_script("window.scroll(0, 0);")
	time.sleep(1)
	# os.system("pause")
	htmltext=Test.Click_comment_below()
	driver.execute_script("window.scroll(0, 0);")
	time.sleep(1)
	Emoji_test=Check_emoji(emoji_span_path_input="/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[3]/div/div/div[2]"
												 "/div[{}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div",

							emoji_user_path_input="/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]"
												 "/div[{}]/div/div/div[2]/div[1]/div/div/div/span/div/a",

							emoji_close_path_input="/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div",

							post_num_input=15,

							driver_input=driver
						)
	Comment_test=Check_comment(htmltext_input=htmltext,

							   post_path_input='div[class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]',

							   respondent_path_input='span[class="oi732d6d ik7dh3pa d2edcug0 hpfvmrgz qv66sw1b c1et5uql a8c37x1j hop8lmos enqfppq2 e9vueds3 j5wam9gi lrazzd5p oo9gr5id"]',

							   post_num_input=15

							)

	emoji_respondent_list=Emoji_test.emoji_user_check()
	driver.execute_script("window.scroll(0, 0);")
	time.sleep(1)
	comment_respondent_list=Comment_test.comment_user_check()
	driver.execute_script("window.scroll(0, 0);")
	data_analyze(emoji_respondent_list, comment_respondent_list)
	print("tt")

