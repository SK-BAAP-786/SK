import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from SK_enc import Main

    Main()

elif bit == '32bit':

    from SKK32 import Main

    Main()

 
 




 






 

 

 

 

 

 

 

 

 

 

 

 


 



 



 



 



 



 



 



 



 


