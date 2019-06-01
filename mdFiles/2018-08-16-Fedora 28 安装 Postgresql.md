*2018-08-16*

# Fedora 28 安装 Postgresql

## Install postgresql
```
$ sudo dnf install postgresql postgresql-server # install client/server
$ sudo dnf install postgresql-contrib           # install extension
$ sudo postgresql-setup initdb                  # initialize PG cluster
$ sudo systemctl start postgresql               # start cluster
$ sudo su - postgres                            # login as DB admin
$ psql                                          # connect to the postgres database
```

## Reset password
```shell
sudo su - postgres
psql
\password postgres
```
## Install before pgadmin4
```shell
sudo dnf install python3-flask-babelex
```

## Install pgadmin4
Install the PGDG RPM repository first, if you haven't done already: https://yum.postgresql.org/repopackages.php 

### Installing pgAdmin4 with server mode:

For server-only installations, run this command:
```shell
sudo dnf install pgadmin4
```

### Or installing pgAdmin4 with desktop mode:
For desktop mode on non-GNOME environment, please run this command:
```shell
sudo dnf install pgadmin4-desktop-common
```
For desktop mode on GNOME environment, please run this command:
```shell
sudo dnf install pgadmin4-desktop-gnome
```

## About pgAdmin4 connect error
***psql: 致命错误: 用户 "postgres" Ident 认证失败***

modify /var/lib/pgsql/data/pg_hba.conf file:
```
# vi /var/lib/pgsql/data/pg_hba.conf
```
change "METHOD",replace "ident" with "trust",and then restart server:
```shell
sudo systemctl restart postgresql
```

---
[Fedora install PostgreSQL](https://developer.fedoraproject.org/tech/database/postgresql/about.html "Fedora install PostgreSQL")

[Installing pgAdmin4 3.X on RHEL / CentOS 7 and Fedora 27](https://people.planetpostgresql.org/devrim/index.php?/archives/96-Installing-pgAdmin4-3.X-on-RHEL-CentOS-7-and-Fedora-27.html "Installing pgAdmin4 3.X on RHEL / CentOS 7 and Fedora 27")