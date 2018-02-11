
import requests
from requests.auth import HTTPBasicAuth
import certifi
# def main():
#	checkURL("josh")
	
def checkURL(givenURL):
	
	try:
		r = requests.get(givenURL, verify=True)
		print("Response code: %d" % r.status_code)
		if(r.status_code == requests.codes.ok):
			print("Website works")
		else:
			print("Website does not work")
		print("Website is certified")
		
	except:
		print("Shit is not secure, yo")
		
	try:
		
		r2 = requests.get(givenURL, auth=HTTPBasicAuth('user', 'pass'))

		print("Website does have basic HTTP Authentication")
	except:
		print("Website does not have basic HTTP Authentication")
	
# if __name__ == "__main__":
#	main()
