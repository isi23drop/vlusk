from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumni(db.model):
    __tablename__ == 'aluno'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    arg_class = db.Column(db.DECIMAL(5, 2), nullable=False)
    ano_entrada = db.Column(db.INT, nullable=True)

    def __repr__(self):
        return '<machineid %r>' % self.machineid



class Lecture(db.model):
    __tablename__ == 'disciplina'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(8), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)
    credito = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<machineid %r>' % self.machineid



class History(db.model):
    __tablename__ == 'historico'

    id_aluno = db.Column(db.Integer, nullable=False, primary_key=True)
    id_disciplina = db.Column(db.Integer, nullable=False, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable = False, primary_key=True)
    semestre = db.Column(db.Integer, nullable = False, primary_key=True)
    nota = db.Column(db.DECIMAL)DECIMAL(5,2) null,

    # PROFESSOR
    aluno = relationship("Alumni")
    disciplina = relationship("Lecture")

    def __repr__(self):
        return '<machineid %r>' % self.machineid

