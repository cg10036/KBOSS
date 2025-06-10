import re
import glob
import os

# csv 폴더 안의 모든 *.csv 파일을 읽어서 txt 변수에 저장
txt = ""
csv_files = glob.glob(os.path.join('../../csv', '*.csv'))

for csv_file in csv_files:
    with open(csv_file, 'r', encoding="utf-8") as f:
        file_content = f.read()
        txt += file_content + "\n"

urls = re.findall(
    r"\d+시 \d+분에 \d+만원 로또 당첨자를 발표해요. 벌써 (\d+,?)+명이 응모했어요.\n\n(https:\/\/\d+.toss.gift\/_m\/[a-zA-Z0-9]+\?id=[a-zA-Z0-9]+&c=([a-zA-Z0-9]+))", txt)

urls = list(set(urls))

with open("lottery.old.txt", "r", encoding="utf-8") as f:
    old_urls = f.read().split("\n")
    if old_urls[-1] == "":
        old_urls.pop()

old_c = []

for url in old_urls:
    old_c.append(url.split("&c=")[1])

final_urls = []

for url in urls:
    _, url, c = url
    if c not in old_c:
        old_c.append(c)
        final_urls.append(url)

with open("lottery.new.txt", "w", encoding="utf-8") as f:
    f.write("\n".join([*old_urls, *final_urls]))

with open("lottery.format.txt", "w", encoding="utf-8") as f:
    f.write("\"")
    f.write("\",\n\"".join([*old_urls, *final_urls]))
    f.write("\"")
