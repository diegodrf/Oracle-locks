## Container para integração com o Zabbix
## Monitoramento de locks em Banco de dados Oracle

* Este container possui 3 funções:
    * Auto descoberta de locks com mais de 90s;
    * Item coletando o tempo em segundos em que o lock está ativo;
    * Quantidade total de locks
    
**Como utilizar:**
* Adicionar o arquivo **_magic.py_** em externalscripts.
* Adicionar todos os parâmetros na ordem abaixo:
    * Para discovery:
        * http://URL_PARA_O_CONTAINER/discovery
        * Usuário do Banco de dados
        * Senha do usuário
        * IP do Banco de dados
        * Porta do Banco de dados
        * TNSNAME
        * 'True' se o Banco rodar em cluster, 'False' se não for cluster (Se  nada for declarado, o padrão será False)
        * Número da instância. **Este campo é obrigatório se o valor anterior for 'True'**
        
    * Para coletar o tempo de lock no item:
        * http://URL_PARA_O_CONTAINER/getlock
        * Usuário do Banco de dados
        * Senha do usuário
        * IP do Banco de dados
        * Porta do Banco de dados
        * TNSNAME
        * 'True' se o Banco rodar em cluster, 'False' se não for cluster (Se  nada for declarado, o padrão será False)
        * Número da instância. **Este campo é obrigatório se o valor anterior for 'True'**
        * ID do Blocking_Session
        
    * Para coletar a quantidade total de locks:
        * http://URL_PARA_O_CONTAINER/lockcount
        * Usuário do Banco de dados
        * Senha do usuário
        * IP do Banco de dados
        * Porta do Banco de dados
        * TNSNAME
        * 'True' se o Banco rodar em cluster, 'False' se não for cluster (Se  nada for declarado, o padrão será False)
        * Número da instância. **Este campo é obrigatório se o valor anterior for 'True'**
