from selenium import webdriver

def get_js():
    # f = open("D:/WorkSpace/MyWorkSpace/jsdemo/js/des_rsa.js",'r',encoding='UTF-8')
    f = open("./get_sign.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

# 创建chrome参数对象
opt = webdriver.ChromeOptions()

#opt.headless = True
drive = webdriver.Chrome(options=opt)

js_str = get_js()

page = drive.get("file:///E:/github/bmp-template-matching/Untitled-1.html")
print(drive.find_element_by_xpath("/html/body").text)

