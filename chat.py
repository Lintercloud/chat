# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 09:30:44 2020

@author: Linter
"""
#讀取檔案
def read_file(namefile):
    with open(namefile, "r", encoding="utf-8-sig") as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines

#轉換格式
def convert(lines):
    new = []
    persona = None
    for line in lines:
        if line == "Allen":
            persona = "Allen"
            continue
        elif line == "Tom":
            persona = "Tom"
            continue
        if persona:
            new.append(persona + ": " + line)
    return new

#寫入檔案
def write_file(namefile, lines):
    with open(namefile, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

#主程式
def main():    
    lines = read_file("input.txt")
    lines = convert(lines)
    write_file("output.txt",lines)
    
main()
    

   