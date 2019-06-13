*2018-05-12*

# Debian 9 上为 Nginx 配置 Let's Encrypt 证书并强制 Https 访问

环境：Debian 9
域名：tester.com（非真实，示例用）
应用：自建的静态页面博客，放在 /var/www/myBlog 目录下。

---
## 使用工具 certbot 来生成 Let's Encrpyt 证书
### 安装 certbot
```shell
 apt install certbot
```
### 生成证书
这过程中会让你输入邮箱地址，按照提示一步步操作就行了，最后会列出生成证书的路径及有效期。
```shell
root@Debian:~# certbot certonly --webroot -w /var/www/myBlog/ -d tester.com -d www.tester.com
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email address (used for urgent renewal and security notices) (Enter 'c' to
cancel):tester@gmail.com

-------------------------------------------------------------------------------
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server at
https://acme-v01.api.letsencrypt.org/directory
-------------------------------------------------------------------------------
(A)gree/(C)ancel: A
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for tester.com
http-01 challenge for www.tester.com
Using the webroot path /var/www/myBlog for all unmatched domains.
Waiting for verification...
Cleaning up challenges
Generating key (2048 bits): /etc/letsencrypt/keys/0000_key-certbot.pem
Creating CSR: /etc/letsencrypt/csr/0000_csr-certbot.pem

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/tester.com/fullchain.pem. Your cert will expire
   on 2018-08-10. To obtain a new or tweaked version of this
   certificate in the future, simply run certbot again. To
   non-interactively renew *all* of your certificates, run "certbot
   renew"
 - If you lose your account credentials, you can recover through
   e-mails sent to tester@gmail.com.
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

root@Debian:~#
```
### 配置 Nginx 服务
我博客网站的服务文件 myBlog.conf，在 /etc/nginx/sites-available 目录下，内容如下：
```
server {
    listen 80;
    server_name tester.com www.tester.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;

    server_name tester.com www.tester.com;

    ssl_certificate /etc/letsencrypt/live/tester.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/tester.com/privkey.pem;

    root /var/www/myBlog;
    index index.html;
}
```
- /etc/letsencrypt/live/tester.com/cert.pem 和 /etc/letsencrypt/live/tester.com/privkey.pem 是证书的生成路径

- 这里利用 `return 301 https://$server_name$request_uri;` 来强制 Https 访问，将来自 Http 的访问转发到 Https 上。

### 重新加载服务
```shell
systemctl reload nginx
```
### 验证
访问
tester.com
www.tester.com
都会跳转到 `https://tester.com`

------------
### 更新证书
Let's encrpyt 证书默认有效期为 3 个月，所以为了避免手工更新，可以添加定时任务来实现自动更新。

#### 添加定时任务
```shell
crontab -e
```
</br>
内容如下：
```
# 每周一凌晨两点更新证书将日志写入“/var/log/letsencrypt.log”并重启 Nginx 服务
0 2 * * 1 certbot renew >> /var/log/letsencrypt.log --post-hook "systemctl reload nginx"
```

---
关于网站如何启用 Https（不同系统不同服务器）的资料介绍，可以看一下这里：
[Certbot](https://certbot.eff.org "Certbot")

