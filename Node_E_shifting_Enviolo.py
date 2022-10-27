
# 0x8:"E-shifting"
# Node = 0x8

Active_Data_Address_for_E_Shifting_Enviolo = {
    0x0:"Error",
    0x1:"Status",
    0x2:"Information_1",
    0x3:"Information_2",
    0x4:"See_Enviolo_Note.",
    0x5:"See_Enviolo_Note.",
    0x6:"See_Enviolo_Note.",
    0x7:"See_Enviolo_Note." ,
    0x8:"See_Enviolo_Note.",
    0x9:"See_Enviolo_Note.",
    0xA:"See_Enviolo_Note.",
    0xB:"See_Enviolo_Note.",
    0xC:"See_Enviolo_Note." ,
    0xD:"See_Enviolo_Note.",
    0xE:"See_Enviolo_Note.",
    0xF:"See_Enviolo_Note.",
    }



# Node = 0x8
Passive_Data_Address_for_E_Shifting_Enviolo = {
    0x0:"Firmware_Version",
    0x1:"Hardware_Version_1",
    0x2:"Hardware_Version_2",
    0x3:"Serial_Number_1",
    0x4:"Serial_Number_2",
    0x5:"See_Enviolo_Note.",
    0x6:"See_Enviolo_Note.",
    0x7:"See_Enviolo_Note." ,
    0x8:"See_Enviolo_Note.",
    0x9:"See_Enviolo_Note.",
    0xA:"See_Enviolo_Note.",
    0xB:"See_Enviolo_Note.",
    0xC:"See_Enviolo_Note." ,
    0xD:"See_Enviolo_Note.",
    0xE:"See_Enviolo_Note.",
    0xF:"Confirmation",
    }




eval_def = {
    0x1:"Corresponding_Error_Occurs", 
    0x0:"Corresponding_Error_was_Gone",
    }

ecode_def = {
    0x80:"Normal", 
    0x81:"Calibration_Error",
    0x82:"Motor_Overcurrent", 
    0x83:"Motor_Stall",
    0x84:"Motor_Thermal_Overload", 
    0x85:"Motor_Encoder_Error",
    0x86:"Under_Voltage", 
    0x87:"Reserved",
    0x88:"Reserved",
    0x89:"Reserved",
    0x8A:"Reserved",
    0x8B:"Reserved",    
    0x8C:"Reserved",
    0x8D:"Reserved",
    0x8E:"Reserved",
    0x8F:"Reserved",    
    }




# ======= [Active] =============

# Data Address = 0x0   "Error"
class E_Shifting_Enviolo_Active_Error_Def:
    
    MASK = 0x1
    
    def __init__(self) -> None:
        self.eval = None
        self.ecode = None        
        self.data_arr_str = ""
        
        
    def Enviolo_Active_Error_Decode(self,data_array):        
        self.eval  = eval_def[ int(data_array[0],16) ]  # Error Value
        self.ecode = ecode_def[ int(data_array[1],16) ] # Error Code  
        
        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","
        
    
    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Error Info]  =======================================")        
        print( space_buffer + "eval: " + self.eval)
        print( space_buffer + "ecode: " + self.ecode)
        print( space_buffer + "==================================================================================")     
                  
    def get_decode_info(self) -> str:        
        str_buff = ""        
        str_buff += "-> [E-Shifting (Enviolo) Node Error Info]  ==========\n"       
        str_buff += "data: " + self.data_arr_str + "\n"         
        str_buff += "eval: " + self.eval + "\n"
        str_buff += "ecode: " + self.ecode + "\n"
        str_buff += "==================================================\n"   
        return str_buff



s_inc_def = {  # Initialization 
    0x1:"E-shifting initialization confirmed [1].", 
    0x0:"E-shifting initialization confirmed [0]."    
    }

s_act_def = { # Active
    0x1:"E-shifting active. Power is applied to e-shifting motor [1]", 
    0x0:"E-shifting is not active. [0]"    
    }


