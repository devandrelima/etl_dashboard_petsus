import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:postgres@localhost:5432/dashpetsus')

def processamento_etl(caminho_csv):
    # Pula as 3 primeiras linhas de cabeçalho
    df = pd.read_csv(caminho_csv, skiprows=3, header=None)
    
    # preenche vazios com 0 e remove espaços
    df = df.fillna(0)
    
    # Cache para evitar duplicidade de bairros no banco
    cache_bairros = {}

    print("Iniciando processamento dos dados...")

    with engine.begin() as conexao:
        for _, row in df.iterrows():
            nome_ubs = str(row[0]).strip()
            nome_bairro = str(row[1]).strip()
            
            if not nome_bairro or nome_bairro == '0':
                continue

            if nome_bairro not in cache_bairros:
                # Verifica se já existe no banco
                query_check = text("SELECT id FROM bairro WHERE nome = :nome")
                resposta = conexao.execute(query_check, {"nome": nome_bairro}).fetchone()

                if resposta:
                    bairro_id = resposta[0]
                else:
                    # Insere novo bairro
                    query_ins = text("INSERT INTO bairro (nome) VALUES (:nome) RETURNING id")
                    bairro_id = conexao.execute(query_ins, {"nome": nome_bairro}).fetchone()[0]
                
                cache_bairros[nome_bairro] = bairro_id
            else:
                bairro_id = cache_bairros[nome_bairro]

            # Inserção na tabela UBS
            conexao.execute(
                text("INSERT INTO ubs (nome, id_bairro) VALUES (:nome, :id_b)"),
                {"nome": nome_ubs, "id_b": bairro_id}
            )

            # Inserção na tabela Abastecimento de Água (Colunas 2 a 7 do arquivo)
            conexao.execute(
                text("""INSERT INTO abastecimento_agua (qnt_rede_encanada, qnt_poco, qnt_cisterna, qnt_carro_pipa, outro, nao_informado, id_bairro)
                        VALUES (:c2, :c3, :c4, :c5, :c6, :c7, :id_b)"""),
                {"c2": row[2], "c3": row[3], "c4": row[4], "c5": row[5], "c6": row[6], "c7": row[7], "id_b": bairro_id}
            )

            # Inserção na tabela Tratamento de Água (Colunas 9 a 14 do arquivo)
            conexao.execute(
                text("""INSERT INTO tratamento_agua (qnt_filtrada, qnt_fervida, qnt_clorada, qnt_mineral, qnt_sem_tratamento, qnt_nao_informado, id_bairro)
                        VALUES (:c9, :c10, :c11, :c12, :c13, :c14, :id_b)"""),
                {"c9": row[9], "c10": row[10], "c11": row[11], "c12": row[12], "c13": row[13], "c14": row[14], "id_b": bairro_id}
            )

            # Inserção na tabela Escoamento Banheiro (Colunas 16 a 22 do arquivo) 
            conexao.execute(
                text("""INSERT INTO escoamento_banheiro (qnt_fossa_septica, qnt_fossa_rudimentar, qnt_direto_rio, qnt_ceu_aberto, qnt_outra_forma, qnt_nao_informado, id_bairro)
                        VALUES (:c17, :c18, :c19, :c20, :c21, :c22, :id_b)"""),
                {"c17": row[17], "c18": row[18], "c19": row[19], "c20": row[20], "c21": row[21], "c22": row[22], "id_b": bairro_id}
            )

            # Inserção na tabela Destino Lixo (Colunas 24 a 28 do arquivo) 
            conexao.execute(
                text("""INSERT INTO destino_lixo (qnt_coletado, qnt_queimado, qnt_ceu_aberto, qnt_outra_forma, qnt_nao_informado, id_bairro)
                        VALUES (:c24, :c25, :c26, :c27, :c28, :id_b)"""),
                {"c24": row[24], "c25": row[25], "c26": row[26], "c27": row[27], "c28": row[28], "id_b": bairro_id}
            )

            # Inserção na tabela Renda Familiar (Colunas 30 a 37 do arquivo) 
            conexao.execute(
                text("""INSERT INTO renda_familiar (qnt_1_4_salario, qnt_1_2_salario, qnt_1_salario, qnt_2_salario, qnt_3_salario, qnt_4_salario, qnt_mais_4_salario, nao_informado, id_bairro)
                        VALUES (:c30, :c31, :c32, :c33, :c34, :c35, :c36, :c37, :id_b)"""),
                {"c30": row[30], "c31": row[31], "c32": row[32], "c33": row[33], "c34": row[34], "c35": row[35], "c36": row[36], "c37": row[37], "id_b": bairro_id}
            )

            # Inserção na tabela Perfil Educacional (Colunas 39 a 60 do arquivo) 
            conexao.execute(
                text("""INSERT INTO perfil_educacional (qnt_creche, qnt_pre_escola, qnt_classe_alfabetizacao, qnt_1_a_4_ano_fundamental, qnt_5_a_8_ano_fundamental, qnt_ensino_fundamental_completo, qnt_ensino_fundamental_especial, qnt_eja_1_a_4_ano, qnt_eja_5_a_8_ano, qnt_ensino_medio, qnt_ensino_medio_especial, qnt_medio_eja, qnt_superior, qnt_mobral, qnt_nenhum, qnt_nao_informado, id_bairro)
                        VALUES (:c39, :c40, :c41, :c43, :c44, :c45, :c47, :c49, :c50, :c51, :c52, :c54, :c55, :c58, :c59, :c60, :id_b)"""),
                {"c39": row[39], "c40": row[40], "c41": row[41], "c43": row[43], "c44": row[44], "c45": row[45], "c47": row[47], "c49": row[49], "c50": row[50], "c51": row[51], "c52": row[52], "c54": row[54], "c55": row[55], "c58": row[58], "c59": row[59], "c60": row[60], "id_b": bairro_id}
            )

            # Inserção na tabela População Masculina e Feminina (Colunas 62 e 63 do arquivo)
            conexao.execute(
                text("INSERT INTO populacao (qnt_masculina, qnt_feminina, id_bairro) VALUES (:masc, :fem, :id_b)"),
                {"masc": row[62], "fem": row[63], "id_b": bairro_id}
            )

    print("Dados carregados no banco de dados com sucesso")

processamento_etl('dados.csv')