# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:43:06 2021

@author: Alberto Sánchez & Sergio Romero
"""

import requests
from bs4 import BeautifulSoup
import csv

class NBAStatsScraper():
    
    def __init__(self, team, season):
        self.url = "https://www.nba.com/%s/stats?season=%s" % (team, season)
        self.teamStats = []

    def scrape(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        bodyStats = soup.find_all("table", {"class": "season-totals"})[0].find_all("tbody");

        # Para cada jugador, recorremos la las celdas de la fila correspondiente para recoger
        # todas sus estadísticas
        for row in bodyStats[0].find_all("tr"):
            player_name = row.find_all("span", {"class": "playerName"})[0].find("a").find(text=True)
            
            tdStats = row.find_all("td", {"class": "gp"})    
            if tdStats:
                games_played = tdStats[0].find(text=True)
            else:
                games_played = "-"
                
            tdStats = row.find_all("td", {"class": "pts"})
            if tdStats:
                points = tdStats[0].find(text=True)
            else:
                points = "-"
            
        
            tdStats = row.find_all("td", {"class": "fg_pct"})
            if tdStats:
                field_goals_pct = tdStats[0].find(text=True)
            else:
                field_goals_pct = "-"
        
            tdStats = row.find_all("td", {"class": "fg3_pct"})
            if tdStats:
                three_point_pct = tdStats[0].find(text=True)
            else:
                three_point_pct = "-"
        
            tdStats = row.find_all("td", {"class": "ft_pct"})
            if tdStats:
                free_throw_pct = tdStats[0].find(text=True)
            else:
                free_throw_pct = "-"
        
            tdStats = row.find_all("td", {"class": "oreb"})
            if tdStats:
                offensive_rebounds = tdStats[0].find(text=True)
            else:
                offensive_rebounds = "-"
        
            tdStats = row.find_all("td", {"class": "dreb"})
            if tdStats:
                deffensive_rebounds = tdStats[0].find(text=True)
            else:
                deffensive_rebounds = "-"
        
            tdStats = row.find_all("td", {"class": "reb"})
            if tdStats:
                rebounds = tdStats[0].find(text=True)
            else:
                rebounds = "-"
        
            tdStats = row.find_all("td", {"class": "ast"})
            if tdStats:
                assists = tdStats[0].find(text=True)
            else:
                assists = "-"
        
            tdStats = row.find_all("td", {"class": "stl"})
            if tdStats:
                steals = tdStats[0].find(text=True)
            else:
                steals = "-"
        
            tdStats = row.find_all("td", {"class": "tov"})
            if tdStats:
                turnovers = tdStats[0].find(text=True)
            else:
                turnovers = "-"
        
            tdStats = row.find_all("td", {"class": "pf"})
            if tdStats:
                fouls = tdStats[0].find(text=True)
            else:
                fouls = "-"
        
            playerStats = [player_name, games_played, points, field_goals_pct, three_point_pct, free_throw_pct, offensive_rebounds, deffensive_rebounds, rebounds, assists, steals, turnovers, fouls]
            self.teamStats.append(playerStats)
            
            # Guardamos la foto del jugadores
            picture_url = "https:" + row.find("img", {"class": "headshot"})["src"]
            r = requests.get(picture_url, stream = True)
            if r.status_code == 200:
                aSplit = picture_url.split('/')
                ruta = "Pictures/" + aSplit[len(aSplit)-1]
                print(ruta)
                with open(ruta, "wb") as picOutput:
                    for chunk in r:
                        picOutput.write(chunk)

    def data2csv(self, filename):
        cabecera="Jugador, Partidos, Puntos, FG%, 3PT%, FT%, OffReb, DefReb, Rebotes, Asistencias, Recuperaciones, Perdidas"
        with open(filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([cabecera])
            for playerStats in self.teamStats:
                writer.writerow(playerStats)