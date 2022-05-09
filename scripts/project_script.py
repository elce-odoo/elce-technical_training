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

model_access = models.execute_kw(db, uid, password,
                                'project.project', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)    

draft_quotes = models.execute_kw(db, uid, password,
                                 'project.project', 'search',
                                 [[['state', '=', 'draft']]])
print(draft_quotes)

if_confirmed = models.execute_kw(db, uid, password,
                                 'project.project', 'action_confirm',
                                 [draft_quotes])
print(draft_quotes)