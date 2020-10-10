import csv
import os

with open("st.csv", "w", newline='') as f:
          write = csv.writer(f, delimiter = ",")
          write.writerow(["one", "two", "three"])
          write.writerow(["four", "five", "six"])

print(os.getcwd())
