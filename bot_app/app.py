# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template, make_response, request, current_app
import ConfigParser
from pyUnipd import pyUnipd
import os
from datetime import timedelta
from functools import update_wrapper

# initialize pyUnipd get configs from settings.ini
pyUni = pyUnipd()

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/settings.ini')
Environment = config.get('main', 'environment')
Auth = str(config.get('main', 'auth_token'))
if Environment == 'debug':
    IsDebug = True
else:
    IsDebug = False

app = Flask(__name__)


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/api/', methods=['GET'])
@crossdomain(origin='*')
def allUni():
    return jsonify(pyUni.allUni())


@app.route('/api/<uniID>/')
@crossdomain(origin='*')
def oneUni(uniID):
    return jsonify(pyUni.oneUni(uniID))


@app.route('/api/<uniID>/udupadova/')
@crossdomain(origin='*')
def udupadova(uniID):
    return jsonify(pyUni.udupadova(uniID))


@app.route('/api/<uniID>/dirittostudio/')
@crossdomain(origin='*')
def dirittostudio(uniID):
    return jsonify(pyUni.dirittostudio(uniID))


@app.route('/api/<uniID>/mensa/')
@crossdomain(origin='*')
def mensa(uniID):
    return jsonify(pyUni.mensa(uniID))


@app.route('/api/<uniID>/mensa/<mensaID>/')
@crossdomain(origin='*')
def singleMensa(uniID, mensaID):
    return jsonify(pyUni.singleMensa(uniID, mensaID))


@app.route('/api/<uniID>/aulastudio/')
@crossdomain(origin='*')
def aulastudio(uniID):
    return jsonify(pyUni.aulastudio(uniID))


@app.route('/api/<uniID>/aulastudio/<aulaID>/')
@crossdomain(origin='*')
def singleAula(uniID, aulaID):
    return jsonify(pyUni.singleAula(uniID, aulaID))


@app.route('/api/<uniID>/biblioteca/')
@crossdomain(origin='*')
def biblioteca(uniID):
    return jsonify(pyUni.biblioteca(uniID))


@app.route('/api/<uniID>/biblioteca/<biblioID>/')
@crossdomain(origin='*')
def singleBiblio(uniID, biblioID):
    return jsonify(pyUni.singleBiblio(uniID, biblioID))


if __name__ == '__main__':
    app.run(debug=IsDebug)
