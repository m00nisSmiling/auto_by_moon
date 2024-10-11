import os 
import sys

aa = sys.argv[1]

file2 = open(aa).read()
file3 = file2.splitlines()

for i in file3:
 os.system(f"sudo docker run projectdiscovery/katana:latest -u {i} -d 5 waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef woff,css,png,svg,jpeg,jpg,gif,svg,woff2 | tee -a all_endpoints.txt")