s_opm_def ={   # E-shifting Operation Mode.
    0x0:"Inactive.",
    0x1:"Auto_shifting (Cadence CTRL)",
    0x2:"Manual_shifting (Ratio CTRL)",
    0x3:"Calibrating.",
    0x4:"Calibration_Needed.",
    0x5:"Low_Power.",
    0x6:"Reserved.",
    0x7:"Reserved.",
    0x8:"Reserved.",
    0x9:"Reserved.",
    0xA:"Reserved.",
    0xB:"Reserved.",
    0xC:"Reserved.",
    0xD:"Reserved.",
    0xE:"Reserved.",
    0xF:"Reserved.",
    }

s_cas_def ={   # E-shifting Calibration Status.
    0x0:"Idle.",
    0x1:"Calibrating", 
    0x2:"Calibration_Successful.",
    0x3:"Calibration_Failed.",
    0x4:"Calibration_Failed_To_Start.",
    0x5:"Calibration_Already_Busy.",
    0x6:"Pedal_Speed_Too_Low.",
    0x7:"Wheel_Speed_Too_Low.",
    0x8:"Calibration_Timeout.(Calibration takes too long)",
    0x9:"Calibration_Range_Error.(Calibration range too low)",
    0xA:"Reserved.",
    0xB:"Reserved.",
    0xC:"Reserved.",
    0xD:"Reserved.",
    0xE:"Reserved.",
    0xF:"Reserved.",
    }


# Data Address = 0x1   "Status"
class E_Shifting_Enviolo_Active_Status_Def:
    
    MASK_1_bit = 0x1
    MASK_4_bit = 0xF
    
    def __init__(self) -> None:
        self.s_inc = None
        self.s_act = None
        self.s_opm = None
        self.s_cas = None
        
        self.data_arr_str = ""

        
    def Enviolo_Active_Status_Decode(self,data_array):        
        self.s_inc = s_inc_def[ (int(data_array[0],16) >> 1) & self.MASK_1_bit]   # s_inc : Initialization confirmed
        self.s_act = s_act_def[ (int(data_array[0],16) >> 0) & self.MASK_1_bit ]  # s_act : Active status
        
        self.s_opm = s_opm_def[ (int(data_array[0],16) >> 4) & self.MASK_4_bit]   # s_opm : Operation Mode.
        self.s_cas = s_cas_def[ (int(data_array[0],16) >> 0) & self.MASK_4_bit]   # s_cas : Calibration Status
  
        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","

    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Status Info]  =======================================")        
        print( space_buffer + "s_inc: " + self.s_inc)
        print( space_buffer + "s_act: " + self.s_act)
        print( space_buffer + "s_opm: " + self.s_opm)
        print( space_buffer + "s_cas: " + self.s_cas)
        print( space_buffer + "===================================================================================")     
                  
    def get_decode_info(self) -> str:        
        str_buff = ""
        str_buff += "-> [E-Shifting (Enviolo) Node Status Info]  =====\n"      
        str_buff += "data: " + self.data_arr_str + "\n"    
        str_buff += "s_inc: " + self.s_inc + "\n"
        str_buff += "s_act: " + self.s_act + "\n"
        str_buff += "s_opm: " + self.s_opm + "\n"
        str_buff += "s_cas: " + self.s_cas + "\n"
        str_buff +=  "==========================================\n"        
        return str_buff

