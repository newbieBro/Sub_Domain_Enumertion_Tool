import sys
import requests

""" This function will do the actual part of the 
    enumeration of subdomain"""
def scan_subdomain(domain_name, sub_domain_list):

    """ create url using subdomain and test domain
        and do a get https request for each constructed url
        """
    for i in sub_domain_list:
        url = f"https://{i}.{domain_name}"

        try:
            requests.get(url)
            print(f"[+] URL: {url}")
        except requests.ConnectionError:
            pass

#main function
if __name__ == '__main__':

    file_with_subdomain_names = sys.argv[1]
    domain_name = sys.argv[2]

    """ Here reading the input file which contains 
        possible subdomain and storing in a List """

    with open(file_with_subdomain_names, "r") as file:
        line = file.read()

        # creating list using splitlines()
        s_domain = line.splitlines()

    print(f"Listing sub-domain of {domain_name}")
    scan_subdomain(domain_name, s_domain)
