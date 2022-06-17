#!/usr/bin/env python3
import time, os, yaml, crayons, sys, requests
from subprocess import call
from datetime import datetime

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

def switchcount(switches):
  i = 0
  for switch in switches:
      i += 1
  return i

def connectthedots(dots):
    for dot in range(dots):
      sys.stdout.write(". ")
      sys.stdout.flush()
      time.sleep(.3)
    print()

def switchlog(switch,ipaddr,severity,command,subcommand):
    with open("switch.log", "a") as switchlog:
        print(f"{datetime.now()} {ipaddr} host:{switch} severity:{severity} command:{command} {subcommand}",file=switchlog)

def getswitchconfig():
    mysource = "https://labs.alta3.com/demo/switchconfig"
    response = requests.get(mysource)
    print(crayons.green(f"source: {mysource}"))
    print(f"HTTP response code: {response.status_code}")
    print(f"HTTP response.text:\n{response.text}")
    switchconfig = yaml.safe_load(response.text)
    return (switchconfig)

def switchconfig():
    clear()
#    OK to read this from a file:     
#    with open("switchconfig", "r") as switches:
#        myswitches = yaml.safe_load(switches)
    myswitches = getswitchconfig()
    #count the switches
    print(crayons.green(f"There are {switchcount(myswitches)} switches to configure, they are:", bold=True))
    # configure one switch at a time
    for switch in myswitches:
        print(crayons.white(f"connecting to {switch.get('switchname')} via {switch.get('sshtarget')}", bold=True), end="" )
        connectthedots(8)
        for command in switch.get('commands'):
            print(crayons.blue(f"sending: " ), end="")
            print(crayons.yellow(f"{command.get('command')} {command.get('subcommand')} ", bold=True))
            switchlog(switch.get('switchname'),switch.get('sshtarget'),5,command.get('command'), command.get('subcommand'))
            time.sleep(1)

def main():
    switchconfig()


main()
