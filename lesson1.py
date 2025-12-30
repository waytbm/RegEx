import re

text = "Карта map и объект bitmap - это разные вещи"

match = re.findall("map", text)
print(match)