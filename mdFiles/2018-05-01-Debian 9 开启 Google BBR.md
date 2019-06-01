*2018-05-01*

# Debian 9 开启 Google BBR

Google BBR （TCP BBR拥塞控制算法）用于实现网络加速。

1、新建文件：
```shell
root@Debian:~# touch /etc/sysctl.d/60-bbr.conf
```

2、添加文件内容：
```shell
root@Debian:~# echo 'net.ipv4.tcp_congestion_control=bbr' >  /etc/sysctl.d/60-bbr.conf
```

3、重启

4、查看是否已开启

```shell
root@Debian:~# lsmod | grep bbr
tcp_bbr                16384  3
```