#!/usr/bin/python3
from sys import argv
chords = []


def lineToHtml(line):
    numbers = "0123456789"
    newLine = ""
    b = ""
    Bool = not True
    for j in range(0, len(line)):

        if line[j] == '|':
            if Bool:
                newLine += "</sup> "
                if b not in chords:
                    chords.append(b);
                    b = ""
            else:
                newLine += "<sup class=\"chord\">"
                b = ""
            Bool = not Bool
        elif line[j] == '\\':
            if Bool:
                newLine += "</sup>"
                if b not in chords:
                    chords.append(b)
                    b = ""
                Bool = False;
        elif line[j] == '\n':
            newLine += "<br />"
        elif line[j] == 'R':
            if len(line) == 2:
                newLine += "<br /><span class=\"verse\">R:</span>"
                j += 1
            elif len(line) == 3:
                newLine += "<br /><span class=\"verse\">R</span>"
        elif (line[j] == 'r') and (j < (len(line) - 1)) and (line[j+1] == ':'):
            newLine += "<br /><span class=\"verse\">Rec:</span>"
        elif (line[j] in numbers) and (j < (len(line) - 1)) and (line[j+1] == ':'):
            newLine += "<br /><span class=\"verse\">" + line[j] + "</span>"
            j += 1
        elif (line[j] == '-') and (line[j+1] == '(') and (line[j+2] == ')') and (line[j+3] == '-'):
            newLine += '<br /><span class="verse">~mezihra~</span>'
            j += 3
        elif (line[j] == 'B') and (j < (len(line) - 1)) and (line[j+1] == ':'):
            newLine += "<br /><span class=\"verse\">Bridge:</span>"
            j += 1
        else:
            if Bool:
                b += line[j]
            newLine += line[j]
    if Bool:
        newLine += "</sup>"
        print(newLine)
    return newLine


if len(argv) != 3:
    print("Usage: chordifier <in> <out>\n")
    exit(1)
else:
    read = open(argv[1], "r", encoding="utf8")
    lines = read.readlines()
    read.close()
    write = open(argv[2], "w", encoding="utf8")
    write.write("<?php\narray_push($names,\""+lines[0]+"\");\narray_push($songs,'")
    for i in range(1, len(lines)):
        write.write(lineToHtml(lines[i]))
    write.write("');\n")
    write.write("$chords = [")
    for i in range(0, len(chords)-1):
        write.write("'"+chords[i]+"',")
    write.write("'"+chords[len(chords)-1]+"'")
    write.write("]);\n?>")
    write.flush()
    write.close()
