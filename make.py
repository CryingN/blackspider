import platform
import os

true = "\033[32m[True]\033[0m "
false = "\033[31m[False]\033[0m "
warn = "\033[33m[Warn]\033[0m "
choose_ = "\033[34m[Choose]\033[0m "
sys = platform.system().lower()
choose_true = {'yes','y','Y'}

def chmod(path,mode):
    import re
    import stat
    import os
    RD, WD, XD = 4,2,1
    BNS = [RD, WD, XD]
    MDS = [
        [stat.S_IRUSR, stat.S_IRGRP, stat.S_IROTH],
        [stat.S_IWUSR, stat.S_IWGRP, stat.S_IWOTH],
        [stat.S_IXUSR, stat.S_IXGRP, stat.S_IXOTH],
    ]
    mode = str(mode)
    if not re.match("^[0-7]{1,3}$",mode):
        raise Exception("mode不属于^[0-7]{1,3}$正则表达")
    mode = "{0:0>3}".format(mode)
    mode_num = 0
    for midx, m in enumerate(mode):
        for bnidx, bn in enumerate(BNS):
            if (int(m) & bn) > 0:
                mode_num += MDS[bnidx][midx]
    os.chmod(path,mode_num)

if sys == "windows":
    print(true+"检测到windows系统")

elif sys == "linux":
    blackspider_data = """#!/bin/sh
cd {get_path}
exec python3 main.py "$@"
""".format(get_path = os.getcwd())
    print(true+"检测到linux系统")
    path = "/bin/blackspider"
    if os.path.exists(path):
        print(warn+"检测到"+path+"文件已存在:")
        with open(path) as read_data:
            data = read_data.read()
        print(data)
        choose = input(choose_+"是否覆盖文件(Y/n):")
        if choose not in choose_true:
            print(true+"文件未进行删改")
            exit()
    try:
        with open(path,"w") as write_data:
            write_data.write(blackspider_data)
        print(true+"文件已覆盖, 正在改写权限")
        chmod(path,755)
        print(true+"权限赋予成功, 将自动删除make.py文件")
        os.remove("./make.py")
    except:
        print(false+"文件覆盖失败, 尝试恢复文件\n(什么, 你怎么知道我还没来得及写这里?)")
else:
    print(false+"系统不属于windows与linux, 你自己配置一下吧:)\n欢迎提交优秀的代码, 客服小祥保佑你哦!!!!!")


