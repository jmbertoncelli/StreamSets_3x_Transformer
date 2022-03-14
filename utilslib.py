import os
import sys
import yaml
import logging
import cryptography
from cryptography.fernet import *


# key = Fernet.generate_key()
# # print(key)
# # b'CHjQEGk9Cvk9J5sqmuvvx96gjzp17SFkX2n2xDLCm08='
# key = 'CHjQEGk9Cvk9J5sqmuvvx96gjzp17SFkX2n2xDLCm08='
# cypher_suite = Fernet(key)
# e = cypher_suite.encrypt("Batman".encode("utf-8"))
# cypher_suite.decrypt(e).decode("utf-8")


os.environ["CYPHER_KEY"] = "CHjQEGk9Cvk9J5sqmuvvx96gjzp17SFkX2n2xDLCm08="


class Config:
    __CONFIG = {}
    __USER = None
    __PASSWORD = None
    __PATH = None
    __KEY = None
    __CYPHER = None
    __ERROR = False
    __URL_SCH = None
    __URL_SDC = None
    __SDK_KEY = None
    __URL_TX = None

    def __init__(self, path):
        Config.__PATH = path
        Config.__KEY = os.environ["CYPHER_KEY"]
        Config.__CYPHER = Fernet(Config.__KEY)

    def load(self):
        if not os.path.exists(Config.__PATH):
            Config.__ERROR = True
            print(f"Config path or file {Config.__PATH} is invalid.")
            return
        Config.__ERROR = False
        Config.__CONFIG = yaml.safe_load(open(Config.__PATH, "r"))
        Config.__USER = Config.__CONFIG["_USER_"]
        Config.__PASSWORD = Config.__CONFIG["_PASSWORD_"]
        Config.__URL_SCH = Config.__CONFIG["__URL_SCH__"]
        Config.__URL_SDC = Config.__CONFIG["__URL_SDC__"]
        Config.__SDK_KEY = Config.__CONFIG["__SDK_KEY__"]
        Config.__URL_TX = Config.__CONFIG["__URL_TX__"]

    def dump(self):
        if Config.__ERROR == True:
            return
        _ = yaml.dump(Config.__CONFIG, open(Config.__PATH, "w"))

    def getUser(self):
        return Config.__CYPHER.decrypt(Config.__USER).decode("utf-8")

    def setUser(self, n):
        Config.__CONFIG["_USER_"] = Config.__CYPHER.encrypt(n.encode("utf-8"))

    def getPassword(self):
        return Config.__CYPHER.decrypt(Config.__PASSWORD).decode("utf-8")

    def setPassword(self, n):
        Config.__CONFIG["_PASSWORD_"] = Config.__CYPHER.encrypt(n.encode("utf-8"))

    def getUrlSch(self):
        return Config.__CYPHER.decrypt(Config.__URL_SCH).decode("utf-8")

    def setUrlSch(self, n):
        Config.__CONFIG["__URL_SCH__"] = Config.__CYPHER.encrypt(n.encode("utf-8"))

    def getUrlSdc(self):
        return Config.__CYPHER.decrypt(Config.__URL_SDC).decode("utf-8")

    def setUrlSdc(self, n):
        Config.__CONFIG["__URL_SDC__"] = Config.__CYPHER.encrypt(n.encode("utf-8"))

    def getUrlTx(self):
        return Config.__CYPHER.decrypt(Config.__URL_TX).decode("utf-8")

    def setUrlTx(self, n):
        Config.__CONFIG["__URL_TX__"] = Config.__CYPHER.encrypt(n.encode("utf-8"))

    def getSdkKey(self):
        return Config.__CYPHER.decrypt(Config.__SDK_KEY).decode("utf-8")

    def setSdkKey(self, n):
        Config.__CONFIG["__SDK_KEY__"] = Config.__CYPHER.encrypt(n.encode("utf-8"))