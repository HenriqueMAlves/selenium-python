import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#select your device (macos, win64 or linux64)
device = 'mac' 
# device = 'win' 
# device = 'linux'

# delay until timeout
delay = 5

op = webdriver.ChromeOptions()
op.add_argument('headless')

if device == 'mac':
    driver = webdriver.Chrome(executable_path=r'geckodriver/chrome/chromedriver-mac')#, options=op)
elif device == 'win':
    driver = webdriver.Chrome(executable_path=r'geckodriver\firefox\chromedriver-win.exe', options=op)
elif device == 'linux':
    driver = webdriver.Chrome(executable_path=r'geckodriver/firefox/chromedriver-linux', options=op)

driver.get('http://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx')

elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'ctl00$PlaceHolderConteudo$txtNumeroCA')))
elem.send_keys('11111' + Keys.ENTER)

elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'ctl00$PlaceHolderConteudo$grdListaResultado$ctl02$btnDetalhar')))
elem.click()

elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'PlaceHolderConteudo_lblSituacao')))
print('Situação: ' + elem.text)

elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'PlaceHolderConteudo_lblDTValidade')))
print('Validade: ' + elem.text)

driver.quit()


### caixa de pesquisa CA -
#<input name="ctl00$PlaceHolderConteudo$txtNumeroCA" 
# type="text" maxlength="6" id="txtNumeroCA" style="width:130px;">

### Conteudo CA -
#<input type="image" name="ctl00$PlaceHolderConteudo$grdListaResultado$ctl02$btnDetalhar"
# id="PlaceHolderConteudo_grdListaResultado_btnDetalhar_0" src="../Content/Imagens/ico_texto.gif">

### Situação CA -
#<span id="PlaceHolderConteudo_lblSituacao" style="color:Red;">VENCIDO</span>

### Validade CA - 
# <span id="PlaceHolderConteudo_lblDTValidade" style="color:Red;">24/10/2005 00:00:00</span>