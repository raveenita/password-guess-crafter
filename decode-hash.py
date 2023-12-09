#!/usr/bin/python3

import sys
from enum import Enum

hash = ""
strategy_type = ""

class STRATEGY_TYPES(Enum): 
	SHA1 = 'SHA1'
	SHA256 = 'SHA256'
	MD5 = 'MD5'

def verify_args():
	global hash
	global strategy_type

	if hash == "":
		hash =  input("Type a hash: ")

	if strategy_type == "":
		strategy_type = input("Type a hash strategy: ")

def define_algoritm(strategy):
    def strategy_sha1():
        return STRATEGY_TYPES.SHA1

    def strategy_sha256():
        return STRATEGY_TYPES.SHA256

    def default_strategy():
        return "Choose a cryptography algoritm"

    switch = {
        1: strategy_sha1,
        2: strategy_sha256
    }

    func = switch.get(strategy, default_strategy)

    return func()

def decode_hash(hash, strategy):
	print(hash)
	print(strategy)

verify_args()
decode_hash(hash, strategy_type)
