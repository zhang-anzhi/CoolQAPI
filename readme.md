# CoolQAPI

> [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的酷Q开发API
>
> 事件功能参考了 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的插件加载

## 环境要求

1.**依赖的Python模块**

已存储在`requirements.txt`中, 可以使用`pip install -r requirements.txt`安装

## 使用

前往[release](https://github.com/zhang-anzhi/CoolQAPI/releases)页面下载最新的release并解压

### 配置酷Q

在解压到的文件夹中找到`CoolQQ.zip`, 解压

解压后运行`CQA.exe`, 登陆账号, 启用插件，看到酷Q http插件的日志页面即为成功

然后打开`/data/app/io.github.richardchien.coolqhttpapi/config/`将我写好的`example.json`替换为同一目录下的`QQ号.json`

重启酷Q http插件

### 配置MCDR

将`CoolQAPI-MCDR.py`和`CoolQAPI`文件夹放入MCDR的plugins文件夹

重载MCDR

## 配置文件

配置文件位于`CoolQAPI\config.yml`

1.**post_host**

默认值: `127.0.0.1`

接收酷Q转发消息的ip地址

2.**post_port**

默认值: `5701`

接收酷Q转发消息的端口

3.**post_url**

默认值: `/post`

接收酷Q转发消息的地址

4.**api_host**

默认值: `127.0.0.1`

酷Qapi的ip地址

5.**post_port**

默认值: `5700`

酷Qapi的端口

6.**command_prefix**

默认值: `/`

触发命令事件的消息前缀

## 指令

| Command                | Function                                 |
| ---------------------- | ---------------------------------------- |
| !!CQ reload all        | 重载所有(接收服务器, 插件, 配置文件)        |
| !!CQ reload plugin     | 重载插件                                  |
