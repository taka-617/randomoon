FROM mysql:5.7
RUN touch /var/log/mysql/mysqld.log

ADD  ./db/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/my.cnf