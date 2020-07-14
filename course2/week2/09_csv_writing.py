import csv

list = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w", newline="") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(list)
    host_csv.close()