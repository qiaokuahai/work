```
vscode go 远程调试环境搭建

1. vscode下载
https://code.visualstudio.com/download
在vscode上面安装go_vscode, 输入关键字搜索，第一个，下载量最多的就是

2. go环境安装以及配置，以centos举例
yum install golang -y
go version

# 修改代理
go env -w GOPROXY=https://goproxy.cn,direct
go env -w GO111MODULE=on

配置之后：
[root@hecs-29587 ~]# go env
GO111MODULE="on"
GOARCH="amd64"
GOBIN=""
GOCACHE="/root/.cache/go-build"
GOENV="/root/.config/go/env"
GOEXE=""
GOEXPERIMENT=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOINSECURE=""
GOMODCACHE="/root/go/pkg/mod"
GONOPROXY=""
GONOSUMDB=""
GOOS="linux"
# gopath, 主要项目开发的依赖包位置，需要注意，go tools的安装目录为$gopath/bin
GOPATH="/root/go"
GOPRIVATE=""
GOPROXY="https://goproxy.cn,https://goproxy.io,direct"
# go的安装位置，不需要修改
GOROOT="/usr/lib/golang"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/lib/golang/pkg/tool/linux_amd64"
GOVCS=""
GOVERSION="go1.18.4"
GCCGO="gccgo"
GOAMD64="v1"
AR="ar"
CC="gcc"
CXX="g++"
CGO_ENABLED="1"
GOMOD="/dev/null"
GOWORK=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build2841097024=/tmp/go-build -gno-record-gcc-switches"


安装依赖
因为之前已经配置了goproxy，所以可以在开发机上直接安装
go install -v github.com/cweill/gotests/gotests@latest
go install -v github.com/fatih/gomodifytags@latest
go install -v github.com/josharian/impl@latest
go install -v github.com/haya14busa/goplay/cmd/goplay@latest
go install -v github.com/go-delve/delve/cmd/dlv@latest
go install -v honnef.co/go/tools/cmd/staticcheck@latest
go install -v golang.org/x/tools/gopls@latest

安装之后要重启vscode!!!然后ctrl+shift+p -> Go:Install/Update Tools

创建launch.json,用于执行调试
Debug: Add Configration, 选择需要的文件
示例：
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Package",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "${fileDirname}"
        }
    ]
}

参考：https://zhuanlan.zhihu.com/p/320343679
go插件离线安装
去官方网站下载插件：https://marketplace.visualstudio.com/
参考https://blog.csdn.net/qq_33446100/article/details/107622225

```