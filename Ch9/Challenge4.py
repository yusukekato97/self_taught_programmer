# Challenge 4

import csv

list = [["トップガン", "リスキービジネス", "マイノリティリポート"], \
        ["タイタニック", "The Revenant", "インセプション"], \
        ["トレーニングデイ", "マンオブファイア", "フライト"]]

with open("movie_list_japanese.csv", "w", encoding="cp932", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for i in list:
        w.writerow(i)
