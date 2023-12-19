from app.database import db
# db
dbnnit = db


class Alumni(dbnnit.Model):
    __tablename__ = 'aluno'


    id = dbnnit.Column(dbnnit.Integer, primary_key=True)
    nome = dbnnit.Column(dbnnit.String(100), nullable=False)
    cpf = dbnnit.Column(dbnnit.String(14), nullable=False)
    arg_class = dbnnit.Column(dbnnit.DECIMAL(5, 2), nullable=False)
    ano_entrada = dbnnit.Column(dbnnit.INT, nullable=True)

    def json(self):
        return {'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf
            }

    def __repr__(self):
        return f'<Alumni {self.nome}, cpf {self.cpf}'



class Lecture(dbnnit.Model):
    __tablename__ = 'disciplina'

    id = dbnnit.Column(dbnnit.Integer, primary_key=True)
    codigo = dbnnit.Column(dbnnit.String(8), unique=True, nullable=False)
    nome = dbnnit.Column(dbnnit.String(100), nullable=False)
    carga_horaria = dbnnit.Column(dbnnit.Integer, nullable=False)
    credito = dbnnit.Column(dbnnit.Integer, nullable=False)
    tipo = dbnnit.Column(dbnnit.Integer, nullable=False)

    def json(self):
        return {'id': self.id,
            'codigo': self.codigo,
            'nome': self.nome
        }
    def __repr__(self):
        return '<machineid %r>' % self.machineid



class History(dbnnit.Model):
    __tablename__ = 'historico'

    id_aluno = dbnnit.Column(dbnnit.Integer, nullable=False, primary_key=True)
    id_disciplina = dbnnit.Column(dbnnit.Integer, nullable=False, primary_key=True)
    status = dbnnit.Column(dbnnit.Integer, nullable=False)
    ano = dbnnit.Column(dbnnit.Integer, nullable = False, primary_key=True)
    semestre = dbnnit.Column(dbnnit.Integer, nullable = False, primary_key=True)
    nota = dbnnit.Column(dbnnit.DECIMAL(5,2), nullable=False)

    # PROFESSOR
    aluno = dbnnit.relationship("Alumni")
    disciplina = dbnnit.relationship("Lecture")

    def json(self):
        return {'id': self.id_aluno,
            'id_disciplina': self.id_disciplina,
            'ano': self.ano,
            'semestre': self.semestre
        }

    def __repr__(self):
        return '<machineid %r>' % self.machineid

