import requests
from colors import colors as c
from pyfiglet import *



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
            print(c.GREEN + c.BOLD + "LIVE SERVER  " + c.END + c.BOLD + c.YELLOW + "url:  " + c.END + c.GREEN + c.BOLD + url + c.END + c.YELLOW + " ----------STATUS " + c.END  + c.BLUE + c.BOLD + str(count) + "/" + str(total_count) + c.END )
        except Exception as e:
            add = "FAILED TO CONNECT:\t" + url
            dead_server_list.append(add)
            count += 1
            print(c.RED + c.BOLD + "DEAD SERVER  " + c.END + c.BOLD + c.YELLOW + "url:  " + c.RED + c.BOLD + url + c.END + c.YELLOW + " ----------STATUS " + c.END + c.BLUE + c.BOLD + str(count) + "/" + str(total_count) + c.END)

    return live_server_list, response_code_list, dead_server_list, url_count



"""Prints introductory message to user on CLI"""
def console_intro(urls):
    #custom_fig = Figlet(font='doh')
    #custom_fig.renderText("Testing  " + str(len(urls)) + "  Sites")
    testing_banner = figlet_format(
        "Testing  " + str(len(urls)) + "  Sites" + "\n"
        "- - - - - - - - -"
        )
    print(testing_banner)




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


def output_results_terminal(urls, live, dead,status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):

    res_type_2xx = "2xx"
    res_type_3xx = "3xx"
    res_type_4xx = "4xx"
    res_type_5xx = "5xx"

    status_banner = figlet_format("Status")

    # Gives message on live sites vs dead sites 
    print( 
    status_banner +
    "FINISHED TESTING -----" + c.UNDERLINE +str(urls) + " SITES\n" + c.END +
    c.GREEN + c.BOLD + "LIVE SITES " + c.END + str(len(live)) + "\n" +
    c.RED   + c.BOLD + "DEAD SITES " + c.END + str(len(dead)) + "\n" 
    )



    #Success Message
    def successmessage(status_group, res_type):
            amount = str(len(status_group))
            print( c.GREEN + c.BOLD + 
            "[*] " + "Status Code--" + res_type + " Domains Found: " + amount + c.END
            )
                
    #Error Message
    def errormessage(status_group, res_type):
            amount = str(len(status_group))        
            print( c.RED + c.BOLD + 
            "[*] " + "Status Code--" + res_type + " Domains Found: " + amount + c.END
            )



    #Prints live site results title
    print( "\n" +
           "\n" +
           c.GREEN + c.BOLD + c.UNDERLINE +
           "LIVE SITE RESULTS:" +
           c.END
        )

    # Gives Success/Error message on all server type responses in number
    if(status_code_2xx):
        successmessage(status_code_2xx, res_type_2xx)
    else: errormessage(status_code_2xx, res_type_2xx)

    if(status_code_3xx):
        successmessage(status_code_3xx, res_type_3xx)
    else: errormessage(status_code_3xx, res_type_3xx)

    if(status_code_4xx):
        successmessage(status_code_4xx, res_type_4xx)
    else: errormessage(status_code_4xx, res_type_4xx)

    if(status_code_5xx):
        successmessage(status_code_5xx, res_type_5xx)    
    else: errormessage(status_code_5xx, res_type_5xx)



def text_file_output_live_server_responses(status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):

    if(status_code_2xx):
        with open ("Status_Codes_2xx", "w") as f:
            for status_code in status_code_2xx:
                f.write(status_code + "\n")


    if(status_code_3xx):
        with open ("Status_Codes_3xx", "w") as f:
            for status_code in status_code_3xx:
                f.write(status_code + "\n")

    if(status_code_4xx):
        with open ("Status_Codes_4xx", "w") as f:
            for status_code in status_code_4xx:
                f.write(status_code + "\n")

    if(status_code_5xx):
        with open ("Status_Codes_5xx", "w") as f:
            for status_code in status_code_5xx:
                f.write(status_code + "\n")



 

    







