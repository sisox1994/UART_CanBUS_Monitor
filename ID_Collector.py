
class ID_Collector_Def:
    
    def __init__(self) -> None:
        self.ID_Array  = []
        self.RTR_Array = []
        pass
    
    def get_len(self):
        return len(self.ID_Array)

    def add_ID(self,ID_In,RTR_In):
        
        exisit = 0
        for idx in range( 0 , self.get_len() ):
        
            if ( (ID_In == self.ID_Array[idx]) and (RTR_In == self.RTR_Array[idx]) ) :
                exisit = 1
                break
            else:
                exisit = 0
    
        if exisit == 0:
            self.ID_Array.append(ID_In) 
            self.RTR_Array.append(RTR_In)
        
    def get_ID_Array(self):
        return self.ID_Array
    
    def get_RTR_Array(self):
        return self.RTR_Array
            
        
if __name__ == "__main__":    

    ID_1 = "0x020"
    ID_2 = "0x4FD"
    ID_3 = "0x020"
    ID_4 = "0x3A0"
    
    RTR_1 = "Remote"
    RTR_2 = "Data"
    RTR_3 = "Remote"
    RTR_4 = "Data"

    myID_Collector = ID_Collector_Def()
    
    myID_Collector.add_ID(ID_1,RTR_1)
    myID_Collector.add_ID(ID_2,RTR_2)
    myID_Collector.add_ID(ID_3,RTR_3)
    myID_Collector.add_ID(ID_4,RTR_4)


    print(myID_Collector.get_ID_Array())
    print(myID_Collector.get_RTR_Array())
    


    
    
    

    
    
    


    
    
