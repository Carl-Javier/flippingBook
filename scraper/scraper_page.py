import scraper.constants as const
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from scraper.export import ExportExcelFile
import datetime

class PageAutomation:
    def __init__(self, driver):
        self.driver = driver
        driver.get(const.BASE_URL)
        driver.maximize_window()
        

    def login_page_bot(self):
        wait = WebDriverWait(self.driver, 20)
        user_name = wait.until(EC.presence_of_element_located((By.XPATH, "//form//div[@class='PA-LoginForm__field']//input[@name='username']")))
        user_name.send_keys(const.USERNMAE)
        passw = wait.until(EC.presence_of_element_located((By.XPATH, "//form//div[@class='PA-LoginForm__field']//input[@name='password']")))
        passw.send_keys(const.PASSWORD)

        submit = wait.until(EC.presence_of_element_located((By.XPATH, "//form//div[@class='PA-LoginForm__buttons']//button")))
        submit.click()

    def book_list_bot(self):
        wait = WebDriverWait(self.driver, 20)
        time.sleep(20)
        elemms = self.driver.find_elements(By.XPATH, "//table//div[@class='FBO-Publications-Table-Row-Name__name']//a")
        books = []
        for item in elemms:
            data = {
                'book_name': item.text,
                'url': item.get_attribute('href'),
            }
            books.append(data)
        
        excelData = []
        for data in books:
            wait.until(EC.presence_of_element_located((By.XPATH, "//table//div[@class='FBO-Publications-Table-Row-Name__nameWrapper']//a")))
            date = datetime.datetime.now() - datetime.timedelta(days=1)
            params = '?current-section=performance&end-date='+date.strftime('%Y-%m-%d')+'&performance-chart=Views&selected-grouping-type=daily&start-date='+date.strftime('%Y-%m-%d')
            
            self.driver.get(data['url']+"/stats/"+params)
            views = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='Views']//span[@class='PA-ChartTabs-Tab__value']/span")))
            visitors = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='Visitors']//span[@class='PA-ChartTabs-Tab__value']/span")))
            downloads = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='Downloads']//span[@class='PA-ChartTabs-Tab__value']/span")))
            time.sleep(5)
            items = {
                'book_name':data['book_name'],
                'views': views.text,
                'visitors': visitors.text,
                'downloads': downloads.text
            }
            excelData.append(items)
            self.driver.get(const.LIST_PAGE)

        export = ExportExcelFile(data=excelData)
        export.generate_excel()