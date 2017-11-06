#程序猿休息小程序
# import time
# import webbrowser
# total_breaks = 3
# break_count = 0
# while break_count < total_breaks:
#     print("please take a rest:" + time.ctime())
#     time.sleep(10) #过10S执行下一句
#     webbrowser.open("http://www.youdaxue.com/")
#     break_count += 1

#秘密消息

import os

def rename_file():
    file_list = os.listdir(r"C:\Users\15262\Downloads\prank")
    print(file_list)
    save_path = os.getcwd()

    print(save_path)
    os.chdir(r"C:\Users\15262\Downloads\prank")
    intab = "0123456789"
    outtab = "          "
    str_trantab = str.maketrans(intab,outtab)

    for file_name in file_list:
        os.rename(file_name,file_name.translate(str_trantab))
        print(file_name)
    print(file_list)
    os.chdir(save_path)
rename_file()
