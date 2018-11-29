from flask import Flask, jsonify, request
from Oracle import Database

app = Flask(__name__)


@app.route('/discovery', methods=['POST'])
def discovery():

    user = request.form['2']
    password = request.form['3']
    server = request.form['4']
    port = request.form['5']
    tnsname = request.form['6']
    cluster = request.form['7']
    cluster_inst_id = request.form['8']

    db = Database(user=user, password=password, server=server, port=port, tnsname=tnsname, cluster=cluster,
                  cluster_inst_id=cluster_inst_id)

    j = db.discovery()
    return jsonify(j)


@app.route('/getlock', methods=['POST'])
def getlock():
    user = request.form['2']
    password = request.form['3']
    server = request.form['4']
    port = request.form['5']
    tnsname = request.form['6']
    cluster = request.form['7']
    cluster_inst_id = request.form['8']
    blocking_session = int(request.form['9'])

    db = Database(user=user, password=password, server=server, port=port, tnsname=tnsname, cluster=cluster,
                  cluster_inst_id=cluster_inst_id)
    j = db.getlock(blocking_session)

    return jsonify(j)


@app.route('/lockcount', methods=['POST'])
def lockcount():
    user = request.form['2']
    password = request.form['3']
    server = request.form['4']
    port = request.form['5']
    tnsname = request.form['6']
    cluster = request.form['7']
    cluster_inst_id = request.form['8']

    db = Database(user=user, password=password, server=server, port=port, tnsname=tnsname, cluster=cluster,
                  cluster_inst_id=cluster_inst_id)
    j = db.lockCount()

    return jsonify(j)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
