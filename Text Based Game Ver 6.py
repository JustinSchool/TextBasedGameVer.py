# run in idle only
# import stuff
import time
from time import sleep
import sys
# arrays
YES = ["YES", "yes", "Yes", "y"]
NO = ["NO", "No", "no", "n"]
HELP = ["HELP","Help","help"]
# =======================================================================================================
# definitions

def HELP():
    slowtext("Type your options in capitals and the options that are capitalised are selectable")


def banana():
    print("Please type an option!")


def MAP():
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣶⣷⣆⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⢸⣷⣦⣤⣿⣿⣿⣿⣶⣦⣤⡀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣤⡀⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡿⢿⢿⣿⣿⣿⣿⣿⣹⣿⣿⣶⣶⣦⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣯⣼⣿⠟⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⣼⡿⣿⣿⣿⣷⣷⣿⣿⣿⣿⣽⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⣤⣠⣤⠤⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⣤⣿⣿⣿⡿⠉⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⣯⣿⣛⣛⣛⣿⡿⣯⣿⣿⣿⣝⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣹⣹⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣾⣿⣷⣿⣿⡛⣮⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣤⣄⣀⠄⠄⠄⠄⠄⣤⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢺⣿⣿⣿⣿⣿⡏⣿⣿⡦⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣏⣏⣻⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣭⡅⠄⠄⠄⠄⠄⠨⣭⣭⣍⣿⣿⣾⣯⣿⣿⣻⣿⣿⣿⣿⣿⣿⡿⠄⠄⢠⣦⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣠⣾⣿⣿⢿⣿⣟⣿⣯⣵⠿⠖⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⢸⣿⣿⣤⣀⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡇⠄⢾⣿⣿⣿⣇⣼⣆⠄⠄⠄⠄⠄⢘⣿⣿⣿⣿⢿⣿⣿⣿⣿⣫⢿⣒⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⣿⣾⣽⣿⣿⣿⢿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣼⣶⣶⡆⠹⣿⣿⣽⣿⠿⢿⣿⣿⣟⣛⣮⣿⣿⣿⣿⣿⡇⠄⠘⢿⣯⣽⣿⣿⡟⠃⠄⠄⢀⣴⣿⣯⣿⣷⣿⣿⣿⣿⣼⡏⠐⠚⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣽⣿⣻⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣮⣯⣿⣿⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⡀⢹⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣯⣽⣇⠄⢀⣾⠿⣿⣿⣻⣅⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⣻⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⡿⣿⣿⡎⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⢝⢟⡿⣽⠛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣯⣽⣿⣿⣿⣿⣛⣿⣿⣿⣿⣿⣿⡟⣁⣿⣿⣿⣿⣷⣾⣿⣿⣆⠻⠿⣿⣿⡿⢿⣿⣿⣿⢗⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣟⣿⣿⣿⣿⣿⢿⣾⣿⣿⣿⣿⢝⢿⢿⣇⠾⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣽⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⡿⢛⣴⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣦⣝⠻⣿⣿⣿⣿⣿⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣟⣻⣷⣿⣵⣽⡿⣿⣽⣿⣶⣈⣿⠄⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣾⣿⣿⣿⣿⢻⣿⠟⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣌⠻⣿⣿⣿⣿⣾⣿⣻⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡻⣿⣿⣿⣷⣿⣿⣿⡿⣿⣳⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⣼⣿⣿⣿⡿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠃⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⢻⣷⣌⠛⡉⣽⣿⣿⣟⢿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣻⣯⣿⣿⣿⣾⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⡻⣿⣿⣿⡟⣿⣿⣟⣻⣿⣿⠿⣿⣧⣿⣿⣿⣿⡿⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠙⣿⣿⣷⣻⠿⣿⣿⣿⣿⣽⣿⣷⣿⣿⢿⣻⣿⣿⣿⣿⣿⣧⣶⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠻⢋⣠⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡿⠿⠶⠶⠿⠿⠿⠿⠿⠿⠟⠟⠻⠄⠄⠄⢠⣷⣾⢷⣿⣿⣿⣿⣏⣟⣿⣿⣿⡿⣿⣿⣻⣿⣿⣿⣭⣿⣝⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⢠⣤⣭⣭⣭⣭⣭⣭⣭⣭⣥⣤⡄⣶⣶⣶⣖⣖⣶⣶⣿⣿⣿⢿⣿⣷⣤⣴⣿⣿⣿⣟⣻⣿⢻⣿⣿⣽⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣻⣻⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣷⣶⣿⣏⣯⣏⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣾⣽⣿⣟⣽⣿⣿⣿⢺⣿⣿⣿⣿⣯⢿⣿⣿⣿⣿⣿⣾⣿⣿⣿⠛⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣽⣿⣿⣟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⡛⣿⣿⣿⣻⣿⣿⣷⣿⣿⣿⡿⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣶⣿⣿⣿⣯⣿⣮⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⠿⢿⣿⣿⣿⣿⣸⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣻⣟⣴⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠉⠁⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣶⠾⠟⠛⠛⠛⠊⠉⠙⠛⠻⠛⠛⠛⠿⣿⣿⣿⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⠿⢿⣷⡶⢆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⡿⢻⣷⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡄⠄⠄⠄⠄⠄⠉⠻⢿⡏⠁⠄⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠈⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣶⣿⣷⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⢀⣀⣠⣶⣶⣦⣤⣤⠄⠄⠄⠄⠄⢸⠄⠠⡆⢀⡀⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠿⣿⣿⣿⣿⣿⠿⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⢿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⣙⣿⣿⡻⣛⣿⣿⡀⠄⠄⠄⠄⢸⠄⠄⠄⠙⠓⠠⠤⢀⡀⠄⠄⠄⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⣨⣽⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⢸⠄⠄⠄⠄⠄⠄⠈⠈⣛⡓⠄⠄⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⢿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠊⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠙⢻⣿⡋⠙⠉⠉⠳⣤⡀⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄⡞⣿⣶⡀⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠠⠋⠉⠄⠄⠄⠄⠄⢿⠄⠄⢸⠄⠄⠄⠄⠄⠄⠄⠄⢿⡿⠉⠁⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
    print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")


