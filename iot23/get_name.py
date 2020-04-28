#!/usr/bin/env python3
import load_data

# open file
f = open("botnet_name_list.txt", "w")
f2 = open("other_name_list.txt", "w")

# load data
data_set = load_data.load_data()
existing1 = {}
existing2 = {}
botnetList = [] 
otherList = []

# init var
for data in data_set:
    orig_addr = data["id_orig_h_Addr"]
    orig_port = data["id_orig_p_Port"]
    resp_addr = data["id_resp_h_Addr"]
    resp_port = data["id_resp_p_Port"]
    label = data["detailed_label_String"]

    resp_addr = resp_addr.replace(".", "")

    # if botnet (Mirai, Okiru, Torii)
    # print(label)
    if(label == "Mirai" or label == "Okiru" or label == "Torii"):
        #f.write(orig_addr + "\n")
        #f.write(resp_addr + "\n")
        if resp_addr in existing1: 
            print("existing1")
        else:
            botnetList.append(resp_addr)

    elif(label == "-"):
        continue
    else:
        #f2.write(orig_addr + "\n")
        #f2.write(resp_addr + "\n")
        if resp_addr in existing2: 
            print("existing2")
        else:
            otherList.append(resp_addr)

for b in botnetList:
    f.write(b + "\n")

for o in otherList:
    f2.write(o + "\n")


# clean
f.close()
f2.close()
