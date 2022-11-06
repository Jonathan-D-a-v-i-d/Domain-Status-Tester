from pyfiglet import *
from colors import colors as c
from termgraph import *
from module import Data, BarChart, Args, Colors


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



    def status(urls,live,dead):
        status_banner = figlet_format("Status")
        live_sites = c.GREEN + c.BOLD + "LIVE SITES" + c.END
        dead_sites = c.RED + c.BOLD + "DEAD SITES" + c.END

        # Gives message on live sites vs dead sites 
        print( 
        status_banner +
        c.BOLD + 
        "FINISHED TESTING" 
        + c.END 
        +  " -----" + c.UNDERLINE +str(urls) + " SITES\n" + c.END,
        )

        """
        data = Data([[len(live), 0], [len(dead)], 0], [live_sites, dead_sites], ["Live","Dead"])
        chart = BarChart(
        data,
        Args(
            #title="Total Marks Per Class",
            colors=[Colors.Green, Colors.Red],
            space_between=False,
        ),
        )
        chart.draw()
        """
        data = Data([[len(live), len(dead)]],labels=" " ,categories=["Live", "Dead"])
        if len(live) == 0:
            print(" There are no Live Sites")
        if len(dead) == 0:
            print("There are no Dead Sites")
        chart = BarChart(
        data,
        Args(
            #title="Site Analysis",
            colors=[Colors.Green, Colors.Red],
            space_between=False,
        ),
        )

        chart.draw()



    """Outputs all status to the CLI"""
    def output(status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):

        res_type_2xx = "2xx"
        res_type_3xx = "3xx"
        res_type_4xx = "4xx"
        res_type_5xx = "5xx"

        #Success Message
        def successmessage(status_group, res_type):
            amount = str(len(status_group))
            print( c.GREEN + c.BOLD + 
            "[*] " + "Status Code--" + res_type + " Domains Found: " + amount + c.END
            )
                
        #Error Message
        def errormessage(status_group, res_type):
            amount = str(len(status_group))        
            print( c.YELLOW + c.BOLD + 
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




    