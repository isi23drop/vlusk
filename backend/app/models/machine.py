from app.database import db, Column, relationship
# db


# class Alumni(db):
class Alumni(db.Model):
    __tablename__ = 'aluno'

    id = Column(db.Integer, primary_key=True)
    nome = Column(db.String(100), nullable=False)
    cpf = Column(db.String(14), nullable=False)
    arg_class = Column(db.DECIMAL(5, 2), nullable=False)
    ano_entrada = Column(db.INT, nullable=True)

    def json(self):
        return {'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf
            }

    def __repr__(self):
        return f'<Alumni {self.nome}, cpf {self.cpf}'



class Lecture(db.Model):
    __tablename__ = 'disciplina'

    id = Column(db.Integer, primary_key=True)
    codigo = Column(db.String(8), unique=True, nullable=False)
    nome = Column(db.String(100), nullable=False)
    carga_horaria = Column(db.Integer, nullable=False)
    credito = Column(db.Integer, nullable=False)
    tipo = Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id,
            'codigo': self.codigo,
            'nome': self.nome
        }
    def __repr__(self):
        return '<machineid %r>' % self.machineid



class History(db.Model):
    __tablename__ = 'historico'

    id_aluno = Column(db.Integer, db.ForeignKey(Alumni.id), nullable=False, primary_key=True)
    id_disciplina = Column(db.Integer, db.ForeignKey(Lecture.id),nullable=False, primary_key=True)
    status = Column(db.Integer, nullable=False)
    ano = Column(db.Integer, nullable = False, primary_key=True)
    semestre = Column(db.Integer, nullable = False, primary_key=True)
    nota = Column(db.DECIMAL(5,2), nullable=False)

    # PROFESSOR
    #aluno = relationship("Alumni(id)")
    #disciplina = relationship("Lecture")
    #discente = Column(db.Integer, db.ForeignKey('Alumni.id'))

    def json(self):
        return {'id': self.id_aluno,
            'id_disciplina': self.id_disciplina,
            'ano': self.ano,
            'semestre': self.semestre
        }

    def __repr__(self):
        return '<machineid %r>' % self.machineid

