import requests
import sys
import pyfiglet
import threading

figlet = pyfiglet.figlet_format("DirHype", font = "slant")
print (figlet)
print ( """

########################################
#  DirHype Version 1.0 >>> By: Lacoste #
########################################

"""
)


if __name__ == "__main__":
            url = sys.argv[1]
            wordlist = "common.txt"
            with open(wordlist, "r") as files:
                wordlist = files.readlines()  
def dirbrute(url, wordlist):
        try:
            for i in wordlist:
                dirb = "{}/{}".format(url, i.strip())
                get = requests.get(dirb)
                status = get.status_code
                if (status != 404):
                    print (dirb, ">>>", status)
   
        except Exception as erro:
            print("<!> Ocorreu o um erro >>>", erro)

            
for i in range(200):
            threading.Thread(target=dirbrute(url, wordlist)).start()
  
