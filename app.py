from functions import *
from output import Output
from terminal import Terminal
import xlsxwriter


DNS_Domains = open('test_domains.txt', 'r')
Domains= (list(map(str.strip ,DNS_Domains.readlines())))


# CLI Intro Message #
##################### 
Terminal.intro(Domains)
##################### 


# Filters live vs dead sites #
#################################### 
live, res_codes, dead, urls = get_url_status(Domains)
####################################

sites_2xx, sites_3xx, sites_4xx, sites_5xx = filter_reponse_code(live, res_codes)


Terminal.output(urls, live, dead,sites_2xx,sites_3xx,sites_4xx,sites_5xx)


Output.dead_urls(dead)
Output.txt(sites_2xx, sites_3xx, sites_4xx, sites_5xx)



