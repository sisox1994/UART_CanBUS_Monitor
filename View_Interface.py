import threading
import tkinter as tk
import time
from tkinter.ttk import Style

string_buffer = ""

l1 = "-> [E-Shifting (Enviolo) Node Error Info]  =======\n"
l2 = "eval: Corresponding_Error_was_Gone\n"
l3 = "ecode: Normal\n"
l4 = "==================================================\n"

string_buffer = l1 + l2 + l3 + l4

class Enviolo_Info_Consoles_def:
    
    def __init__(self) -> None:
        self.e_rolling = None
        
        self.t_err = None
        self.t_status = None
        self.t_info_1 = None
        self.t_info_2 = None
        
        self.t_err_str = "err"
        self.t_status_str = "status"
        self.t_info_1_str = "info_1"
        self.t_info_2_str = "info_2"
        
        
        self.t_cmf = None
        self.t_fwv_1 = None
        self.t_hwv_1 = None
        self.t_hwv_2 = None
        self.t_sn_1 = None
        self.t_sn_2 = None
        
        self.t_cmf_str = "cmf"
        self.t_fwv_1_str = "fwv_1"
        self.t_hwv_1_str = "hwv_1"
        self.t_hwv_2_str = "hwv_2"
        self.t_sn_1_str = "sn_1"
        self.t_sn_2_str = "sn_2"

        self.t_sg_cmd_1 = None
        self.t_sg_cmd_2 = None

        self.t_sg_cmd_1_str = "sg_cmd_1"
        self.t_sg_cmd_2_str = "sg_cmd_2"


        pass
    
enviolo_info_consoles = Enviolo_Info_Consoles_def()
    

def ui_data_update():
    
    # ---------------------------------------   Active   ---------------------------------------
    
    # Error 
    if enviolo_info_consoles.t_err_str != None:
        enviolo_info_consoles.t_err.delete(0.0,"end")
        enviolo_info_consoles.t_err.insert(0.0,enviolo_info_consoles.t_err_str)

    # Status 
    if enviolo_info_consoles.t_status_str != None:
        enviolo_info_consoles.t_status.delete(0.0,"end")
        enviolo_info_consoles.t_status.insert(0.0,enviolo_info_consoles.t_status_str)

    # info 1 
    if enviolo_info_consoles.t_info_1_str != None:
        enviolo_info_consoles.t_info_1.delete(0.0,"end")
        enviolo_info_consoles.t_info_1.insert(0.0,enviolo_info_consoles.t_info_1_str)

    # info 2 
    if enviolo_info_consoles.t_info_2_str != None:
        enviolo_info_consoles.t_info_2.delete(0.0,"end")
        enviolo_info_consoles.t_info_2.insert(0.0,enviolo_info_consoles.t_info_2_str)
        
    # ---------------------------------------   Passive   ---------------------------------------
    
    # Confirmation 
    if enviolo_info_consoles.t_cmf_str != None:
        enviolo_info_consoles.t_cmf.delete(0.0,"end")
        enviolo_info_consoles.t_cmf.insert(0.0,enviolo_info_consoles.t_cmf_str)
        
        
    # Firmware_Version_1 
    if enviolo_info_consoles.t_fwv_1_str != None:
        enviolo_info_consoles.t_fwv_1.delete(0.0,"end")
        enviolo_info_consoles.t_fwv_1.insert(0.0,enviolo_info_consoles.t_fwv_1_str)
        
    # Hardware_Version_1 
    if enviolo_info_consoles.t_hwv_1_str != None:
        enviolo_info_consoles.t_hwv_1.delete(0.0,"end")
        enviolo_info_consoles.t_hwv_1.insert(0.0,enviolo_info_consoles.t_hwv_1_str) 
    
    # Hardware_Version_2 
    if enviolo_info_consoles.t_hwv_2_str != None:
        enviolo_info_consoles.t_hwv_2.delete(0.0,"end")
        enviolo_info_consoles.t_hwv_2.insert(0.0,enviolo_info_consoles.t_hwv_2_str) 
        
        
    # Serial_Number_1 
    # if enviolo_info_consoles.t_sn_1_str != None:
    #     enviolo_info_consoles.t_sn_1.delete(0.0,"end")
    #     enviolo_info_consoles.t_sn_1.insert(0.0,enviolo_info_consoles.t_sn_1_str) 

    # Serial_Number_2 
    # if enviolo_info_consoles.t_sn_2_str != None:
    #     enviolo_info_consoles.t_sn_2.delete(0.0,"end")
    #     enviolo_info_consoles.t_sn_2.insert(0.0,enviolo_info_consoles.t_sn_2_str) 
        

  # ----------------------------   Active  from SG   ---------------------------------------
    
    
    if enviolo_info_consoles.t_sg_cmd_1_str != None:
        enviolo_info_consoles.t_sg_cmd_1.delete(0.0,"end")
        enviolo_info_consoles.t_sg_cmd_1.insert(0.0,enviolo_info_consoles.t_sg_cmd_1_str) 
        
    if enviolo_info_consoles.t_sg_cmd_2_str != None:
        enviolo_info_consoles.t_sg_cmd_2.delete(0.0,"end")
        enviolo_info_consoles.t_sg_cmd_2.insert(0.0,enviolo_info_consoles.t_sg_cmd_2_str) 
        

