import requests
from colors import colors as c
import xlsxwriter


""" Tests domain list to search for live servers behind requests, returns two lists based off if there is a server response """
def get_url_status(urls): 

    ## Server Lists
    live_server_list = [] 
    dead_server_list = []

    ## Status Counter
    total_count = len(urls)
    count = 0

    ## Timeout
    time_out = 60

    for url in urls:
        try:
            r = requests.get(url, timeout = time_out)
            add = "SERVER STATUS " + str(r.status_code) + ":   " + url
            live_server_list.append(add)
            count +=1
            print(c.GREEN + c.BOLD + "LIVE SERVER  " + c.END + c.BOLD + c.YELLOW + "url:  " + c.END + c.GREEN + c.BOLD + url + c.END + c.YELLOW + " ----------STATUS " + c.END  + c.BLUE + c.BOLD + str(count) + "/" + str(total_count) + c.END )
        except Exception as e:
            add = "FAILED TO CONNECT:\t" + url
            dead_server_list.append(add)
            count += 1
            print(c.RED + c.BOLD + "DEAD SERVER  " + c.END + c.BOLD + c.YELLOW + "url:  " + c.RED + c.BOLD + url + c.END + c.YELLOW + " ----------STATUS " + c.END + c.BLUE + c.BOLD + str(count) + "/" + str(total_count) + c.END)
    
    #Test for list -- worked
    """
    print("LIVE SERVER LIST")
    print(type(live_server_list))
    for x in live_server_list:
        print(x)

    print("**********************")
    print("**********************")
    print("**********************")
    print("**********************")

    print("DEAD SERVER LIST")
    print(type(dead_server_list))
    for x in dead_server_list:
        print(x)

    """
    return live_server_list, dead_server_list



"""Prints introductory message to user on CLI"""
def console_intro(urls):
    print( c.BLUE + c.BOLD + "\n" +
    "***************************************************\n"
    "                 Testing " + str(len(urls)) + " Sites\n" 
    "***************************************************\n"
     + c.END
    )


def console_server_response_summary(urls,live,dead):

    print( c.BLUE + c.BOLD  +"\n" +
    "***************************************************\n"
    "         Finished Testing " + str(len(urls)) + " Sites\n" + 
    c.GREEN + c.BOLD + "LIVE SITES " + c.END + str(len(live)) + "\n" +
    c.RED   + c.BOLD + "DEAD SITES " + c.END + str(len(dead)) + "\n" +
    c.BLUE + c.BOLD +
    "***************************************************\n"
     + c.END
    )


def text_file_output_dead_urls(dead):

    with open ("no_server_response", "w") as dead_f:
        for url in dead:
            dead_f.write(url + "\n")

    print( c.BLUE + c.BOLD + "\n" +
    "***************************************************\n"
            
    "Outputting " + c.RED + c.BOLD +  "DEAD SERVER "  + c.END  + c.YELLOW + c.BOLD + "URLS " + c.END
     + c.BLUE + c.BOLD  + "to no_server_response.txt        \n" 
    "***************************************************\n"
     + c.END
    )


def filter_reponse_code(live):
    options_4xx = ["400","401","402","403","404","405","406","407","408","409","410","411","412","413","414","415","416","417","418","419","420","421","422","423","424","425","426","428","429","431","451"]
    options_2xx = ["200","201","202","203","204","205","206","207","208","226"]
    options_3xx = ["301","302","303","304","305","306","307","308"]
    options_5xx = ["500","501","502","503","504","505","506","507","508","510","511"]

    sites_4xx = []
    sites_2xx = []
    sites_3xx =[]
    sites_5xx =[]

    for live_response in live:
        if any(x in live_response for x in options_4xx):
            sites_4xx.append(live_response)
        elif any(x in live_response for x in options_2xx):
            sites_2xx.append(live_response)
        elif any(x in live_response for x in options_3xx):
            sites_3xx.append(live_response)
        elif any(x in live_response for x in options_5xx):
            sites_5xx.append(live_response)
    return sites_2xx, sites_3xx, sites_4xx, sites_5xx





        


def text_file_output_live_server_responses(status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):

    #Success Message
    def successmessage(status_group):
        if(status_group == False):
            print( c.GREEN + c.BOLD + "\n" +
            "***************************************************\n"
            " Successfully found "+ str(status_group) + " domains in your search pool"+"\n" 
            "***************************************************\n"
            + c.END
            )
    #Error Message
    def errormessage(status_group):
        if(status_group == False):
            print( c.RED + c.BOLD + "\n" +
            "***************************************************\n"
            "  " + str(status_group) + "Don't exist in your search pool" +"\n" 
            "***************************************************\n"
            + c.END
            )

    if(status_code_2xx):
        with open ("Status_Codes_2xx", "w") as f:
            for status_code in status_code_2xx:
                f.write(status_code + "\n")
        successmessage(status_code_2xx)
    else: errormessage(status_code_2xx)


    if(status_code_3xx):
        with open ("Status_Codes_3xx", "w") as f:
            for status_code in status_code_3xx:
                f.write(status_code + "\n")
        successmessage(status_code_3xx)
    else: errormessage(status_code_3xx)

    if(status_code_4xx):
        with open ("Status_Codes_4xx", "w") as f:
            for status_code in status_code_4xx:
                f.write(status_code + "\n")
        successmessage(status_code_4xx)
    else: errormessage(status_code_4xx)

    if(status_code_5xx):
        with open ("Status_Codes_5xx", "w") as f:
            for status_code in status_code_5xx:
                f.write(status_code + "\n")
        successmessage(status_code_5xx)    
    else: errormessage(status_code_5xx)

    

    







