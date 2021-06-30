#!/usr/bin/python3

import cgi
import subprocess
import time
print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
ins = cmd.split()
if ins[0] == "1":
    img_name = ins[1]
    deployment_name = ins[2]
    command = "kubectl create deployment " + (deployment_name) + " --image=" + (img_name)
    o = subprocess.getoutput("sudo " + command + " --kubeconfig /root/admin.conf")
    print(o)
elif ins[0] == "2":
    pod_name = ins[2]
    img_name = ins[1]
    command = "kubectl run " + (pod_name) + " --image=" + (img_name)
    o = subprocess.getoutput("sudo " + command + " --kubeconfig /root/admin.conf")
    print(o)
elif ins[0] == "3":
    pod_name = ins[1]
    command = "kubectl delete pod " + (pod_name)
    o = subprocess.getoutput("sudo " + command + " --kubeconfig /root/admin.conf")
    print(o)
elif ins[0] == "4":
    deployment_name = ins[1]
    command = "kubectl delete deployment " + (deployment_name)
    o = subprocess.getoutput("sudo " + command + " --kubeconfig /root/admin.conf")
    print(o)
elif ins[0] == "5":
    deployment_name = ins[1]
    port_no = ins[2]
    expose_type =  ins[3]
    command = "kubectl expose deployment " + (deployment_name) + " --port=" + (port_no) + " --type=" + (expose_type)
    o = subprocess.getoutput("sudo " + command + " --kubeconfig /root/admin.conf")
    print(o)
elif ins[0] == "6":
    deployment_name = ins[1]
    replica = ins[2]
    command = "kubectl scale deployment " + (deployment_name) + " --replicas=" + (replica)
    o = subprocess.getoutput("sudo " + command + " --kubeconfig /root/admin.conf")
    print(o)
elif ins[0] == "7":
    command = "sudo kubectl get pods --kubeconfig /root/admin.conf"
    o = subprocess.getoutput(command)
    print(o)

elif ins[0] == "8":
    command = "sudo kubectl get svc --kubeconfig /root/admin.conf"
    o = subprocess.getoutput(command)
    print(o)
elif ins[0] == "9":
    command = "sudo kubectl delete all --all --kubeconfig /root/admin.conf"
    o = subprocess.getoutput(command)
    print(o)
