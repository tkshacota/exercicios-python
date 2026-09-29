# ==============================================================================
# PROJETO: Desafio PayPython - Função aplicar_desconto com 3 Métodos de Teste
# MÉTODOS ABORDADOS: 1. Assert (Asserções puras)
#                    2. Doctest (Testes dentro da documentação/docstring)
#                    3. Unittest (Testes unitários orientados a objetos)
# ==============================================================================

# Importamos o módulo doctest para ler e validar os exemplos dentro das docstrings
import doctest

# Importamos o módulo unittest para criar suítes de testes estruturadas com classes
import unittest


# ==============================================================================
# PARTE 1: A FUNÇÃO PRINCIPAL COM REGRA DE NEGÓCIO E DOCTEST
# ==============================================================================
def aplicar_desconto(total, percentual):
    """
    Calcula o valor final após aplicar um percentual de desconto sobre o valor total.

    Parâmetros:
        total (float): O valor monetário total inicial do produto/serviço.
        percentual (float): A porcentagem de desconto a ser aplicada (de 0 a 100).

    Retorna:
        float: O valor final já com o desconto subtraído.

    Regras de Negócio:
        - 10% de desconto em 100.00 resulta em 90.00.
        - 0% de desconto não altera o valor (retorna o próprio total).
        - Desconto não pode ser maior que 100% (dispara ValueError).

    Exemplos de testes com DOCTEST:
    (O doctest executa as linhas iniciadas com '>>>' e compara com a linha logo abaixo)

    >>> aplicar_desconto(100.0, 10)
    90.0

    >>> aplicar_desconto(100.0, 0)
    100.0

    >>> aplicar_desconto(100.0, 150)
    Traceback (most recent call last):
        ...
    ValueError: O desconto não pode ser maior que 100%
    """

    # REGRA DE VALIDAÇÃO:
    # Se o percentual informado for maior do que 100%, lançamos uma exceção (ValueError).
    # O comando 'raise' interrompe a execução imediatamente para impedir descontos abusivos.
    if percentual > 100:
        raise ValueError("O desconto não pode ser maior que 100%")

    # CÁLCULO MATEMÁTICO:
    # 1. Transformamos o percentual em fração decimal e multiplicamos pelo total para obter o valor do abatimento.
    desconto = total * (percentual / 100)

    # 2. Subtraímos o valor do abatimento do valor original e retornamos o preço final a ser pago.
    return total - desconto


# ==============================================================================
# PARTE 2: MÉTODO 1 - TESTES COM ASSERTIONS PURAS (assert)
# ==============================================================================
def testar_com_assert():
    """
    Função dedicada a testar a lógica usando o comando 'assert'.
    O 'assert' avalia se uma condição é True. Se for False, gera um erro de AssertionError.
    """

    # Teste 1: Caso clássico (10% de desconto em 100.00 deve ser igual a 90.00)
    assert aplicar_desconto(100.0, 10) == 90.0, "Erro: desconto de 10% deveria resultar em 90.0"

    # Teste 2: Caso de fronteira com 0% (o valor não pode mudar)
    assert aplicar_desconto(100.0, 0) == 100.0, "Erro: desconto de 0% não deve alterar o total"

    # Teste 3: Caso de exceção para percentual inválido (> 100%)
    # Como aplicar_desconto(100.0, 150) DEVE disparar um erro, usamos try/except:
    try:
        aplicar_desconto(100.0, 150)
        # Se a linha acima NÃO disparar erro, significa que a validação falhou,
        # então forçamos uma falha no teste com assert False:
        assert False, "Erro: Deveria ter lançado ValueError para desconto acima de 100%"
    except ValueError:
        # Se capturamos o ValueError, significa que o sistema funcionou como esperado!
        pass

    print("[1/3] ASSERTIONS: Todos os testes com assert passaram com sucesso!")


# ==============================================================================
# PARTE 3: MÉTODO 3 - TESTES COM UNITTEST
# ==============================================================================
class TestAplicarDesconto(unittest.TestCase):
    """
    Classe de teste unitário que herda de unittest.TestCase.
    O módulo unittest executa automaticamente todos os métodos iniciados por 'test_'.
    """

    def test_desconto_10_porcento(self):
        """Verifica se 10% de desconto em 100.00 resulta em 90.00."""
        # self.assertEqual(valor_obtido, valor_esperado) compara se ambos são estritamente iguais
        self.assertEqual(aplicar_desconto(100.0, 10), 90.0)

    def test_desconto_zero(self):
        """Verifica se 0% de desconto mantém o valor de 100.00 inalterado."""
        self.assertEqual(aplicar_desconto(100.0, 0), 100.0)

    def test_desconto_maior_que_100(self):
        """Verifica se valores acima de 100% levantam corretamente a exceção ValueError."""
        # O gerenciador de contexto 'with self.assertRaises(TipoDeErro)' garante
        # que o código dentro do bloco gere a exceção esperada.
        with self.assertRaises(ValueError):
            aplicar_desconto(100.0, 150)


# ==============================================================================
# PARTE 4: BLOCO DE EXECUÇÃO PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    # Garante que os testes só rodem quando este script for executado diretamente
    print("=" * 70)
    print("INICIANDO A BATERIA DE TESTES DO DESAFIO PAYPYTHON")
    print("=" * 70)

    # 1. Executa os testes usando assert
    testar_com_assert()

    print("\n" + "=" * 70)
    # 2. Executa os testes embutidos na documentação (doctest)
    # O parâmetro verbose=True detalha cada caso testado no terminal
    print("[2/3] DOCTEST: Executando testes da documentação:")
    doctest.testmod(verbose=True)

    print("\n" + "=" * 70)
    # 3. Executa a suíte de testes do unittest
    # O parâmetro exit=False evita que o unittest encerre o script prematuramente
    print("[3/3] UNITTEST: Executando testes formais do unittest:")
    unittest.main(exit=False)