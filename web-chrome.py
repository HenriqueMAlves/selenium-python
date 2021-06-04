import time
import platform
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


device = platform.system()

# delay until timeout
delay = 5

ca_number = '498'

op = webdriver.ChromeOptions()
op.add_argument('headless')

if device == 'Darwin':
    driver = webdriver.Chrome(
        executable_path=r'geckodriver/chrome/chromedriver-mac')#, options=op)
elif device == 'Windows':
    driver = webdriver.Chrome(
        executable_path=r'geckodriver\chrome\chromedriver-win.exe', options=op)
elif device == 'Linux':
    driver = webdriver.Chrome(
        executable_path=r'geckodriver/chrome/chromedriver-linux', options=op)

driver.get('http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx')

try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.NAME, 'ctl00$PlaceHolderConteudo$txtNumeroCA')))
    elem.send_keys(ca_number + Keys.ENTER)

    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.NAME, 'ctl00$PlaceHolderConteudo$grdListaResultado$ctl02$btnDetalhar')))
    elem.click()

    elem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, 'PlaceHolderConteudo_lblSituacao')))
    situation = elem.text
    print('Situação: ' + situation)

    elem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, 'PlaceHolderConteudo_lblDTValidade')))
    validity = elem.text
    print('Validade: ' + validity)

    driver.quit()

    if(situation == 'VÁLIDO'):
        status = True
    else:
        status = False

except TimeoutException:
    driver.quit()
