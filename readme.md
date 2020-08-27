# CoolQAPI

> [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的QQ开发API
>
> 事件功能参考了 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的插件加载

## 环境要求

### 依赖的Python模块

已存储在 `requirements.txt` 中, 可以使用 `pip install -r requirements.txt` 安装

## 使用

前往 [release](https://github.com/zhang-anzhi/CoolQAPI/releases) 页面下载最新的release并解压

### 配置mirai

自行下载 [mirai-console](https://github.com/mamoe/mirai-console) 并按照安装 [cqhttp-mirai](https://github.com/yyuueexxiinngg/cqhttp-mirai) 插件

运行一次mirai后关闭

打开 `\plugins\CQHTTPMirai\setting.yml` 写入以下基本配置

```yaml
'QQ号':
  http:
    enable: true
    host: 127.0.0.1
    port: 5700
    postUrl: "http://127.0.0.1:5701/post"
    postMessageFormat: array
```

启动mirai

### 配置MCDR

将 `CoolQAPI-MCDR.py` 和 `CoolQAPI` 文件夹放入MCDR的plugins文件夹

重载MCDR

### 关于多服使用

`QQBridge` 可以将一个机器人接受的信息分发给多个服务器进行处理

这里是进行多个服务器配置的方法 [QQBridge使用文档](doc/QQBridge.md)

## 配置文件

配置文件位于 `CoolQAPI\config.yml`

`post_host`

默认值: `127.0.0.1`

接收转发消息的ip地址

`post_port`

默认值: `5701`

接收转发消息的端口

`api_host`

默认值: `127.0.0.1`

api的ip地址

`post_port`

默认值: `5700`

api的端口

`command_prefix`

默认值: `/`

触发命令事件的消息前缀

## 指令

| Command                | Function                                 |
| ---------------------- | ---------------------------------------- |
| !!CQ reload all        | 重载所有(接收服务器, 插件, 配置文件)        |
| !!CQ reload plugin     | 重载插件                                  |
| !!CQ update            | 检查并自动更新                            |

## 开发

请阅读 [开发文档](doc/plugin.md) 了解开发相关内容
