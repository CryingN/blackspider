import urllib.request as ur
from bs4 import BeautifulSoup as bs
import configparser as cf
import time
import platform

url:str = None            #'http://www.baidu.com'
file:str = "blackarch"            #'百度'
tag:str = "tr"           #'tr'
attrname:str = "text"        #'type','text','src'
keyword = "python,xss"#None             #'Auto,SQL,tool'
query = False              #'name','all','sync'

dictionary = cf.ConfigParser()
picture_dic = []
choose_true = {'yes','y','Y'}

# 色彩管理系统
if platform.system().lower() == "windows":
    try:
        from colorama import init
        init()
        true = "\033[32m[True]\033[0m "
        false = "\033[31m[False]\033[0m "
        warn = "\033[33m[Warn]\033[0m "
        choose_ = "\033[34m[Choose]\033[0m "
        bool_color = True
    except:
        true = "[True] "
        false = "[False] "
        warn = "[Warn] "
        choose_ = "[Choose] "
        bool_color = False
else:
    true = "\033[32m[True]\033[0m "
    false = "\033[31m[False]\033[0m "
    warn = "\033[33m[Warn]\033[0m "
    choose_ = "\033[34m[Choose]\033[0m "
    bool_color = False

# 读取当前文档数据
def read_file(query, key, bool_load_color):
    print(true+"正在查询内部信息")
    if query == "name":
        try:
            print(true+"查询到文件名称如下")
            data = dictionary.options(key)
            for i in data:
                print("\033[37m"+i+"\033[0m")
        except:
            print(false+"文件名查询错误,喵了个咪你怎么这里都能报错")
    elif query == "all":
        try:
            print(true+"查询到文件信息如下")
            data = dictionary.items(key)
            for i,j in data:
                if bool_load_color:
                    print("\033[37m"+i+"\033[0m    url:\033[36m"+j.replace("[equal]","=")+"\033[0m")
                else:
                    print(i+"    url:"+j.replace("[equal]","="))
        except:
            print(false+"文件信息查询错误,喵了个咪你怎么这里都能报错")
    elif query == 'sync':
        dictionary.remove_section("test")
        dictionary.add_section("test")
        data = dictionary.items("group")
        for i,j in data:
            dictionary.set("test",i,j)
        dictionary.write(open(".Manage.ini","w"))
        print(true+"test测试信息重置成功")
    else:
        print(false+"当前-q(--query)仅支持:\n  name-----[查询file文件名称]\n  all -----[查询文件信息]\n  sync-----[将test测试部分信息重置为当前group主程序信息,该部分用于调试信息]")
    pass

# 默认file名字
def get_file(url,file):
    if file == None:
        try:
            file = url.split('.')
            file = file[1]
            file = file[:8:]
        except:
            file = args.url[:8:]
    print(true+"设置文件名称:{}".format(file))
    return file

# 获取源代码
def get_html(url):
    try:
        html = ur.urlopen(url)
        html = html.read()
        data = html.decode()
        print(true+"获取源代码成功")
    except:
        print(false+'网站打开失败')
        exit()
    return data

# 获取对应tag节点所需物品
def get_tag(data,tag):
    try:
        soup = bs(data,features="html.parser")
    except:
        print(false+"解析文档失败，无法解析为html文件")
        exit()
    tags = soup.find_all(tag)
    print(true+"已从原文档中获取")
    return tags

# keyword多查询与单查询函数
def bool_keyword(keyword,text):
    keyword = keyword.split(",")
    if len(keyword) != 1:
        bool_key = True
        for i in keyword:
            if i.upper() not in text.upper():
                bool_key = False
        return bool_key
    elif keyword[0].upper() in text.upper():
        return True
    else:
        return False

# 获取图片并判别时候下载
def find_picture(tags,keyword,attrname):
    print(true+'查询到以下tag图片所在网址：')
    for one_tag in tags:
        if keyword == None:
            picture_dic_src(one_tag,attrname)
        elif bool_keyword(keyword,one_tag.text):
            picture_dic_src(one_tag,attrname)
    choose = input(choose_+'统计图片总共有：{number}份，要下载吗？(Y/n):'.format(number = len(picture_dic)))
    return choose

