
notion_colors = [
     "gray", "brown", "orange", "yellow", 
    "green", "blue", "purple", "pink", "red", 
]
import random
target = ["学习工作","社会经验","心情","身体","生活日常"]
dictsli = []
for t in target: 
    dicts = {"color":random.sample(notion_colors, 1)[0]}
    dicts["name"] = t 
    dictsli.append(dicts)
print(dictsli)
s = {"options":dictsli}
print(s)