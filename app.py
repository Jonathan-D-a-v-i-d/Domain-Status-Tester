from functions import *
from output import Output
from terminal import Terminal
from termgraph import termgraph
import xlsxwriter


DNS_Domains = open('test_domains.txt', 'r')
Domains= (list(map(str.strip ,DNS_Domains.readlines())))



# CLI Intro Message #
Terminal.intro(Domains)


# Filters live vs dead sites #
#################################### 
live, res_codes, dead, urls = get_url_status(Domains)
####################################

# Adds Global Variables of res-codes per res-code in lists #
#################################################################################
sites_2xx, sites_3xx, sites_4xx, sites_5xx = filter_reponse_code(live, res_codes)
#################################################################################



# CLI Status Message #
Terminal.status(urls, live, dead)
# CLI Outputs res codes per type #
Terminal.output(sites_2xx,sites_3xx,sites_4xx,sites_5xx)




Output.dead_urls(dead)
Output.txt(sites_2xx, sites_3xx, sites_4xx, sites_5xx)
Output.pie_chart_live_vs_dead_sites(live,dead)



