import requests
import lxml
import time
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


standingsURL = 'https://fbref.com/en/comps/9/11160/2021-2022-Premier-League-Stats'
# data = requests.get(standingsURL)
#
# soup = BeautifulSoup(data.text)
# links = standingsTable.find_all('a')
# links = [l.get('href') for l in links]
# links = [l for l in links if '/squads/' in l]
# teamURLs = [f'https://fbref.com{l}' for l in links]
# data = requests.get(teamURLs[0])
#
# matches = pd.read_html(data.text, match='Scores & Fixtures')[0]
#
# soup = BeautifulSoup(data.text)
#
# links = soup.find_all('a')
#
# links = [l.get('href') for l in links]
#
# links = [l for l in links if l and 'all_comps/shooting/' in l]
#
# data = requests.get(f'https://fbref.com{links[0]}')
#
# shooting = pd.read_html(data.text, match='Shooting')[0]
#
# shooting.columns = shooting.columns.droplevel()
#
# teamData = matches.merge(shooting[['Date', 'Sh', 'SoT', 'Dist', 'FK', 'PK', 'PKatt']], on='Date')

years = list(range(2022, 2015, -1))

allMatches = []

for year in years:
    data = requests.get(standingsURL)
    time.sleep(15)
    soup = BeautifulSoup(data.text)
    standingsTable = soup.select('table.stats_table')[0]

    links = [l.get('href') for l in standingsTable.find_all('a')]
    links = [l for l in links if '/squads/' in l]
    teamURLs = [f'https://fbref.com{l}' for l in links]
    data = requests.get(standingsURL)
    time.sleep(15)
    previousSeasons = soup.select('a.button2.prev')[0].get('href')
    standingsURL = f'https://fbref.com{previousSeasons}'

    data = requests.get(teamURLs[0])
    time.sleep(15)


    for teamURL in teamURLs:
        links = standingsTable.find_all('a')
        links = [l.get('href') for l in links]
        links = [l for l in links if '/squads/' in l]
        teamURLs = [f'https://fbref.com{l}' for l in links]
        teamName = teamURL.split('/')[-1].replace('-Stats', '').replace('-', ' ')

        data = requests.get(teamURL)
        matches = pd.read_html(teamURL)[1]

        soup = BeautifulSoup(data.text)
        links = [l.get('href') for l in soup.find_all('a')]
        time.sleep(20)
        links = [l for l in links if l and 'all_comps/shooting/' in l]
        teamLink = f'https://fbref.com{links[0]}'
        print(teamLink)
        data = requests.get(teamLink)
        shooting = pd.read_html(data.text, match='Shooting')[0]
        shooting.columns = shooting.columns.droplevel()

        try:
            teamData = matches.merge(shooting[['Date', 'Sh', 'SoT', 'Dist', 'FK', 'PK', 'PKatt']], on='Date')
        except ValueError:
            continue

        teamData = teamData[teamData['Comp'] == 'Premier League']
        teamData['Season'] = year
        teamData['Team'] = teamName
        allMatches.append(matches)
        time.sleep(10)

matchDF = pd.concat(allMatches)

matchDF.columns = [c.lower() for c in matchDF.columns]

matchDF.to_csv('myMatches.csv')
