class field_key(object):
    basic_compare_list = {
		'EQUAL',
		'NOT_EQUAL',
	}

    PKT_compare_list = basic_compare_list.union({'OVER', 'UNDER'})
    TCP_FLAG_compare_list = basic_compare_list.union({'AND', 'OR'})

    value_list = {
		'ipv4': {"method": basic_compare_list, "validator":"regipv4"},
		'ipv6': basic_compare_list,
		'mac': basic_compare_list,
		'CIDR': basic_compare_list,
		'port': basic_compare_list,
		'TCP_UDP': basic_compare_list,
		'PKT_LEN': PKT_compare_list,
		'PKT_VOLUME': PKT_compare_list,
		'TCP_FLAGS': TCP_FLAG_compare_list,
		'GSLB': basic_compare_list,
		'ASN': basic_compare_list,
		'COUNTRY': basic_compare_list,
		'REGION': basic_compare_list,
		'SUB_REGION': basic_compare_list,
		'ME_ID': basic_compare_list,
		'FILTER_ID': basic_compare_list,
		'ME_RESULT': basic_compare_list,
	}

    field_list = {
		'LOCAL_IP': {'ipv4', 'ipv6', 'mac'},
		'REMOTE_IP': {'ipv4', 'ipv6', 'mac'},
		'NEXT_HOP': {'ipv4', 'ipv6', 'mac'},
		'LOCAL_CIDR_A/B/C/D': {'CIDR'},
		'REMOTE_CIDR_A/B/C/D': {'CIDR'},
		'IP_VER': {'ipv4', 'ipv6'},
		'LOCAL_PORT': {'port'},
		'REMOTE_PORT': {'port'},
		'NAT_PORT': {'port'},
		'NIC_PORT': {'port'},
		'PROTOCOL': {'TCP_UDP'},
		'PKT_LEN': {'PKT_LEN'},
		'PKT_VOLUME': {'PKE_VOLUME'},
		'TCP_FLAGS': {'TCP_FLAGS'},
		'LOCAL_GSLB': {'GSLB'},
		'REMOTE_GSLB': {'GSLB'},
		'LOCAL_ASN': {'ASN'},
		'REMOTE_ASN': {'ASN'},
		'LOCAL_COUNTRY': {'COUNTRY'},
		'REMOTE_COUNTRY': {'COUNTRY'},
		'LOCAL_REGION': {'REGION'},
		'REMOTE_REGION': {'REGION'},
		'LOCAL_SUB_REG': {'SUB_RESGION'},
		'REMOTE_SUB_REG': {'SUB_REGION'},
		'ME_ID': {'ME_ID'},  # not for field rule
		'FILTER_ID': {'FILTER_ID'},  # not for field rule
		'ME_RESULT': {'ME_RESULT'},
	}

    @classmethod
    def key_to_dict(cls, key):
    	return {i: cls.value_list[i] for i in cls.field_list[key]}


a = field_key()

print(a.field_list['LOCAL_IP'])

print(a.field_list['REMOTE_IP'])

print(field_key.key_to_dict('LOCAL_IP'))

r_k = field_key.key_to_dict('LOCAL_IP')
print(r_k.items())
try:
	print(r_k.items()['mac'])
except:
	print("r_k.items()['mac'] is not callable")
	pass

dict_r_k = dict(r_k.items())
print(dict_r_k['mac'])

# reference: https://www.zhihu.com/question/62962708
# python3 中的dict不是列表，需要自己轉list(dict.items)