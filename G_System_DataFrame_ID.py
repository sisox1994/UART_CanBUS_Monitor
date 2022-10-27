# G-System Canbus Data Frame ID analyze

from Node_E_shifting_Enviolo import *
from Node_Remote import *
from Node_User_Interface_Enviolo import *


Enviolo_MODE = True

FUNCTION_GROUP = {
    0x0:"Network_manager",
    0x1:"Error_Indication",
    0x2:"Response_Data_For_Remote",
    0x3:"Normal_data_transmission",
    }

NODE_GROUP = {
    0x0:"Reserved",
    0x1:"Service_Tool",
    0x2:"User_Interface",
    0x3:"Sensor",
    0x4:"Remote",
    0x5:"Display",
    0x6:"Drive_chain",
    0x7:"YAMAHA",
    0x8:"E-shifting",
    0x9:"E-suspension",
    0xA:"SMP",
    0xB:"Sub_Energy_Pack",
    0xC:"Energy_Pack",
    0xD:"PANASONIC",
    0xE:"Charger",
    0xF:"E-YouBike_and_FW_Update"
    }

TYPE_GROUP = {
    0x0:"Active",
    0x1:"Passive",
    }

# ============== Active Data ======================================

# Node = 0x2
Active_Data_Address_for_User_Interface = {
    0x0:"Error",
    0x1:"Remote_Control_Command",
    0x2:"Display",
    0x3:"Cycling",
    0x4:"Dual_Battery_Command",
    }

# Node = 0x3
Active_Data_Address_for_Sensor_System = {
    0x0:"Error",
    0x1:"Cycling",
    0x2:"Posture_1",
    0x3:"Calibration",
    0x4:"Posture_2",
    0x5:"Posture_3",
    }


# Node = 0x6
Active_Data_Address_for_Drive_Chain = {
    0x0:"Error",
    0x1:"Cycling_Command",
    0x2:"Cycling_Data_1",
    0x3:"Cycling_Data_2",
    0x4:"Cycling_Data_3",
    0x5:"See_YAMAHA_E-shifting Note.",
    0x6:"See_YAMAHA_E-shifting Note.",
    0x7:"See_YAMAHA_E-shifting Note." ,
    0x8:"See_YAMAHA_E-shifting Note.",
    0x9:"See_YAMAHA_E-shifting Note.",
    0xA:"See_YAMAHA_E-shifting Note.",
    0xB:"See_YAMAHA_E-shifting Note.",
    0xC:"See_YAMAHA_E-shifting Note." ,
    0xD:"See_YAMAHA_E-shifting Note.",
    0xE:"Cycling_Data_4",
    0xF:"undefined",
    }

# Node = 0xB
Active_Data_Address_for_Sub_Energy_Pack = {
    0x0:"Error_Alarm",
    0x1:"Capacity",
    0x2:"Measure_data_1",
    0x3:"Smart_Charge",
    0x4:"Dual_Battery",
    }

# Node = 0xC
Active_Data_Address_for_Energy_Pack = {
    0x0:"Error_Alarm",
    0x1:"Capacity",
    0x2:"Measure_data_1",
    0x3:"Smart_Charge",
    0x4:"Dual_Battery",
    }

# Node = 0xE
Active_Data_Address_for_Charge_System = {
    0x0:"Error",
    0x1:"Status",
    0x2:"Charge_Situation",
    }

# Node = 0xF
Active_Data_Address_for_GIANT_Application_System = {
    0x0:"Firmware_Update_Command",
    0x1:"Firmware_Update_Data",
    0x4:"E-Youbike_Command",
    0xE:"Parameter_Writing_Command",
    0xF:"Parameter_Writing_Data",
    }

# ============== Passive  Data ======================================

# Node = 0x2
Passive_Data_Address_for_User_Interface = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version",
    0x2:"EV_Category",
    0x3:"Default_Parameter",
    0x4:"Service",
    0x5:"Riding_1",
    0x6:"Internal_Error_Time_1" ,
    0x7:"Internal_Error_Time_2",
    0x8:"Riding_2",
    0x9:"Reserved",
    0xA:"External_Error_Time_1",
    0xB:"External_Error_Time_2",
    0xC:"Frame_Number_1",
    0xD:"Frame_Number_2",
    0xE:"Frame_Number_3",
    0xF:"Confirmation",
    }

