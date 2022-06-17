with open("registro.txt","r") as file :
   first_line = file.readline()
   for last_line in file :
      pass
print("\033[94mUsado por primera vez : \033[0m"+first_line)
print("\033[94mUtilizado más recientemente : \033[0m"+last_line)
