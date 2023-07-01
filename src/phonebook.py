class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido' # correção de erro de digitação
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido' # correção de erro de digitação
        if '%' in name:
            return 'Nome invalido'

        if len(number) == 0:
            return 'Numero invalido' # correção de erro de digitação

        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'

        else: # validação em caso de nome duplicado
            return 'Nome duplicado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invalido' # correção de erro de digitação
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido' # correção de erro de digitação
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido' # correção de erro de digitação

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook sem registro'
        """
        self.entries = {}
        return 'phonebook sem registro' # melhoria na mensagem

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name: # bug - "not in" foi removido para que o usuário passado por parametro fosse localizado
                result.append({name, number})

        return result
    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        sorted_dict = dict(sorted(self.entries.items()))
        return sorted_dict  # bug: alteramos para retornar um dicionário ordenado

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        reversed_dict = dict(reversed(list(self.entries.items())))
        return reversed_dict

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        # melhoria: adicionamos uma validação para verificar se existe o nome antes de excluir
        if name not in self.entries:
            return 'Usuário não existente'
        else:
            self.entries.pop(name)
            return 'Numero deletado'

    def change_number(self, name, number):

        """
        Update number
        :param name: String with name
        :param number: String with number
        :return: 'Numero atualizado'
        """
        if name not in self.entries:
            return 'Usuário não existente'

        else:
            self.entries[name] = number
            return 'Numero atualizado'

    def get_name_by_number(self, number):

        value = {i for i in self.entries if self.entries[i] == number}
        return list(value)