# Data Address = 0x2   "information 1"
class E_Shifting_Enviolo_Active_information_1_Def:
    def __init__(self) -> None:
        self.ca_spd = 0   # Cadence speed.  0 ~ 255 rpm
        self.ar_ig = 0    # Actual ratio of internal gear. (0.1 ratio per bit) 0x00 ~ 0xFF : 0 ~ 25.5 ratio
        self.ve_spd = 0   # Vehicle speed. (0.5 km/h per bit) 0x00 ~ 0xFF  0 ~ 127.5 km/h.
        self.gr_idx = 0   # Gear Index. 0x00 ~ 0x08 : Gear 1 ~ 9 , 0x09 ~ 0xFF : Reserved.
        self.ws = 0       # Wheel Speed  0x0000 ~ 0xFFFF : 0 ~ 65535 rpm.
        self.ld = 0       # Lifetime Distance 0x0000 ~ 0xFFFF : 0 ~ 65535 km.
        
        self.data_arr_str = ""
        
    def Enviolo_Active_Information_1_Decode(self,data_array):        
        self.ca_spd = int(data_array[0],16)   # Rpm
        self.ar_ig  = int(data_array[1],16)   # Gear Ratio (0 ~ 25.5)
        self.ve_spd = int(data_array[2],16)   # Vehicle speed. (0.5 km/h per bit) 0x00 ~ 0xFF  (0 ~ 127.5 km/h)
        self.gr_idx = 1 + int(data_array[3],16)   # Gear Index (1 ~ 9)        
        self.ws = int(data_array[4],16) + (int(data_array[5],16) << 8)  # Wheel Speed (0 ~ 65535 rpm.)
        self.ld = int(data_array[6],16) + (int(data_array[7],16) << 8)  # Lifetime Distance (0 ~ 65535 km.)        

        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","


    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Information_1 Info]  =======================================")        
        print( space_buffer + "ca_spd (Cadence): " + str(self.ca_spd) + " rpm (0 ~ 255)")
        print( space_buffer + "ar_ig (Gear Ratio): " + str(self.ar_ig) + " ratio (0 ~ 25.5)") 
        print( space_buffer + "ve_spd (Vehicle speed): " + str(self.ve_spd * 0.5) + " km/h (0 ~ 127.5)"  )
        print( space_buffer + "gr_idx (Gear Index): " + str(self.gr_idx) + " (1 ~ 9)" ) 
        print( space_buffer + "ws (Wheel Speed): " + str(self.ws) + " rpm (0 ~ 65535)" )
        print( space_buffer + "ld (Lifetime Distance): " + str(self.ld) + " km (0 ~ 65535)" )
        print( space_buffer + "==========================================================================================")     
                  
                  
    def get_decode_info(self) -> str:        
        str_buff = ""
             
        str_buff += "-> [E-Shifting (Enviolo) Node Information_1 Info]  ====\n"
        str_buff += "data: " + self.data_arr_str + "\n"  
        str_buff += "ca_spd (Cadence): " + str(self.ca_spd) + " rpm (0 ~ 255) \n"
        str_buff += "ar_ig (Gear Ratio): " + str(self.ar_ig) + " ratio (0 ~ 25.5) \n" 
        str_buff += "ve_spd (Vehicle speed): " + str(self.ve_spd * 0.5) + " km/h (0 ~ 127.5) \n"
        str_buff += "gr_idx (Gear Index): " + str(self.gr_idx) + " (1 ~ 9) \n" 
        str_buff += "ws (Wheel Speed): " + str(self.ws) + " rpm" + "(0 ~ 65535)\n"
        str_buff += "ld (Lifetime Distance): " + str(self.ld) + " km" + "(0 ~ 65535)\n"
        str_buff += "=================================================\n"
                  
        return str_buff

