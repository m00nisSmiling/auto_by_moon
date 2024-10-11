import os
import sys
from termcolor import colored
import time

print(colored("""
++++++++++++++++++++
+AUTOMATION_SCRIPTS+
++++++++++++++++++++

+ BY_m00nIsSmiling
+ https://github.com/m00nissmiling

""","blue"))
time.sleep(3)
try:
 pj = sys.argv[1]
 pjn = sys.argv[2]
 dm = sys.argv[3]
 dmn = sys.argv[4]
except IndexError:
 print(colored("Correct Syntax $ python main.py -pj [name] -d [domain]","red"))
else:
 os.system(f"mkdir ./projects/{pjn}")
 print(colored("\n-- SUBDOMAIN FINDING PHASE --","red"))
 os.system(f"subfinder -d {dmn} -o sub1.txt")
 print(colored("_________________________________","blue"))
 print(colored("-Subdomain Counts-","blue"))
 os.system("wc -l sub1.txt")
 print(colored("_________________________________","blue"))
 time.sleep(3)
 #os.system(f"python3 gitsub.py -t [your_token] -d {dmn} |tee -a sub1.txt")
 #print(colored("_________________________________","blue"))
 #print(colored("-Subdomain Counts-","blue"))
 #os.system("wc -l sub1.txt")
 #print(colored("_________________________________","blue"))
 #os.system(f"gobuster dns -d {dmn} -w './wordlists/subs.txt' -o aa.txt")
 #os.system(f"cat aa.txt | grep -Po 'Found: \K.*' >> sub1.txt")
 #print(colored("_________________________________","blue"))
 #print(colored("-Subdomain Counts-","blue"))
 #os.system("wc -l sub1.txt")
 #print(colored("_________________________________","blue"))
 #time.sleep(3)
 print(colored("\n-- ALIVE DOMAINS FILTERING PHASE --","red"))
 os.system("cat sub1.txt | sort | uniq > sub2.txt")
 os.system("cat sub2.txt | httprobe -c 100 | tee -a sub3.txt")#sub3.txt
 os.system("rm -rf sub2.txt sub1.txt aa.txt")
 print(colored("_________________________________","blue"))
 print(colored("-Alive Domain Counts-","blue"))
 os.system("wc -l sub3.txt")
 print(colored("_________________________________","blue")) 
 print(colored("\n-- TECH CHECKING PHASE --","red"))
 time.sleep(3)
 os.system("cat sub3.txt | httpx-toolkit -ip -sc -td -location -title -random-agent | tee -a domain_details.txt") #domain_details.txt
 os.system("cat domain_details.txt | grep WordPress | tee -a wp_do.txt")
 print(colored(f"[+] Wordpress Domains file in [./projects/{pjn}/wp_do.txt] --","red"))#wp_do.txt
 os.system("cat domain_details.txt | grep 404 | tee -a 404_do.txt")
 print(colored(f"[+] 404 Domains file in [./projects/{pjn}/404_do.txt] --","red"))#404_do.txt
 os.system("cat domain_details.txt | grep 200 | tee -a 200_do.txt")
 print(colored(f"[+] 200 Domains file in [./projects/{pjn}/200_do.txt] --","red"))#200_do.txt
 os.system("cat domain_details.txt | grep 500 | tee -a 500_do.txt")
 print(colored(f"[+] 500 Domains file in [./projects/{pjn}/500_do.txt] --","red"))#500_do.txt
 os.system("cat domain_details.txt | grep Drupal | tee -a drupal_do.txt")
 print(colored(f"[+] Drupal Domains file in [./projects/{pjn}/drupal_do.txt] --","red"))#drupal_do.txt
 os.system("cat domain_details.txt | grep Apache | tee -a apache_do.txt")
 print(colored(f"[+] Apache Domains file in [./projects/{pjn}/apache_do.txt] --","red"))#apache_do.txt
 os.system("cat domain_details.txt | grep 'Next.js' | tee -a nextjs_do.txt")
 print(colored(f"[+] Next.js Domains file in [./projects/{pjn}/nextjs_do.txt] --","red"))#nextjs_do.txt
 print(colored("\n-- ENDPOINT ENUMERATION PHASE --","red"))
 os.system("python ./tools/ktn.py sub3.txt")  #all_endpoints.txt
 os.system(f"mv sub3.txt alive_domains.txt")
 os.system(f"mv alive_domains.txt ./projects/{pjn}/")
 os.system(f"mv 200_do.txt ./projects/{pjn}/")
 os.system(f"mv 404_do.txt ./projects/{pjn}/")
 os.system(f"mv 500_do.txt ./projects/{pjn}/")
 os.system(f"mv wp_do.txt ./projects/{pjn}/")
 os.system(f"mv drupal_do.txt ./projects/{pjn}/")
 os.system(f"mv nextjs_do.txt ./projects/{pjn}/")
 os.system(f"mv apache_do.txt ./projects/{pjn}/")
 os.system(f"mv all_endpoints.txt ./projects/{pjn}/")
 os.system(f"mv domain_details.txt ./projects/{pjn}/")
 time.sleep(1)
 print(colored('ALl','red'))
 time.sleep(1)
 print(colored('   Files','green')) 
 time.sleep(1)
 print(colored('        Are','blue'))
 time.sleep(1)
 print(colored('           In','red'))
 time.sleep(1)
 print(colored(f'             ./projects/{pjn}/','green'))
