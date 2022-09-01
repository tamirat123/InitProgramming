             Assignment 1 – Malware Hunting 
1. The following are some examples of security flaws that you may encounter in your day-to-day life: 
	- Phishing attack   
	-Denial-of-Services attack 
	-Ransomware attack 
	- SQL injections 
	- Malware attacks 
	- Ransomware Attack 
2. The following are the characters of a malicious email 
	- First we need to identify the sender’s email  
	- It may contain suspicious links embeded into them
	- It might contain Grammatical errors 
	- The content is bizarre or unbelievable 
##		Assignment 2 
1. To identify new created process we can use task manager or sysinternals in windows and forkstat to identify new processes and services running.
2. <img src="./shot%20(6).png">
We were able to find the registery folders of the malwares using sysinternals.
## Icons

The executable programs had an icon of a folder while the javascript files and VB scripts were the deafult icons on windows.

3. Malicious softwares contain the following behaviour :
	* They may not contain any icon, description or company name
	*  Often times they don't have a signed Microsoft image
 	* They live in windows directory or user profile 
	* They are packed 


	* They include strange urls attached to them 
	* Have suspicious DLLs 
5. A. We can use the "net users" command to find list of users in our computer.
     B. We can use Event viewer software to know our login history 

<img src="shot (1).png">

>At the first shot we could not find any suspicious processes running in the background.

<img src="shot (3).png">

>Once the malware samples were executed new processes and services strated popping up.these include:

    * javascript files
    * Visual basic scripts and
    * Executable programs


<img src="shot (4).png">

>Most of the malwares samples have managed to enter the administrator folder of the system.

>No new users were created during this process.


# Eradication

Finally we can eradicate the malicious programs by deleting the processes using sysinternals.