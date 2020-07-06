# 开发文档

可以阅读[example_plugin.py](https://github.com/zhang-anzhi/CoolQAPI/blob/master/example_plugin.py)来理解

## 事件

当从QQ接收到消息, 会触发以下各类事件

只需要在你的插件中包含以下事件即可, 不必每个事件都写

CoolQQAPI会为每个事件新建一个线程来运行, 不要让你的插件变成死循环了!!!

| 方法                               | 触发条件        | 参考用途            |
| ---------------------------------- | -------------- | ------------------ |
| on_qq_load(server, bot)            | 加载插件        | 初始化             |
| on_qq_info(server, info, bot)      | 接收到消息      | 处理消息            |
| on_qq_command(server, info, bot)   | 接收到指令      | 处理qq指令          |
| on_qq_notice(server, info, bot)    | 接收到通知      | 处理通知消息        |

各参数的消息如下:

### server

MCDReforged的`server`对象, 推荐阅读MCDR的[开发文档](https://github.com/Fallen-Breath/MCDReforged/blob/master/doc/plugin_cn.md#server)

### info

解析后的消息内容, 阅读传递的`raw`属性有助于理解

你可以直接使用`info[path]`获取特定路径的内容

它具有以下属性:

| 属性            | 类型      | 内容                                     |
| --------------- | -------- | ---------------------------------------- |
| raw             | dict     | 原始的dict                                |
| time            | int      | 消息时间戳                                |
| post_type       | str      | 类型, 如`message`, `notice`               |
| source_type     | str      | 来源的类型                                |
| source_id       | int      | 来源的QQ号                                |
| user_id         | int      | 相关的用户id                              |
|                 |          |                                          |
| message_id      | int      | 消息的id, 可在撤回消息中使用               |
| source_sub_type | str      | 消息来源的子类型                          |
| raw_content     | array    | 消息内容的数组, 将消息分段(不同类型消息)    |
| content         | str      | 消息内容的纯字符串(优化过图片等)            |
|                 |          |                                          |
| notice_type     | str      | 事件的类型                                |
| duration        | int      | `ban`的持续时长                           |
| operator_id     | int      | 操作者的QQ号                              |
| notice_sub_type | str      | 事件子类型                                |
| file_busid      | int      | 文件busid                                |
| file_id         | str      | 文件id                                   |
| file_name       | str      | 文件名                                   |
| file_size       | int      | 文件大小, 单位B                           |

### bot

将酷Q的API进行封装, `bot.py`的Bot类

推荐阅读酷Q官方的[API文档](https://cqhttp.cc/docs/4.15/#/API?id=api-%E5%88%97%E8%A1%A8)

它具有以下方法, 每个方法都会返回requests的post结果对象:

| 方法                                   | 功能                                           |
| -------------------------------------- | --------------------------------------------- |
| send_msg(message, xx_id=id)            | 发送一条消息, 目标类型会根据xx_id的xx判断        |
| send_private_msg(user_id, message)     | 发送一条私人消息                                |
| send_group_msg(group_id, message)      | 发送一条群组消息                                |
| send_discuss_msg(discuss_id, message)  | 发送一条讨论组消息                              |
| delete_msg(message_id)                 | 撤回一条消息                                   |
| set_group_kick(group_id, user_id, reject_add_request=False) | 踢出群成员                |
| set_group_ban(group_id, user_id, duration) | 群组禁言, 时间单位s, 设为0解除禁言           |
| set_group_whole_ban(group_id, enable)  | 群组全员禁言                                   |
| set_group_card(group_id, user_id, card='') | 设置群名片                                 |
| set_group_special_title(group_id, user_id, special_title, duration) 设置群聊专属头衔    |
| set_friend_add_request(flag, approve, remark) | 处理加好友请求                          |
| set_group_add_request(flag, type, approve, reason) | 处理加群请求                       |
| get_login_info()                       | 返回当前登录账号的信息                          |
| get_friend_list()                      | 返回好友列表                                   |
| get_group_list()                       | 返回群列表                                     |
| get_group_info(group_id)               | 返回群信息                                     |
| get_group_member_list(group_id)        | 返回群成员列表                                 |
| get_group_member_info(group_id, user_id) | 返回群成员信息                               |
| get_record(file, out_format, full_path) | 获取语言, 返回文件名或文件路径(full_path)      |
| get_image(file)                        | 获取图片, 返回文件路径                         |

## API

1.**reload_plugins()**

用于重新载入插件

2.**get_bot()**

用于获取`bot`对象
