from pyfiglet import *
from colors import colors as c


class Terminal:

    """Prints introductory message to user on CLI"""
    def intro(urls):
        #custom_fig = Figlet(font='doh')
        #custom_fig.renderText("Testing  " + str(len(urls)) + "  Sites")
        testing_banner = figlet_format(
        "Testing  " + str(len(urls)) + "  Sites" + "\n"
        "- - - - - - - - -"
        )
        print(testing_banner)




    """Outputs all status to the CLI"""
    def output(urls, live, dead,status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):

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