# Data Address = 0x3   "information 2"
class E_Shifting_Enviolo_Active_information_2_Def:
    
    def __init__(self) -> None:        
        self.du_cll = 0   # DU Cadence Low Limit. (Read)   0x00 ~ 0xFF: 0 ~ 255 rpm.
        self.du_chl = 0   # DU Cadence High Limit. (Read)  0x00 ~ 0xFF: 0 ~ 255 rpm.
        self.rll_rig = 0  # Range Low Limit of Ratio of Internal Gear. (Read) (0.1 ratio per bit)  (0x00 ~ 0xFF: 0 ~ 25.5 ratio)
        self.rhl_rig = 0  # Range High Limit of Ratio of Internal Gear. (Read) (0.1 ratio per bit)  (0x00 ~ 0xFF: 0 ~ 25.5 ratio)
        self.in_bv = 0    # Input Battery Voltage. (0.25V per bit)  (0x00 ~ 0xFF: 0 ~ 63.75 V.)
        self.na = 0       # No Application.  (Default = 0xFF.)
        
        self.data_arr_str = ""
        

    def Enviolo_Active_Information_2_Decode(self,data_array):        
        self.du_cll  = int(data_array[0],16)   # DU Cadence Low Limit (0 ~ 255) rpm
        self.du_chl  = int(data_array[1],16)   # DU Cadence High Limit (0 ~ 255) rpm
        self.rll_rig = int(data_array[2],16)   # [Range Low Limit] of [Ratio of Internal Gear]  (0 ~ 25.5) ratio   [0.1 ratio/bit]
        self.rhl_rig = int(data_array[3],16)   # [Range High Limit] of [Ratio of Internal Gear] (0 ~ 25.5) ratio   [0.1 ratio/bit]     
        self.in_bv = int(data_array[4],16)     # Input Battery Voltage (0 ~ 63.75 V)  [ 0.25V / bit ]
        self.na = int(data_array[5],16)        #  No Application.  (Default = 0xFF.)    

        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","

    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Information_2 Info]  =======================================")        
        print( space_buffer + "du_cll (DU Cadence Low Limit): " + str(self.du_cll) + " rpm (0 ~ 255)")
        print( space_buffer + "du_chl (DU Cadence High Limit): " + str(self.du_chl) + " rpm (0 ~ 255)")
        print( space_buffer + "rll_rig ([Low Limit] of [Ratio Gear] ): " + str(self.rll_rig * 0.1) + " ratio (0 ~ 25.5)")
        print( space_buffer + "rhl_rig ([High Limit] of [Ratio Gear]): " + str(self.rhl_rig * 0.1) + " ratio (0 ~ 25.5)")
        print( space_buffer + "in_bv (Input Battery Voltage): " + str(self.in_bv * 0.25) + " V (0 ~ 63.75 V)")
        print( space_buffer + "na (No Application): " + hex(self.na) )
        print( space_buffer + "==========================================================================================")     
                  
    def get_decode_info(self) -> str:        
        str_buff = ""             
        str_buff += "-> [E-Shifting (Enviolo) Node Information_2 Info] ====\n"      
        str_buff += "data: " + self.data_arr_str + "\n"   
        str_buff += "du_cll (DU Cadence Low Limit): " + str(self.du_cll) + " rpm (0 ~ 255)\n"
        str_buff += "du_chl (DU Cadence High Limit): " + str(self.du_chl) + " rpm (0 ~ 255) \n"
        str_buff += "rll_rig ([Low Limit] of [Ratio Gear] ): " + str(self.rll_rig * 0.1) + " ratio (0 ~ 25.5) \n"
        str_buff += "rhl_rig ([High Limit] of [Ratio Gear]): " + str(self.rhl_rig * 0.1) + " ratio (0 ~ 25.5) \n"
        str_buff += "in_bv (Input Battery Voltage): " + str(self.in_bv * 0.25) + " V (0 ~ 63.75 V) \n"
        str_buff += "na (No Application): " + hex(self.na) + "\n"
        str_buff += "================================================\n"
        return str_buff


# ======= [Passive] =============


