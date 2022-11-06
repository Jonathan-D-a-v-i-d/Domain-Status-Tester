from pip import main
import matplotlib.pyplot as plt
import mplcyberpunk


class Output:
  def txt(status_code_2xx,status_code_3xx,status_code_4xx,status_code_5xx):

    if(status_code_2xx):
        with open ("2xx__Codes", "w") as f:
            for status_code in status_code_2xx:
                f.write(status_code + "\n")


    if(status_code_3xx):
        with open ("3xx__Codes", "w") as f:
            for status_code in status_code_3xx:
                f.write(status_code + "\n")

    if(status_code_4xx):
        with open ("4xx__Codes", "w") as f:
            for status_code in status_code_4xx:
                f.write(status_code + "\n")

    if(status_code_5xx):
        with open ("5xx__Codes", "w") as f:
            for status_code in status_code_5xx:
                f.write(status_code + "\n")




  def dead_urls(dead):
      with open ("Dead_Sites.txt", "w") as f:
          for damn_he_dead in dead:
              f.write(damn_he_dead + "\n")



  def pie_chart_live_vs_dead_sites(live,dead):

      # Labels
      labels = 'Live Sites', 'Dead Sites'

      #Data
      sizes = [len(live), len(dead)]

      # Colors
      colors = ['tab:green', 'tab:red']

      plt.style.use('dark_background')  
      fig1, ax1 = plt.subplots()
      ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
              shadow=False, startangle=90)

      centre_circle = plt.Circle((0,0),0.70,fc='white')
      fig = plt.gcf()
      fig.gca().add_artist(centre_circle)
    
      ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
      ax1.set_title("Live Sites vs Dead Sites", fontsize = 20)

      #plt.style.use('cyberpunk')
      mplcyberpunk.add_glow_effects()







      plt.show()



    