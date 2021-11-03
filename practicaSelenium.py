# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:52:02 2021

@author: Alberto Sánchez & Sergio Romero
"""

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



from time import sleep

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.implicitly_wait(5)

"""Abro la página de la NBA"""
driver.get("https://www.nba.com/players")

"""Acepto las cookies"""
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

sleep(2)


"""Selecciono el valor que quiero"""
comboPosiciones =  Select(driver.find_element(By.NAME, 'POSITION'))
todaspaginas=Select(driver.find_element(By.XPATH, '//*[@title="Page Number Selection Drown Down List"]'))


sleep(2)
guards=comboPosiciones.select_by_visible_text('Guard')
sleep(5)

sleep(2)
todaspaginas.select_by_visible_text('All')
sleep(5)


sleep(2)
forwards=comboPosiciones.select_by_visible_text('Forward')
sleep(5)

sleep(2)
todaspaginas.select_by_visible_text('All')
sleep(5)


sleep(2)
forwards=comboPosiciones.select_by_visible_text('Center')
sleep(5)

sleep(2)
todaspaginas.select_by_visible_text('All')
sleep(5)