# Data Address = 0x0   " Shift Brand Code 1"  , "Firmware Version 1"
class E_Shifting_Enviolo_Passive_Shift_Brand_Code_Firmware_Version_1_Def:
    
    def __init__(self) -> None:
        self.ahi_f1 = 0 # AHI firmware version 1. Naming by ASCII code. (to be discussed with Enviolo)
        self.ahi_f2 = 0 # AHI firmware version 2. Naming by ASCII code. (to be discussed with Enviolo)
        self.ahi_f3 = 0 # AHI firmware version 3. Naming by ASCII code. (to be discussed with Enviolo)
        self.year = 0   # Year of publication  [0x00 ~ 0x09: 2000 ~ 2009]  [0x10 ~ 0x19: 2010 ~ 2019] ~ [0x90 ~ 0x99: 2090 ~ 2099]
        self.month = 0  # Month of publication [0x01 ~ 0x09: January ~ September] [0x10 ~ 0x12: October ~ December]
        self.day = 0    # Day of publication   [0x01 ~ 0x09: First ~ 9th] .. [0x10 ~ 0x19: 10th ~ 19th] .. [0x20 ~ 0x29: 20th ~ 29th] .. [0x30 ~ 0x31: 30th ~ 31st]
        self.esid = 0   # E-shifting identification  [0x01: Enviolo e-shifting.]  [ 0x00, 0x02 ~ 0xFF : are used for GIANT in-house system ]
        
        self.data_arr_str = ""
        
        pass

    def Enviolo_Passive_Firmware_Version_1_Decode(self,data_array):        
        self.ahi_f1  = int(data_array[0],16)   # AHI firmware version 1 (ASCII)
        self.ahi_f2  = int(data_array[1],16)   # AHI firmware version 2 (ASCII)
        self.ahi_f3  = int(data_array[2],16)   # AHI firmware version 3 (ASCII)
        
        y_temp = int(data_array[3],16)   # 
        y_dig_10 = int(y_temp / 0x10)
        y_dig_1  = y_temp % 0x10
        self.year = 2000 + y_dig_10 * 10 + y_dig_1
        
        m_temp = int(data_array[4],16)   #
        m_dig_10 = int(m_temp / 0x10)
        m_dig_1  = m_temp % 0x10
        self.month = (m_dig_10 * 10) + m_dig_1
        
        
        d_temp = int(data_array[5],16)   #
        d_dig_10 = int(d_temp / 0x10)
        d_dig_1  = d_temp % 0x10
        self.day = (d_dig_10 * 10) + d_dig_1
        
        self.esid = int(data_array[6],16)  #[0x01: Enviolo e-shifting.] 

        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","

    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Firmware Version 1 Info]  =====") 
        year = str(self.year)
        mounth = str(self.month)
        day = str(self.day)
        str_AHI = chr(self.ahi_f1) + chr(self.ahi_f2) + chr(self.ahi_f3)
        str_Date = year + mounth + day
        str_Id = chr(0x30 + self.esid)
        
        Firmware_String =  str_AHI + str_Date + str_Id
        
        print( space_buffer + "Fimware Version 1: " + Firmware_String )
        print( space_buffer + "Firmware AHI: " + str_AHI )
        print( space_buffer + "Firmware Publish Date: " + year + "." + mounth + "." + day )
        print( space_buffer + "Firmware Publish ID: " + str_Id )      
        print( space_buffer + "=======================================================")     
                  

    def get_decode_info(self) -> str:        
        str_buff = ""             

        str_buff += "-> [E-Shifting (Enviolo) Node Firmware Version 1 Info] ====\n" 
        str_buff += "data: " + self.data_arr_str + "\n"  
        year = str(self.year)
        mounth = str(self.month)
        day = str(self.day)
        str_AHI = chr(self.ahi_f1) + chr(self.ahi_f2) + chr(self.ahi_f3)
        str_Date = year + mounth + day
        str_Id = chr(0x30 + self.esid)
        
        Firmware_String =  str_AHI + str_Date + str_Id
        
        str_buff += "Fimware Version 1: " + Firmware_String + "\n"
        str_buff += "Firmware AHI: " + str_AHI + "\n"
        str_buff += "Firmware Publish Date: " + year + "." + mounth + "." + day + "\n"
        str_buff += "Firmware Publish ID: " + str_Id + "\n"   
        str_buff += "============================================\n" 
        return str_buff

# Data Address = 0x1   "Hardware_Version_1"
class E_Shifting_Enviolo_Passive_Hardware_Version_1_Def:
    
    def __init__(self) -> None:
        self.Hardware_Version_1 = ""
        
        self.data_arr_str = ""        

        
    def Enviolo_Passive_Hardware_Version_1_Decode(self,data_array):
        
        hardware_version_1_buff = ""
        for _char in data_array:
            hardware_version_1_buff += chr(int(_char,16))
            
        self.Hardware_Version_1 = hardware_version_1_buff
        
        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","


    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Hardware Ver 1 [id_1 ~ id_8] Info] ====") 
        print( space_buffer + "Hardware Version 1: " + self.Hardware_Version_1 ) 
        print( space_buffer + "======================================================================")     
                 

    def get_decode_info(self) -> str:        
        str_buff = ""             
        str_buff += "-> [E-Shifting (Enviolo) Node Hardware Ver 1 [id_1 ~ id_8] Info] ====\n"
        str_buff += "data: " + self.data_arr_str + "\n"  
        str_buff += "Hardware Version 1: " + self.Hardware_Version_1 + "\n"
        str_buff += "========================================================\n"  
        return str_buff       



