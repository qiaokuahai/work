```
1. yum 安装包并下载
    1） yum install yum-utils -y
    2)  yumdownloader 包名   # 只下载当前包
    3） yumdownloader 包名 --resolve --destdir=/root/pkg/包名
    例如：
        yumdownloader httpd --resolve --destdir=/root/pkg/httpd
        yumdownloader autoconf --resolve --destdir=/root/pkg/autoconf
        yumdownloader automake --resolve --destdir=/root/pkg/automake

    yum install --downloadonly --downloaddir=~/pkg/autoconf autoconf
    
    yum list: 列出所有的包， 包括已经安装的和没有安装的
    yum list installed: 列出所有已经安装的包
``` 