# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:43:06 2021

@author: Alberto Sánchez & Sergio Romero
"""

import requests
from bs4 import BeautifulSoup
import csv

class NBAStatsScraper():
    """

    La clase NBAStatsScraper implementa el scraper para la descarga de estadísticas y fotos de 
    jugadores de la página web www.nba.com. La información se encuentra dentro de la página del
    equipo de cuyos jugadores nos queremos baja la información.
    
    La información del equipo y la temporada para la cual vamos a descargar la información se
    recibirá como parámetro a la hora de inicializar la clase.

    """   
    def __init__(self, team, season):
        # Inicialización de la clase.
        self.team = team
        self.season = season
        
        # URL de la página web que contiene la información a descargar. Esta URL se forma con
        # dos parámetros que se pasan al inicializar la clase: el nombre del equipo y la
        # temporada
        self.url = "https://www.nba.com/%s/stats?season=%s" % (team, season)
        
        # Array donde guardamos la información que nos vamos a descargar de la página.
        # Cada elemento del array contiene la informción de un jugador.
        self.teamStats = []

    def scrape(self):
        # El método scrape se encarga de recorrer la página guardando la información en el
        # atributo teamStats.

        def descargarEquipo(soup):
            # Descarga la información de un equipo específico. La página parseada se pasa en la
            # variable soup
            
            # Las información que necesitamos se encuentra en la talba de clase season-totals
            bodyStats = soup.find_all("table", {"class": "season-totals"})[0].find_all("tbody");
    
            # Para cada jugador, recorremos la las celdas de la fila correspondiente para recoger
            # todas sus estadísticas.
            # No todos los jugadores tienen toda la información por lo que debemos controlas posibles
            # valores vacíos.
            for row in bodyStats[0].find_all("tr"):
                # Nombre del jugador
                player_name = row.find_all("span", {"class": "playerName"})[0].find("a").find(text=True)
                
                # Partidos jugados
                tdStats = row.find_all("td", {"class": "gp"})    
                if tdStats:
                    games_played = tdStats[0].find(text=True)
                else:
                    games_played = "-"
                    
                # Puntos
                tdStats = row.find_all("td", {"class": "pts"})
                if tdStats:
                    points = tdStats[0].find(text=True)
                else:
                    points = "-"
                
                # Porcentaje de tiros de campo
                tdStats = row.find_all("td", {"class": "fg_pct"})
                if tdStats:
                    field_goals_pct = tdStats[0].find(text=True)
                else:
                    field_goals_pct = "-"
            
                # Porcentaje de tiros de tres
                tdStats = row.find_all("td", {"class": "fg3_pct"})
                if tdStats:
                    three_point_pct = tdStats[0].find(text=True)
                else:
                    three_point_pct = "-"
            
                # Porcentaje de tiros libres
                tdStats = row.find_all("td", {"class": "ft_pct"})
                if tdStats:
                    free_throw_pct = tdStats[0].find(text=True)
                else:
                    free_throw_pct = "-"
            
                # Rebotes ofensivos
                tdStats = row.find_all("td", {"class": "oreb"})
                if tdStats:
                    offensive_rebounds = tdStats[0].find(text=True)
                else:
                    offensive_rebounds = "-"
            
                # Rebotes defensivos
                tdStats = row.find_all("td", {"class": "dreb"})
                if tdStats:
                    deffensive_rebounds = tdStats[0].find(text=True)
                else:
                    deffensive_rebounds = "-"
            
                # Rebotes totales
                tdStats = row.find_all("td", {"class": "reb"})
                if tdStats:
                    rebounds = tdStats[0].find(text=True)
                else:
                    rebounds = "-"
            
                # Asistencias
                tdStats = row.find_all("td", {"class": "ast"})
                if tdStats:
                    assists = tdStats[0].find(text=True)
                else:
                    assists = "-"
            
                # Recuperaciones
                tdStats = row.find_all("td", {"class": "stl"})
                if tdStats:
                    steals = tdStats[0].find(text=True)
                else:
                    steals = "-"
            
                # Perdidas
                tdStats = row.find_all("td", {"class": "tov"})
                if tdStats:
                    turnovers = tdStats[0].find(text=True)
                else:
                    turnovers = "-"
            
                # Faltas personales
                tdStats = row.find_all("td", {"class": "pf"})
                if tdStats:
                    fouls = tdStats[0].find(text=True)
                else:
                    fouls = "-"
            
                # Guardamos la información recopilada en el atributo teamStats
                playerStats = [player_name, games_played, points, field_goals_pct, three_point_pct, free_throw_pct, offensive_rebounds, deffensive_rebounds, rebounds, assists, steals, turnovers, fouls]
                self.teamStats.append(playerStats)
                
                # Guardamos la foto del jugadores
                picture_url = "https:" + row.find("img", {"class": "headshot"})["src"]
                r = requests.get(picture_url, stream = True)
                if r.status_code == 200:
                    # Las fotos se guardan en la carpeta Pictures con el nombre del jugador.
                    ruta = "Pictures\\" + player_name.replace(" ", "_") + ".png"
                    with open(ruta, "wb") as picOutput:
                        for chunk in r:
                            picOutput.write(chunk)        

        
        # Si el nombre del equipo no es 'all'
        if self.team != 'all': 
            # Cogemos el contenido de la página del equipo
            url = "https://www.nba.com/%s/stats?season=%s" % (self.team, self.season)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            descargarEquipo(soup)
        # Si el nombre es 'all', vamos a descargar la información de todos los equipos
        else:
            teamNames = ['celtics', 'nets', 'sixers', 'raptors', 'bulls', 'cavaliers', 'pistons', 
             'pacers', 'bucks', 'hawks', 'hornets', 'heat', 'magic', 'wizards', 'nuggets', 'timberwolves',
             'thunder', 'blazers', 'jazz', 'warriors', 'clippers', 'suns', 'kings', 'rockets',
             'grizzlies', 'pelicans', 'spurs']
            # Recorremos todos los equipos
            for x in teamNames:
                # Cogemos el contenido de la página del equipo
                print('Guardando información de ' + x)
                url = "https://www.nba.com/%s/stats?season=%s" % (x, self.season)
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                descargarEquipo(soup)


    def data2csv(self, filename):
        # El método data2csv guarda toda la información del atributo teamStats en un fichero
        # CSV
        
        # Cabecera del fichero
        cabecera = ['Jugador', 'Partidos', 'Puntos', 'FG%', '3PT%', 'FT%', 'OffReb', 'DefReb', 'Rebotes', 'Asistencias', 'Recuperaciones', 'Perdidas', 'Faltas']
        
        # Creamos el fichero csv.
        with open(filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(cabecera)
            # Por cada elemento del array teamStats creamos una línea en el fichero
            for playerStats in self.teamStats:
                writer.writerow(playerStats)