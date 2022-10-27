
from G_System_DataFrame_ID import *
from G_System_RemoteFrame_ID import *

def G_System_ID_Decode(ID,RTR):
    
    return_instance = None
    
    if(ID != 'Null'):
    
        if(RTR == "Remote"):
            return_instance = RemoteFrame_ID_Def(int(ID,16))
        elif(RTR == "Data"):
            return_instance = DataFrame_ID_Def(int(ID,16))
            
        return return_instance
    

if __name__ == "__main__":
    
    my_ID = "0x020"
    my_RTR = "Remote"
    
    my_GID_instance = G_System_ID_Decode(my_ID,my_RTR)
    

    my_GID_instance.print_info()
    
    
    my_ID = "0x4DF"
    my_RTR = "Data"
    
    my_GID_instance = G_System_ID_Decode(my_ID,my_RTR)
    

    my_GID_instance.print_info()
    

