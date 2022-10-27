# 0x4:"Remote",

# Node = 0x4
Active_Data_Address_for_Remote_System = {
    0x0:"Remote_1_Encode",
    0x1:"Remote_1_Button_CMD_State",
    0x2:"Reserved",
    0x3:"Reserved",
    0x4:"Reserved",
    0x5:"Reserved",
    0x6:"Reserved",
    0x7:"Remote_1_Confirmation",
    0x8:"Remote_2_Encode",
    0x9:"Remote_2_Button_CMD_State",
    0xA:"Reserved" ,
    0xB:"Reserved" ,
    0xC:"Reserved",
    0xD:"Reserved",
    0xE:"Reserved",
    0xF:"Remote_2_Confirmation",
    }


# Node = 0x4
# 問Primo "Remote node" 的 "Data Ftame" 的 "Passive Data" 定義在哪裡?
# 下面的網址只有定義 "Active Data"
# https://docs.google.com/spreadsheets/d/1zJcEorsDtyZFvj79Oo5twtJAAhUJfYAMTJwM1J1BmtY/edit#gid=601705787
# Passive_Data_Address_for_Remote_System = {
#     0x0:"Remote_1_Encode",
#     0x1:"Remote_1_ButtonState",
#     0x2:"Reserved",
#     0x3:"Reserved",
#     0x4:"Reserved",
#     0x5:"Reserved",
#     0x6:"Reserved",
#     0x7:"Remote_1_Confirmation",
#     0x8:"Remote_2_Encode",
#     0x9:"Remote_1_ButtonState",
#     0xA:"Reserved" ,
#     0xB:"Reserved" ,
#     0xC:"Reserved",
#     0xD:"Reserved",
#     0xE:"Reserved",
#     0xF:"Remote_2_Confirmation",
#     }



Remote_Command_List = {
    0x00:"No_Cmd_1",
    0x01:"Change_Battery",
    0x02:"Change_Light_Status",
    0x03:"Info_Display",
    0x04:"Assist_Up",
    0x05:"No_Cmd_2",
    0x06:"Reset_Value",
    0x07:"No_Cmd_3",
    0x08:"Brake",
    0x09:"Walk_Assist",
    0x0A:"Crank_ADJ_Manual",
    0x0B:"MEME_ADJ",
    0x0C:"Auto_Assist",
    0x0D:"Shutdown",
    0x0E:"Speed_Limit_ON_OFF",
    0x0F:"Walk_Assist_Excute",
    0x10:"Change_Display_Unit",    
    0x11:"Switch_Backlight_Mode",
    0x12:"Assist_Down",
    0x13:"Assist_Mode_Up_Cycle",
    0x14:"Gear_Shift_Up",
    0x15:"Gear_Shift_Down",
    0x16:"Gear_Shifter_ADJ",
    0x50:"Enviolo_Change_Zone(temp)"
}


Remote_Button_Shift = {
    0:"ON_OFF",
    1:"Mode_Up",
    2:"Mode_Down",
    3:"Walk_Assist",
    4:"Light",
    5:"Information",
    6:"Smart_Assist",
    7:"Rvd",        
}


class Remote_Active_Button_CMD_State_Def:
    
    MASK = 0x1
    
    def __init__(self) -> None:
        self.cmd = None
        self.btn_status = None
        self.btn_press_list = []
        self.press_num = 0
        
        pass
    
    def Button_CMD_State_Decode(self,data_array):

        data_len = len(data_array)

        if (data_len == 2):
            self.cmd = Remote_Command_List[ int(data_array[0],16) ]
            self.btn_status = int(data_array[1],16)
            
            self.btn_press_list = []
            self.press_num = 0
            
            for shift in Remote_Button_Shift:
                if( (self.btn_status >> shift) & self.MASK == 1 ):
                    self.btn_press_list.append(Remote_Button_Shift[shift])     
                    self.press_num += 1    
                    
    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [Remote Node Data Info]  =======================================")
        pressed_buttons_str_buffer = "Button_Pressed: ["
        
        for btn_name in self.btn_press_list:    
            pressed_buttons_str_buffer += btn_name + " "        
        pressed_buttons_str_buffer += "]"        
        
        print( space_buffer + "CMD: " + self.cmd)
        print( space_buffer + "Button_Pressed_Amount: " + str(self.press_num))
        print( space_buffer + pressed_buttons_str_buffer)        
        print( space_buffer + "===================================================================")     
                                    

if __name__ == "__main__":
    
    
    remote_active_btn_cmd_state = Remote_Active_Button_CMD_State_Def()
    
    ex_remote_data = ['0x00','0x2']
    
    remote_active_btn_cmd_state.Button_CMD_State_Decode(ex_remote_data)
    
    remote_active_btn_cmd_state.print_decode_info(0)
    
    #print(ex_remote_data)
    
    pass    
    