*2018-04-29*

# Linux 禁止 root SSH 登录

目的：防止被尝试暴力破解 root 密码。

方法：新建一个普通用户，普通用户进行 ssh 登录，登录后再切换到 root 。

1、新建一个普通用户
```shell
adduser testuser
```

2、设置用户密码
```shell
passwd testuser
```

3、修改 sshd 配置，禁止 root 登录，打开文件：
```shell
vi /etc/ssh/sshd_config
```
找到 “PermitRootLogin yes” 这一行，将 “yes” 改为 “no” 后，保存退出。

4、重启 sshd 服务
```shell
service sshd restar
```

完成上面的步骤后，用 root 不能进行 ssh 登录连接，会提示 “Permission denied, please try again. ” 错误。可以用普通用户 testuser 进行 ssh 登录后再 su - 切换到 root 。