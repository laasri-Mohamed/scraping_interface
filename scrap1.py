
import pandas as pd
from bs4 import BeautifulSoup
import requests 
import time

import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pyautogui




#buttons = driver.find_element(by=By.XPATH, value='//div[@class="btn btn-orange mt-2 mt-md-3 mb-1"]')

url="https://agroalimentaire.e-pro.fr/rhone/industries-alimentaires-n-c-a_a_Lyon,69123,158V"

response=requests.get(url)
soup =BeautifulSoup(response.content,'lxml')


#LE NOM DE L'ENTREPRISE
list_items = soup.find_all('div',{'class':'row card-strip pt-4 pb-4'})
#print(list_items[0].find('h4').get_text())
#LA VILLE
list_itemes = soup.find_all('div',{'class':'mt-2 mt-md-0'})
#print(list_itemes[0].get_text().strip())
#L'ADRESSE
print(list_items[0].find('span').get_text().strip())
#LE NUMERO DE TELEPHONE
#list_itemees = soup.find_all('div',{'class':'numabouthi'})
#print(len(list_itemees))
#print(list_itemees[0].get_text())
#list_itemeees=soup.find_all('div',{'class':'mt-2 mb-2 mt-md-3'})
#print(list_itemeees[0].find('span').find('href'))
#print(len(list_itemeees))

nomEntreprise=[result.find('h4').get_text() for result in list_items]
ville=[result.get_text().strip() for result in list_itemes]
adresses=[result.find('span').get_text().strip() for result in list_items]
#numTelephone=[result.get_text().strip() for result in list_itemees]
time.sleep(1)
telephone = []
os.environ['PATH'] += r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\SelniumDrivers"
driver =webdriver.Chrome() 
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://agroalimentaire.e-pro.fr/rhone/industries-alimentaires-n-c-a_a_Lyon,69123,158V")
for i in range(1,len(list_items)+1,1):
    button = driver.find_element(by=By.XPATH,value=f'//*[@id="id_bouton_appeler_{i}"]')
    button.click()
    if i == 1:
            time.sleep(3)
    else:
        time.sleep(2)

    pyautogui.click(1258, 276)
    try:
        button = driver.find_element(by=By.XPATH,value=f'//*[@id="div-tel_{i}"]/a/div').text
        telephone.append(button)
    except:
        print(f"probleme à la ligne {i}")
        pass


print(nomEntreprise)
print(ville)
print(adresses)
print(telephone)


time.sleep(20000)



#print(numTelephone)

#imdb_df=pd.DataFrame({'NomEntreprise':nomEntreprise,'Ville':ville,'Adresse':adresses,'Num Telephne':numTelephone})
#print(imdb_df)
#imdb_df.to_excel('InfoEnterorise1.xlsx',index=False)
#imdb_df.to_csv('./data/infoEnteroprise1.csv')


#html_text = requests.get('https://agroalimentaire.e-pro.fr/rhone/industries-alimentaires-n-c-a_a_Lyon,69123,158V').text

#soup = BeautifulSoup(html_text,'lxml')
#print(soup.prettify())

       