import time
from datetime import datetime as dt
import web_list

host_path = {
    'windows' : r"C:\Windows\System32\drivers\etc\hosts",
    'mac' : "/etc/hosts",
    'linux' : "/etc/hosts"
}

redirect = "127.0.0.1"

host_temp = host_path['linux']

website_list =web_list.web_list;

with open(host_temp, 'r+') as file:
    content = file.readlines();
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line);
    file.truncate();
