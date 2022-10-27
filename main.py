
import serial
import threading
import os
import time
from G_System_ID import *
from ID_Collector import *
from Node_Remote import *
from Node_E_shifting_Enviolo import *
from Node_User_Interface_Enviolo import *
from View_Interface import *

# ==================== Global =======================

# ==== Enviolo 自己主動發的 [Data Frame] "Active" ====================================
enviolo_err = E_Shifting_Enviolo_Active_Error_Def()
enviolo_status = E_Shifting_Enviolo_Active_Status_Def()
enviolo_info_1 = E_Shifting_Enviolo_Active_information_1_Def()
enviolo_info_2 = E_Shifting_Enviolo_Active_information_2_Def()


# ==== Enviolo 回應其他節點的 [Data Frame]  "Passive"  Ex: 回應 韌體版本、硬體版本... =====
enviolo_cmf = E_Shifting_Enviolo_Passive_Confirmation_Def()
enviolo_fwv1 = E_Shifting_Enviolo_Passive_Shift_Brand_Code_Firmware_Version_1_Def()
enviolo_hwv1 = E_Shifting_Enviolo_Passive_Hardware_Version_1_Def()
enviolo_hwv2 = E_Shifting_Enviolo_Passive_Hardware_Version_2_Def()
enviolo_sn_1 = E_Shifting_Enviolo_Passive_Serial_Number_1_Def()
enviolo_sn_2 = E_Shifting_Enviolo_Passive_Serial_Number_2_Def()

# ===== SG 自己主動發的命令 [Data Frame] "Active" ===============================
sg_to_enviolo_cmd_1 = User_Interface_Enviolo_Active_Control_Command_1_Def()
sg_to_enviolo_cmd_2 = User_Interface_Enviolo_Active_Control_Command_2_Def()

# ==================== UART Parameter Config Region =================
uart = serial.Serial()
uart.port = "/dev/tty.usbserial-0001"
uart.baudrate = 921600
uart.bytesize = serial.EIGHTBITS  # number of bits per bytes
uart.parity = serial.PARITY_NONE  # set parity check
uart.stopbits = serial.STOPBITS_ONE  # number of stop bits
uart.timeout = 0.5  # non-block read 0.5s
uart.writeTimeout = 0.5  # timeout for write 0.5s
uart.xonxoff = False  # disable software flow control
uart.rtscts = False  # disable hardware (RTS/CTS) flow control
uart.dsrdtr = False  # disable hardware (DSR/DTR) flow control

#========== Global variable Define ============
uart_rx_buffer = b''


def clr_uart_rx_buffer():
    global uart_rx_buffer
    uart_rx_buffer = b''



class CanMsgRxBufferType:
    
    def __init__(self) -> None:
        self.StdID = None
        self.ExID = None
        self.IDE = None
        self.RTR = None
        self.DLC = None
        self.TimeStamp = None
        self.FilterMachindex = None        
        self.Data = []  
        
    def FeedRawDateIn(self,rawdata:bytes):
        #print(str(rawdata))
  
        if(len(rawdata) >= 36):
            ID_result = hex( int(rawdata[3] << 24) + int(rawdata[2] << 16) + int(rawdata[1] << 8) + int(rawdata[0]) )
            self.StdID = ID_result
            
            IExID_result = hex( int(rawdata[7] << 24) + int(rawdata[6] << 16) + int(rawdata[5] << 8) + int(rawdata[4]) )
            self.ExID = IExID_result
            
            IDE_result = hex( int(rawdata[11] << 24) + int(rawdata[10] << 16) + int(rawdata[9] << 8) + int(rawdata[8]) )
            self.IDE = IDE_result
            
            
            RTR_result = hex( int(rawdata[15] << 24) + int(rawdata[14] << 16) + int(rawdata[13] << 8) + int(rawdata[12]) )
            if RTR_result == "0x2":
                self.RTR = "Remote"
            elif RTR_result == "0x0":
                self.RTR = "Data"
            else:
                self.RTR = RTR_result
            
            DLC_result = hex( int(rawdata[19] << 24) + int(rawdata[18] << 16) + int(rawdata[17] << 8) + int(rawdata[16]) )
            self.DLC = int(DLC_result,16)
            
            TimeStamp_Result = hex( int(rawdata[23] << 24) + int(rawdata[22] << 16) + int(rawdata[21] << 8) + int(rawdata[20]) )
            self.TimeStamp = TimeStamp_Result
            
            FilterMachindex_Result = hex( int(rawdata[27] << 24) + int(rawdata[26] << 16) + int(rawdata[25] << 8) + int(rawdata[24]) )
            self.FilterMachindex = FilterMachindex_Result
            
            
            if(self.Data != None):
                self.Data.clear()
            
            
            if (self.DLC == 0):
                self.Data = None
            else:
                self.Data = []
                
                for indx in range(28,28 + self.DLC ):                
                    self.Data.append( hex(int(rawdata[indx])) )
            
        else:
            self.StdID = "Null"
        
        #print(type(self.StdID))
        #print(self.StdID) 
        
        pass



