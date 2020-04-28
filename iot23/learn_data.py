#!/usr/bin/env python3
import load_data

# open file
f = open("orig_resp.txt", "w")
f2 = open("orig_resp_no_dot.txt", "w")

# load data
data_set = load_data.load_data()

# init var
orig_addr_dic = dict()
resp_addr_dic = dict()

for data in data_set:
    orig_addr = data["id_orig_h_Addr"]
    orig_port = data["id_orig_p_Port"]
    resp_addr = data["id_resp_h_Addr"]
    resp_port = data["id_resp_p_Port"]

    if orig_addr in orig_addr_dic:
        orig_addr_dic[orig_addr] += 1
    else: 
        orig_addr_dic[orig_addr] = 1

    if resp_addr in resp_addr_dic:
        resp_addr_dic[resp_addr] += 1
    else: 
        resp_addr_dic[resp_addr] = 1

    orig_resp_write_str = orig_addr + " " + resp_addr + "\n"
    f.write(orig_resp_write_str)

    # orig_resp_write_no_dot_str = orig_addr.replace('.', '') + " " + resp_addr.replace('.', '') + "\n"
    orig_resp_write_no_dot_str = orig_addr.replace('.', '_') + " " + resp_addr.replace('.', '_') + "\n"
    f2.write(orig_resp_write_no_dot_str)

# orign addr analysis
orig_addr_dic_sorted = {k: v for k, v in sorted(orig_addr_dic.items(), key=lambda item: item[1], reverse=True)}
for k, v in orig_addr_dic_sorted.items():
    print(k, v)

# orig addr analysis
resp_addr_dic_sorted = {k: v for k, v in sorted(resp_addr_dic.items(), key=lambda item: item[1], reverse=True)}
for k, v in resp_addr_dic_sorted.items():
    print(k, v)

# clean
f.close()
f2.close()
