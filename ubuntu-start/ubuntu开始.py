'''
1.设置 root密码
    第一次进入su root提示密码不对，在当前用户下重设一下密码就好了
        $su passwd
2.Ubuntu 上执行 sudo apt install sl 命令，结果报错：E:Unable to locate package sl
    先更新现在系统
    $ sudo apt-get update
3.安装 ubuntu-desktop -图形化桌面
    $sudo apt-get install ubuntu-desktop

4.安装 compiz -桌面配置管理
    $sudo apt-get install compizconfig-settings-manager
5.安装 xlaucnh --虚拟连接
    在windows10安装
6.1安装 xinit 图形化桌面- 不成功
    $sudo apt-get install xinit
    ->下载慢解决
       $sudo vim /etc/apt/sources.list
        $ sudo apt-get update 换源后必须更新

6.2 安装xfce4
    $sudo apt-get install xfce4
7.启动桌面
    $ export DISPLAY=localhost:0
    $sudo xfce4-session
8. 10分钟自动黑屏处理
    $ xset --help 查复命令帮助
    $ xset q    查 xset信息屏保相关 如下
            Screen Saver:
                prefer blanking:  yes    allow exposures:  yes
                    timeout:  600    cycle:  600
        $ xset s  noblank
            $ xset s noexpose
                $ xset s 0 0
                    $ xset q
                        Screen Saver:
                        prefer blanking:  no    allow exposures:  no
                            timeout:  0    cycle:  0
---------------未解决但不影响运行------------------------
1.网卡驱动
2.声卡驱动
3.远程接入未试
2. 命令
    ctrl+shift+f5 --启动过程中选这个命令--命令行启动
    创建用户
        sudo
    reboot-重启

vim -基本操作



















'''