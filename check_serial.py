import serial


uart = serial.Serial()
uart.port = "/dev/tty.usbserial-0001"
uart.baudrate = 19200
uart.bytesize = serial.EIGHTBITS  # number of bits per bytes
uart.parity = serial.PARITY_NONE  # set parity check
uart.stopbits = serial.STOPBITS_ONE  # number of stop bits
uart.timeout = 0.5  # non-block read 0.5s
uart.writeTimeout = 0.5  # timeout for write 0.5s
uart.xonxoff = False  # disable software flow control
uart.rtscts = False  # disable hardware (RTS/CTS) flow control
uart.dsrdtr = False  # disable hardware (DSR/DTR) flow control



try:
    uart.open()
    print("open Serial OK ")
    # ===== UART TX ==========
    #w_buffer = b'MEASure:VOLTage:DC?\n'    # MEASure:VOLTage:DC?
    #uart.write(w_buffer)
    # ===== UART TX ==========
except Exception as ex:
    print("open uart error " + str(ex))
    exit()