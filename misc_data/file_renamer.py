import os;

url_li = [];
#url_li.append("D:\\IMG\\Validation\\Battery")
url_li.append("D:\\IMG\\Validation\\Can_alumi")
url_li.append("D:\\IMG\\Validation\\Can_iron")
url_li.append("D:\\IMG\\Validation\\Glass_brown")
url_li.append("D:\\IMG\\Validation\\Glass_green")
url_li.append("D:\\IMG\\Validation\\Glass_white")
url_li.append("D:\\IMG\\Validation\\Light")
url_li.append("D:\\IMG\\Validation\\Paper")
url_li.append("D:\\IMG\\Validation\\Pet_colored")
url_li.append("D:\\IMG\\Validation\\Pet_uncolored")
url_li.append("D:\\IMG\\Validation\\Plastic_bag")
url_li.append("D:\\IMG\\Validation\\Plastic_PE")
url_li.append("D:\\IMG\\Validation\\Plastic_PP")
url_li.append("D:\\IMG\\Validation\\Plastic_PS")
url_li.append("D:\\IMG\\Validation\\ST")
print("starting renaming...")

for i in range(0,url_li.__len__()) :
    os.chdir(url_li[i]);
    file_li = os.listdir();
    file_li.sort();
    for j in range(0,len(file_li)) :
        os.rename(file_li[j], str(j)+'.jpg');
    print("complete %s... (%d / %d)" %(url_li[i],i+1,len(url_li)));

print("end renaming...")