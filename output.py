from pip import main


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
    