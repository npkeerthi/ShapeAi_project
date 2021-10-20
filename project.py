# BOOTCAMP - PYTHON WEBSCRAPPING Shape Ai
from bs4 import BeautifulSoup
import re, requests, sys
import pandas as pd


NAME = []
AGE = []
OVA = []
POT = []
TEAM_NAME = []
CONTRACT = []
VALUE = []
WAGE = []
TOTAL_STATS = []

sys.stdout.write("\033[1;36m")
print('''N PADMA KEERTHI
''')  


def get_name():
    for i in soup.find_all('a', class_='tooltip'):
        name = re.sub(r'^<a.*">|<img.*</a>|15</span>|\xa0|</div></a>|</span>|21|1|2|3|4|5|0|6|7|8|9', '', str(i))
        NAME.append(name)
    NAME.pop()
    NAME.pop()
    NAME.pop()
    NAME.pop()


def get_age():
    for i in soup.find_all('td', class_='col col-ae'):
        age = re.sub('^<td.*ae">|</td>', '', str(i))
        AGE.append(age)
    # print(AGE)
    # print(len(AGE))


def get_ova():
    for i in soup.find_all('td', class_='col col-oa'):
        ova = re.sub('^<td.*p-79">|<td class="col col-oa" data-col="oa">|<span.*">|</span></td>', '', str(i))
        OVA.append(ova)
    # print(OVA)
    # print(len(OVA))


def get_pot():
    for i in soup.find_all('td', class_='col col-pt'):
        pot = re.sub('^<td.*p-79">|<td class="col col-pt" data-col="pt">|<span.*">|</span></td>', '', str(i))
        POT.append(pot)
    # print(OVA)
    # print(len(OVA))


def get_team():
    for i in soup.find_all('div', class_='bp3-text-overflow-ellipsis'):
        team = re.sub('<div class="bp3-text-overflow-ellipsis">|Free|<figure class="avatar avatar-sm transparent">\n|<img.*.png"|/>\n|</figure>|</div>|\n|<a.*/">|<a.*.gif"/>|</a>|<div.*sub">|1|2|3|4|5|6|7|8|9|0| ~ |\xa0|<span.*/span>|,', '', str(i))
        TEAM_NAME.append(team)
    for a in TEAM_NAME:
        if a in NAME:
            TEAM_NAME.remove(a)
    # print(TEAM_NAME)
    # print(f"tram {len(TEAM_NAME)}")


def get_contract():
    for i in soup.find_all('div', class_='sub'):
        cont = re.sub('^<div.*sub">|\n|<span.*/span>|</div>', '', str(i))
        CONTRACT.append(cont)
    # print(CONTRACT)
    # print(CONTRACT.__len__())


def get_value():
    for i in soup.find_all('td', class_='col col-vl'):
        val = re.sub('^<td.*vl">€|</td>', '', str(i))
        VALUE.append(val)
    # print(VALUE)
    # print(len(VALUE))


def get_wage():
    for i in soup.find_all('td', class_='col col-wg'):
        wage = re.sub('^<td.*wg">€|</td>', '', str(i))
        WAGE.append(wage)
    # print(WAGE)
    # print(len(WAGE))


def get_total():
    for i in soup.find_all('td', class_='col col-tt'):
        total = re.sub('^<td.*t">|<span.*p">|</span>|</td>', '', str(i))
        TOTAL_STATS.append(total)
    # print(TOTAL_STATS.__len__())


for i in range(0, 541, 60):
    URL = f"https://sofifa.com/players?offset={i}"
    # print(URL)
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')

    get_name()
    get_age()
    get_ova()
    get_pot()
    get_team()
    get_contract()
    get_value()
    get_wage()
    get_total()

# pandas data frame
df = pd.DataFrame({"Name": NAME,
                   "Age": AGE,
                   "Overall_Rating": OVA,
                   "Potential": POT,
                   "Team_Name": TEAM_NAME,
                   "Contract_Year": CONTRACT,
                   "Value(M)": VALUE,
                   "Wage(K)": WAGE,
                   "Total_Stats": TOTAL_STATS})


df.to_excel('players.xlsx') # Export the data (Path To Excel File)

sys.stdout.write('\033[1;31m')
print("Data Exported To Excel File") # project success confirmation
