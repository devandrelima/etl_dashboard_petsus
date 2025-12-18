CREATE DATABASE dashpetsus;

CREATE TABLE IF NOT EXISTS bairro (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ubs (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    id_bairro INT,
    CONSTRAINT fk_ubs_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id)
);

CREATE TABLE IF NOT EXISTS populacao (
    id SERIAL PRIMARY KEY,
    qnt_masculina INT DEFAULT 0,
    qnt_feminina INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_populacao_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_populacao_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);

CREATE TABLE IF NOT EXISTS perfil_educacional (
    id SERIAL PRIMARY KEY,
    qnt_creche INT DEFAULT 0,
    qnt_pre_escola INT DEFAULT 0,
    qnt_classe_alfabetizacao INT DEFAULT 0,
    qnt_1_a_4_ano_fundamental INT DEFAULT 0,
    qnt_5_a_8_ano_fundamental INT DEFAULT 0,
    qnt_ensino_fundamental_completo INT DEFAULT 0,
    qnt_ensino_fundamental_especial INT DEFAULT 0,
    qnt_eja_1_a_4_ano INT DEFAULT 0,
    qnt_eja_5_a_8_ano INT DEFAULT 0,
    qnt_ensino_medio INT DEFAULT 0,
    qnt_ensino_medio_especial INT DEFAULT 0,
    qnt_medio_eja INT DEFAULT 0,
    qnt_superior INT DEFAULT 0,
    qnt_mobral INT DEFAULT 0,
    qnt_nenhum INT DEFAULT 0,
    qnt_nao_informado INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_educacao_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_educacao_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);

CREATE TABLE IF NOT EXISTS renda_familiar (
    id SERIAL PRIMARY KEY,
    qnt_1_4_salario INT DEFAULT 0,
    qnt_1_2_salario INT DEFAULT 0,
    qnt_1_salario INT DEFAULT 0,
    qnt_2_salario INT DEFAULT 0,
    qnt_3_salario INT DEFAULT 0,
    qnt_4_salario INT DEFAULT 0,
    qnt_mais_4_salario INT DEFAULT 0,
    nao_informado INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_renda_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_renda_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);

CREATE TABLE IF NOT EXISTS abastecimento_agua (
    id SERIAL PRIMARY KEY,
    qnt_rede_encanada INT DEFAULT 0,
    qnt_poco INT DEFAULT 0,
    qnt_cisterna INT DEFAULT 0,
    qnt_carro_pipa INT DEFAULT 0,
    outro INT DEFAULT 0,
    nao_informado INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_agua_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_agua_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);

CREATE TABLE IF NOT EXISTS tratamento_agua (
    id SERIAL PRIMARY KEY,
    qnt_filtrada INT DEFAULT 0,
    qnt_fervida INT DEFAULT 0,
    qnt_clorada INT DEFAULT 0,
    qnt_mineral INT DEFAULT 0,
    qnt_sem_tratamento INT DEFAULT 0,
    qnt_nao_informado INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_tratamento_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_tratamento_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);

CREATE TABLE IF NOT EXISTS destino_lixo (
    id SERIAL PRIMARY KEY,
    qnt_coletado INT DEFAULT 0,
    qnt_queimado INT DEFAULT 0,
    qnt_ceu_aberto INT DEFAULT 0,
    qnt_outra_forma INT DEFAULT 0,
    qnt_nao_informado INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_lixo_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_lixo_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);

CREATE TABLE IF NOT EXISTS escoamento_banheiro (
    id SERIAL PRIMARY KEY,
    qnt_fossa_septica INT DEFAULT 0,
    qnt_fossa_rudimentar INT DEFAULT 0,
    qnt_direto_rio INT DEFAULT 0,
    qnt_ceu_aberto INT DEFAULT 0,
    qnt_outra_forma INT DEFAULT 0,
    qnt_nao_informado INT DEFAULT 0,
    id_bairro INT NOT NULL,
    id_ubs INT NOT NULL,
    CONSTRAINT fk_banheiro_bairro FOREIGN KEY (id_bairro) REFERENCES bairro(id),
    CONSTRAINT fk_banheiro_ubs FOREIGN KEY (id_ubs) REFERENCES ubs(id)
);