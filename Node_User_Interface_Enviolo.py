# 0x2:"User_Interface" (GIANT Core System)
# Node = 0x2

Active_Data_Address_for_User_Interface_Enviolo = {
    0x0:"undefined_for_Enviolo (0x0)",
    0x1:"Giant_Core_System_Control_CMD_1",  # 0x1:"Control_Command_1",
    0x2:"undefined_for_Enviolo (0x2)",
    0x3:"undefined_for_Enviolo (0x3)",
    0x4:"undefined_for_Enviolo (0x4)",
    0x5:"undefined_for_Enviolo (0x5)",
    0x6:"undefined_for_Enviolo (0x6)",
    0x7:"undefined_for_Enviolo (0x7)",
    0x8:"undefined_for_Enviolo (0x8)",
    0x9:"undefined_for_Enviolo (0x9)",
    0xA:"undefined_for_Enviolo (0xA)",
    0xB:"undefined_for_Enviolo (0xB)",
    0xC:"undefined_for_Enviolo (0xC)",
    0xD:"undefined_for_Enviolo (0xD)",
    0xE:"undefined_for_Enviolo (0xE)",    
    0xF:"Giant_Core_System_Control_CMD_2",  # 0xF:"Control_Command_2",
    }


mslp_def = {   # Manual sleep
    0x1:"Active",
    0x0:"Inactive"
    }

aslp_def = {   # Automatic sleep
    0x1:"Active",
    0x0:"Inactive"
    }

rmod_def = { # Riding Mode
    0x1:"Riding_mode",
    0x0:"Not_Riding_mode"
    }

amod_def = { # Adjusting Mode
    0x00:"See_Enviolo_Note (0x0)",            
    0x01:"See_Enviolo_Note (0x1)",
    0x02:"See_Enviolo_Note (0x2)",
    0x03:"See_Enviolo_Note (0x3)",
    0x04:"See_Enviolo_Note (0x4)",
    0x05:"See_Enviolo_Note (0x5)",
    0x06:"Service_Mode (0x06)",
    0x07:"Service_Mode (0x07)",
    0x08:"Service_Mode (0x08)",
    0x09:"Service_Mode (0x09)",
    0x0A:"Service_Mode (0x0A)",
    0x0B:"Check_Mode",
    0x0C:"Off_State",
    0x0D:"Error_Mode",
    0x0E:"Off_state",
    0x0F:"See_Enviolo_Note (0x0F)",
    0x10:"See_Enviolo_Note (0x10)",
    0x11:"See_Enviolo_Note (0x11)",
    0x12:"See_Enviolo_Note (0x12)",
    0x13:"See_Enviolo_Note (0x13)",
    0x14:"See_Enviolo_Note (0x14)",
    0x15:"See_Enviolo_Note (0x15)",
    0x16:"See_Enviolo_Note (0x16)",
    0x17:"See_Enviolo_Note (0x17)",
    0x18:"See_Enviolo_Note (0x18)",
    0x19:"See_Enviolo_Note (0x19)",
    0x1A:"See_Enviolo_Note (0x1A)",
    0x1B:"See_Enviolo_Note (0x1B)",
    0x1C:"See_Enviolo_Note (0x1C)",
    0x1D:"See_Enviolo_Note (0x1D)",
    0x1E:"See_Enviolo_Note (0x1E)",
    0x1F:"See_Enviolo_Note (0x1F)",
    }

# ======= [Active] =============

# Data Address = 0x1   "Control_Command_1"
class User_Interface_Enviolo_Active_Control_Command_1_Def:

    MASK_1_bit = 0x1
    MASK_5_bit = 0x1F
    
    
    def __init__(self) -> None:
        self.mslp = None
        self.aslp = None
        self.rmod = None
        self.amod = None
        self.data_arr_str = ""
        
    def User_Interface_Active_Control_Command_1_Decode(self,data_array):        
        self.mslp  = mslp_def[ (int(data_array[0],16) >> 6) & self.MASK_1_bit ]  # Manual_sleep
        self.aslp  = aslp_def[ (int(data_array[0],16) >> 5) & self.MASK_1_bit ]  # Automatic_sleep
        
        self.rmod = rmod_def[ (int(data_array[3],16) >> 7) & self.MASK_1_bit ]  # Manual_sleep
        self.amod = amod_def[ (int(data_array[3],16) >> 0) & self.MASK_5_bit ]  # Automatic_sleep
        
        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","
            
        pass
    
    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [User_Interface Node Control Command 1 Info (for Enviolo)]  ========================")        
        print( space_buffer + "mslp: " + self.mslp )
        print( space_buffer + "aslp: " + self.aslp )
        print( space_buffer + "rmod: " + self.rmod )
        print( space_buffer + "amod: " + self.amod )
        print( space_buffer + "=======================================================================================")     
               
        pass
    
    def get_decode_info(self) -> str:        
        str_buff = ""
             
        str_buff += "-> [User_Interface Node Control Command 1 Info (for Enviolo)] ===\n"
        str_buff += "data: " + self.data_arr_str + "\n" 
        str_buff += "mslp: " + self.mslp + "\n"
        str_buff += "aslp: " + self.aslp + "\n"
        str_buff += "rmod: " + self.rmod + "\n"
        str_buff += "amod: " + self.amod + "\n"
        str_buff += "====================================================\n"
                  
        return str_buff


