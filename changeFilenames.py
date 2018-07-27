import os
path1 ="douyu_pic/"
path2 = "douyu_pic2/"
file_names = os.listdir(path1)
pic_num =1
for file_name in file_names:
    with open(path1+file_name,'rb') as f:
        content = f.read()
    new_name = "pic"+str(pic_num)+".jpg"
    with open(path2+new_name,'wb') as f1:
        f1.write(content)
    pic_num += 1