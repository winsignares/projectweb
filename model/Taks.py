from config.db import bd, app, ma

class Taks(bd.Model):
    __tablename__ ='tbltaks'
    id = bd.Column(bd.Integer, primary_key = True)
    nametak = bd.Column(bd.String(50))
    idUser_fk = bd.Column(bd.Integer, bd.ForeignKey('tblusers.id'))
    idCategory_fk = bd.Column(bd.Integer,bd.ForeignKey('tblcategory.id'))
    def __init__(self, nametak, idUser_fk):
        self.nametak = nametak
        self.idUser_fk = idUser_fk

with app.app_context():
    bd.create_all()

class TaksSchema(ma.Schema):
    class Meta:
        fields =('id', 'nametak', 'idUser_fk', 'idCategory_fk')