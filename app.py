import googlesearch as gsearch
import colorama
from getpass import *
colorama.init();
def injections():
    validation =  False;
    username = "allexmabrouk";
    password = 'allexmabrouk';
    try : 
        while validation == False:
                user = str(input('=> Enter Your Username Account :'));
                pswd = getpass('=> Enter Your Password Account :');
                if(username == user and password == pswd):
                    validation = True;
                    print('Hy ' + username + "\n");
                    target = str(input('=> Enter Your Dork Here :'));
                    for urls in gsearch.search(target,stop=50):
                        print(colorama.Fore.GREEN+'[+]'+ urls);
                        fopen = open('urls.txt',"a");
                        fopen.write(urls + "\n");
                        fopen.close();
                    print(colorama.Fore.GREEN+'urls saved success');
                        
                else :
                    print('=> Soory Try Again !')
    except Exception as error:
        print(colorama.Fore.RED+error);
injections();