# Data Address = 0x2   "Hardware_Version_2"
class E_Shifting_Enviolo_Passive_Hardware_Version_2_Def:
    
    def __init__(self) -> None:
        self.Hardware_Version_2 = ""
        
        self.data_arr_str = ""
        
        
    def Enviolo_Passive_Hardware_Version_2_Decode(self,data_array):
        
        hardware_version_2_buff = ""
        for _char in data_array:
            hardware_version_2_buff += chr(int(_char,16))
            
        self.Hardware_Version_2 = hardware_version_2_buff

        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","

    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Hardware Ver 2 [id_9 ~ id_12] Info]  ======") 
        print( space_buffer + "Hardware Version 2: " + self.Hardware_Version_2 ) 
        print( space_buffer + "=============================================================================")     
    
    def get_decode_info(self) -> str:        
        str_buff = ""             
        str_buff += "-> [E-Shifting (Enviolo) Node Hardware Ver 2 [id_9 ~ id_12] Info] ==\n" 
        str_buff += "data: " + self.data_arr_str + "\n"  
        str_buff += "Hardware Version 2: " + self.Hardware_Version_2 + "\n"
        str_buff += "===============================================================\n"     
        return str_buff       



# Data Address = 0x3   "Serial_Number_1"
class E_Shifting_Enviolo_Passive_Serial_Number_1_Def:
    
    def __init__(self) -> None:
        self.Serial_Number_1 = ""

        self.data_arr_str = ""
                
    def Enviolo_Passive_Serial_Number_1_Decode(self,data_array):
        
        serial_number_1_buff = ""
        for _char in data_array:
            serial_number_1_buff += chr(int(_char,16))
            
        self.Serial_Number_1 = serial_number_1_buff

        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","


    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Serial Number 1 [id_1 ~ id_8] Info]  ==============") 
        print( space_buffer + "Serial Number 1 : " + self.Serial_Number_1 ) 
        print( space_buffer + "=================================================================================")     
                 

    def get_decode_info(self) -> str:        
        str_buff = ""             
        str_buff += "-> [E-Shifting (Enviolo) Node Serial Number 1 [id_1 ~ id_8] Info]  ===========\n"
        str_buff += "data: " + self.data_arr_str + "\n"  
        str_buff += "Serial Number 1 : " + self.Serial_Number_1 + "\n"
        str_buff += "================================================================\n"     
                 
        return str_buff  



# Data Address = 0x4   "Serial_Number_2"
class E_Shifting_Enviolo_Passive_Serial_Number_2_Def:
    
    def __init__(self) -> None:
        self.Serial_Number_2 = ""
        
        self.data_arr_str = ""        
        
    def Enviolo_Passive_Serial_Number_2_Decode(self,data_array):
        
        serial_number_2_buff = ""
        for _char in data_array:
            serial_number_2_buff += chr(int(_char,16))
            
        self.Serial_Number_2 = serial_number_2_buff        

        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","


    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Serial Number 2 [id_9 ~ id_10] Info]  ============") 
        print( space_buffer + "Serial Number 2 : " + self.Serial_Number_2 ) 
        print( space_buffer + "================================================================================")     
                 
    def get_decode_info(self) -> str:        
        str_buff = ""             
        str_buff += "-> [E-Shifting (Enviolo) Node Serial Number 2 [id_9 ~ id_10] Info]  ========\n" 
        str_buff += "data: " + self.data_arr_str + "\n"  
        str_buff += "Serial Number 2 : " + self.Serial_Number_2 + "\n"
        str_buff += "================================================================\n"                 
        return str_buff  

# Data Address = 0xE   "Firmware Version 2"
class E_Shifting_Enviolo_Passive_Firmware_Version_2_Def:
    
    pass


cfm_def = {    
    0x0:"Confirmation_Failure",
    0x1:"Confirmation_Success" 
    }

