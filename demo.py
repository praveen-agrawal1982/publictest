print("Greetings")
print("hello")  
import sys
import os
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(os.getenv('name'))
print(os.getenv('CDAL_host'))

f= open(os.getenv('MODEL_PATH') + "/model.pl","w+")
f.write("This is demo file")
f.close()
