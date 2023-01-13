emails = ["test.email+kevin@dailybyte.com", "test.e.mail+john.smith@dailybyte.com", "testemail+david@daily.byte.com", "jane.doe+test@gmail.com", "jane.doe+test@gmail.com"]
unique = 0
final = []
final_d = dict()

for email in emails:
  email_str = ""
  ignore = email[email.index('+') : email.index('@')].replace(".", "")
  email_str = email[:email.index('@')].replace(".", "").replace(ignore, "")   +email[email.index('@'):]

  final.append(email_str)

for em in final:
        if(final_d.get(em, 0) == 0):
            final_d[em] = 1
        else:
            final_d[em] +=1

print(len(final_d)) #3

"""
This question is asked by Google. Email addresses are made up of local and domain names. For example in kevin@dailybyte.com, kevin is the local name and dailybye.com is the domain name. Email addresses may also contain '+' or '.' characters besides lowercase letters. If there is a '.' in the local name of the email address it is ignored. Everything after a '+' in the local name is also ignored. For example ke.vin+abc@dailybyte.com is equivalent to kevin@dailybyte.com Given a list of email addresses, find the number of unique addresses.

Ex: Given the following emails...

emails = [
    "test.email+kevin@dailybyte.com", 
    "test.e.mail+john.smith@dailybyte.com", 
    "testemail+david@daily.byte.com"
], return 2. "testemail@dailybyte.com" and "testemail@daily.byte.com" are unique since the first two email addresses in the list are equivalent.
"""
