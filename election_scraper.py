Introduction = '''
project_3.py : Third project for the Engeto online Python Academy - election_scraper
name         : Marek Trojan
email        : troj3.marek@gmail.com
git          : marek3jan
'''

#1_Head_and_Introduction:
#         - importing needed modules and creating a list of arguments that are going to by inserted to this program
import csv
from requests import get
from bs4 import BeautifulSoup
import os
import sys

arguments = list(sys.argv)


#2_Core_of_Program:
#        - defining functions that generate the web-scraper program
def election_values(soup, *index_) -> dict:
    election_details: dict = {}

    for index in index_:
        election_details[set_index_value(index)] = soup[index].text.strip()

    return election_details


def set_index_value(index: int) -> str:

    return {
        0: 'Number',
        1: 'Location',
        2: 'Votes',
        3: 'Registered',
        6: 'Envelopes',
        7: 'Valid',
        8: 'Election attendance'
    }.get(index)


def write_csv_file():
    core_html = BeautifulSoup(get(web_page).text, features="html.parser")
    if core_html.find_all('table', {'class': 'table'}):
        tables_root = core_html.find_all('table', {'class': 'table'})
        print(f"DOWNLOADING THE FILES FROM GIVEN URL: {web_page}")

        for table in tables_root:
            root = table.find_all("tr")
            header_tag, *elections = root[1:]

            for election in elections:
                dictionary = election_values(election.find_all('td'), 0, 1)

                if election.find('a'):
                    link = "/".join(web_page.split("/")[:-1]) + "/" + election.find('a')['href']
                    html = BeautifulSoup(get(link).text, features="html.parser")
                    tables_root2 = html.find('table', {'class': 'table'})
                    root2 = tables_root2.find_all("tr")
                    *header_tag, election_ = root2
                    data = election_values(election_.find_all("td"), 3, 6, 7, 8)
                    data['Election attendance'] = str(data['Election attendance']).replace(',', '.') + ' %'
                    d_keys = list(data.keys())
                    d_values = list(data.values())

                    for key in range(len(d_keys)):
                        d_values[key] = str(d_values[key]).replace('\xa0', '')
                        dictionary[d_keys[key]] = d_values[key]

                    tables_root3 = html.find_all('div', class_='t2_470')

                    for new_table in tables_root3:
                        root3 = new_table.find_all('tr')
                        head, *parties = root3[1:]

                        for votes in parties:
                            votes = election_values(votes.find_all('td'), 1, 2)
                            votes['Votes'] = str(votes['Votes']).replace('\xa0', '')
                            v_value = tuple(votes.values())
                            if v_value == ('-', '-'):
                                continue
                            dictionary[v_value[0]] = v_value[1]

                    mode = "w" if f'{file_name}' not in os.listdir() else "a"
                    with open(f'{file_name}', mode, newline='') as file:
                        header = list(dictionary.keys())
                        row = list(dictionary.values())
                        writer = csv.DictWriter(file, fieldnames=header)
                        w = csv.writer(file)
                        if mode == "w":
                            writer.writeheader()
                        w.writerow(row)

        return print("csv file generated".upper())
    else:
        return print("Wrong web-page".upper())


#3_Program_Runner:
#       - code that generates the input of arguments into the program and runs the program to create a csv file
if __name__ == "__main__":
    if len(arguments) < 2:
        print("First argument needed".upper())

    elif len(arguments) > 2:
        print("More arguments than required".upper())

    else:
        url = input("Insert your webpage: ".upper())
        arguments.insert(1, url)
        web_page = str(arguments[1])
        file_name = str(arguments[2]) + '.csv'
        write_csv_file()
