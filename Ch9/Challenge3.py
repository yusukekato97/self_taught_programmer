# Challenge 3

import csv

list = [["Top Gun", "Risky Buiness", "Minority Report"], \
        ["Titanic", "The Revenant", "Inception"], \
        ["Training day", "Man of Fire", "Flight"]]

with open("movie_list.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for i in list:
        w.writerow(i)
