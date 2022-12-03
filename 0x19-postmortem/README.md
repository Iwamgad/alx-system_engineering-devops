Postmortem
![situation](https://www.pngitem.com/pimgs/m/10-104820_oh-god-why-png-oh-my-god-cartoon.png)
# Issue Summary
### On 24/10/2022 7:00 pm PST, I was unable to ssh into my web_server_2 from the provided sandbox terminal, due to this I was not able to do my tasks at ease. The root cause of the outage was when configuring the webserver I forgot to generate a public/private key at my sandbox terminal so I can put the public key inside my server to grant permission to ssh.   
# Timeline
### 7:00 pm: after I entered my web_server_2 locally and logging out I tried to ssh into it from the sandbox provided by ALX but I recived the permission denied (publickey) message.
### 7:15 pm: I entered mysandbox terminal and generated public and private keys and grabed the public key.
### 7:15 pm: I entered into my web_server_2 again locally and searched for the authorized_keys file in side this folder ~/.ssh when I opened the file and added the public key I grabbed before to it.
# Root cause and resolution 
### The root cause is forgeting to add the public key to the authorized_keys file inside the server.
### The resolution was generating a private and public key at root place you want to ssh into a server and after grabbing the public key add it to the authorized_keys file by entering the server from another permmited machine. 
# Corrective and preventative measures
### The corrective measure I took was properly generating a public and private key and making sure I added the public key to the authorized_keys file inside the server.