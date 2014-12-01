# import os
#
# for i in range(30):
#     pipe = os.popen('python ED.py')
#     pipe.close()
#
# pip = os.popen('python boxp.py')
# pip.close()

from subprocess import Popen, PIPE

result = []

def escribir(fx):
    index=[]
    file = open("datos.txt","a+")
    for x in range(len(fx)):
        for y in range (len(fx[x])):
            if(fx[x][y].isdigit() or fx[x][y]=="." or fx[x][y]=="n" or fx[x][y]=="e" or fx[x][y]=="+" or fx[x][y]=="-"):
                if(fx[x][y]=="n"):
                    index.append("\t")
                else:
                    index.append(fx[x][y])

    for z in range (len(index)):
        file.write(index[z])
    file.write("\n")

    file.close()



output = Popen(['python', 'ED.py'], stdout=PIPE)
salida = output.stdout.read()
result.append(salida)
output.stdout.close();
escribir(str(result))
