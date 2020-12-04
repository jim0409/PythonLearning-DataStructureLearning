import requests

godaddy_production_url='https://api.godaddy.com'

def request_for_godaddy_domain(customer_id, api_key, api_secret):
	url=godaddy_production_url
	headers={'X-Shopper-Id': '{}'.format(customer_id), "Authorization": 'sso-key {}:{}'.format(api_key, api_secret)}
	
	return requests.get('{}/v1/domains'.format(url), headers=headers)

# request_for_godaddy_domain()


# customer_id/ apikey/ apisecret
res=request_for_godaddy_domain(customer_id,apikey, apisecret)

print(res)
print(res.content)