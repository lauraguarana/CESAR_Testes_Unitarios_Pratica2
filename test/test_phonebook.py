from src.phonebook import Phonebook
from unittest import TestCase

class TestPhonebook(TestCase):

    def test_add(self):
        # Setup
        name = "Laura"
        number = "999998888"
        resultado_esperado = "Numero adicionado"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_duplicado(self):
        # Setup
        name = "Beatriz"
        number = "999998888"
        resultado_esperado = "Nome duplicado"

        phonebook = Phonebook()
        phonebook.add(name=name, number=number)

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_invalido_cerquilha(self):
        # Setup
        name = "#"
        number = "999998888"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_invalido_arroba(self):
        # Setup
        name = "@"
        number = "999998888"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_invalido_exclamacao(self):
        # Setup
        name = "!"
        number = "999998888"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_invalido_cifrao(self):
        # Setup
        name = "$"
        number = "999998888"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_invalido_porcentagem(self):
        # Setup
        name = "%"
        number = "999998888"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_numero_vazio(self):
        # Setup
        name = "Amanda"
        number = ""
        resultado_esperado = "Numero invalido"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup(self):
        # Setup
        name = "Laura"
        resultado_esperado = "123456789"

        phonebook = Phonebook()
        phonebook.add(name=name, number="123456789")

        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_name_cerquilha(self):
        # Setup
        name = "#"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        #Chamada
        resultado = phonebook.lookup(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_name_arroba(self):
        # Setup
        name = "@"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        #Chamada
        resultado = phonebook.lookup(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_name_exclamacao(self):
        # Setup
        name = "!"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        #Chamada
        resultado = phonebook.lookup(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_name_cifrao(self):
        # Setup
        name = "$"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        #Chamada
        resultado = phonebook.lookup(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_name_porcentagem(self):
        # Setup
        name = "%"
        resultado_esperado = "Nome invalido"

        phonebook = Phonebook()

        #Chamada
        resultado = phonebook.lookup(name=name)

        #Avaliacao
        assert resultado_esperado == resultado

    def test_getNames(self):
        # Setup
        resultado_esperado = ["POLICIA", "Laura", "Amanda"]

        phonebook = Phonebook()
        phonebook.add(name="Laura", number="123456789")
        phonebook.add(name="Amanda", number="987654321")

        # Chamada
        resultado = phonebook.get_names()

        # Avaliacao
        self.assertListEqual(resultado_esperado, resultado)

    def test_getNumbers(self):
        # Setup
        resultado_esperado = ["190", "123456789", "987654321"]

        phonebook = Phonebook()
        phonebook.add(name="Laura", number="123456789")
        phonebook.add(name="Amanda", number="987654321")

        # Chamada
        resultado = phonebook.get_numbers()

        # Avaliacao
        self.assertListEqual(resultado_esperado, resultado)

    def test_clear(self):
        # Setup
        resultado_esperado = "phonebook sem registro"

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.clear()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_search(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add(name="Laura", number="123456789")

        resultado_esperado = [{"123456789", "Laura"}]

        # Chamada
        resultado = phonebook.search(search_name="Laura")

        # Avaliacao
        self.assertListEqual(resultado_esperado, resultado)

    def test_search_invalido(self):
        # Setup
        phonebook = Phonebook()
        name = "Laura"
        phonebook.add(name=name, number="123456789")

        resultado_esperado = []

        # Chamada
        resultado = phonebook.search(search_name="Amanda")

        # Avaliacao
        self.assertListEqual(resultado_esperado, resultado)

    def test_getPhoneSorted(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add(name="Laura", number="123456789")
        phonebook.add(name="Amanda", number="987654321")

        resultado_esperado = {"Amanda": "987654321", "Laura": "123456789", "POLICIA": "190"}

        # Chamada
        resultado = phonebook.get_phonebook_sorted()

        # Avaliacao
        self.assertDictEqual(resultado_esperado, resultado)

    def test_getPhoneReverse(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add(name="Laura", number="123456789")
        phonebook.add(name="Amanda", number="987654321")

        resultado_esperado = {"POLICIA": "190", "Laura": "123456789", "Amanda": "987654321"}

        # Chamada
        resultado = phonebook.get_phonebook_reverse()

        # Avaliacao
        self.assertDictEqual(resultado_esperado, resultado)

    def test_delete(self):
        # Setup
        phonebook = Phonebook()
        name = "Laura"
        phonebook.add(name=name, number="123456789")

        resultado_esperado = "Numero deletado"

        # Chamada
        resultado = phonebook.delete(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_invalido(self):
        # Setup
        phonebook = Phonebook()
        name = "Laura"
        phonebook.add(name=name, number="123456789")

        resultado_esperado = "Usuário não existente"

        # Chamada
        resultado = phonebook.delete(name="Amanda")

        # Avaliacao
        assert resultado_esperado == resultado

    def test_change_number(self):
        # Setup
        name = "Amanda"
        number = "999999888"
        resultado_esperado = "Numero atualizado"
        phonebook = Phonebook()

        phonebook.add(name=name, number=number)

        # Chamada
        resultado = phonebook.change_number(name=name, number="964015555")

        # Avaliacao
        assert resultado_esperado == resultado

    def test_change_number_nao_existente(self):
        # Setup
        name = "Amanda"
        number = "999999888"
        resultado_esperado = "Usuário não existente"

        phonebook = Phonebook()
        phonebook.add(name=name, number=number)

        # Chamada
        resultado = phonebook.change_number(name="Beatriz", number="964015555")

        # Avaliacao
        assert resultado_esperado == resultado

    def test_getNameByNumber(self):
        # Setup
        number = "999999888"
        resultado_esperado = ["Amanda"]

        phonebook = Phonebook()
        phonebook.add(name="Amanda", number=number)

        # Chamada
        resultado = phonebook.get_name_by_number(number=number)

        # Avaliacao
        self.assertListEqual(resultado_esperado, resultado)












