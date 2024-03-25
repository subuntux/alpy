# create alpy

Following functions are actually used

v.1.0
```python
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
```

v.1.1
```python
import os 
import sys

def show(text):
    print(text)
    
def user(text):
    return input(text)
    
def user_l(text):
    return input(text).lower()
    
def case(variable, content):
    return variable == content

def cmd(command):
    os.system(command)
    
def sys_clear():
    os.system("clear")
    
def arg_start(total_args, min_args):
    if len(sys.argv) < min_args + 1:
        print(f"Usage: {sys.argv[0]} <arguments>")
        print(f"At least {min_args} arguments required.")
        sys.exit(1)
    if len(sys.argv) > total_args + 1:
        print(f"Usage: {sys.argv[0]} <arguments>")
        print(f"Too many arguments. Expected {total_args} arguments.")
        sys.exit(1)

def arg(*args):
    for arg in args:
        if arg in sys.argv:
            return True
    return False
```

## Import

```python
from alpy import alpy
```

### Instruction

<details id="option-menu">
  <summary>Option Menu</summary>
  1. In Python (Without alpy modul)
  ```Python
  import os
  
  def main_menu()
    os.system("clear")
    print("[1] Option 1")
    print("[2] Option 2")
    print("[3] Option 3")
    
    choice = input(select: ).lower()
    
    if choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    else:
        print("Error")
    ```

    2. In Python (With alpy modul)
    ```python
    from alpy import alpy
    
    def main_menu()
        alpy.sys_clear()
        alpy.show("[1] Option 1")
        alpy.show("[2] Option 2")
        alpy.show("[3] Option 3")
        
        choice = alpy.user_l("select: ")
        
        if alpy.case(choice, '1'):
            option1()
        elif alpy.case(choice, '2'):
            option2()
        elif alpy.case(choice, '3'):
            option3()
        else:
            alpy.show("Error")
            
</detail>