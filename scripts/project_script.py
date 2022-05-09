from xmlrpc import client

url = 'https://elce-odoo-elce-technical-training-moon-4862646.dev.odoo.com'
db = 'elce-odoo-elce-technical-training-moon-4862646'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version)