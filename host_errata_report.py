#!/usr/bin/env python
from passlib.hash import sha256_crypt
from cryptography.fernet import Fernet
from datetime import datetime
import json
import sys
import csv

try:
    import requests
except ImportError:
    print "Please install the python-requests module."
    sys.exit(-1)

current_date = datetime.now().strftime('%Y-%m-%d_%H%M%S')
crypted_password = 'gAAAAABezhga5-1y_EUoyUiOaLL6jfd0gL8UPbcGM-P_WFXPMVclU51T_1TZGEB2sG83W1bvkbwW7a1mCZXTkT799UDW6rZwrYw6WhetzSECNtZy8Ut1MyQ='
key = 'gSI6xSqONg-h15A5VGqHyhcsV_tqFzvdD0Xnb_KoRd0='
f = Fernet(key)
decrypted = f.decrypt(crypted_password)

# URL to your Satellite 6 server
URL = "https://satellite.example.com"
# URL for the API to your deployed Satellite 6 server
SAT_API = "%s/api/v2/" % URL
# Katello-specific API
KATELLO_API = "%s/katello/api/" % URL
POST_HEADERS = {'content-type': 'application/json'}
# Default credentials to login to Satellite 6
USERNAME = "admin"
PASSWORD = decrypted
# Ignore SSL for now
SSL_VERIFY = True

# Name of the organization to be either created or used
ORG_NAME = "example_org"
# Name for life cycle environments to be either created or used
csv_file = 'errata_report-' + current_date + '.csv'


def get_json(url):
    # Performs a GET using the passed URL location
    r = requests.get(url, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    return r.json()

def get_results(url):
    jsn = get_json(url)
    if jsn.get('error'):
        print "Error: " + jsn['error']['message']
    else:
        if jsn.get('results'):
            return jsn['results']
        elif 'results' not in jsn:
            return jsn
        else:
            None
    return None

def display_all_results(url):
    results = get_results(url)
    if results:
        return json.dumps(results, indent=4, sort_keys=True)

def katello_agent_installed(host_id):
    katello_package_installed = display_all_results(URL + '/api/v2/hosts/' + str(host_id) + "/packages?search=katello-agent")
    if katello_package_installed:
        return True
    else:
        return False

def get_errata(host_id):
    host_errata = display_all_results(URL + '/api/hosts/%s/errata?per_page=5000' % str(host_id))
    return host_errata

def main():
    # Get all hosts
    get_hosts = display_all_results(URL + '/api/v2/hosts?per_page=5000')
    hosts = (json.loads(get_hosts))

    csv_resource_fields = "Hostname;Katello agent installed;Errata ID;Type;Severity;Issued date;Installable;Reboot suggested;Errata name;Package list"
    write_csv = open(csv_file, 'a')
    write_csv.write(csv_resource_fields)

    # Get all Errata per host
    for host in hosts:
        if katello_agent_installed(host['id']):
                if host['content_facet_attributes']['errata_counts']['total'] is not 0:
                        print "\nErrata for host %s:" % host['name']
                        print('=' * 30)
                        #write_csv.write("\n"+host['name'])
                        #get_errata = display_all_results(URL + '/api/hosts/%s/errata?per_page=5000' % str(host['id']))
                        errata = (json.loads(get_errata(host['id'])))
                        for erratum in errata:
                                separator = ','
                                write_csv.write("\n" + host['name'] + ";True;" + erratum['errata_id'] + ";" + erratum['type'] + ";" + erratum['severity'] + ";" + erratum['issued'] + ";" + str(erratum['installable']) + ";" + str(erratum['reboot_suggested']) + ";" + erratum['name'] + ";" + separator.join(erratum['packages']))
                                print "\t\tErrata ID: " + (erratum['errata_id'])
                                print "\t\tType: " + (erratum['type'])
                                print "\t\tSeverity: " + (erratum['severity'])
                                print "\t\tIssued date: " + (erratum['issued'])
                                print "\t\tInstallable: " + str(erratum['installable'])
                                print "\t\tReboot suggested: " + str((erratum['reboot_suggested']))
                                print "\t\tErrata name: " + (erratum['name'])
                                #print "\t\tDescription: " + (erratum['description'])
                                #print "\t\tSolution: " + (erratum['solution'])
                                print "\t\t--> Packages to update: "
                                for package in erratum['packages']:
                                        print "\t\t    " + package
                else:
                        print "\nNo errata for host %s available. Host is up to date." % host['name']
        else:
                print "\nNo Katello agent installed on host %s." % host['name']
                write_csv.write("\n" + host['name'] + ";False")

    write_csv.close()

if __name__ == "__main__":
    main()