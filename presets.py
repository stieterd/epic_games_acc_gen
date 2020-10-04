import os
import pickle

def clear():

	os.system("cls")

cls = clear

def get_response(fn):

	with open(f"{fn}.resp", 'rb') as reader:

		return pickle.load(reader)
