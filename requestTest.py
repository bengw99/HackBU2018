
import requests
#from requests.auth import HTTPBasicAuth
import certifi
#def main():
	#checkURL("www.zon.com")
	
def checkURL(givenURL):
	
	if(givenURL[0:4] != 'http'):
		givenURL = 'http://' + givenURL
	try:
		r = requests.get(givenURL,verify=True)
		return 1
		#print("Response code: %d" % r.status_code)
		#if(r.status_code == requests.codes.ok):
			#print("Website works")
		#else:
			#print("Website does not work")
		#print("Website is certified")
		
	except:
		return 0
		#try:
			#r = requests.get(givenURL, verify=False)
			#print("Response code: %d" % r.status_code)
			#if(r.status_code == requests.codes.ok):
				#print("Website works")
			#else:
				#print("Website does not work")
		#except:
			#print("Website does not work")
		#print("Site does not have a certificate")
		
	#try:
		
		#r2 = requests.get(givenURL, auth=HTTPBasicAuth('user', 'pass'))

		#print("Website does have basic HTTP Authentication")
		#security += 5
	#except:
		#print("Website does not have basic HTTP Authentication")

	#return security
	
#if __name__ == "__main__":
	#main()