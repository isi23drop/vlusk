drop table historico;
drop table disciplina;
drop table aluno;

CREATE TABLE aluno (
     id SERIAL PRIMARY KEY,
     nome VARCHAR(60) NOT NULL,
     cpf VARCHAR(14) NOT NULL,
     arg_class DECIMAL(5,2) not null,
     ano_entrada INT NULL
);


CREATE TABLE disciplina (
     id SERIAL PRIMARY KEY,
     codigo VARCHAR(8) NOT NULL UNIQUE,
     nome VARCHAR(100) NOT NULL,
     carga_horaria INT NULL,
     credito int NULL,
     tipo int NOT NULL
     --cada disciplina tem 1 perfil
);


CREATE TABLE historico (
     id_aluno INT NOT NULL,
     id_disciplina INT NOT NULL,
     status int not null,
     ano int not null,
     semestre int not null,
     nota DECIMAL(5,2) null,
     --PROFESSOR
     PRIMARY KEY (id_aluno, id_disciplina, ano, semestre),
     FOREIGN KEY (id_aluno) REFERENCES aluno(id),
     FOREIGN KEY (id_disciplina) REFERENCES disciplina(id)
);




