# Challenge 1

import os

file_path = r"C:\Users\yusuke kato\Documents\就活\メモ.txt"

with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
