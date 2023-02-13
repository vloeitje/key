import csv
from eth_account import Account
import secrets

results = []
for i in range(1000):
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    serial_number = "RN" + str(i + 1).zfill(6)
    results.append([serial_number, private_key, acct.address])

with open('accounts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Serial Number", "Private Key", "Address"])
    writer.writerows(results)
