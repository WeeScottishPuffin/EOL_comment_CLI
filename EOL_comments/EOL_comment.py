import argparse
import os

default_comments = {
    ".c":"//",
    ".cpp":"//",
    ".cs":"//",
    ".htm":"\'",
    ".html":"\'",
    ".java":"//",
    ".py":"#",
    ".pyw":"#",
}

parser = argparse.ArgumentParser(description="CLI Tool to apply my commenting style",prog="CEOL")
parser.add_argument("filename")
parser.add_argument("-cs","--comment_start",required=False)

args = parser.parse_args()
print(args)

if not os.path.isfile(args.filename):
    print("[\033[1m\033[0;31mERR\033[0m] File not found %s\\%s"%(os.getcwd(),args.filename))
    exit()

comment_char = args.comment_start
if args.comment_start == None:
    file_name,file_ext = os.path.splitext(args.filename)
    if file_ext in default_comments.keys():
        print("[\033[1m\033[1;33mINF\033[0m] No comment character specified. Defaulting to \'%s\' for %s"%(default_comments[file_ext],file_ext))
        comment_char = default_comments[file_ext]
    else:
        print("[\033[1m\033[1;33mINF\033[0m] No comment character specified. File extension not known. Defaulting to \'//\'")
        comment_char = "//"

longest_line = 0
lines = []


with open(args.filename,"r") as scanf:
    for line in scanf.readlines():
        longest_line = max(len(line),longest_line)
        lines.append(line.replace("\n",""))

with open(args.filename,"w") as writef:
    wlines = []
    for line in lines:
        ldiff = longest_line//4 - len(line)//4 + 1
        line += ldiff * "\t" + comment_char + "\n"
        wlines.append(line)
    writef.writelines(wlines)

