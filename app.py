from functions import *
import xlsxwriter

DNS_Domains = open('test_domains.txt', 'r')
Domains= (list(map(str.strip ,DNS_Domains.readlines())))


# CLI Intro Message #
##################### 
console_intro(Domains)
##################### 


# Filters live vs dead sites #
#################################### 
live, res_codes, dead, urls = get_url_status(Domains)
####################################

sites_2xx, sites_3xx, sites_4xx, sites_5xx = filter_reponse_code(live, res_codes)

output_results_terminal(urls, live, dead,sites_2xx,sites_3xx,sites_4xx,sites_5xx)


sites_2xx, sites_3xx, sites_4xx, sites_5xx = filter_reponse_code(live, res_codes)

text_file_output_live_server_responses(sites_2xx, sites_3xx, sites_4xx, sites_5xx)



