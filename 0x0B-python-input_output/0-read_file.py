#!/usr/bin/python3
"""IMPLEMETATION"""

def read_file(filename=""):
	"""Reads the files contents and print to the stdou"""
	with open(filename) as file:
		print(file.rstrip())
