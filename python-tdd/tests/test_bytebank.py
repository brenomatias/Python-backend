from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:

    def test_quando_instancia_recebe_nome(self):
        entrada = "Breno Matias"
        
        funcionario_teste = Funcionario(entrada, '23/02/2000', 1000)
        resultado = funcionario_teste.nome

        assert resultado

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho
    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"

        funcionario_teste = Funcionario(entrada, "13/04/2020", 1111)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado
    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "13/04/1990", entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100
        funcicionario_teste = Funcionario('Teste', "13/12/2000", entrada)
        resultado = funcicionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_excpetion(self):
        with pytest.raises(Exception):
            entrada = 100000

            funcionario_teste = Funcionario("teste", "13/10/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
        