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
import csv

#Función para mostrar todos los jugadores de una posición que paso por parámetro
def muestraPosicion(combo, posicion):
    sleep(2)
    combo.select_by_visible_text(posicion)
    sleep(5)

    sleep(2)
    #OJO, FORZAMOS A QUE CAMBIE LA PAGINACIÓN 2 VECES
    #Si no forzamos el cambio, al cambiar entre posiciones la paginación de 'All' no funciona!!!
    todaspaginas.select_by_visible_text('1')
    todaspaginas.select_by_visible_text('All')
    sleep(5)

#Función para crear un dataset con un nombre concreto y una lista de jugadores    
def data2csv(filename, rows):
    with open(filename, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for trJugador in rows:
            # Get the columns (all the column 2)        
            datosJugador = trJugador.find_elements(By.CLASS_NAME, "text") 
            nombreJugador=datosJugador[0].text
            nombreJugador=nombreJugador.replace('\n', ' ').replace('\r', '')
            equipo=datosJugador[1].text
            posicion=datosJugador[2].text
            parametrosJugador=[nombreJugador, equipo, posicion]
            writer.writerow(parametrosJugador)



s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.implicitly_wait(5)

#Abro la página de la NBA
driver.get("https://www.nba.com/players")

#Aceptamos las cookies
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

sleep(2)

#Seleccionamos el combo de posiciones para elegir entre bases, aleros y pivots
comboPosiciones =  Select(driver.find_element(By.NAME, 'POSITION'))
#Tocamos la paginación para mostrar todos los elementos
todaspaginas=Select(driver.find_element(By.XPATH, '//*[@title="Page Number Selection Drown Down List"]'))

#Trabajamos con los bases

#Llamamos a la función para mostrar todos los bases sin paginación
muestraPosicion(comboPosiciones, 'Guard')
#obtenemos la lista de jugadores
listaJugadores=driver.find_element(By.CLASS_NAME, 'players-list')
rows = listaJugadores.find_elements(By.TAG_NAME, "tr") 
#los exportamos al dataset
data2csv("Bases.csv", rows)

#Repetimos la operación anterior para aleros
muestraPosicion(comboPosiciones, 'Forward')
listaJugadores=driver.find_element(By.CLASS_NAME, 'players-list')
rows = listaJugadores.find_elements(By.TAG_NAME, "tr")
data2csv("Aleros.csv", rows)

#Repetimos la operación para pívots
muestraPosicion(comboPosiciones, 'Center')
listaJugadores=driver.find_element(By.CLASS_NAME, 'players-list')
rows = listaJugadores.find_elements(By.TAG_NAME, "tr") 
data2csv("Pivots.csv", rows)






