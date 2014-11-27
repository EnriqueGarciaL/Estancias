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
    file = open("datos.txt","a+")
    for x in range(len(fx)):
        file.write(str(fx[x])+"\t")
    file.write("\n")
    file.close()

output = Popen(['python', 'ED.py'], stdout=PIPE)
result.append(output.stdout.read())
escribir(result)
