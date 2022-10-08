import sqlite3 as sq
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
from selenium.webdriver.chrome.options import Options
import pyautogui


db = 'secure.db'
 
 
def connect():
   
    
    conn = sq.connect(db)
     
    
    c = conn.cursor()
     
    
    c.execute("""
                 CREATE TABLE IF NOT EXISTS data (
                     nom text,
                     adresse text,
                     ville text,
                     numero text


                     
                 )             
    """)
    items = c.fetchall()
    for item in items:
        print(item)
     
    # to commit the sql command, it will commit the
    # current transaction or
    conn.commit()
    conn.close()
 
 
def enter(url):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES(?)", (url))
    conn.commit()
    conn.close()
 
 
def show():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
     
    # ça va stocker toutes les données de la table à
    # la variable i sous forme de liste 2d
    i = c.fetchall()
    conn.commit()
    conn.close()
    return i

def URL(url):
    
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #os.environ['PATH'] += r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\SelniumDrivers"
    driver = webdriver.Chrome(executable_path=r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\chromedriver.exe",chrome_options=options)
    driver.maximize_window() 
    driver.implicitly_wait(2)
    driver.get(url)
    for i in range(1,107,1):
        button = driver.find_element(by=By.XPATH,value=f'//*[@id="id_bouton_appeler_{i}"]')
        button.click()
        if i == 1:
            time.sleep(3)
        else:
            time.sleep(2)

        pyautogui.click(1287, 283)
        try:
            conn = sq.connect(db)
            c = conn.cursor()
            ville = driver.find_element(by=By.XPATH,value=f'//*[@id="main-content"]/section[2]/div[{i+1}]/div[2]/div/div[3]/div[1]').text
            nom = driver.find_element(by=By.XPATH,value=f'//*[@id="main-content"]/section[2]/div[{i+1}]/div[2]/div/div[1]/div/a/h4').text
            num = driver.find_element(by=By.XPATH,value=f'//*[@id="div-tel_{i}"]/a/div').text
            adresse = driver.find_element(by=By.XPATH,value=f'//*[@id="main-content"]/section[2]/div[{i+1}]/div[2]/div/div[2]/span').text
            c.execute("INSERT INTO data VALUES(?,?,?,?)", (nom,adresse,ville,num))
            conn.commit()
            conn.close()
        except:
            print(f"probleme à la ligne {i}")
            pass


def NOM(url):
    conn = sq.connect(db)
    c = conn.cursor()

    i = c.fetchall()
    conn.commit()
    conn.close()
    

    response=requests.get(url)
    soup =BeautifulSoup(response.content,'lxml')

    list_items = soup.find_all('div',{'class':'row card-strip pt-4 pb-4'})

    nom=[result.find('h4').get_text() for result in list_items]
    return nom
def data():
    conn = sq.connect(db)
    c = conn.cursor()

    i = c.fetchall()
    conn.commit()
    conn.close()
    

    response=requests.get(url)
    soup =BeautifulSoup(response.content,'lxml')

    list_items = soup.find_all('div',{'class':'row card-strip pt-4 pb-4'})
    longueur=len(list_items)
    return longueur
def ADRESSE(url):
    conn=sq.connect(db)
    c= conn.cursor()

    i =c.fetchall()
    conn.commit()
    conn.close()

    response= requests.get(url)
    soup=BeautifulSoup(response.content,'lxml')

    list_itemes = soup.find_all('div',{'class':'mt-2 mt-md-0'})
    adresse=[result.find('span').get_text().strip() for result in list_items]
    return adresse

def VILLE(url):
    conn = sq.connect(db)
    c = conn.cursor()
    
     
    i = c.fetchall()
    conn.commit()
    conn.close()
    response= requests.get(url)
    soup=BeautifulSoup(response.content,'lxml')

    list_items = soup.find_all('div',{'class':'row card-strip pt-4 pb-4'})
    ville=[result.get_text().strip() for result in list_itemes]
    return ville


def NUM(url):
    conn = sq.connect(db)
    c = conn.cursor()
    
     
    i = c.fetchall()
    conn.commit()
    conn.close()
    response= requests.get(url)
    soup=BeautifulSoup(response.content,'lxml')
    list_items = soup.find_all('div',{'class':'row card-strip pt-4 pb-4'})
    telephone = []
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

    time.sleep(20000)
    return telephone

 
def check():
    # cette fonction vérifiera si la base de données
    # est vide ou non
    if len(show()) == 0:
        return False
    else:
        return True

def precedentId():
    data=c.execute(SELECT * FROM)

os.remove("secure.db")
connect()
