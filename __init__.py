import telnetlib
import time
import json

HOST = "192.168.178.110"
tn = telnetlib.Telnet(HOST, 23, 1)

#peak meter
tn.write("GET 1 PKMTRLVL 23 1\n".encode('ascii')) #23 = Your Instance ID
tn.write("GET 1 PKMTRLVL 23 2\n".encode('ascii')) #23 = Your Instance ID
tn.write("GET 1 PKMTRLVL 23 3\n".encode('ascii')) #23 = Your Instance ID
tn.write("GET 1 PKMTRLVL 23 4\n".encode('ascii')) #23 = Your Instance ID
tn.write("GET 1 PKMTRLVL 23 5\n".encode('ascii')) #23 = Your Instance ID
tn.write("GET 1 PKMTRLVL 23 6\n".encode('ascii')) #23 = Your Instance ID

#level control
tn.write("GET 1 FDRMUTE 29 1\n".encode('ascii')) #29 = Your Instance ID
tn.write("GET 1 FDRLVL 29 1\n".encode('ascii')) #29 = Your Instance ID

time.sleep(0.3)
tn_read =  tn.read_very_eager()
tn.close()

arr = tn_read.splitlines()

vals = {}
vals['peakmeter-ch1'] = arr[3].decode("utf-8")
vals['peakmeter-ch2'] = arr[5].decode("utf-8")
vals['peakmeter-ch3'] = arr[7].decode("utf-8")
vals['peakmeter-ch4'] = arr[9].decode("utf-8")
vals['peakmeter-ch5'] = arr[11].decode("utf-8")
vals['peakmeter-ch6'] = arr[13].decode("utf-8")
vals['levelcontrol-mute'] = arr[15].decode("utf-8")
vals['levelcontrol-volume'] = arr[17].decode("utf-8")

json = json.dumps(vals)

print(json)
