from xmlrpc import client

url = 'https://elce-odoo-elce-technical-training-moon-4862646.dev.odoo.com'
db = 'elce-odoo-elce-technical-training-moon-4862646'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version)

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))


# model_access = models.execute_kw(db, uid, password,
#                                 'moon.spaceship', 'check_access_rights',
#                                 ['write'], {'raise_exception': False})
# print(model_access)  

# spaceships = models.execute(db, uid, password,
#                             'moon.spaceship', 'create',
#                             [
#                                 {
#                                     'name': 'Apolo 20 mil',
#                                     'state': 'draft',
#                                     'active': True,
#                                     'height': 5,
#                                     'width': 2,
#                                     'depth': 3
#                                 },
#                                 {
#                                     'name': 'Apolo 21 mil',
#                                     'state': 'draft',
#                                     'active': True,
#                                     'height': 5,
#                                     'width': 2,
#                                     'depth': 3
#                                 },
#                             ]
#                             )
# print(spaceships)