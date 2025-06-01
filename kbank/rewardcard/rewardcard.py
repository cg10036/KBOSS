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
    r"친구가 현금이 담긴 리워드 카드를 보냈어요!\n카드를 열면 현금을 드려요\n(https://m\.kbanknow\.com/banking/k/[a-zA-Z0-9]+)", txt)

urls = list(set(urls))

with open("rewardcard.old.txt", "r", encoding="utf-8") as f:
    old_urls = f.read().split("\n")

final_urls = []

for url in urls:
    if url not in old_urls:
        final_urls.append(url)

with open("rewardcard.new.txt", "w", encoding="utf-8") as f:
    f.write("\n".join([*old_urls, *final_urls]))

with open("rewardcard.format.txt", "w", encoding="utf-8") as f:
    f.write("\"")
    f.write("\",\n\"".join([*old_urls, *final_urls]))
    f.write("\"")
