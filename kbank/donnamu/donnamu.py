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
    r"돈나무 영양제 1개가 기다리고 있어요\n케이뱅크가 처음이라면 5천원을 받아요!\n\n(https://m\.kbanknow\.com/banking/k/[a-zA-Z0-9]+)", txt)

urls = list(set(urls))

with open("donnamu.old.txt", "r", encoding="utf-8") as f:
    old_urls = f.read().split("\n")

final_urls = []

for url in urls:
    if url not in old_urls:
        final_urls.append(url)

with open("donnamu.new.txt", "w", encoding="utf-8") as f:
    f.write("\n".join([*old_urls, *final_urls]))

with open("donnamu.format.txt", "w", encoding="utf-8") as f:
    f.write("\"")
    f.write("\",\n\"".join([*old_urls, *final_urls]))
    f.write("\"")
