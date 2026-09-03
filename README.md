# Biblioteca_db - Aplicação com Banco de dados

Implementação do exemplo clássico da Biblioteca salvando os dados em um banco de dados *sqlite*.


As tabelas do projeto são:

**usuarios**(*id, nome*)  
**autores**(*id, nome*)  
**livros**(*id, titulos, autor_id, editora_id, ano_publicacao, edicao, disponivel*)  
**emprestimos**(*id, usuarios_id, data*)  
**editoras**(*id, nome*)  
**emprestimos_livros**(*emprestimo_id, livro_id, data_devolucao*)  