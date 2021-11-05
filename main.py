# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:43:06 2021
@author: Alberto Sánchez & Sergio Romero
"""

# Importamos la clase NBAStatsScraper que tiene toda la lógica del scraper
from scraper import NBAStatsScraper

import re

# El script pide dos parámetros: el nombre del equipo y la temporada

# Equipo
team = ""
teamNames = ['all', 'celtics', 'nets', 'sixers', 'raptors', 'bulls', 'cavaliers', 'pistons', 
             'pacers', 'bucks', 'hawks', 'hornets', 'heat', 'magic', 'wizards', 'nuggets', 'timberwolves',
             'thunder', 'blazers', 'jazz', 'warriors', 'clippers', 'suns', 'kings',
             'rockets', 'grizzlies', 'pelicans', 'spurs']
while team == "":
    print("Elija el equipo: ")
    team = input()
    # Comprobamos que el nmbre introducido corresponda con el de un equipo válido.
    if (not team in teamNames):
        print('Debe introducir un equipo válido:')
        print(teamNames)
        team = ""

# Temorada
pattern = re.compile('[0-9]{4}-[0-9]{2}')
season = ''
while season == '':
    print("Elija la temporada (formato aaaa-aa): ")
    season = input()
    # Comprobamos la cadena introducida tiene el formato válido
    if pattern.match(season) is None:
        print('Debe introducir una temporda válida')
        season = ''

# El nombre del fichero será equipo_temporada.csv
output_file = "%s_%s.csv" % (team, season)

try:
    # Iniciaizamos la clase NBAStatsScraper
    scraper = NBAStatsScraper(team, season);
    # Cogemos los datos
    scraper.scrape();
    # Exportamos el dataset al fichero csv
    scraper.data2csv(output_file);

    print("La información se ha guardado correctamente.")
except:
    print("Se ha procudido un error durante el proceso.")