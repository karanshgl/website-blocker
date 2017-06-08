import time

host_path = {
    'windows' : r"C:\Windows\System32\drivers\etc\hosts",
    'mac' : "/etc/hosts",
    'linux' : "/etc/hosts"
}

redirect = "127.0.0.1"

website_list =['www.facebook.com', 'facebook.com'];


while True:
    time.sleep(60)
