# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:43:06 2021

@author: Alberto Sánchez & Sergio Romero
"""

from scraper import NBAStatsScraper

print("Elija el equipo: ")
team = input()
#team = "hawks"
print("Elija la temporada: ")
season = input()
#season = "2021-22"
output_file = "%s_%s.csv" % (team, season)

scraper = NBAStatsScraper(team, season);
scraper.scrape();
scraper.data2csv(output_file);