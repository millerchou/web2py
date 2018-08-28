# -*- coding: utf-8 -*-


from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires bladework 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# db = DAL('mysql://root:kingslayer@localhost/test',migrate=False)
db = DAL('mysql://root:kingslayer@www.zzrdsg.xyz/test',migrate=False)







# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db)

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=True)

# -------------------------------------------------------------------------
# configure email


# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

configuration=dict()
db.define_table('test',
                Field('name', 'string')
                )