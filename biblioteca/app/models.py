from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.uf}"
    

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.cidade} ({self.site}) "
    

class Leitor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - Email: {self.email}; CPF: {self.cpf}"


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - Cidade: {self.cidade}; ({self.site}); "
    

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    preco = models.PositiveIntegerField()
    data_publicacao = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.nome} - {self.genero}, {self.data_publicacao} - {self.editora}, {self.autor}. Preço: {self.preco}; Disponibilidade: {self.status}"
    
    
class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data_emprestimo} - {self.data_devolucao} ({self.leitor} / {self.livro})"

