#!/usr/bin/env python3

import re
import csv
import operator

logs = open("syslog.log", "r").readlines()
log_count = dict()

for log in logs:
    error = re.findall(r'ERROR.*\(', log)

    if len(error) != 0:
        log_text = error[0].replace("Error", "").replace("(", "").strip()
        if log_text in log_count.keys():
            log_count[log_text] += 1
        else:
            log_count[log_text] = 1

log_count = sorted(log_count.items(), key=operator.itemgetter(1), reverse=True)

with open("error_message.csv", "w", newline="") as csvFile:
    err_writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    err_writer.writerow(["Error", "Count"])

for log in log_count:
    key, value = log
    with open("error_message.csv", "a", newline="") as csvFile:
        err_writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        err_writer.writerow([key, value])

info_count = dict()
error_count = dict()
for log in logs:
    username = re.search(r'\(.*\)', log).group().strip("()")
    error = re.search(r'(ERROR|INFO)', log).group()
    if error == "ERROR":
        if username in error_count.keys():
            error_count[username] += 1
        else:
            error_count[username] = 1
    else:
        if username in info_count.keys():
            info_count[username] += 1
        else:
            info_count[username] = 1

with open('user_statistics.csv', "w", newline='') as csvFile:
    err_writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    err_writer.writerow(["Username", "INFO", "ERROR"])

i = set(info_count.keys())
e = set(error_count.keys())
z = e - i
d = dict.fromkeys(z, 0)
info_count.update(d)

info_count = sorted(info_count.items(), key=operator.itemgetter(0))
error_count = sorted(error_count.items(), key=operator.itemgetter(0))

username = [i[0] for i in info_count]
value1 = [i[1] for i in info_count]
value2 = [i[1] for i in error_count]
error_info = zip(value1, value2)
total = list(zip(username, error_info))[:8]

for i, j in total:
    with open("user_statistics.csv", "a", newline="") as csvFile:
        total_write = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        total_write.writerow([i, j[0], j[1]])
