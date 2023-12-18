<div align="center" style="display:grid;place-items:center;">
<p>
    <a href="https://gitee.com/cryingn/blackspider" target="_blank"><img width="180" src="./blackspider.png" alt="Blackspider logo"></a>
<h1>Blackspider</h1>
</p>
</div>

**注意:** 为支持中国VY开源社区的许可证, 1.0.3版本开始blackspider从BSD许可证更换为VY通用许可证

# 环境搭建

`Blackspider` 是由python3构建的网站关键词抓取工具, 可以通过获取源码后直接执行, 其中`Blackspider`使用到第三方库如下:

* `urllib3`

* `beautifulsoup`

以下为windows与linux的环境搭建方式:

## windows搭建

- 请确认电脑上已经配置好[python](https://www.python.org/downloads/)环境与pip工具包
  
  - 在终端(例如:`cmd`, `powershell`)中输入`python --version`(或`python3 --version`)以检验python环境是否安装成功;
  
  - 在终端(例如:`cmd`,`powershell`)中输入`pip --version`(或`pip3 --version`)以检验可以正常使用python的工具包管理工具.

- 安装所需第三方库
  
  - 在终端(例如:`cmd`,`powershell`)中输入`pip install urllib3 bs4`(或`pip3 install urllib3 bs4`)以安装`urllib3`库与`beautifulsoup`库
  
  - 在终端(例如:`cmd`,`powershell`)中输入`pip list`(或`pip3 list`)检查`urllib3`库与`beautifulsoup`库是否正常安装

- 获取代码并解压

- 尝试运行`blackspider.py`文件, 也可以在解压好的文件地址终端(例如:`cmd`,`powershell`)输入`python main.py -f blackarch -t tr -a text -k python,xss`(或`python3 main.py -f blackarch -t tr -a text -k python,xss`)

## linux搭建

不同linux发行版的包管理器会有部分区别, 以下主要以archlinux与debian两个主流发行版进行举例:

### archlinux

- 使用前保证已经安装以下工具(使用pacman包进行安装):
  
  - git
  
  - python
  
  - python-beautifulsoup4
  
  - python-urllib3
  
  若还未安装可以使用以下命令安装: `sudo pacman -S git python python-beautifulsoup4 python-urllib3`

- `git clone https://gitee.com/cryingn/blackspider`

- `python make.py`

### debian

- 希腊奶, 不玩debian喵~

```bash
=========================================================================
'||'''|,'||`            '||     .|'''|.            ..     ||`            
 ||   || ||              ||     ||                 ''     ||             
 ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
 ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
.||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                        ||
                                       .||
地  址：https://github.com/CryingN/blackspider
        https://gitee.com/cryingn/blackspider
版本号：[当前版本号]
邮  箱：CryingNights7v@gmail.com
=========================================================================
```

### VY许可证说明

在不进行个人补充的情况下VY许可证又称为VY通用许可证, 公开使用时只需标注社(VYCMa.png)标或声明源码来自VYCMa, 便可以免费修改和商用素材.
对于分发问题, 为方便更多人理解, 在VY许可证中有重新定义"版权转移"概念: 他人修改源码后可以闭源, 每个修改过的文件需放置版权说明, 如果要进行公开展示需标注作者个人的标志,若作者无特殊说明需标注社标(VYCMa.png)标或声明源码来自VYCMa.
![VYCMa.png](./VYCMa.png)

### 环境

* python 推荐使用3.11.3版本

* argparse，urllib，bs4库

### 环境布置方式

下载[python](https://www.python.org/downloads/),在cmd或者powershell使用pip命令布置第三方库,推荐使用国内镜像源进行下载，这里使用中科大源：

```bash
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ urllib3==1.26.15
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ bs4==4.12.2
```

### 文件描述

| 文件                               | 描述                                                                        |
| -------------------------------- | ------------------------------------------------------------------------- |
| [blackspider.py](./blackspider)  | 工具的核心部分, 可直接通过该文件直接进行调试运行                                                 |
| [Manage.py](./Manage.py)         | 工具的空间管理部分, 主要用于检查文件是否完整与编辑内部文件                                            |
| [.Manage.ini](./.Manage.ini)     | 储存的文件数据, test储存调试用的测试数据, 易恢复, group储存数据由main.py文件直接管理. url中"[equal]"表示"=" |
| [main.py](./main.py)             | 配置好的工具入口, 一般通过该文件使用blackspider                                            |
| [\_\_pycache\_\_](./__pycache__) | 用于进行python文件之间的调用                                                         |
| [.git](./.git)                   | git管理工具                                                                   |
| [blackarch](./blackarch)         | 个人推荐默认储存的文件, 可直接快速获取需要的渗透工具                                               |
| [LINCENSE](./LINCENSE)           | VY通用许可证引用书                                                                |
| [make.py](./make.py)             | 一键构建舒服的blackspider环境                                                      |

## v1.0.4版本更新内容

* 加入`make.py`文件, 方便一键配置更加舒适的环境, 当前版本`make.py`支持linux一键构建

* 更新了一个非常帅气logo

* 优化了文档部分内容

## v1.0.3版本更新内容

##### 修复了1.0.2版本使用中出现的一些问题,提高了一定的兼容性问题,使用方法参考v1.0.2

* 完善了文件保护机制, 修复了部分骂微软的原因
* 添加了本地文件查询功能`query`
* 修复了url不能包含"="的问题
* LICENSE更换为VY通用许可证

##### 当前存在问题

* 管理和代码的简洁性不太好均衡. 太久没看, 有点忘记以前为什么要这么写代码了, 交互能用但是感觉很奇怪, 估计会在下一个版本重构索引部分代码.
* 大小写敏感问题估计也会在下一个版本解决

## v1.0.2版本使用说明书

这是一次很大胆的更新,从版本号就可以想到在大家看不见的地方我进行了多次重写,至少现在的逻辑与以前发布出来的版本有了很大不同.

值得一提的是大版本更新后不代表错误比以前少,相反在实操中可能会出现更多问题,但是随着更新,代码的使用维护将会越来越容易.

### 更新内容

* 重构了部分代码,简化了部分操作;
* 采用单文件`.Manage.ini`存放字典;
* 使用`Manage.py`管理文件页,`blackspider.py`调试代码,`main.py`执行代码

### 使用示例

```bash
python main.py -f blackarch -t tr -a text -k log4j
```

返还值:

```bash
[True] 扫描到.Manage.ini文件
[True] 扫描到.git文件
[True] 扫描到VYCMa.png文件
[True] 扫描到__pycache__文件
[True] 扫描到readme.md文件
[True] 扫描到LICENSE文件
[True] 扫描到Manage.py文件
[True] 扫描到main.py文件
[True] 扫描到blackspider.py文件
[True] 扫描未丢失受保护文件

=========================================================================
'||'''|,'||`            '||     .|'''|.            ..     ||`      
 ||   || ||              ||     ||                 ''     ||       
 ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
 ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
.||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                        ||
                                       .||
地  址：https://github.com/CryingN/blackspider
        https://gitee.com/cryingn/blackspider
版本号：v1.0.3
邮  箱：CryingNights7v@gmail.com
=========================================================================

[Choose] 从文件名搜索到url:https://www.blackarch.org/tools.html,是
否使用(Y/n):n
[True] 从本地获取源代码
[Warn] 字典部分设置失败,请检查url格式
[True] 已从原文档中获取
[True] 查询到以下tag文本：

log4j-bypass
33.f5c92f9
Log4j web app tester that includes WAF bypasses.
 blackarch-webapp



log4j-scan
88.07f7e32
A fully automated, accurate, and extensive scanner for finding log4j RCE CVE-44228.
 blackarch-webapp
```

## v0.4版本使用说明书

### 更新内容

修复了部分不能正常查询的bug；

更新了blackspider的管理方式；

现在blackspider正尝试向linux看齐。

## v0.3.1 BUG修复

  因理解偏差，经检验0.3以前无法直接在终端中使用多关键词查询，现已修复bug；
  同时源代码中不再支持tuple格式进行多关键词查询，多关键词查询可在str格式中用","进行分割，如下例子：

```python
keyword:str = 'Auto,SQL,tool'
```

## v0.3版本使用说明书

### 使用示例

  $\color{#FF0000}使用须知：为维护网络环境，切勿对同一网站进行多次访问。$

```bash
usage: blackspider.py [-h] [--url URL] [--file FILE] [--file_name FILE_NAME] [--tag TAG]
                    [--attrname ATTRNAME] [--keyword KEYWORD]
```

optional arguments:
  -h, --help            show this help message and exit
  --url URL             网站ip地址，例如：--url 'http://www.baidu.com'
  --file FILE           文件位置,当不存在文件时会搜索网站地址并生成对应文件，例如：--file '百度'
  --file_name FILE_NAME
                        用于定义网站地址生成的文件名称，例如：--file_name '百度'
  --tag TAG             html文件中的tag节点,默认为<body>，可通过元素审查搜索对应节点，例如：--tag 'div'
  --attrname ATTRNAME   查询tag节点元素，默认None查询全部，'text'为查询文本，下载图片为：--tag 'img' --attrname
                        'src'
  --keyword KEYWORD     索引关键词,若默认为None则全部查询，例如：--keyword 'Auto','SQL','tool'

```
### 更新内容
* 添加了虽然没什么用但是可以看起来很酷炫的logo；
* 重构了储存方式，网站将以文件夹形式储存；
* 增加了图片爬取功能，可通过``` --tag 'img' --attrname 'src'```对网页图片进行爬取；
* ```--file [文件名] --file_name [文件名]```中的`[文件名]`变更为文件夹名，不再需要输入文件后缀名；
* 增加了选择功能，可通过(Y,y,yes)三种方式进行操作。
### 使用示例
#### 对网站爬取
```bash
py blackspider.py --url 'http://www.baidu.com' --file_name '百度' --tag 'a' --attrname 'text' --keyword '百度' 
```

返还值：

```bash
=========================================================================
 '||'''|,'||`            '||     .|'''|.            ..     ||`
  ||   || ||              ||     ||                 ''     ||
  ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
  ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
 .||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                         ||
                                        .||
 地  址：https://github.com/CryingN/blackspider
 版本号：0.3                                                                               
 邮  箱：CryingNights7v@gmail.com                                                          
 =========================================================================                                                                                                           [True] 获取源代码成功                                                                     [Ture] 已创建文件夹: 百度                                                                 [True] 已创建百度文档                                                                     [True] 已打印至demo.html文档                                                              [True] 已从原文档中获取                                                                   [True] 查询到以下tag文本：
 百度首页
 查看全部百度产品 >
 关于百度
使用百度前必读 
```

#### 对文件爬取

```bash
py blackspider.py --file '百度' --tag 'img' --attrname 'src'
```

返还值：

```bash
=========================================================================
'||'''|,'||`            '||     .|'''|.            ..     ||`
 ||   || ||              ||     ||                 ''     ||
 ||;;;;  ||  '''|. .|'', || //` `|'''|,'||''|,'||''|| .|''|| .|''|,'||''|
 ||   || || .|''|| ||    ||\{   ..   || ||  || ||  || ||  || ||..|| ||
.||...|'.||.`|..||.`|..'.|| \\. '|...|' ||..|'.||..||.`|..||.`|... .||.
                                        ||
                                       .||
地  址：https://github.com/CryingN/blackspider
版本号：0.3
邮  箱：CryingNights7v@gmail.com
=========================================================================

[True] 已找到源网站地址
[True] 文件打开成功
[True] 已从原文档中获取
[True] 查询到以下tag图片所在网址：
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newfanyi-da0cea8f7e.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newxueshuicon-a5314d5c83.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newwenku-d8c9b7b0fb.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newbaike-889054f349.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newzhidao-da1cf444b0.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newjiankang-f03b804b4b.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/yingxiaoicon-612169cc36.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newzhibo-a6a0831ecd.png
https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newyinyue-03ecd1e9b9.png
//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
//www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png
//www.baidu.com/img/flexible/logo/pc/result.png
//www.baidu.com/img/flexible/logo/pc/result@2.png
//www.baidu.com/img/flexible/logo/pc/peak-result.png
http://ss.bdimg.com/static/superman/img/footer/aria-3006e33cce.png
http://ss.bdimg.com/static/superman/img/qrcode/qrcode@2x-daf987ad02.png
http://ss.bdimg.com/static/superman/img/qrcode/qrcode-hover@2x-f9b106a848.png
[Choose] 统计图片总共有：18份，要下载吗？(Y/n):y
[True] 获取图片(1/18)
[True] 获取图片(2/18)
[True] 获取图片(3/18)
[True] 获取图片(4/18)
[True] 获取图片(5/18)
[True] 获取图片(6/18)
[True] 获取图片(7/18)
[True] 获取图片(8/18)
[True] 获取图片(9/18)
[False] PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
[False] PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
[False] PCfb_5bf082d29588c07f842ccde3f97243ea.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png
[False] result.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/flexible/logo/pc/result.png
[False] result@2.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/flexible/logo/pc/result@2.png
[False] peak-result.png下载失败
[Analyse] 图片地址：http://www.baidu.com//www.baidu.com/img/flexible/logo/pc/peak-result.png
[True] 获取图片(16/18)
[True] 获取图片(17/18)
[True] 获取图片(18/18)
[True] 已完成图片保存
```

## v0.2版本使用说明书

### 使用示例

$\color{#FF0000}使用须知：为维护网络环境，切勿对同一网站进行多次访问。$

```bash
usage: blackspider.py [-h] [--url URL] [--file FILE] [--file_name FILE_NAME] [--tag TAG]
                      [--attrname ATTRNAME] [--keyword KEYWORD]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             网站ip地址
  --file FILE           文档位置,不存在文件时搜索网站ip地址并生成html格式网页文件
  --file_name FILE_NAME
                        不存在文件时用于定义ip地址生成HTML文件的名称，默认None生成demo.html文件
  --tag TAG             所寻找HTML文件中的tag节点,默认为div，可在网页元素审查中搜索
  --attrname ATTRNAME   查询tag节点元素，默认None查询全部，可选择查询：class或text
  --keyword KEYWORD     索引关键词,若默认为None则全部查询
```

#### 查询网页并生成文件

```bash
# 查询百度并生成“百度.html”文件
py blackspider.py --url 'http://www.baidu.com' --file_name '百度.html' --tag 'a' --attrname 'text' --keyword '百度'
```

返还值：

```bash
[True] 获取源代码成功
[True] 已创建百度.html文档
[True] 已打印至demo.html文档
[True] 已从原文档中获取
[True] 查询到以下tag文本：
百度首页
查看全部百度产品 >
关于百度
使用百度前必读
```

#### 查询文件

```bash
# 从上面网页生成的文件进行查询
py blackspider.py --file '百度.html' --tag 'a' --attrname 'text' --keyword '百度'
```

返还值：

```bash
[True] 文件打开成功
[True] 已从原文档中获取
[True] 查询到以下tag文本：
百度首页
查看全部百度产品 >
关于百度
使用百度前必读
```

``
