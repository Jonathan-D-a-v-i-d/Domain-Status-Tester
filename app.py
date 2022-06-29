from functions import *
import xlsxwriter

DNS_Domains = open('All_Domains.txt', 'r')
Domains= (list(map(str.strip ,DNS_Domains.readlines())))


# CLI Intro Message #
##################### 
console_intro(Domains)
##################### 


# Filters live vs dead sites #
#################################### 
live,dead = get_url_status(Domains)
####################################

# CLI live/dead server summary message #
#################################################
console_server_response_summary(Domains,live,dead)
#################################################

text_file_output_dead_urls(dead)



sites_2xx, sites_3xx, sites_4xx, sites_5xx = filter_reponse_code(live)

text_file_output_live_server_responses(sites_2xx, sites_3xx, sites_4xx, sites_5xx)



"""
for x in live:
    print(x)

print(
    "2xx codes " +str(bool(sites_2xx)) + "\n"
    "3xx codes " +str(bool(sites_3xx)) + "\n"
    "4xx codes " +str(bool(sites_4xx)) + "\n"
    "5xx codes " +str(bool(sites_5xx)) + "\n"
    
    )
"""