import socket
import threading
from pacman import PacmanGame, runGames

UDP_IP = "127.0.0.1"
UDP_PORT = 1338
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))
command = ""
print("Server on port: " + str(UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    commandArgs = data.split(',')
    UDPcommand = commandArgs[0]
    if(UDPcommand == "STARTGAME"):
        pacmanGame = PacmanGame()
        command = pacmanGame.readCommand([])
        pacmanGame.start()
        print("command")
        print(command)
        pacmanGame.onThread(runGames, **command)
    elif(UDPcommand == "MOVE"):
        print("move")
        agentId = int(commandArgs[1])
        pacmanGame.onThread(PacmanGame.move, int(commandArgs[1]), commandArgs[2])
        #if(agentId == 0):
        #    print("pacman moves " + commandArgs[2])
        #    command['pacman'].keys = [commandArgs[2],commandArgs[2]]