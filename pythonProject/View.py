'''
Д.з. № 2
П.2.
Абстрактный класс для вывода информации
'''

from abc import ABC, abstractmethod
from datetime import datetime as dt


class View(ABC):
    @abstractmethod
    def show_content(self):
        pass

    @abstractmethod
    def set_aligning(self, align):
        pass

    @abstractmethod
    def set_spaces_count(self, spaces):
        pass


class CommandsView(View):

    def __init__(self, command_list, align, spaces):
        self.commands = command_list
        self.align = align
        self.spaces = spaces

    def set_aligning(self, align):
        self.align = align

    def set_spaces_count(self, spaces):
        self.spaces = spaces

    def show_content(self):
        format_str = str('{:%s%d}' % (self.align, self.spaces))
        for command in self.commands:
            print(format_str.format(command))


class LogView(View):
    def __init__(self, message='', align='<', spaces=0):
        self.align = align
        self.spaces = spaces
        self.message = message

    def show_content(self):
        format_str = str('{:%s%d}' % (self.align, self.spaces))
        print(format_str.format(self.message))

    def set_aligning(self, align):
        self.align = align

    def set_spaces_count(self, spaces):
        self.spaces = spaces

    def set_message(self, message):
        self.message = message

    def log(self, action):
        current_time = dt.strftime(dt.now(), '%H:%M:%S')
        message = f'[{current_time}] {action}'
        self.set_message(message)
        self.show_content()
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')


class BookView(View):
    def __init__(self, account, align='<', spaces=0):
        self.align = align
        self.spaces = spaces
        self.account = account

    def show_content(self):
        if self.account['birthday']:
            birth = self.account['birthday'].strftime("%d/%m/%Y")
        result = "_" * self.spaces + "\n" + f"Name: {self.account['name']} \nPhones: {', '.join(self.account['phones'])} \nBirthday: {birth} \nEmail: {self.account['email']} \nStatus: {self.account['status']} \nNote: {self.account['note']}\n" + "_" * self.spaces
        print(result)

    def set_aligning(self, align):
        self.align = align

    def set_spaces_count(self, spaces):
        self.spaces = spaces

    def set_account(self, account):
        self.account = account
