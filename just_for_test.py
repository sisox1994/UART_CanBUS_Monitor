from G_System_ID import*

ID_LIST = ['0x020', '0x4df', '0x497', '0x59f', '0x42c', '0x590', '0x591', '0x592', '0x426', '0x4d0', '0x4d1', '0x4d2', '0x640', '0x641', '0x642', '0x643', '0x644', '0x646', '0x647', '0x648', '0x120', '0x280', '0x22c', '0x281', '0x580', '0x581', '0x582', '0x583', '0x22b', '0x42b', '0x424', '0x490', '0x491', '0x624', '0x126', '0x425', '0x12c', '0x6c0', '0x6c2', '0x6c4', '0x6ce', '0x780', '0x781', '0x782', '0x783', '0x6c1', '0x6c3']




# ID_LIST = ['0x20', '0x4df', '0x497', '0x59f', '0x426', '0x42c', '0x590', '0x591', '0x592', '0x4d0', '0x4d1', '0x4d2', '0x640', '0x641', '0x642', '0x643', '0x644', '0x646', '0x647', '0x648', '0x120', '0x280', '0x22c', '0x281', '0x582', '0x583', '0x580', '0x581', '0x22b', '0x42b', '0x424', '0x490', '0x491', '0x624', '0x126', '0x425', '0x12c', '0x6c0', '0x6c1', '0x6c2', '0x6c3', '0x6c4', '0x6ce', '0x780', '0x781', '0x782', '0x783']
# RTR_LIST = ['Remote', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Data', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Remote', 'Data', 'Data', 'Remote', 'Remote', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data']



ID_LIST = ['0x20', '0x59f', '0x4df', '0x497', '0x42c', '0x590', '0x591', '0x592', '0x426', '0x4d0', '0x4d1', '0x4d2', '0x640', '0x641', '0x642', '0x643', '0x644', '0x646', '0x647', '0x648', '0x120', '0x22c', '0x580', '0x581', '0x582', '0x583', '0x584', '0x22b', '0x42b', '0x424', '0x490', '0x491', '0x492', '0x624', '0x126', '0x425', '0x12c', '0x228', '0x500', '0x501', '0x502', '0x503', '0x64f', '0x6c0', '0x6c1', '0x6c2', '0x6c3', '0x6c4', '0x6ce', '0x6cf', '0x680', '0x681', '0x51f', '0x700', '0x701', '0x702', '0x703', '0x780', '0x781', '0x782', '0x783', '0x784', '0x6c5', '0x428', '0x510', '0x511', '0x512']
RTR_LIST = ['Remote', 'Data', 'Data', 'Data', 'Remote', 'Data', 'Data', 'Data', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Remote', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Data', 'Data', 'Data']

# ['0x20', '0x4df', '0x497', '0x59f', '0x426', '0x42c', '0x590', '0x591', '0x592', '0x4d0', '0x4d1', '0x4d2', '0x640', '0x641', '0x642', '0x643', '0x644', '0x646', '0x647', '0x648', '0x680', '0x120', '0x22c', '0x580', '0x581', '0x582', '0x583', '0x681', '0x22b', '0x42b', '0x424', '0x490', '0x491', '0x624', '0x126', '0x425', '0x6c0', '0x6c1', '0x6c2', '0x6c3', '0x6c4', '0x6ce', '0x780', '0x781', '0x782', '0x783', '0x124']
# ['Remote', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote', 'Remote', 'Remote', 'Data', 'Data', 'Remote', 'Remote', 'Remote', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Data', 'Remote']

        
if __name__ == "__main__":
    
    #myID = G_System_ID_Decode(CanRxBuffer.StdID,CanRxBuffer.RTR)  
    #myID.print_info() 
    
    
    for index in range(0,len(ID_LIST)):
        print("NO. " + str(index) )
        myID = G_System_ID_Decode( ID_LIST[index] , RTR_LIST[index] )
        myID.print_info() 
        
    
        

    
    
    

    
    
    


    
    
