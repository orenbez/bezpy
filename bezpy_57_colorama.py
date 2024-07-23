import colorama
from colorama import Fore, Back, Style

# How To Print Colored Text in Python  https://pypi.org/project/colorama/
# https://www.youtube.com/watch?v=u51Zjlnui4Y

# BLACK=30, BLUE=34, CYAN=36, GREEN=32, MAGENTA=35, RED=31, WHITE=37, YELLOW=33,  RESET=39
# LIGHTBLACK_EX=90, LIGHTBLUE_EX=94, LIGHTCYAN_EX=96, LIGHTGREEN_EX=92,
# LIGHTMAGENTA_EX=95, LIGHTRED_EX=91, LIGHTWHITE_EX=97, LIGHTYELLOW_EX=93

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL # Note RESET_ALL will also reset Fore & Back Colors

colorama.init(autoreset=True)  # After each print statement color/styles are reset to default
                               # To do it manually you would use for example Print(f"{Fore.RED}...{Fore.RESET}")

print(f'{Fore.RED}some red text{Fore.RESET}')     # SAME AS BELOW
print('\033[31m' + 'some red text' + '\033[39m')  # UNDER THE HOOD THIS IS WHATS HAPPENING

# TECHNICALLY {Fore.RESET} not required since you have set 'autoreset=True'

print(f"{Fore.RED}C{Fore.GREEN}O{Fore.YELLOW}L{Fore.BLUE}O{Fore.MAGENTA}R{Fore.CYAN}S{Fore.WHITE}!")
print(f"{Fore.RED}Fore.RED")
print(f"{Fore.GREEN}Fore.GREEN")
print(f"{Fore.YELLOW}Fore.YELLOW")
print(f"{Fore.BLUE}Fore.BLUE")
print(f"{Fore.MAGENTA}Fore.MAGENTA")
print(f"{Fore.CYAN}Fore.CYAN")
print(f"{Fore.WHITE}Fore.WHITE")
print(f"{Fore.LIGHTRED_EX}Fore.LIGHTRED_EX")
print(f"{Fore.LIGHTGREEN_EX}Fore.LIGHTGREEN_EX")
print(f"{Fore.LIGHTYELLOW_EX}Fore.LIGHTYELLOW_EX")
print(f"{Fore.LIGHTBLUE_EX}Fore.LIGHTBLUE_EX")
print(f"{Fore.LIGHTMAGENTA_EX}Fore.LIGHTMAGENTA_EX")
print(f"{Fore.LIGHTCYAN_EX}Fore.LIGHTCYAN_EX")
print(f"{Fore.LIGHTWHITE_EX}Fore.LIGHTWHITE_EX")
print(f"{Fore.RESET}Fore.RESET") # Not required as you have set 'autoreset=True'  above
print(f"{Back.RED}B{Back.GREEN}A{Back.YELLOW}C{Back.BLUE}K{Back.MAGENTA}G{Back.CYAN}R{Back.WHITE}O{Back.RED}U{Back.GREEN}N{Back.YELLOW}D{Back.BLUE}!")
print(f"{Back.RED}Back.RED")
print(f"{Back.GREEN}Back.GREEN")
print(f"{Back.YELLOW}Back.YELLOW")
print(f"{Back.BLUE}Back.BLUE")
print(f"{Back.MAGENTA}Back.MAGENTA")
print(f"{Back.CYAN}Back.CYAN")
print(f"{Back.WHITE}Back.WHITE")
print(f"{Back.LIGHTRED_EX}Back.LIGHTRED_EX")
print(f"{Back.LIGHTGREEN_EX}Back.LIGHTGREEN_EX")
print(f"{Back.LIGHTYELLOW_EX}Back.LIGHTYELLOW_EX")
print(f"{Back.LIGHTBLUE_EX}Back.LIGHTBLUE_EX")
print(f"{Back.LIGHTMAGENTA_EX}Back.LIGHTMAGENTA_EX")
print(f"{Back.LIGHTCYAN_EX}Back.LIGHTCYAN_EX")
print(f"{Back.LIGHTWHITE_EX}Back.LIGHTWHITE_EX")
print(f"{Back.RESET}Back.RESET")
print(f"{Style.DIM}Style.DIM")
print(f"{Style.NORMAL}Style.NORMAL")
print(f"{Style.BRIGHT}Style.BRIGHT")
print(f"{Style.RESET_ALL}Style.RESET_ALL")
print(f"{Style.BRIGHT}{Fore.RED}Style.BRIGHT")
print(f"{Style.BRIGHT}{Fore.GREEN}Style.BRIGHT")
print(f"{Style.BRIGHT}{Fore.YELLOW}Style.BRIGHT")
print(f"{Style.BRIGHT}{Fore.BLUE}Style.BRIGHT")
print(f"{Style.BRIGHT}{Fore.MAGENTA}Style.BRIGHT")
print(f"{Style.BRIGHT}{Fore.CYAN}Style.BRIGHT")
print(f"{Style.BRIGHT}{Fore.WHITE}Style.BRIGHT")

print(f"{Fore.YELLOW}{Back.RED}C{Back.GREEN}{Fore.RED}O{Back.YELLOW}{Fore.BLUE}M{Back.BLUE}{Fore.BLACK}B{Back.MAGENTA}{Fore.CYAN}I{Back.CYAN}{Fore.GREEN}N{Back.WHITE}A{Back.RED}T{Back.GREEN}I{Back.YELLOW}O{Back.BLUE}N")
print(f"{Fore.GREEN}{Back.RED}{Style.BRIGHT}Green Text - Red Background - Bright")
print(f"{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}Cyan Text - Black Background - Bright")