# Node = 0x3
Passive_Data_Address_for_Sensor_System = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version",
    0x2:"Reserved",
    0x3:"Reserved",
    0x4:"Reserved",
    0x5:"Reserved",
    0x6:"Internal_Error_Time",
    0x7:"Reserved",
    0x8:"Reserved",
    0x9:"Reserved",
    0xA:"Reserved" ,
    0xB:"Reserved" ,
    0xC:"Reserved",
    0xD:"Reserved",
    0xE:"Reserved",
    0xF:"Confirmation",
    }



# Node = 0x6 
Passive_Data_Address_for_Drive_Chain = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version",
    0x2:"EV_Category",
    0x3:"Default_Parameter_1",
    0x4:"Service",
    0x5:"Riding_Data_1",
    0x6:"Internal_Error_Time_1",
    0x7:"Internal_Error_Time_2",
    0x8:"Internal_Error_Time_3",
    0x9:"Internal_Error_Time_4",
    0xA:"Internal_Error_Time_5",
    0xB:"Default_Parameter_2"    ,
    0xC:"Riding_Data_2" ,
    0xD:"Internal_Error_Time_6",
    0xE:"Reserved",
    0xF:"Confirmation",    
    }

# Node = 0xB
Passive_Data_Address_for_Sub_Energy_Pack = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version",
    0x2:"Meature_Data_2",
    0x3:"History_Data_1",
    0x4:"History_Data_2",
    0x5:"History_Data_3",
    0x6:"Internal_Error_Time_1",
    0x7:"Internal_Error_Time_2",
    0x8:"Reserved",
    0x9:"Reserved",
    0xA:"Service",
    0xB:"Core-Pack_type",
    0xC:"Reserved",
    0xD:"Reserved", 
    0xE:"Reserved",
    0xF:"Confirmation", 
    }

# Node = 0xC
Passive_Data_Address_for_Energy_Pack = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version",
    0x2:"Meature_Data_2",
    0x3:"History_Data_1",
    0x4:"History_Data_2",
    0x5:"History_Data_3",
    0x6:"Reserved",
    0x7:"Internal_Error_Time_2",
    0x8:"Reserved",
    0x9:"Reserved",
    0xA:"Service",
    0xB:"Core-Pack_type",
    0xC:"Reserved",
    0xD:"Reserved", 
    0xE:"Reserved",
    0xF:"Confirmation", 
    }

# Node = 0xE
Passive_Data_Address_for_Charge_System = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version",
    0x2:"History",
    0x3:"Reserved",
    0x4:"Reserved",
    0x5:"Reserved",
    0x6:"Internal_Error_Time",
    0x7:"Reserved",
    0x8:"Reserved",
    0x9:"Reserved",
    0xA:"Reserved",
    0xB:"Reserved",
    0xC:"Reserved",
    0xD:"Reserved", 
    0xE:"Reserved",
    0xF:"Reserved", 
    }

# Node = 0xF
Passive_Data_Address_for_GIANT_Application_System = {
    0x0:"Firmware_Updating_ACK_Command",
    0x1:"Firmware_Updating_ACK_Data",
    0x2:"History",
    0x3:"Reserved",
    0x4:"Reserved",
    0x5:"Reserved",
    0x6:"Reserved",
    0x7:"Reserved",
    0x8:"Reserved",
    0x9:"Reserved",
    0xA:"Reserved",
    0xB:"Reserved",
    0xC:"Reserved",
    0xD:"Reserved", 
    0xE:"Parmeter Writing ACK",
    0xF:"Reserved", 
    }




    # 0x0:"Reserved",
    # 0x1:"Service_Tool",
    # 0x2:"User_Interface",
    # 0x3:"Sensor",
    # 0x4:"Remote",
    # 0x5:"Display",
    # 0x6:"Drive_chain",
    # 0x7:"YAMAHA",
    # 0x8:"E-shifting",
    # 0x9:"E-suspension",
    # 0xA:"SMP",
    # 0xB:"Sub_Energy_Pack",
    # 0xC:"Energy_Pack",
    # 0xD:"PANASONIC",
    # 0xE:"Charger",
    # 0xF:"E-YouBike_and_FW_Update"
    # }