def Background_Task():
    
    sys_cnt = 0
    while True:
        #==========  Do Something Background  ==============
        if (enviolo_info_consoles.e_rolling != None):
            enviolo_info_consoles.e_rolling.delete(0,"end")
            enviolo_info_consoles.e_rolling.insert(0, str(sys_cnt))

            ui_data_update()
        #===================================================
        sys_cnt+=1
        if(sys_cnt % 10 == 0):
            #print("sys:",sys_cnt/10)
            pass
        time.sleep(0.001)    


def create_ui_window():
    
    # setDaemon 可以讓背景程序 Background_Task 隨視窗關閉結束
    task_2 = threading.Thread(target = Background_Task)
    task_2.setDaemon(True)
    task_2.start()
    # 建立 TK UI Window 視窗
    global win
    win = tk.Tk()
    win.geometry("1400x800")
    win.title("CANBUS_Monitor")
    
    
    f_rolling = tk.Frame(win)
    
    l_rolling = tk.Label(f_rolling,text="rolling")
    l_rolling.pack(side=tk.LEFT)
    
    enviolo_info_consoles.e_rolling = tk.Entry(f_rolling)
    enviolo_info_consoles.e_rolling.pack(side=tk.LEFT)
    
    f_rolling.pack()

    f_enviolo_active = tk.Frame(win)
    f_enviolo_active.pack(side=tk.LEFT,padx= 5)
    
    f_enviolo_passive = tk.Frame(win)
    f_enviolo_passive.pack(side=tk.LEFT,padx=5)

    f_sg_active = tk.Frame(win)
    f_sg_active.pack(side=tk.LEFT,padx=5)


    # ---------------------------------------   Active   ---------------------------------------
    
    # xxxxxxxxxx Error xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_err = tk.Frame(f_enviolo_active)
    frame_err.configure(background='Gray')
    frame_err.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_err = tk.Text(f_enviolo_active, width=40, height=5 ,font=("consolas",14))
    enviolo_info_consoles.t_err.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_err.delete(0.0,"end")
    enviolo_info_consoles.t_err.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
    # xxxxxxxxx Status xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_status = tk.Frame(f_enviolo_active)
    frame_status.configure(background='Gray')
    frame_status.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_status = tk.Text(f_enviolo_active, width=40, height=7 ,font=("consolas",14))
    enviolo_info_consoles.t_status.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_status.delete(0.0,"end")
    enviolo_info_consoles.t_status.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   

    # xxxxxxxxxxxxxx Info 1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_info_1 = tk.Frame(f_enviolo_active)
    frame_info_1.configure(background='Gray')
    frame_info_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_info_1 = tk.Text(f_enviolo_active, width=40, height=9 ,font=("consolas",14))
    enviolo_info_consoles.t_info_1.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_info_1.delete(0.0,"end")
    enviolo_info_consoles.t_info_1.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
    
    # xxxxxxxxxxxxxx Info 2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_info_2 = tk.Frame(f_enviolo_active)
    frame_info_2.configure(background='Gray')
    frame_info_2.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_info_2 = tk.Text(f_enviolo_active, width=40, height=9 ,font=("consolas",14))
    enviolo_info_consoles.t_info_2.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_info_2.delete(0.0,"end")
    enviolo_info_consoles.t_info_2.insert(0.0,string_buffer)

    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    
    # ---------------------------------------   Passive   ---------------------------------------
    
    # xxxxxxxxxx Confirmation xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_cfm = tk.Frame(f_enviolo_passive)
    frame_cfm.configure(background='Gray')
    frame_cfm.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_cmf = tk.Text(f_enviolo_passive, width=50, height=4 ,font=("consolas",14))
    enviolo_info_consoles.t_cmf.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_cmf.delete(0.0,"end")
    enviolo_info_consoles.t_cmf.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    # xxxxxxxxxx Firmware_Version_1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_fwv_1 = tk.Frame(f_enviolo_passive)
    frame_fwv_1.configure(background='Gray')
    frame_fwv_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_fwv_1 = tk.Text(f_enviolo_passive, width=50, height=7 ,font=("consolas",14))
    enviolo_info_consoles.t_fwv_1.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_fwv_1.delete(0.0,"end")
    enviolo_info_consoles.t_fwv_1.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
    # xxxxxxxxxx Hardware_Version_1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_hwv_1 = tk.Frame(f_enviolo_passive)
    frame_hwv_1.configure(background='Gray')
    frame_hwv_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_hwv_1 = tk.Text(f_enviolo_passive, width=50, height=4 ,font=("consolas",14))
    enviolo_info_consoles.t_hwv_1.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_hwv_1.delete(0.0,"end")
    enviolo_info_consoles.t_hwv_1.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   

    # xxxxxxxxxx Hardware_Version_2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxframe_hwv_2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_hwv_2 = tk.Frame(f_enviolo_passive)
    frame_hwv_2.configure(background='Gray')
    frame_hwv_2.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_hwv_2 = tk.Text(f_enviolo_passive, width=50, height=4 ,font=("consolas",14))
    enviolo_info_consoles.t_hwv_2.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_hwv_2.delete(0.0,"end")
    enviolo_info_consoles.t_hwv_2.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
    
    # xxxxxxxxxx Serial Number 1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxframe_sn_1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    # frame_sn_1 = tk.Frame(f_enviolo_passive)
    # frame_sn_1.configure(background='Gray')
    # frame_sn_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    # enviolo_info_consoles.t_sn_1 = tk.Text(f_enviolo_passive, width=50, height=3 ,font=("consolas",14))
    # enviolo_info_consoles.t_sn_1.pack(side=tk.TOP)
    
    # enviolo_info_consoles.t_sn_1.delete(0.0,"end")
    # enviolo_info_consoles.t_sn_1.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
     # xxxxxxxxxx Serial Number 2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxframe_sn_1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    # frame_sn_2 = tk.Frame(f_enviolo_passive)
    # frame_sn_2.configure(background='Gray')
    # frame_sn_2.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    # enviolo_info_consoles.t_sn_2 = tk.Text(f_enviolo_passive, width=50, height=3 ,font=("consolas",14))
    # enviolo_info_consoles.t_sn_2.pack(side=tk.TOP)
    
    # enviolo_info_consoles.t_sn_2.delete(0.0,"end")
    # enviolo_info_consoles.t_sn_2.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    # xxxxxxxxxx SG Active CMD 1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    f_sg_active_cmd_1 = tk.Frame(f_enviolo_passive)
    f_sg_active_cmd_1.configure(background='Gray')
    f_sg_active_cmd_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_sg_cmd_1 = tk.Text(f_sg_active_cmd_1, width=50, height=7 ,font=("consolas",14))
    enviolo_info_consoles.t_sg_cmd_1.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_sg_cmd_1.delete(0.0,"end")
    enviolo_info_consoles.t_sg_cmd_1.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
      # xxxxxxxxxx SG Active CMD 2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    f_sg_active_cmd_2 = tk.Frame(f_enviolo_passive)
    f_sg_active_cmd_2.configure(background='Gray')
    f_sg_active_cmd_2.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_sg_cmd_2 = tk.Text(f_sg_active_cmd_2, width=50, height=11,font=("consolas",14))
    enviolo_info_consoles.t_sg_cmd_2.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_sg_cmd_2.delete(0.0,"end")
    enviolo_info_consoles.t_sg_cmd_2.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
    
    #==========  UI code here ====================

    #=========================================
    #win.protocol("WM_DELETE_WINDOW", Window_on_Close)
    win.mainloop()
    
    pass


if __name__ == "__main__":
    

    create_ui_window()

