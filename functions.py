import requests
from colors import colors as c
from pyfiglet import *
import pandas as pd



def get_url_status(urls): 
    """ Tests domain list to search for live servers behind requests, returns two lists based off if there is a server response """

    ## counts urls for status message in later function 
    url_count = len(urls)

    ## Server Lists
    live_server_list = [] 
    dead_server_list = []
    response_code_list =[]

    ## Status Counter
    total_count = len(urls)
    count = 0

    ## Timeout
    time_out = 60

    for url in urls:
        try:
            r = requests.get(url, timeout = time_out)
            status_code = str(r.status_code)
            add = "SERVER STATUS " + status_code + ":   " + url
            live_server_list.append(add)
            response_code_list.append(status_code)
            count +=1
            print(c.GREEN + c.BOLD + "LIVE SERVER  " + c.END + c.BOLD + c.YELLOW + "url:  " + c.END + c.GREEN + c.BOLD + url + c.END + c.YELLOW + " ----------STATUS " + c.END  + c.BOLD + str(count) + "/" + str(total_count) + c.END )
        except Exception as e:
            add = "FAILED TO CONNECT:\t" + url
            dead_server_list.append(add)
            count += 1
            print(c.RED + c.BOLD + "DEAD SERVER  " + c.END + c.BOLD + c.YELLOW + "url:  " + c.RED + c.BOLD + url + c.END + c.YELLOW + " ----------STATUS " + c.END + c.BOLD + str(count) + "/" + str(total_count) + c.END)

    return live_server_list, response_code_list, dead_server_list, url_count



def filter_reponse_code(live, res_codes):

    # Creating lists for export into txt/csv
    sites_4xx = []
    sites_2xx = []
    sites_3xx =[]
    sites_5xx =[]
    
    # Dataframe by zipping each live response with its response code
    df = zip(live, res_codes)
    
    # Appending the live_url to each list based off the first char in the response code
    for d in df:
        response_code = d[1]
        live_url = d[0]
        if response_code[0] == "2":
            sites_2xx.append(live_url)
        elif response_code[0] == "3":
            sites_3xx.append(live_url)
        elif response_code[0] == "4":
            sites_4xx.append(live_url)
        elif response_code[0] == "5":
            sites_5xx.append(live_url)


    return sites_2xx, sites_3xx, sites_4xx, sites_5xx





 

    







