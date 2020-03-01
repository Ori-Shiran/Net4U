zone={"www.google.com":"8.8.8.8",
      "www.facebook.com":"172.10.1.1",
      "www.ynet.co.il":"192.168.40.1",
      "www.walla.co.il":"192.168.60.1",
      "www.instagram.com":"172.10.4.14"}

choise=input(''' Menu:
1. Add new A record.
2. Delete record.
3. Update existing record.
4. Print zone.
''')

if choise =="1":
    new_url=input("please enter new URL: ")
    while new_url in zone:
        print("Sorry, URL already exists: " + new_url + " IP: " +zone[new_url])
        new_url = input("please enter new URL: ")
    new_ip=input("please enter the corresponding IP: ")
    while new_ip in zone.values():
        new_ip=input("IP already exists, please enter new IP :")
    zone[new_url]=new_ip

elif choise =="2":
    remove_url=input("Please enter the URL record to remove: ")
    if remove_url in zone:
        del(zone[remove_url])
        print("URL was deleted successfully")
    else:
        print("Cant find the URL you've entered in the zone. ")

elif choise =="3":
    update_url=input("Please enter which URL you would like to update: ")
    if update_url in zone:
        zone[update_url]=input("Please enter new IP for: ")
    else:
        print("Cant find the URL you've entered in the zone. ")

elif choise =="4":
    for x in zone:
    print("URL: " + x + ", IP: " + zone[x])