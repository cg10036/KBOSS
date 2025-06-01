import re

with open('moneygun.txt', 'r', encoding="utf-8") as f:
    txt = f.read()

urls = re.findall(
    r"용돈을 선물 받았어요👏 \n얼마가 들어 있을까요\?\n(https://m\.kbanknow\.com/banking/k/[a-zA-Z0-9]+)", txt)

urls = list(set(urls))

with open("moneygun.old.txt", "r", encoding="utf-8") as f:
    old_urls = f.read().split("\n")

final_urls = []

for url in urls:
    if url not in old_urls:
        final_urls.append(url)

with open("moneygun.new.txt", "w", encoding="utf-8") as f:
    f.write("\n".join([*old_urls, *final_urls]))
