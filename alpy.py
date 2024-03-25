import os 
import sys

def show(text):
    print(text)
    
def user(text):
    return input(text)
    
def user_l(text):
    return input(text).lower()
    
def cmd(command):
    os.system(command)
    
def sys_clear():
    os.system("clear")
    
