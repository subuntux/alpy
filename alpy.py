import os 

def show(text):
    print(text)
    
def user(text):
    return input(text)
    
def user_l(text):
    return input(text).lower()
    
def case_if(variable, content):
    if variable == content:
        return True

def case_elif(variable, content):
    if variable == content:
        return True

def case_else(output):
    if output is not None:
        output()
        
def cmd(command):
    os.system(command)
    
def sys_clear():
    os.system("clear")