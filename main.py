class Material:

  def __init__(self, titulo, autor_ou_editora):
      self.titulo = titulo
      self.autor_ou_editora = autor_ou_editora

  def exibir_informacoes(self):
      print(f"Título: {self.titulo}")
      print(f"Autor/Editora: {self.autor_ou_editora}")

class Livro(Material):

  def __init__(self, titulo, autor_ou_editora, genero):
      super().__init__(titulo, autor_ou_editora)
      self.genero = genero

  def exibir_informacoes(self):
      super().exibir_informacoes()
      print(f"Gênero: {self.genero}")

class Revista(Material):

  def __init__(self, titulo, autor_ou_editora, edicao):
      super().__init__(titulo, autor_ou_editora)
      self.edicao = edicao

  def exibir_informacoes(self):
      super().exibir_informacoes()
      print(f"Edição: {self.edicao}")

# Cria um objeto da classe Livro
livro = Livro("Dom Casmurro", "Machado de Assis", "Romance")
print("Detalhes do Livro:")
livro.exibir_informacoes()

# Cria um objeto da classe Revista
revista = Revista("National Geographic", "National Geographic Society", "Novembro 2023")
print("\nDetalhes da Revista:")
revista.exibir_informacoes()
