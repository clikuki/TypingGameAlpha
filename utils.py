import os

def clear_screen():
    os.system("clear")
    # subprocess.run("clear", shell=True)
    
def print_separator():
    size_x,_ = os.get_terminal_size()
    print("─" * size_x)