class DataFrame_ID_Def:
    
    mask_0 = 0x00F # Address
    mask_1 = 0x010 # Type (active/passive)
    mask_2 = 0x1E0 # Node group  
    mask_3 = 0x600 # Function group
    
    def __init__(self,data) -> None:
        self.RTR = "Data"
        self.ID = data
        self.function_value = None
        self.node_value = None
        self.type_value = None
        self.address_value = None
        
        self.address_value =  (data & self.mask_0)
        self.type_value = (data & self.mask_1) >> 4
        self.node_value = (data & self.mask_2) >> 5
        self.function_value = (data & self.mask_3) >> 9
        pass
    
    def print_info(self):
        if(self.RTR == "Data"):
            self.print_data_frame_info(0) 
    
    def print_data_frame_info(self,shift_space) -> str:
                
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
                
        print( space_buffer + "-> [Data Frame Info]  ===============================================")
        print( space_buffer + "[Data]  ID:[" + hex(self.ID) +"]" )
        print( space_buffer + "Function:[" + self.get_function() +"]")
        print( space_buffer + "Node:[" + self.get_node() + "]" )
        print( space_buffer + "Type:[" + self.get_packet_type() + "]" )    
        print( space_buffer + "Address:[" + self.get_data_address() + "]" )
        print( space_buffer + "=====================================================================")
        pass
    
    def get_function(self) -> str:
        return FUNCTION_GROUP[self.function_value]
    
    def get_node(self) -> str:
        return NODE_GROUP[self.node_value]

    def get_packet_type(self) -> str:
        return TYPE_GROUP[self.type_value]
    
    def get_data_address(self) -> str:
        if (self.get_packet_type() == "Active"):
            
            if(self.get_node() == "User_Interface"):
                
                # 參考 Enviolo 專用 G-System 文件 
                if Enviolo_MODE == True:
                    return Active_Data_Address_for_User_Interface_Enviolo[self.address_value]
                    
                # 參考 G-System 通用文件     
                else:
                    if (self.address_value < len(Active_Data_Address_for_User_Interface)):
                        return Active_Data_Address_for_User_Interface[self.address_value]
                    else:
                        return "undefined"
                
                
                
            elif(self.get_node() == "Sensor"):
                return Active_Data_Address_for_Sensor_System[self.address_value]
            elif(self.get_node() == "Drive_chain"):                
                return Active_Data_Address_for_Drive_Chain[self.address_value] 
            elif(self.get_node() == "Remote"):
                return Active_Data_Address_for_Remote_System[self.address_value]
            elif(self.get_node() == "Sub_Energy_Pack"):
                return Active_Data_Address_for_Sub_Energy_Pack[self.address_value] 
            elif(self.get_node() == "Energy_Pack"):
                return Active_Data_Address_for_Energy_Pack[self.address_value] 
            elif(self.get_node() == "Charger"):
                return Active_Data_Address_for_Charge_System[self.address_value] 
            elif(self.get_node() == "E-YouBike_and_FW_Update"):
                return Active_Data_Address_for_GIANT_Application_System[self.address_value] 
            elif(self.get_node() == "E-shifting"):
                return Active_Data_Address_for_E_Shifting_Enviolo[self.address_value] 
           
           
            else:
                return "undefined"
            pass  
        elif (self.get_packet_type()  == "Passive" ):
            
            if(self.get_node() == "User_Interface"):
                return Passive_Data_Address_for_User_Interface[self.address_value]
            elif(self.get_node() == "Sensor"):
                return Passive_Data_Address_for_Sensor_System[self.address_value]
            #elif(self.get_node() == "Remote"):
                #return Passive_Data_Address_for_Remote_System[self.address_value]
            elif(self.get_node() == "Drive_chain"):
                return Passive_Data_Address_for_Drive_Chain[self.address_value] 
            elif(self.get_node() == "Sub_Energy_Pack"):
                return Passive_Data_Address_for_Sub_Energy_Pack[self.address_value] 
            elif(self.get_node() == "Energy_Pack"):
                return Passive_Data_Address_for_Energy_Pack[self.address_value] 
            elif(self.get_node() == "Charger"):
                return Passive_Data_Address_for_Charge_System[self.address_value] 
            elif(self.get_node() == "E-YouBike_and_FW_Update"):
                return Passive_Data_Address_for_GIANT_Application_System[self.address_value] 
            elif(self.get_node() == "E-shifting"):
                return Passive_Data_Address_for_E_Shifting_Enviolo[self.address_value] 
           
            else:                
                return "undefined"
            
            pass



if __name__ == "__main__":
    
    # case 1: ID is String 
    ID_Data_Example = "0x491"
    my_Test_id = DataFrame_ID_Def(int(ID_Data_Example,16))
    
    # case 2: ID is Int
    #ID_Data_Example = 0x4DF
    #my_Test_id = DataFrame_ID_Def(ID_Data_Example)
    my_Test_id.print_data_frame_info(0)