
# G-System Canbus Remote Frame ID analyze

MOTIONS = {
    0x0:"Heartbeat"    ,
    0x1:"Confirmation" ,
    0x2:"Active_data_1",
    0x3:"Active_data_2",
    0x4:"Passive_data_1",
    0x5:"Passive_data_2",
    0x6:"Passive_data_3",
    0x7:"Passive_data_4"
    }

REQUIREMENT_NODE = {
    0x0:"Reserved"    ,
    0x1:"Service_Tool" ,
    0x2:"User_Interface",
    0x3:"Sensor",
    0x4:"Remote",
    0x5:"Display",
    0x6:"Drive_chain",
    0x7:"YAMAHA",
    0x8:"E-shifting"    ,
    0x9:"E-suspension" ,
    0xA:"SMP",
    0xB:"Sub_Energy_Pack",
    0xC:"Energy_Pack",
    0xD:"PANASONIC",
    0xE:"Charger",
    0xF:"E-YouBike_and_FW_Update"
    }

RESPONSE_NODE = {
    0x0:"All_System"    ,
    0x1:"Service_Tool" ,
    0x2:"User_Interface",
    0x3:"Sensor",
    0x4:"Remote",
    0x5:"Display",
    0x6:"Drive_Chain",
    0x7:"YAMAHA",
    0x8:"E-shifting"    ,
    0x9:"E-suspension" ,
    0xA:"SMP",
    0xB:"Sub_Energy_Pack",
    0xC:"Energy_Pack",
    0xD:"PANASONIC",
    0xE:"Charger_System",
    0xF:"E-YouBike_and_FW_Update"
    }


class RemoteFrame_ID_Def:
    
    mask_0 = 0x00F
    mask_1 = 0x0F0
    mask_2 = 0x700
    
    def __init__(self,data) -> None:
        self.RTR = "Remote"
        self.ID = data
        self.motion_value = None
        self.Req_Node_value = None
        self.Res_Node_value = None
        
        self.res_node_value =  (data & self.mask_0)
        self.req_node_value = (data & self.mask_1) >> 4
        self.motion_value = (data & self.mask_2) >> 8
        pass
    
    def print_info(self):
        if(self.RTR == "Remote"):
            self.print_remote_frame_info(0)
    
    
    def print_remote_frame_info(self,shift_space) -> str:
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [Remote Frame Info]  ==============================================")
        print( space_buffer + "[Remote]  ID:[" + hex(self.ID) +"]" )
        print( space_buffer + "Motion:[" + self.get_motion() +"]")
        print( space_buffer + "REQ Node:[" + self.get_req_node() + "]" )
        print( space_buffer + "RES Node:[" + self.get_res_node() + "]" )
        print( space_buffer + "=====================================================================")
        pass
        
    
    
    def get_motion(self) -> str:
        return MOTIONS[self.motion_value]
    
    def get_req_node(self) -> str:
        return REQUIREMENT_NODE[self.req_node_value]

    def get_res_node(self) -> str:
        return RESPONSE_NODE[self.res_node_value]


if __name__ == "__main__":
    
    # case 1: ID is String 
    ID_Data_Example = "0x426"
    my_Test_id = RemoteFrame_ID_Def(int(ID_Data_Example,16))
    
    # case 2: ID is Int
    #ID_Data_Example = 0x426
    #remote_id = RemoteFrame_ID_Def(ID_Data_Example)
    my_Test_id.print_remote_frame_info(0)



