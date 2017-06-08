import time
from datetime import datetime as dt

host_path = {
    'windows' : r"C:\Windows\System32\drivers\etc\hosts",
    'mac' : "/etc/hosts",
    'linux' : "/etc/hosts"
}

redirect = "127.0.0.1"

website_list =['www.facebook.com', 'facebook.com'];


while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16)):
        print("1")
    else:
        print("2")
    time.sleep(60) #refrehs every minute
