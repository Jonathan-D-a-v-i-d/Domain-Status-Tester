import requests
from colors import colors as c
import xlsxwriter


""" Tests domain list to search for live servers behind requests, returns two lists based off if there is a server response """
def get_url_status(urls): 

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
    return live_server_list, response_code_list, dead_server_list 



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





        


def text_file_output_live_server_responses(status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):
    res_type_2xx = "2xx"
    res_type_3xx = "3xx"
    res_type_4xx = "4xx"
    res_type_5xx = "5xx"

    #Success Message
    def successmessage(status_group, res_type):
            amount = str(len(status_group))
            if len(status_group) == 1:
                print( c.GREEN + c.BOLD + "\n" +
                "******************************************************\n"
                + amount + " " + res_type + " domain found in your search pool"+"\n" 
                "******************************************************\n"
                + c.END
                )
            else:
                print( c.GREEN + c.BOLD + "\n" +
                "******************************************************\n"
                + amount + " " + res_type + " domains found in your search pool"+"\n" 
                "******************************************************\n"
                + c.END
                )


    #Error Message
    def errormessage(res_type):
            print( c.RED + c.BOLD + "\n" +
            "***************************************************\n"
             "No " + res_type + " domains found in your search pool" +"\n" 
            "***************************************************\n"
            + c.END
            )

    if(status_code_2xx):
        with open ("Status_Codes_2xx", "w") as f:
            for status_code in status_code_2xx:
                f.write(status_code + "\n")
        successmessage(status_code_2xx, res_type_2xx)
    else: 
        errormessage(res_type_2xx)


    if(status_code_3xx):
        with open ("Status_Codes_3xx", "w") as f:
            for status_code in status_code_3xx:
                f.write(status_code + "\n")
        successmessage(status_code_3xx, res_type_3xx)
    else: errormessage(res_type_3xx)

    if(status_code_4xx):
        with open ("Status_Codes_4xx", "w") as f:
            for status_code in status_code_4xx:
                f.write(status_code + "\n")
        successmessage(status_code_4xx, res_type_4xx)
    else: errormessage(res_type_4xx)

    if(status_code_5xx):
        with open ("Status_Codes_5xx", "w") as f:
            for status_code in status_code_5xx:
                f.write(status_code + "\n")
        successmessage(status_code_5xx, res_type_5xx)    
    else: errormessage(res_type_5xx)

    

    







