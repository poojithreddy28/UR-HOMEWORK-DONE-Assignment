#!/usr/bin/env python
# coding: utf-8

# # Creating a Clients.txt file which contains Last Name ,First Name and Client Number.

# In[10]:


Clients=open("clients.txt","wt")
#File created
n=int(input("enter no of clients : "))
for i in range(n):
    details=input().split()
    d=",".join(details)
    Clients.write(d+"\n")
Clients.close()
#file closed


# # Opening the Clients.txt file

# In[12]:


s=open("clients.txt","rt")
for i in s:
    print(i)
s.close()


# In[31]:


#Creating new file for printing client and usernames
new_file=open("User__Names.txt","wt")
#New file created 


# # Main program for assigning Usernames for Clients.

# In[32]:


def make_user(fname,lname,client_number,new_file):
    f=fname[0:2].lower()
    l=lname[0:2].lower()
    c=client_number[-4:]
    #appending username into new file
    new_file.write(fname+" "+lname+" "+f+l+c)
    
def get_parts(details,new_file):
    l=details.split(",")
    fname=l[1]
    lname=l[0]
    client_number=l[2]
    make_user(fname,lname,client_number,new_file)
    
clients=open("Clients.txt","rt")
new_file=open("User__Names.txt","at")
for details in clients:
    get_parts(details,new_file)
    
clients.close()
new_file.close()


# # Opening User__Names.txt file and Printing Client and User Names.

# In[39]:


n=open("User__Names.txt","rt")
print("Client         Username")
print("=======================")
for i in n:
    i=i.split(" ")
    print(i[0]+" "+i[1]+" : "+i[2])

