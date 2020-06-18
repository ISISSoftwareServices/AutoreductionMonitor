FROM mysql:8

ENV MYSQL_ROOT_PASSWORD admin
ENV MYSQL_DATABASE system_monitoring
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD admin
ADD system_monitoring.sql /docker-entrypoint-initdb.d
EXPOSE 3306