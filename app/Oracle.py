# -*- coding: utf-8 -*-
import cx_Oracle
import json
from collections import OrderedDict


class Database:
    def __init__(self, user, password, server, port, tnsname, cluster='False', cluster_inst_id='False'):
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.tnsname = tnsname
        self.value = 0
        self.cluster = str(cluster).capitalize()
        self.cluster_inst_id = cluster_inst_id

    # Função discovery para listar as sessões em lock. Por padrão, encontra-se definida para retornar apenas locks com
    # mais de 90 segundos
    def discovery(self):
        if self.cluster == 'False':
            query = """SELECT
             blocking_session,
             sid, 
             serial#, 
             seconds_in_wait 
             FROM 
             gv$session 
             WHERE 
             blocking_session IS NOT NULL"""

        elif self.cluster == 'True':
            query = """SELECT
            blocking_session, 
            sid, 
            serial#, 
            seconds_in_wait,
            inst_id
            FROM
            gv$session
            WHERE
            blocking_session IS NOT NULL
            AND
            inst_id={}""".format(self.cluster_inst_id)

        self.conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(self.user,
                                                              self.password,
                                                              self.server,
                                                              self.port,
                                                              self.tnsname))

        self.cursor = self.conn.cursor()

        self.cursor.execute(query)

        self.rows = self.cursor.fetchall()

        self.conn.close()

        object_list = []
        for row in self.rows:
            if row[3] > 90:
                d = OrderedDict()
                d["{#BLOCKING_SESSION}"] = row[0]
                d["{#SECONDS_IN_WAIT}"] = row[3]
                object_list.append(d)
            else:
                continue

        j = json.dumps(object_list)

        self.discovery_item = '{\n"data":' + j + '\n}'
        with open('/tmp/{}_{}_lock.json'.format(self.tnsname, self.server), 'w') as f:
            f.write(self.discovery_item)

        return self.discovery_item

    # Função getlock para retornar o tempo em que a sessão encontra-se em lock
    def getlock(self, blocking_session):
        self.blocking_session = blocking_session

        with open('/tmp/{}_{}_lock.json'.format(self.tnsname, self.server), 'r') as f:
            data = json.loads(f.read())
            for i in range(len(data['data'])):
                if self.blocking_session == data['data'][i]['{#BLOCKING_SESSION}']:
                    self.value = data['data'][i]['{#SECONDS_IN_WAIT}']

                    return self.value
                else:
                    continue

        return self.value

    # Função lockCount para a contagem de locks acima de 60s
    def lockCount(self):
        with open('/tmp/{}_{}_lock.json'.format(self.tnsname, self.server), 'r') as f:
            data = json.loads(f.read())

        return len(data['data'])
