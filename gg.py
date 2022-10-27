        self.t_cmf = None
        self.t_cmf = None
        self.t_hwv_1 = None
        self.t_hwv_2 = None
        
        self.t_cmf_str = "cmf"
        self.t_cmf_str = "fwv_1"
        self.t_hwv_1_str = "hwv_1"
        self.t_hwv_2_str = "hwv_2"
   
   
    # xxxxxxxxxx Firmware_Version_1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_fwv_1 = tk.Frame(f_enviolo_passive)
    frame_fwv_1.configure(background='Gray')
    frame_fwv_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_fwv_1 = tk.Text(f_enviolo_passive, width=60, height=6 ,font=("consolas",14))
    enviolo_info_consoles.t_fwv_1.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_fwv_1.delete(0.0,"end")
    enviolo_info_consoles.t_fwv_1.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   