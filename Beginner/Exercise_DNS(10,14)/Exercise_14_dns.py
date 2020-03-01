def menu(zone):
    out=1
    while out==1:
        choise=input(''' \nMenu:
        1. Add record.
        2. Remove record.
        3. Update record.
        4. Print zone.
        5. Exit menu.
        ''')
        if choise =="1":
            add_url(zone)
        elif choise =="2":
            remove_url(zone)
        elif choise =="3":
            update_url(zone)
        elif choise =="4":
            print_zone(zone)
        elif choise == "5":
            print("Bye.")
            out=0

def add_url(zone):
    url=input("Enter URL: ")
    if search_url(zone,url,"0")=="1":
        print("URL already exists.")
        return ()
    ip = input("Enter IP address: ")
    if search_url(zone,url,ip) == "2":
        print("IP already exists.")
        return ()
    zone[url]=ip
    print("New record added.")
    return ()

def remove_url (zone):
    url=input("Enter URL to remove from zone: ")
    if search_url(zone,url,"0") == "1":
        del (zone[url])
        print("Record removed.")
    else:
        print("URL doesnt exists in this zone.")
    return ()

def update_url (zone):
    url=input("Enter URL to update: ")
    if search_url(zone,url,"0") == "1":
        ip=input("Enter IP: ")
        if search_url(zone,"0",ip) == "2":
            print("Ip exists in this zone already.")
        else:
            zone[url]=ip
            print("Record updated.")
        return ()
    else:
        print("No suck URL in this zone.")
    return ()

def search_url(zone,url,ip):
    if url in zone:
        return ("1")
    elif ip in zone.values():
        return("2")
    else:
        return ("0")

def print_zone(zone):
    for x in zone:
        print("URL: " + x + ", IP: " + zone[x])

zone={"www.google.com":"8.8.8.8",
      "www.facebook.com":"172.10.1.1",
      "www.ynet.co.il":"192.168.40.1",
      "www.walla.co.il":"192.168.60.1",
      "www.instagram.com":"172.10.4.14"}

menu(zone)