# =======================================================================================================
# slow text code i totally didnt steal
def slowtext(text):
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)


# fast text code i totally didnt steal
def fasttext(text):
    for char in text:
        sleep(0.025)
        sys.stdout.write(char)
    # more text code i didnt steal!!


def dramatic(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        # more text code i didnt steal!!


def speech(text):
    for char in text:
        sleep(0.03)
        sys.stdout.write(char)


# =======================================================================================================
fasttext(
    "Instructions \nWhen the text written in captial letters, this is a selectable option\nWhen ""-"" is displayed it means you can type your option\nand make sure to have caps lock on\nType HELP for help")
slowtext("\nType START the begin your journey... ")
####
while True:
    start = input("\n-")
    if start == "START":
        break
    elif start == "HELP":
        HELP()
    else:
        print("Please Type START ")
fasttext("\n\nYou are currently stationed in Brooklyn \nyour first mission is to explore the alleyways.")

dramatic("\n\n\n\nChapter 1 Your First Mission")

fasttext(
    "\n\nYou are a detective in Brooklyn it’s 9pm and you hear loud bangs.\nWhat do you do? Do you IGNORE the bang or INVESTIGATE?")
while True:
    x = input("\n\n-")
    if x == "INVESTIGATE":
        slowtext("You walk towards the direction of the loud bangs, you see bright explosions")
        break
    elif x == "HELP":
        print("You have two options ""IGNORE"" and ""INVESTIGATE""")
    elif x == "IGNORE":
        slowtext("You turn around and see a group of homeless people running away from \nthe direction of the bang")
        slowtext(
            "\n\nYou decide to investigate\nYou walk towards the direction of the loud bangs, you see bright explosions")
        break
    else:
        banana()
slowtext("\n\nA fireball flies towards your direction!\nWhat do you do? Run behind the DUMPSTER or the BOXES?")
while True:
    z = input("\n\n-")
    if z == "DUMPSTER":
        slowtext("The fireball narrowly misses you.\nYou creep up closer to the source of the fire.")
        break
    elif z == "BOXES":
        slowtext("You suffer severe burns to the shoulder")
        break
    elif z == "HELP":
        print("You have two options ""DUMPSTER"" and ""BOXES""")
    else:
        banana()
slowtext("\n\nYou discover that the source of the fire is an unattended box of fireworks")
slowtext("\nYou turn around you're surrounded by a group of men in dark trench coats")
slowtext("\nThey slowly close in onto you what do you do? RUN or FIGHT")
while True:
    n = input("\n\n-")
    if n == "RUN":
        slowtext("\nYou run into the nearby bushes and you keep quiet")
        break
    elif n == "FIGHT":
        slowtext("\nYou grab your gun and miss your bullet... You run into the bushes")
        break
    elif n == "HELP":
        print("You have two options ""RUN"" and ""FIGHT""")
    else:
        banana()
slowtext("\nYou hide in the bushes...\nHours go by and you are still there\n")
fasttext("\nHours go by and you return to the base")
dramatic("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
dramatic("\n\n\nYou are sent out to investigate a disturbance possibly involving a firearm")
slowtext("\nYou drive to the location of the disturbance")
slowtext(
    "\nA man in a black trench coat is running away from a warehouse and you assume the firearm threat is in there...")
fasttext("\nYou get out of your car and you creep in, you find a person tied up on a chair with guns pointed to him.")
slowtext("\nWhat do you do\nCALL for backup or run in SOLO")
while True:
    a = input("\n\n-")
    if a == "CALL":
        slowtext("\nYou call the headquarters but you alerted the attackers")
        break
    elif a == "SOLO":
        slowtext("You run in and slip and fall and alert the attackers")
        break
    elif a == "HELP":
        print("You have two options ""CALL"" and ""SOLO""")
    else:
        banana()
fasttext(
    "\nThe attackers are on high alert and are searching for you. You press the panic button and your backup is called.\nYour backup arrives and a firefight commences")
fasttext("\nYou go to the headquarters with a prisoner. He is sent off for questioning")
print("\nJoseph: ")
speech(
    "Good work out there, we couldn't have done it without you. I have a theory with all the crime tho...\nCome with me. All of this crime is based around the inner city and it is in a shape.\n I'll show you the map.")
print("\n")
MAP()
speech("You see?")
while True:
    l=input("\n\n-")
    if any(l in c for c in [YES, NO]):
        speech("\nYou see its weird that it would be shaped like that.")
    elif any(z in n for n in [HELP]):
        print("")
        break
    else:
        banana()
speech("\nThis is like they are trying to communicate something to us...")
dramatic("\n\n\n\n\nThe next day")
speech("\nYou think about the map and you realise the next crime will be committed around the middle of the triangle.")
dramatic("\nYou organise a stakeout...")
print("\nYou:")
speech("\nHey Joseph, want to help me uncover the criminals")
print("\nJoseph:")
speech("\nAnything for you boss...")
dramatic("\nThe next day...")
speech(
    "\nYou travel to the location of where you think the next crime will take place.\nYou arrive and you sit in a van by a bush and you get hungry do you get MCDONALDS or KFC")
while True:
    food = input("\n\n-")
    if food == "MCDONALDS":
        print("Joseph: ")
        speech("good choice")
        break
    elif food == "KFC":
        print("Joseph: ")
        speech("Idiot")
        break
    elif food == "HELP":
        print("You have two options, ""MCDONALDS"" and ""KFC")
    else:
        banana()
fasttext("\nYou walk into the restaurant and you eat.")
dramatic("\nLater in the night you are ready to scout")
dramatic("\nYou see a man running through the bushes behind the building he is wearing a dark shirt with a skimask\nWhat do you do, CHASE or SHOOT with taser")
while True:
    action = input("\n\n-")
    if action == "CHASE":
        fasttext("You run after him and you grab his leg and handcuff him.")
        break
    elif action == "SHOOT":
        fasttext("The suspect falls and hits the ground and you apprehend him")
        break
    elif action == "HELP":
        print("You have two options, ""CHASE"" and ""RUN""")
    else:
        banana()
fasttext("\nYou handcuff the suspect and detain him")