#!/usr/bin/env python3

def load_data():
    data_set = []
    data_line_set = {}
    f = open("opt/Malware-Project/BigDataset/IoTScenarios/CTU-IoT-Malware-Capture-1-1/bro/conn.log.labeled", "r")
    #separator \x09
    #set_separator	,
    #empty_field	(empty)
    #unset_field	-
    #path	conn
    #open	2018-05-21-21-03-43
    #fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents   label   detailed-label
    #types	time	string	addr	port	addr	port	enum	string	interval	count	count	string	bool	bool	count	string	count	count	count	count	set[string]   string   string

    #	tunnel_parents   label   detailed-label
    #	set[string]   string   string
    for line in f:
        if (line[0] != "#"):
            line_split = line.split()

            fields_Types = line_split[0].split(".")[0]
            ts_Time = line_split[0].split(".")[1]
            uid_String = line_split[1]

            id_orig_h_Addr = line_split[2]
            id_orig_p_Port = line_split[3]
            id_resp_h_Addr = line_split[4]
            id_resp_p_Port = line_split[5]

            proto_Enum = line_split[6]
            service_String = line_split[7]
            duration_Interval = line_split[8]

            orig_bytes_Count = line_split[9]
            resp_bytes_Count = line_split[10]
            conn_state_String = line_split[11]

            local_orig_Bool = line_split[12]
            local_resp_Bool = line_split[13]
            missed_bytes_Count = line_split[14]
            history_String = line_split[15]

            orig_pkts_Count = line_split[16]
            orig_ip_bytes_Count = line_split[17]
            resp_pkts_Count  = line_split[18]
            resp_ip_bytes_Count = line_split[19]

            tunnel_parents_Set_String = line_split[20]
            label_String  = line_split[21]
            detailed_label_String  = line_split[22]

            data_line_set = {

                    "fields_Types" : fields_Types,
                    "ts_Time" : ts_Time,
                    "uid_String" : uid_String,

                    "id_orig_h_Addr" : id_orig_h_Addr,
                    "id_orig_p_Port" : id_orig_p_Port,
                    "id_resp_h_Addr" : id_resp_h_Addr,
                    "id_resp_p_Port" : id_resp_p_Port,

                    "proto_Enum" : proto_Enum,
                    "service_String" : service_String,
                    "duration_Interval" : duration_Interval,

                    "orig_bytes_Count" : orig_bytes_Count,
                    "resp_bytes_Count" : resp_bytes_Count,
                    "conn_state_String" : conn_state_String,

                    "local_orig_Bool" : local_orig_Bool,
                    "local_resp_Bool" : local_resp_Bool,
                    "missed_bytes_Count" : missed_bytes_Count,
                    "history_String" : history_String,

                    "orig_pkts_Count" : orig_pkts_Count,
                    "orig_ip_bytes_Count" : orig_ip_bytes_Count,
                    "resp_pkts_Count" : resp_pkts_Count,
                    "resp_ip_bytes_Count" : resp_ip_bytes_Count,

                    "tunnel_parents_Set_String" : tunnel_parents_Set_String,
                    "label_String" : label_String,
                    "detailed_label_String" : detailed_label_String,

            }

            data_set.append(data_line_set)

    return data_set
