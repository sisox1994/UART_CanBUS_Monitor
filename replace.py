    # xxxxxxxxxx SG Active CMD 2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    f_sg_active_cmd_2 = tk.Frame(f_enviolo_active)
    f_sg_active_cmd_2.configure(background='Gray')
    f_sg_active_cmd_2.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    enviolo_info_consoles.t_sg_cmd_2 = tk.Text(f_sg_active_cmd_2, width=40, height=5 ,font=("consolas",24))
    enviolo_info_consoles.t_sg_cmd_2_str.pack(side=tk.TOP)
    
    enviolo_info_consoles.t_sg_cmd_2_str.delete(0.0,"end")
    enviolo_info_consoles.t_sg_cmd_2_str.insert(0.0,string_buffer)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   