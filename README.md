# SSH_Batch-script-execution
批量给交换机路由器及linux服务器刷脚本

本人在某通信大厂做核心网工作经常要配置数百台交换机路由器
这是我自己写的一个程序可以便捷的通过SSH连接各种设备然后刷入需要配置的脚本

运行需要两个文件
第一个是list.xlsx用于存放交换机路由器的地址（ipv4和ipv6均可）和SSH的用户名密码
格式如下

![Image text](https://github.com/Arthas-2234/SSH_Batch-script-execution/blob/master/img/list.png)

另外一个config.txt文件用于存放待刷脚本

![Image text](https://github.com/Arthas-2234/SSH_Batch-script-execution/blob/master/img/config.png)

将test.exe文件和config.txt，list.xlsx放至同一路径 运行test.exe
运行界面如下

![Image text](https://github.com/Arthas-2234/SSH_Batch-script-execution/blob/master/img/running.png)

如果ssh连接失败将会抛出异常

![Image text](https://github.com/Arthas-2234/SSH_Batch-script-execution/blob/master/img/error.png)





