如何在 Ubuntu 上启动或停止 PostgreSQL 服务器？

在 Ubuntu 中，可以使用多种方法启动或停止 Postgres 服务器。在本文中，将讨论在 Linux (Ubuntu) 上启动或重新启动 Postgres 服务器的几种众所周知的方法：

方法1：使用“systemctl”命令
方法2：使用systemctl调用的脚本“/etc/init.d/postgresql”。

方法1：使用“systemctl”命令启动和停止 Postgres 服务器

以下是使用“systemctl”命令在 ubuntu 上启动或停止 Postgres 服务器的步骤：

sudo systemctl status postgresql
sudo systemctl start postgresql
sudo systemctl stop postgresql


Method 2: Start and Stop Postgres Server Using “/etc/init.d/postgresql”
Use the “/etc/init.d/postgresql” command with the start option to initiate the Postgres server:
/etc/init.d/postgresql start
/etc/init.d/postgresql status
/etc/init.d/postgresql stop



启用对Postgres 的远程访问

1.修改PostgreSQL配置文件

使用您喜欢的文本编辑器打开 PostgreSQL 配置文件“postgresql.conf”。该文件通常位于 /etc/postgresql/12/main 目录中。要从 Linux 终端打开该文件，请执行：sudo nano /etc/postgresql/12/main/postgresql.conf 

然后，找到该行#listen_addresses = 'localhost'并取消注释（删除该行开头的 # 字符）。

接下来，将“listen_addresses”的值更改为“*”。这允许 PostgreSQL 监听所有可用的 IP 地址。或者，您可以指定允许连接到服务器的特定 IP 地址或 IP 地址范围。

2、修改pg_hba.conf文件

使用您喜欢的文本编辑器打开“pg_hba.conf”文件。该文件通常位于 /etc/postgresql/12/main 目录中。要从 Linux 终端打开该文件，请执行：sudo nano /etc/postgresql/12/main/pg_hba.con

采取以下部分：
# IPv4 local connections: 
host    all             all             127.0.0.1/32            md5 

并这样修改： 
# IPv4 local connections:
host    all             all             0.0.0.0/0            md5 

3.允许5432端口通过防火墙
要启用端口 5432 上的流量通过防火墙，请执行以下命令：
sudo ufw allow 5432/tcp
sudo ufw status

4. 重启PostgreSQL
运行以下命令重新启动 PostgreSQL：sudo service postgresql restart