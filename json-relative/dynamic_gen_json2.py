import json


class ACLlsit(object):
    def __new__(clz):
        acl_list = dict()
        acl_list['enable'] = 0
        acl_list['prefix'] = []
        acl_list['asn'] = []
        acl_list['gslb'] = []
        print(acl_list)

    def __init__(self, enable_status, ):


mit1 = dict()
mit1['id'] = 'MAT'

mit1_prefix_list = ['10.255.255.3']
mit1['prefix'] = mit1_prefix_list

mit1_white_dict = dict()
mit1['white_list'] = mit1_white_dict

mit1_white_dict_enable = 0
mit1_white_dict['enable'] = mit1_white_dict_enable

mit1_white_dict_prefix_list = ["220.136.0.0/16", "2001:db8:3c4d:15::/64"]
mit1_white_dict['prefix'] = mit1_white_dict_prefix_list

mit1_white_dict_asn_lsit = ["2.15169", "3462"]
mit1_white_dict['asn'] = mit1_white_dict_asn_lsit

mit1_white_dcit_gslb_list = ["1100", "2426"]
mit1_white_dict['gslb'] = mit1_white_dcit_gslb_list

mitigation_entity_data = [mit1, ]

print(type(mitigation_entity_data))
print(mitigation_entity_data[0])

ACLlsit()