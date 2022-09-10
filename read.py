import telnetlib
import time
import json

HOST = "192.168.178.110"
tn = telnetlib.Telnet(HOST, 23, 1)

tn.write("GET 1 PKMTRLVL 23 1\n".encode('ascii'))
tn.write("GET 1 PKMTRLVL 23 2\n".encode('ascii'))
tn.write("GET 1 PKMTRLVL 23 3\n".encode('ascii'))
tn.write("GET 1 PKMTRLVL 23 4\n".encode('ascii'))
tn.write("GET 1 PKMTRLVL 23 5\n".encode('ascii'))
tn.write("GET 1 PKMTRLVL 23 6\n".encode('ascii'))


time.sleep(0.2)
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

json = json.dumps(vals)

print(json)
