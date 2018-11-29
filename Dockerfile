FROM tiangolo/uwsgi-nginx-flask:python3.7
MAINTAINER "Diego Rodrigues"

# Copia os arquivos do diretório do projeto para o diretório /app
COPY . /app
WORKDIR /app

# Instala as dependências necessárias para conectar-se ao Oracle.
# Instala o pacote para Python
# Limpa o cache do apt e remove os arquivos desnecessários.
RUN apt-get update && \
apt-get install -y libaio1 && \
dpkg -i /app/app/tmp/oracle-instantclient11.2-basic_11.2.0.4.0-2_amd64.deb && \
dpkg -i /app/app/tmp/oracle-instantclient11.2-devel_11.2.0.4.0-2_amd64.deb && \
dpkg -i /app/app/tmp/oracle-instantclient11.2-sqlplus_11.2.0.4.0-2_amd64.deb && \
echo "/usr/lib/oracle/11.2/client64/lib" >/etc/ld.so.conf.d/oracle.conf && \
ldconfig && \
rm -rf /app/app/tmp/ && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* && \
pip install -r requirements.txt
