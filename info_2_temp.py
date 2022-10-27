    
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_info_1 = tk.Frame(win)
    frame_info_1.configure(background='Gray')
    frame_info_1.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    
    label_E_Shifting_Enviolo_Node_Info_1 = tk.Label(frame_info_1,text="E-Shifting (Enviolo) Node Information_1 Info",font=("Arial", 16))
    label_E_Shifting_Enviolo_Node_Info_1.pack(anchor=tk.W,ipady=2)
    
    # ==== ca_spd (Cadence):  ============================================
    f_ca_spd = tk.Frame(frame_info_1)
    f_ca_spd.pack()
    
    l_ca_spd = tk.Label(f_ca_spd,text="ca_spd (Cadence): ")
    l_ca_spd.pack(side=tk.LEFT)
    
   
    info_1.e_ca_spd = tk.Entry(f_ca_spd)
    info_1.e_ca_spd.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== ar_ig (Gear Ratio): ============================================
    f_ar_ig = tk.Frame(frame_info_1)
    f_ar_ig.pack()
    
    l_ar_ig = tk.Label(f_ar_ig,text="ar_ig (Gear Ratio): ")
    l_ar_ig.pack(side=tk.LEFT)
    
    info_1.e_ar_ig = tk.Entry(f_ar_ig)
    info_1.e_ar_ig.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== ve_spd (Vehicle speed): ============================================
    f_ve_spd = tk.Frame(frame_info_1)
    f_ve_spd.pack()
    
    l_ve_spd = tk.Label(f_ve_spd,text="ve_spd (Vehicle speed): ")
    l_ve_spd.pack(side=tk.LEFT)
    
    info_1.e_ve_spd = tk.Entry(f_ve_spd)
    info_1.e_ve_spd.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== gr_idx (Gear Index): ============================================
    f_gr_idx = tk.Frame(frame_info_1)
    f_gr_idx.pack()
    
    l_gr_idx = tk.Label(f_gr_idx,text="gr_idx (Gear Index): ")
    l_gr_idx.pack(side=tk.LEFT)
    
    info_1.e_gr_idx = tk.Entry(f_gr_idx)
    info_1.e_gr_idx.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== ws (Wheel Speed):  ============================================
    f_ws = tk.Frame(frame_info_1)
    f_ws.pack()
    
    l_ws = tk.Label(f_ws,text="ws (Wheel Speed): ")
    l_ws.pack(side=tk.LEFT)
    
    info_1.e_ws = tk.Entry(f_ws)
    info_1.e_ws.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== ld (Lifetime Distance):  ============================================
    f_ld = tk.Frame(frame_info_1)
    f_ld.pack()
    
    l_ld = tk.Label(f_ld,text="ld (Lifetime Distance): ")
    l_ld.pack(side=tk.LEFT)
    
    info_1.e_ld = tk.Entry(f_ld)
    info_1.e_ld.pack(side=tk.LEFT)
    # ================================================================
    
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    frame_info_2 = tk.Frame(win)
    frame_info_2.configure(background='Gray')
    frame_info_2.pack(side=(tk.TOP),anchor=tk.N,ipadx=5,ipady=5)
    
    
    label_E_Shifting_Enviolo_Node_Info_2 = tk.Label(frame_info_2,text="E-Shifting (Enviolo) Node Information_2 Info",font=("Arial", 16))
    label_E_Shifting_Enviolo_Node_Info_2.pack(anchor=tk.W,ipady=2)
    
    # ==== du_cll (DU Cadence Low Limit):  ============================================
    f_du_cll = tk.Frame(frame_info_2)
    f_du_cll.pack()
    
    l_du_cll = tk.Label(f_du_cll,text="du_cll (DU Cadence Low Limit): ")
    l_du_cll.pack(side=tk.LEFT)
    
   
    info_2.e_du_cll = tk.Entry(f_du_cll)
    info_2.e_du_cll.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== u_chl (DU Cadence High Limit): ============================================
    f_du_chl = tk.Frame(frame_info_2)
    f_du_chl.pack()
    
    l_du_chl = tk.Label(f_du_chl,text="u_chl (DU Cadence High Limit): ")
    l_du_chl.pack(side=tk.LEFT)
    
    info_2.e_du_chl = tk.Entry(f_du_chl)
    info_2.e_du_chl.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== "rll_rig ([Low Limit] of [Ratio Gear] ):  ============================================
    f_rll_rig = tk.Frame(frame_info_2)
    f_rll_rig.pack()
    
    l_rll_rig = tk.Label(f_rll_rig,text="rll_rig ([Low Limit] of [Ratio Gear] ): ")
    l_rll_rig.pack(side=tk.LEFT)
    
    info_2.e_rll_rig = tk.Entry(f_rll_rig)
    info_2.e_rll_rig.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== rhl_rig ([High Limit] of [Ratio Gear]): ============================================
    f_rhl_rig = tk.Frame(frame_info_2)
    f_rhl_rig.pack()
    
    l_rhl_rig = tk.Label(f_rhl_rig,text="rhl_rig ([High Limit] of [Ratio Gear]): ")
    l_rhl_rig.pack(side=tk.LEFT)
    
    info_2.e_rhl_rig = tk.Entry(f_rhl_rig)
    info_2.e_rhl_rig.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== in_bv (Input Battery Voltage):  ============================================
    f_in_bv = tk.Frame(frame_info_2)
    f_in_bv.pack()
    
    l_in_bv = tk.Label(f_in_bv,text="in_bv (Input Battery Voltage): ")
    l_in_bv.pack(side=tk.LEFT)
    
    info_2.e_in_bv = tk.Entry(f_in_bv)
    info_2.e_in_bv.pack(side=tk.LEFT)
    # ================================================================
    
    # ==== na (No Application):   ============================================
    f_na = tk.Frame(frame_info_2)
    f_na.pack()
    
    l_na = tk.Label(f_na,text="na (No Application): ")
    l_na.pack(side=tk.LEFT)
    
    info_2.e_na = tk.Entry(f_na)
    info_2.e_na.pack(side=tk.LEFT)


    # ================================================================
    

    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx