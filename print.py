print("Greetings")
  
import sys
import os
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(os.getenv('praveen'))
print(os.getenv('sunil'))


f= open(os.getenv('MODEL_PATH') + "/model.pl","w+")
f.write("sampleline")
f.close()
