import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options

PATH ="C:\Program Files (x86)\chromedriver.exe"

search_term = input()

def check_number(search_term):
	if search_term.isdigit() and len(search_term)==7:
		return True
	else:
		return False

def get_results(search_term):

	url = "https://www.registre-entreprises.tn/search/ExtraitRegistre.do?action=getPage&&name=0"
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	browser = webdriver.Chrome(PATH,options=options)
	browser.get(url)
	search_box = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/form/div/div/div/div[2]/input")
	search_box.send_keys(search_term)
	search_box.submit()

	texts = browser.find_elements_by_xpath("/html/body/div[1]/form[1]/div/div/div/div/table/tbody/tr[8]/td[2]/table/tbody/tr[2]/td[1]")
	results = []
	for text in texts:
		results.append(text)
	browser.close()
	return results

if(check_number(search_term)):
	if(get_results(search_term)):
		print("true")
	else:
		print("false")


