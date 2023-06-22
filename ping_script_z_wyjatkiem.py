# -*- coding: utf-8 -*-

import subprocess
import os
os.environ['PATH'] = os.environ['PATH'] + ';C:\\Windows\\System32'

def ping_hosts(hosts):
    for host in hosts:
        try:
            output = subprocess.check_output(["C:\\Windows\\System32\\ping", "-n", "1", host], universal_newlines=True)
            if "172.16.0.1" in output or "Destination host unreachable" in output:
                print(f"Host {host} is unreachable.( Zbugowyn SYFFF 172.16.0.1 NIE osiągalny )")
            else:
                print(f"Host {host} is reachable.( osiągalny GITARA)")
        except subprocess.CalledProcessError:
            print(f"Host {host} is unreachable.( NIE osiągalny )")
           

hosts = ["psa242.porta.local", "psa079", "psa042", "pkb129", "pkb226", "psa052", "pkb189", "pkb185", "pkb249", "psa073", "psa014", "pkb122", "pkb164", "pkb248", "pkb215", "psa069", "pkb142", "pkb178", "pkb247", "pkb241", "pkb253", "pkb167", "pkb166", "psa210", "pkb224", "psa013", "pkb169", "pkb243", "psa044", "pkb163", "pkb237", "pkb218", ""]

ping_hosts(hosts)



#Kod koryguje adres 172.16.0.1 który oznazca że jest nie osiągalny i pinguje brame




"""  output = subprocess.check_output(["C:\\Windows\\System32\\ping", "-n", "1", host], universal_newlines=True)
            print(f"Host {host} is reachable.( osiagąlny GITARA)")
        except subprocess.CalledProcessError:
            if host == "172.16.0.1":
                print(f"Host {host} is unreachable ( PIERDOLONE 172.16.0.1 NIE osiągalny )")
            else:
                print(f"Host {host} is unreachable.( NIE osiagalny )") */"""



