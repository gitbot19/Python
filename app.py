import json
emails = list()
accounts = list()

    
with open('names.json') as f:
    d = json.load(f)
    print(d)
for i in d:
    if i['ID'] not in emails:
        emails.append(i['ID'])
        emails.append(i['Name'])
print('-----------------------')
print('Get unique accounts from json file')
print('-----------------------')
print(emails)
print('-----------------------')
def frog(num):
    templist = list()
    for i in d:
        if i['ID'] == num and i['ID'] not in accounts:
            templist.append(i['Reign']) 
    return templist

myaccounts = []
print("This is a fog")
print('-----------------------')
print('Get Reign for each account')
print('-----------------------')
for email in range(len(emails)):
    if (email % 2) == 0:
        x = email
        myaccounts.append(emails[x])
        

for acc in myaccounts:
    print("Sending email to LOB -> account",acc, frog(acc))


    