# Data Address = 0xF   "Confirmation"
class E_Shifting_Enviolo_Passive_Confirmation_Def:
    
    MASK_1_bit = 0x1
    def __init__(self) -> None:
        self.cfm = None

        self.data_arr_str = ""
        
        
    def Enviolo_Passive_Confirmation_Decode(self,data_array):
        self.cfm = cfm_def[int(data_array[0],16) & self.MASK_1_bit]   
        
        self.data_arr_str = ""
        for element in data_array:
            self.data_arr_str += str(element) + ","  
        pass


    def print_decode_info(self,shift_space):
        
        space = " "
        space_buffer = ""
        for cnt in range(0,shift_space):
            space_buffer += space
        
        print( space_buffer + "-> [E-Shifting (Enviolo) Node Confirmation Info]  ============") 
        print( space_buffer + "(cfm)Confirmation : " + self.cfm ) 
        print( space_buffer + "==============================================================")     


    def get_decode_info(self) -> str:        
        str_buff = ""             
        str_buff += "-> [E-Shifting (Enviolo) Node Confirmation Info]  ======\n" 
        str_buff += "data: " + self.data_arr_str + "\n"  
        str_buff += "(cfm)Confirmation : " + self.cfm + "\n"
        str_buff += "==============================================\n"
        return str_buff  


# ======= [Remote Frame] =============






if __name__ == "__main__":
    
    
    e_shifting_err = E_Shifting_Enviolo_Active_Error_Def()
    e_shifting_err_data = ['0x00','0x80']
    e_shifting_err.Enviolo_Active_Error_Decode(e_shifting_err_data)
    print(e_shifting_err.get_decode_info())
    
    # ex_enviolo_passive_firmware_version_data = ['0x56','0x31','0x34','0x22','0x10','0x4','0x1']
    # e_shifting_firmware_ver = E_Shifting_Enviolo_Passive_Shift_Brand_Code_Firmware_Version_1_Def()
    # e_shifting_firmware_ver.Enviolo_Passive_Firmware_Version_1_Decode(ex_enviolo_passive_firmware_version_data)
    # e_shifting_firmware_ver.print_decode_info(0)
        

    # ex_enviolo_passive_hardware_version_1_data = ['0x30','0x31','0x32','0x33','0x34','0x35','0x36','0x37']
    # e_shifting_hardware_ver_1 = E_Shifting_Enviolo_Passive_Hardware_Version_1_Def()
    # e_shifting_hardware_ver_1.Enviolo_Passive_Hardware_Version_1_Decode(ex_enviolo_passive_hardware_version_1_data)
    # e_shifting_hardware_ver_1.print_decode_info(0)
    
    # ex_enviolo_passive_hardware_version_2_data = ['0x30','0x31','0x32','0x33']
    # e_shifting_hardware_ver_2 = E_Shifting_Enviolo_Passive_Hardware_Version_2_Def()
    # e_shifting_hardware_ver_2.Enviolo_Passive_Hardware_Version_2_Decode(ex_enviolo_passive_hardware_version_2_data)
    # e_shifting_hardware_ver_2.print_decode_info(0)
    
    
    # ex_enviolo_passive_sn_1_data = ['0x30','0x31','0x32','0x33','0x34','0x35','0x36','0x37']
    # e_shifting_sn_1 = E_Shifting_Enviolo_Passive_Serial_Number_1_Def()
    # e_shifting_sn_1.Enviolo_Passive_Serial_Number_1_Decode(ex_enviolo_passive_sn_1_data)
    # e_shifting_sn_1.print_decode_info(0)
    
    # ex_enviolo_passive_sn_2_data = ['0x30','0x31']
    # e_shifting_sn_2 = E_Shifting_Enviolo_Passive_Serial_Number_2_Def()
    # e_shifting_sn_2.Enviolo_Passive_Serial_Number_2_Decode(ex_enviolo_passive_sn_2_data)
    # e_shifting_sn_2.print_decode_info(0)
    
    
    # ex_enviolo_passive_cfm_data = ['0x1']
    # ex_enviolo_passive_cfm = E_Shifting_Enviolo_Passive_Confirmation_Def()
    # ex_enviolo_passive_cfm.Enviolo_Passive_Confirmation_Decode(ex_enviolo_passive_cfm_data)
    # ex_enviolo_passive_cfm.print_decode_info(0)
    
    
    
    #print(ex_remote_data)
    
    pass    