cae_def = { # Clear All Error Code
    0x1:"Active",
    0x0:"Inactive"
    }

cal_def = { # Calibrate
    0x1:"Initiate_Calibration", # 啟動校正
    0x0:"Inactive"
    }

w_opm_def = { # Write Operation Mode.
    0x0:"Inactive (Low Power Consumption Mode)",
    0x1:"Auto-shifting (Cadence Control)", 
    0x2:"Manual-Shifting (Ratio Control)",
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
    0xE:"Reserved",
    0xF:"Reserved",    
    }


    
# Data Address = 0xF   "Control_Command_2"
class User_Interface_Enviolo_Active_Control_Command_2_Def:

    MASK_1_bit = 0x1
    MASK_4_bit = 0xF

    def __init__(self) -> None:
        
        self.data_arr_str = ""
        self.cae = None # Clear All Error Code
        self.cal = None # Calibrate
        self.w_opm = None # Write Operaton Mode
        
        # Write actual ratio of internal gear. (0.1 ratio per bit)
        # [0x00 ~ 0xFE: 0 ~ 25.4 ratio.] 
        # [0xFF: In ‘w_grix’ control mode or auto-shifting (Cadence control mode).]
        self.w_arig = 0
        
        
        # Write gear index.
        # [0x00 ~ 0x08: Gear 1 ~ 9]
        # [0x09 ~ 0xFE: Reserved]
        # [0xFF: In ‘w_arig’ control mode or auto-shifting (Cadence control mode).]
        self.w_grix = 0 
        
         # DU desired cadence. (Write)
         # 0x00 ~ 0xFE: 0 ~ 254 rpm.
         # 0xFF: In ‘w_arig’ control mode or ‘w_grix’ control mode         
        self.w_dudc = 0  
        
        # Battery relative state of charge.
        # [ (0x00 ~ 0x64) : (0 ~ 100%) }
        # 0xFF: No battery communication.        
        self.brsoc = 0
        
        pass
    
    
    def User_Interface_Active_Control_Command_2_Decode(self,data_array):        
        self.cae  = cae_def[ (int(data_array[0],16) >> 5) & self.MASK_1_bit ]  # Clear All Error Code
        self.cal  = cal_def[ (int(data_array[0],16) >> 4) & self.MASK_1_bit ]  # Calibrate        
        self.w_opm  = w_opm_def[ (int(data_array[0],16) >> 0) & self.MASK_4_bit ]  # Write Operaton Mode
       
        self.w_arig = int(data_array[1],16) # 0x00 ~ 0xFE: 0 ~ 25.4 ratio (0.1 ratio per bit))
        self.w_grix = int(data_array[2],16) 
        self.w_dudc = int(data_array[3],16) 
        self.brsoc = int(data_array[4],16) 
        
        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","
            
        pass
    

    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [User_Interface Node Control Command 2 Info (for Enviolo)]  ==========================")        
        print( space_buffer + "cae (Clear All Error): " + self.cae )
        print( space_buffer + "cal (Calibration): " + self.cal )
        print( space_buffer + "w_opm (Operation Mode): " + self.w_opm )
        
         # ========= w_arig  (0 ~ 25.4) ratio  ==================================  
        if (self.w_arig <= 0xFE):
            print( space_buffer + "w_arig (Gear Ratio): " + str(self.w_arig * 0.1) + " ratio")
        elif (self.w_arig == 0xFF):
            print( space_buffer + "w_arig: " +" (0xFF) In [Auto Shifting] or [Gear Level CTRL (1 ~ 9)] " )
        
        # ========= w_grix  Level (1 ~ 9) ==================================
        if (self.w_grix <= 0x08):            
            print( space_buffer + "w_grix (Gear Index): " + str(1 + self.w_grix) + " (1 ~ 9)" )
        elif ((self.w_grix >= 0x09) and (self.w_grix <= 0xFE)):
            print( space_buffer + "w_grix: " + hex(self.w_grix) + " (0x09 ~ 0xFE) is Reserved!" )
        elif (self.w_grix == 0xFF):
            print( space_buffer + "w_grix: " +" (0xFF) In [Auto Shifting] or [Gear Ratio CTRL (0 ~ 25.4)] " )
            
            
        # ========= w_dudc  (0 ~ 254) rpm   ==================================  
        if (self.w_dudc <= 0xFE):
            print( space_buffer + "w_dudc (DU Desired Cadence): " + str(self.w_dudc) + " rpm (0 ~ 254)")
        elif (self.w_dudc == 0xFF):
            print( space_buffer + "w_dudc: " + " (0xFF) In [Gear Ratio CTRL (0 ~ 25.4)] or [Gear Index CTRL (1 ~ 9)] " )
            
         # ========= brsoc  ( 0x00 ~ 0x64 : 0 ~ 100 %)   ==================================  
        if (self.brsoc <= 0x064):            
            print( space_buffer + "brsoc (Battery Relative State of Charge): " + str(self.brsoc) + " %" )
        elif ((self.brsoc >= 0x09) and (self.brsoc <= 0xFE)):
            print( space_buffer + "brsoc: " + hex(self.brsoc) +" (0x65 ~ 0xFE) is Reserved!" )
        elif (self.brsoc == 0xFF):
            print( space_buffer + "brsoc: " + " (0xFF) [No battery communication] " )
            
        print( space_buffer + "========================================================================================")     
               
        pass
    
    def get_decode_info(self) -> str:        
        str_buff = ""
              
        str_buff += "-> [User_Interface Node Control Command 2 Info (for Enviolo)] ===\n"        
        str_buff += "data: " + self.data_arr_str + "\n"
        str_buff += "cae (Clear All Error): " + self.cae + "\n"
        str_buff += "cal (Calibration): " + self.cal + "\n"
        str_buff += "w_opm (Operation Mode): " + self.w_opm + "\n"
        
         # ========= w_arig  (0 ~ 25.4) ratio  ==================================  
        if (self.w_arig <= 0xFE):
            str_buff += "w_arig (Gear Ratio): " + str(self.w_arig * 0.1) + " ratio ====\n" 
        elif (self.w_arig == 0xFF):
            str_buff += "w_arig: " +" (0xFF) In [Auto Shifting] or [Gear Level CTRL (1 ~ 9)] \n"
            
        # ========= w_grix  Level (1 ~ 9) ==================================
        if (self.w_grix <= 0x08):            
            str_buff += "w_grix (Gear Index): " + str(1 + self.w_grix) + " (1 ~ 9) \n" 
        elif ((self.w_grix >= 0x09) and (self.w_grix <= 0xFE)):
            str_buff += "w_grix: " + hex(self.w_grix) + " (0x09 ~ 0xFE) is Reserved! \n"
        elif (self.w_grix == 0xFF):
            str_buff += "w_grix: " +" (0xFF) In [Auto Shifting] or [Gear Ratio CTRL (0 ~ 25.4)] \n"
            
            
        # ========= w_dudc  (0 ~ 254) rpm   ==================================  
        if (self.w_dudc <= 0xFE):
            str_buff += "w_dudc (DU Desired Cadence): " + str(self.w_dudc) + " rpm (0 ~ 254) \n"
        elif (self.w_dudc == 0xFF):
            str_buff += "w_dudc: " + " (0xFF) In [Gear Ratio CTRL (0 ~ 25.4)] or [Gear Index CTRL (1 ~ 9)] \n"
            
         # ========= brsoc  ( 0x00 ~ 0x64 : 0 ~ 100 %)   ==================================  
        if (self.brsoc <= 0x064):            
            str_buff +=  "brsoc (Battery Relative State of Charge): " + str(self.brsoc) + " %\n"
        elif ((self.brsoc >= 0x09) and (self.brsoc <= 0xFE)):
            str_buff += "brsoc: " + hex(self.brsoc) +" (0x65 ~ 0xFE) is Reserved! \n"
        elif (self.brsoc == 0xFF):
            str_buff += "brsoc: " + " (0xFF) [No battery communication] \n"
            
        str_buff += "============================================\n"         
                  
                  
        return str_buff