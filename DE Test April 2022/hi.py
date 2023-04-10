line = "03/11/21 08:51:06 INFO    :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0\n"

split_point  = line.index(":.")
print(split_point)
log_level = line[18:split_point]
print(log_level)
message = line[split_point:].replace("\n","")

