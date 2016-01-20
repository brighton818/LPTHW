import sys,string

given_name = raw_input("What is your first name? ")
family_name = raw_input("What is your last name? ")
phone_number = raw_input("What is your phone number? ")
email_address = raw_input("What is your email address? ")
home_address = raw_input("What is your home address? ")

print ("So, your given name is %s, family name is %s, and the phone number is %s. Also your email address is %s, and your home address is %s.") % (given_name, family_name, phone_number, email_address, home_address)

txtName = given_name.lower() + family_name + '.txt'

output_file = open(txtName, 'w')
output_file.write(("So, your given name is %s, family name is %s, and the phone number is %s. Also your email address is %s, and your home address is %s.") % (given_name, family_name, phone_number, email_address, home_address))
output_file.close()
