import psutil as ps

print("CPU Counts: {}".format(ps.cpu_count()))
print("CPU Counts: {}",ps.cpu_count(), 3, 23.5) #print function can receive several parameters of diferent types
#print("Hardware temperature: ", end=" ")
#ps.sensors_temperatures() # this function is only available on linux
print("Boot time: ", ps.boot_time())
print("Current pids: ", ps.pids())
print("Sensors battery:", ps.sensors_battery())
print("users: ", ps.users())