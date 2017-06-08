import time
from datetime import datetime as dt

host_path = {
    'windows' : r"C:\Windows\System32\drivers\etc\hosts",
    'mac' : "/etc/hosts",
    'linux' : "/etc/hosts"
}

redirect = "127.0.0.1"

host_temp = "hosts"

website_list =['www.facebook.com', 'facebook.com'];


while True:
    if not (dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16)):
        with open(host_temp, 'r+') as file:
            content = file.readlines();
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line);
            file.truncate();


    else:
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    time.sleep(60) #refrehs every minute