def Master():    
    print("<Master ID>:", threading.get_ident())   
    
    
    sim_data = b'\x80\x02\x00\x00'
    
    CanRxBuffer = CanMsgRxBufferType()
    print(type(sim_data))
    CanRxBuffer.FeedRawDateIn(sim_data)
    
    cnt = 0 
    while(cnt < 65535):
        
        #w_buffer = b'hello\r\n'  
        #uart.write(w_buffer)
        #print(cnt)
        
        cnt+=1
        time.sleep(1)




# ================ UART RX ===============================
def uartRxBack():  



    global uart_rx_buffer     
    print("<uartRxBack ID>:", threading.get_ident())

    rolling = 0

    CanRxBuffer = CanMsgRxBufferType()

    ID_Colloctor = ID_Collector_Def()
    
    remote_btn_status_check = Remote_Active_Button_CMD_State_Def()
    
    while 1:
        
        try:
            read_byte = uart.read(1)
            #print(read_byte)
        except:
            read_byte = b''
        
        if(read_byte != b'\n'):
            uart_rx_buffer += read_byte
        elif ((read_byte == b'\n')):
            # 偵測到 '\n' 換行符號 用utf8解析，並print出來
            
            packet_buffer_str = ""
            
            CanRxBuffer.FeedRawDateIn(uart_rx_buffer)
            
            if (CanRxBuffer.StdID != 'Null'): # and (CanRxBuffer.StdID == '0x681'):  

                if( CanRxBuffer.Data != None ):
                    # 有Data
                    data_buffer = ""
                    for idx in range(0,CanRxBuffer.DLC):
                        data_buffer += CanRxBuffer.Data[idx] + " "                    
                    packet_buffer_str = "No" + str(rolling) + ". ID: " + CanRxBuffer.StdID + " , RTR: " + CanRxBuffer.RTR + " , len: " + str(CanRxBuffer.DLC) + " ,  Data: [ " + data_buffer + "]" 
                    #print("No" + str(rolling) + ". ID: " + CanRxBuffer.StdID + " , RTR: " + CanRxBuffer.RTR + " , len: " + str(CanRxBuffer.DLC) + " ,  Data: [ " + data_buffer + "]" )
                    pass  
                else:
                    # 沒有Data
                    packet_buffer_str = "No" +str(rolling) + ". ID: " + CanRxBuffer.StdID + " , RTR: " + CanRxBuffer.RTR + " , len: " + str(CanRxBuffer.DLC)
                    #print("No" +str(rolling) + ". ID: " + CanRxBuffer.StdID + " , RTR: " + CanRxBuffer.RTR + " , len: " + str(CanRxBuffer.DLC) )
                    pass  
            
                #if CanRxBuffer.RTR == "Data":

                #先解析ID再決定要怎麼處理資料
                myID = G_System_ID_Decode( CanRxBuffer.StdID , CanRxBuffer.RTR )  
           
                # print( "\n-> [Rawdata Data]  ==========================================")
                # print(packet_buffer_str)
                # print( "=============================================================")
           

           
                # Enviolo 自己主動發的 [Data Frame] "Active"  Ex:檔位、輪速度、時速、踏頻...
                if(myID.RTR == "Data" and  myID.get_node() == "E-shifting" and myID.get_packet_type() == "Active"):
                    # print( "\n-> [Rawdata Data]  ==========================================")
                    # print(packet_buffer_str)
                    # print( "=============================================================")
                    # myID.print_data_frame_info(4)   
                    
                    if (myID.get_data_address() == "Error"):
                        
                        enviolo_err.Enviolo_Active_Error_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_err_str = enviolo_err.get_decode_info()
                        # enviolo_err.print_decode_info(8)                        
                        pass
                    
                    if (myID.get_data_address() == "Status"):
                        
                        enviolo_status.Enviolo_Active_Status_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_status_str = enviolo_status.get_decode_info()
                        # enviolo_status.print_decode_info(8)                        
                        pass
                    
                    if (myID.get_data_address() == "Information_1"):
                        
                        enviolo_info_1.Enviolo_Active_Information_1_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_info_1_str = enviolo_info_1.get_decode_info()
                        # enviolo_info_1.print_decode_info(8)                        
                        pass
                               
                    if (myID.get_data_address() == "Information_2"):
                        
                        enviolo_info_2.Enviolo_Active_Information_2_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_info_2_str = enviolo_info_2.get_decode_info()
                        # enviolo_info_2.print_decode_info(8)                        
                        pass
                                     
                    pass 
                
                # Enviolo 回應其他節點的 [Data Frame]  "Passive"  Ex: 回應 韌體版本、硬體版本...
                if(myID.RTR == "Data" and  myID.get_node() == "E-shifting" and myID.get_packet_type() == "Passive"):
                    # print( "\n-> [Rawdata Data]  ==========================================")
                    # print(packet_buffer_str)
                    # print( "===============================================================")
                    # myID.print_data_frame_info(4)       
                    
                    if (myID.get_data_address() == "Confirmation"):
                       
                        enviolo_cmf.Enviolo_Passive_Confirmation_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_cmf_str = enviolo_cmf.get_decode_info()
                        # enviolo_cmf.print_decode_info(8)   
                        pass
                    
                    if (myID.get_data_address() == "Firmware_Version"):
                        
                        enviolo_fwv1.Enviolo_Passive_Firmware_Version_1_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_fwv_1_str = enviolo_fwv1.get_decode_info()
                        # enviolo_fwv1.print_decode_info(8)   
                        pass
                    if (myID.get_data_address() == "Hardware_Version_1"):
                        
                        enviolo_hwv1.Enviolo_Passive_Hardware_Version_1_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_hwv_1_str = enviolo_hwv1.get_decode_info()
                        # enviolo_hwv1.print_decode_info(8)   
                        pass
                    if (myID.get_data_address() == "Hardware_Version_2"):                       

                        enviolo_hwv2.Enviolo_Passive_Hardware_Version_2_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_hwv_2_str = enviolo_hwv2.get_decode_info()
                        # enviolo_hwv2.print_decode_info(8)   
                        pass  
                    
                    if (myID.get_data_address() == "Serial_Number_1"):                       
                        
                        enviolo_sn_1.Enviolo_Passive_Serial_Number_1_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_sn_1_str = enviolo_sn_1.get_decode_info()
                        # enviolo_sn_1.print_decode_info(8)   
                        
                    
                    if (myID.get_data_address() == "Serial_Number_2"):                       
                        
                        enviolo_sn_2.Enviolo_Passive_Serial_Number_2_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_sn_2_str = enviolo_sn_2.get_decode_info()
                        # enviolo_sn_2.print_decode_info(8)   
                        
                        pass  
                    
                                                  
                    pass                
                
                # 查看 其他節點(SG)發出 Remote Frame 跟 Enviolo 要資料
                if(myID.RTR == "Remote" and  myID.get_res_node() == "E-shifting"):
                    # print( "\n-> [Rawdata Data]  ==========================================")
                    # print(packet_buffer_str)
                    # print( "=============================================================")
                    # myID.print_remote_frame_info(4)                     
                    pass       

                # SG 自己主動發的命令 [Data Frame] "Active" 
                if(myID.RTR == "Data" and  myID.get_node() == "User_Interface" and myID.get_packet_type() == "Active" ):
                    
                    if( myID.get_data_address() == "Giant_Core_System_Control_CMD_1"): 
                        
                        # print( "\n-> [Rawdata Data]  ==========================================")
                        # print(packet_buffer_str)
                        # print( "===============================================================")
                        # myID.print_data_frame_info(4)                          
                        
                        sg_to_enviolo_cmd_1.User_Interface_Active_Control_Command_1_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_sg_cmd_1_str = sg_to_enviolo_cmd_1.get_decode_info()
                        #sg_to_enviolo_cmd_1.print_decode_info(8)      
                        pass
                        
                    if( myID.get_data_address() == "Giant_Core_System_Control_CMD_2"):                    
                        # print( "\n-> [Rawdata Data]  ==========================================")
                        # print(packet_buffer_str)
                        # print( "===============================================================")
                        # myID.print_data_frame_info(4)                                                  
                       
                        sg_to_enviolo_cmd_2.User_Interface_Active_Control_Command_2_Decode(CanRxBuffer.Data)
                        enviolo_info_consoles.t_sg_cmd_2_str = sg_to_enviolo_cmd_2.get_decode_info()
                        #sg_to_enviolo_cmd_2.print_decode_info(8) 
                        pass        
           
           
           
                #xxxxxxxxxxxxxxxxxxx  篩選 Data Frame (RTR = 0)  Remote_CT 主動丟出來的資料 (Active)  xxxxxxxxxxxxxxxxxxxxxxxxxxxx
                # Remote_CT_Filter = False
                # if(myID.RTR == "Data" and  myID.get_node() == "Remote" and myID.get_packet_type() == "Active" and Remote_CT_Filter == True): 
                      
                #     if (myID.get_data_address() == "Remote_1_Button_CMD_State"):                     
            
                #         remote_btn_status = Remote_Active_Button_CMD_State_Def()
                #         remote_btn_status.Remote_Node_Data_Decode(CanRxBuffer.Data)
                        
                #         status_change = 0
                #         if(remote_btn_status_check.btn_status != remote_btn_status.btn_status):
                #             remote_btn_status_check.btn_status = remote_btn_status.btn_status                                
                #             status_change = 1                             
                #         if(remote_btn_status_check.cmd != remote_btn_status.cmd):
                #             remote_btn_status_check.cmd = remote_btn_status.cmd                                
                #             status_change = 1 
                                                        
                        
                #         if (remote_btn_status.btn_status != 0 and status_change == 1):                                
                        
                #             print( "\n-> [Rawdata Data]  ==========================================")
                #             print(packet_buffer_str)
                #             print( "=============================================================")
                            
                #             myID.print_data_frame_info(4)                                   
                #             remote_btn_status.print_decode_info(8)
                
                # elif(myID.RTR == "Data" and myID.get_node() == "Remote" and myID.get_packet_type() == "Passive"):
                #     print( "\n-> [Rawdata Data]  ==========================================")
                #     print(packet_buffer_str)
                #     print( "=============================================================")                                                        
                #     print(myID.print_data_frame_info(4))
                #     pass
                #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                
                # 看CanBUS上到底有哪些Packet在傳輸
                # ID_Colloctor.add_ID(CanRxBuffer.StdID,CanRxBuffer.RTR)
                # print(ID_Colloctor.get_ID_Array())  #印出所有目前偵測到的ID(不重複)
                # print(ID_Colloctor.get_RTR_Array()) #印出所有目前偵測到的RTR(不重複)
                # pass
                
                
    
                      
            #print(uart_rx_buffer )
            rolling += 1
            # print( str(type(uart_rx_buffer)) + " " + str(len(uart_rx_buffer))+ " " +  str(rolling ) + ": "  + " ID: " +str(hex(uart_rx_buffer[1]  *256 + uart_rx_buffer[0])) )
            
            #string_buffer = str( uart_rx_buffer , encoding = "utf-8" )
            #print(string_buffer)
           
            # 資料包解析完成 清空 uart_rx_buffer 才能接收下一包資料
            clr_uart_rx_buffer()

# ================ UART RX ====================================

if __name__ == "__main__":
    
    
    
    
    print("<Main ID>:", threading.get_ident())

    try:
        uart.open()
        print("open Kethley Serial OK ")

        # ===== UART TX ==========
        #w_buffer = b'MEASure:VOLTage:DC?\n'    # MEASure:VOLTage:DC?
        #uart.write(w_buffer)
        # ===== UART TX ==========

    except Exception as ex:
        print("open Kethley error " + str(ex))
        exit()

   

    task_1 = threading.Thread(target=Master)
    task_2 = threading.Thread(target=uartRxBack)

    # 如果有寫UI才需要把 task_2.setDaemon 設 True (功能:視窗關閉時，同時結束task_2)
    task_2.setDaemon(True)

    task_1.start()
    task_2.start()
    
    create_ui_window()