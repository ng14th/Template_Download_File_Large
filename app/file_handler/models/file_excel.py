from app.core.database.mongo import umongo_cnx
from umongo import fields, Document


@umongo_cnx.register
class FileExcel(Document):
    header_1 = fields.StringField(require = True)
    header_2 = fields.StringField(require = True)
    header_3 = fields.StringField(require = True)
    header_4 = fields.StringField(require = True)
    header_5 = fields.StringField(require = True)
    header_6 = fields.StringField(require = True)
    header_7 = fields.StringField(require = True)
    header_8 = fields.StringField(require = True)
    header_9 = fields.StringField(require = True)
    header_10 = fields.StringField(require = True)
    header_11 = fields.StringField(require = True)
    header_12 = fields.StringField(require = True)
    header_13 = fields.StringField(require = True)

    
    class Meta:
        collection_name = "FileExcel"