docker 1
create user root identified by  'password';
grant replication slave, replication client on *.* to root@'db-replica' identified by 'password';

show master status;

SELECT user, host FROM mysql.user;

flush privileges;

SELECT user, host FROM mysql.user;

show slave hosts;

docker 2
CHANGE MASTER TO MASTER_HOST='db',
    MASTER_USER='root',
    MASTER_PASSWORD='password',
    MASTER_LOG_FILE='mysql-bin.000003',
    MASTER_LOG_POS=0;

start slave;
show status slave\G;
stop slave;