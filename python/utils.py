import hmac
import base64
import time
import datetime
import consts as c
import hashlib

def sign(message, secretKey):
    #mac = hmac.new(bytes(secretKey, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    #d = mac.digest()
    #return base64.b64encode(d)
    print "message" , message 
    print "secretKey" , secretKey
    print "sign",base64.b64encode(hmac.new(secretKey, message, digestmod=hashlib.sha256).digest())
    return base64.b64encode(hmac.new(secretKey, message, digestmod=hashlib.sha256).digest())


def pre_hash(timestamp, method, request_path, body):
    print "pre_hash", str(timestamp) + str.upper(method) + request_path + body
    return str(timestamp) + str.upper(method) + request_path + body


def get_header(api_key, sign, timestamp, passphrase , source = "API"):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.SC_ACCESS_KEY] = api_key
    header[c.SC_ACCESS_SIGN] = sign
    header[c.SC_ACCESS_TIMESTAMP] = str(timestamp)
    header[c.SC_ACCESS_PASSPHRASE] = passphrase
    header[c.SC_ACCESS_FROM] = source

    #print header
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def get_timestamp():
    return time.time()
    #now = datetime.datetime.now()
    # t = now.isoformat("T", "milliseconds")
    #t = now.isoformat("T")[0:-3]
    #return t + "Z"


def signature(timestamp, method, request_path, body, secret_key):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)
    print "message", message , "!!"
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)
