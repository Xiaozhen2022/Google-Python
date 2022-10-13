# Replacing the old domain name (abc.edu) with a new domain name (xyz.edu).
# Storing all domain names, including the updated ones, in a new file.

import csv
import re
def contain(address, domain):
    pattern = r' [\w\.-]+@'+domain+'$'
    if re.match(pattern, address):
        return True
    return False
def replace(address, old_domain, new_domain):
    pattern = r''+old_domain+'$'
    address = re.sub(pattern, new_domain, address)
    return address
#print(contain(' blossom@abc.edu','abc.edu'))
#print(replace('123@abc.edu','abc.edu','xyz.edu'))
def main():
    old_domain = 'abc.edu'
    new_domain = 'xyz.edu'
    new_user_email_list = []
    with open('user_emails.csv','r') as f:
        user_email_list = list(csv.DictReader(f)) 
        #print(user_email_list)
        for user in user_email_list:
            #print(user[' Email Address'])
            if contain(user[' Email Address'],old_domain):
                user[' Email Address'] = replace(user[' Email Address'],old_domain,new_domain)
                #print(user[' Email Address'])
        f.close()
        
    keys = ['Full Name', ' Email Address']
    with open('update_user_emails.csv','w+') as outfile:
        writer = csv.DictWriter(outfile,fieldnames=keys)
        writer.writerows(user_email_list)
        outfile.close()
main()
