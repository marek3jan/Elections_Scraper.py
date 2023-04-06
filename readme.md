# Election_Scraper Project
This project is an example of a web-scraper. 

The aim of this project is to harness information of election results from regions of Czech republic.

The program  will find the information  about election details from the given web-page.

The election details will be downloaded as a csv file in your computer.

# Proper guide to election_scraper.py 

## Accessing the website of interest:
* Access the website https://www.volby.cz/index_en.htm

* You will see the Table of the Results of Elections and Referendums
* Go to Chamber of Deputies -> click on the chosen year
* Another web-page shows up -> click on  Results for territorial units
* Similar page like this will show up:  https://www.volby.cz/pls/ps2002/ps4?xjazyk=EN
  * You can use this web-page for web-scraping if you want to harness information on the national scale
* On the territorial scale, select your territorial subdivision on the shown table
* Click on the x sign on the last column  (Choice of municipality column)
* Similar page like this will show up: https://www.volby.cz/pls/ps2002/ps45?xjazyk=EN&xkraj=2&xokres=2101
  * This web-page can be used to harness data on the scale of the chosen territorial subdivision

## Brief user guide:

* Install Python 3.11.2 (or newer version)
  * For more user-friendly practise, installing PyCharm is recommended

* Open the Command Prompt:
  * make sure that your root directory corresponds with the directory of your downloaded python file
  * make sure your virtual environment is active and that Python and pip is succesfully installed
    * you can also proceed this by installing PyCharm, downloading this project on Pycharm and using the Terminal
    
* Type the arguments into the directory: >python   election_scraper.py   name_of_your_file
  * The last argument is supposed to be the name of your csv file 
  * Do not write .csv as the suffix to your last argument, the program will do that automatically
* The program will command you to insert the web-page > insert your selected web-page
* Your csv file shoud be generated automatically



## Required and recommended programs
* Python 3.11.2 (or newer versions)
  * go to: https://www.python.org/
* PyCharm  
  * go to: https://www.jetbrains.com/pycharm/



## Found a bug?
If you found an issue or would like to submit an improvement to this project:

- contact me on my DISCORD profile ->  marek3jan
