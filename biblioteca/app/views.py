from django.shortcuts import render
from . models  import *

def consulta_genero(request):
    consultas = {
        'consultas': Genero.objects.all()
    }

    return render(request,'consulta/genero.html',consultas)


def consulta_cidade(request):
    consultas = {
        'consultas': Cidade.objects.all()
    }

    return render(request,'consulta/cidade.html',consultas)


def consulta_editora(request):
    consultas = {
        'consultas': Editora.objects.all()
    }

    return render(request,'consulta/editora.html',consultas)


def consulta_leitor(request):
    consultas = {
        'consultas': Leitor.objects.all()
    }

    return render(request,'consulta/leitor.html',consultas)


def consulta_livro(request):
    consultas = {
        'consultas':Livro.objects.all()
    }

    return render(request,'consulta/livro.html',consultas)


def consulta_autor(request):
    consultas = {
        'consultas': Autor.objects.all()
    }

    return render(request,'consulta/autor.html',consultas)


def reserva(request):
    if request.POST:
        nova_reserva= Emprestimo()
        nova_reserva.data_emprestimo = request.POST.get('data')
        nova_reserva.data_devolucao = request.POST.get('data2')

        try:
            leitor = Leitor.objects.get(pk=request.POST.get('leitor'))
            livro = Livro.objects.get(pk=request.POST.get('livro'))
            nova_reserva.leitor = leitor
            nova_reserva.livro = livro
            nova_reserva.save() 
        except Leitor.DoesNotExist:
                print("Leitor não encontrado")
        except Livro.DoesNotExist:
                print("Livro não encontrado")
        except Exception as e:
                print("Erro de integridade:", e)

    reservas = {
        'leitores':Leitor.objects.all(),
        'livros':Livro.objects.all(),
    }
        
    return render(request,'reserva/reserva.html', reservas)