# 将图片链接导入字典
def picture_dic_src(one_tag,attrname):
    scr = one_tag[attrname]
    print(scr)
    picture_dic.append(scr)

# 导入图片
def get_picture(file,picture,url):
    try:
        pic_name = picture.split('/')
        if pic_name[0] != 'https:' and pic_name[0] != 'http:' :
            picture = url + picture
        pic_name = pic_name[len(pic_name)-1]
        data = ur.urlopen(picture,timeout = 10)
        text = file+'/picture/'+pic_name
        picture_data = open(text,'wb')
        picture_data.write(data.read())
        print(true+"获取图片({num}/{all_num})".format(num = picture_num,all_num = all_num))
    except:
        print(warn+'{name}下载失败\n[Analyse] 图片地址：{error}'.format(name = name,error = picture))
 
# 获取data文件夹(阉割版)
def get_data(file,url):
    try:
        data = open("{file}/{file}.html".format(file=file),"r",encoding="utf-8")
        print(true+"从本地获取源代码")
    except:
        data = get_html(url)
        print(warn+"当前模式无法保存文件,若需保存请使用main.py方法")
    return data

if __name__ == "__main__":
    dictionary.read('.Manage.ini',encoding="utf-8")
    if bool(query):
        try:
            read_file(query,"test",bool_color)
        except:
            print(warn+"无法读取.Manage.ini文件")
        quit()
    if file == None:
        if url == None:
            print(false+"请至少输入url或文件名称")
            exit()
        else:
            try:
                file = get_file(url)
                data = get_data(file,url)
                dictionary.set("test",file,url.replace('=','[equal]'))
                dictionary.write(open(".Manage.ini",mode="w",encoding="utf-8"))
                print(true+"已更新字典{file}:{url}".format(file=file,url=url))
            except:
                print(warn+"无法设置文件名,请检查url格式")
    else:
        try:
            url_test = dictionary.get("test",file).replace("[equal]","=")
            choose = input(choose_+"从文件名搜索到url:{},是否使用(Y/n):".format(url_test))
            if choose in choose_true:
                url = url_test
                data = get_data(file,url)
            else:
                try:
                    data = get_data(file,url)
                    dictionary.set("test",file,url.replace("=","[equal]"))
                    dictionary.write(open(".Manage.ini",mode="w",encoding="utf-8"))
                    print(warn+"当前模式无法保存文件,若需保存请使用main.py方法")
                    print(true+"已更新字典{file}:{url}".format(file=file,url=url))
                except:
                    print(warn+"字典部分设置失败,请检查url格式")
        except:
            if url == None:
                print(warn+"未找到url")
            else:
                try:
                    data = get_data(file,url)
                    dictionary.set("test",file,url.replace("=","[equal]"))
                    dictionary.write(open(".Manage.ini",mode="w",encoding="utf-8"))
                    print(warn+"当前模式无法保存文件,若需保存请使用main.py方法")
                    print(true+"已更新字典{file}:{url}".format(file=file,url=url))
                except:
                    print(warn+"无法设置字典,请检查url格式")
    tags = get_tag(data,tag)
    if attrname == None:
        print(true+'查询到以下tag：')
        for one_tag in tags:
            if keyword == None:
                print(one_tag)
            elif bool_keyword(keyword,one_tag.text):
                print(one_tag)
    elif attrname == 'text':
        print(true+'查询到以下tag文本：')
        for one_tag in tags:
            if keyword == None:
                print(one_tag.text)
            elif bool_keyword(keyword,one_tag.text):
                print(one_tag.text)
    elif tag == 'img' and attrname == 'src':
        choose = find_picture(tags,keyword,attrname)
        if choose in choose_true:
            picture_num = 0
            all_num = len(picture_dic)
            for picture in picture_dic:
                picture_num += 1
                get_picture(file,picture,url)
                time.sleep(0.5)
            print(true+'已完成图片保存')
        else:
            print(false+'结束操作')
    else:
        try:
            print(true+'查询到以下tag元素：')
            for one_tag in tags:
                if the_keyword == None:
                    print(one_tag[attrname])
                elif bool_keyword(the_keyword,one_tag.text):
                    print(one_tag[attrname])
        except:
            print(false+'无法查询attrname，请检查是否存在对应元素')
