import os

print("Requirements are installing ................")
os.system("pip install termcolor")
os.system("sudo apt install docker.io")
os.system("docker pull projectdiscovery/katana:latest")
os.system("sudo apt install httpx-toolkit") 
os.system("sudo apt install subfinder")
os.system("sudo apt install httprobe")
os.system("rm -rf ./setup.py")
