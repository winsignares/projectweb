from config.db import bd,app,ma
class Users(bd.Model):
    __tablename__='tblcategory'
    id = bd.Column(bd.Integer,primary_key=True)
    namecategory = bd.Column(bd.String(50))
    
def __init__(self,namecategory):
    self.namecategory = namecategory
   
with app.app_context():
    bd.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields=('id','namecategory')