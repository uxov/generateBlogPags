*2018-05-16*

# Nginx 配置二级域名及Gogs启用Https

## 生成证书包括二级域名
```shell
certbot certonly --standalone -w -d test.com -d www.test.com -d gogs.test.com
```
## Nginx 配置文件示例
/etc/nginx/sites-available/server.conf
```
server {
    listen 80;
    server_name test.com www.test.com;

    location / {
        return 404;
    }
}


server {
    listen 80;
    server_name gogs.test.com;

    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name gogs.test.com;
    ssl_certificate /etc/letsencrypt/live/test.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/test.com/privkey.pem;

    client_max_body_size   20m;

    location / {
        proxy_pass         http://127.0.0.1:3000;
    }
}
```
配置完后，重启服务后就可以用 https://gogs.test.com 访问了

## 提交到 Gogs 遇到的问题
### 1、验证问题
fatal: unable to access 'http://gogs.test.com/tester/testRep.git/': SSL certificate problem: unable to get local issuer certificate

解决方法：关闭验证
```shell
git config http.sslVerify false
```

### 2、文件上传太大问题
Total 10 (delta 0), reused 0 (delta 0)
error: RPC failed; HTTP 413 curl 22 The requested URL returned error: 413 Request Entity Too Large
fatal: The remote end hung up unexpectedly
fatal: The remote end hung up unexpectedly
Everything up-to-date

原因：Nginx 对上传文件的大小有限制

解决方法：在 Nginx 的 server 配置文件中加上一句：
```
client_max_body_size   20m;
```

