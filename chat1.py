# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 11:34:01 2020

@author: Linter
"""

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
    allen_word_count = 0
    allen_sticker_count = 0
    allen_pictur_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_pictur_count = 0
    for line in lines:
        s = line.split(" ")
        #print(s)
        if s[1] == "Allen":
            for m in s[2:]: 
                if s[2] == "貼圖":
                    allen_sticker_count +=len(m)
                elif s[2] == "圖片":
                    allen_pictur_count +=len(m)
                else:
                    allen_word_count += len(m)
            
        elif s[1] == "Viki":
            for m in s[2:]:                
                if s[2] == "貼圖":
                    viki_sticker_count +=len(m)
                elif s[2] == "圖片":
                    viki_pictur_count +=len(m)
                else:
                    viki_word_count += len(m)
    
    print("Allen共打了", allen_word_count, "個字")
    print(allen_sticker_count, "個貼圖")
    print(allen_pictur_count, "個圖片")
    print("Viki共打了", viki_word_count, "個字")
    print(viki_sticker_count, "個貼圖")
    print(viki_pictur_count, "個圖片")
      

#寫入檔案
def write_file(namefile, lines):
    with open(namefile, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

#主程式
def main():    
    lines = read_file("LINE-Viki.txt")
    lines = convert(lines)
    #write_file("output.txt",lines)
    
main()
    

   