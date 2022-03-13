import cmd
import importlib
import pynames
import shlex


class NameGen(cmd.Cmd):
    abstract_generators = ['FromTablesGenerator', 'FromListGenerator', 'FromCSVTablesGenerator']
    language = pynames.LANGUAGE.NATIVE
    prompt = '(NameGen) '

    def do_language(self, args):
        args = shlex.split(args)[0]
        if args == 'RU':
            self.language = pynames.LANGUAGE.RU
            print('Language is set to Russian.')
        elif args == 'EN':
            self.language = pynames.LANGUAGE.EN
            print('Language is set to English.')
        else:
            self.language = pynames.LANGUAGE.NATIVE
            print('Language is set to Native.')

    def do_generate(self, args):
        args = shlex.split(args)
        module = importlib.import_module(f'pynames.generators.{args[0].lower()}')
        if args[0] == 'elven' and len(args) > 1:
            generator = args[1] + 'NamesGenerator'
        elif args[0] == 'iron_kingdoms' and len(args) > 1:
            generator = args[1] + 'FullnameGenerator'
        else:
            generator = [gen for gen in dir(module) if gen.endswith('Generator') and gen not in self.abstract_generators][0]
        generator = getattr(module, generator)
        gender = pynames.GENDER.FEMALE if args[-1] == 'female' else pynames.GENDER.MALE
        try:
            name = generator().get_name_simple(gender=gender, language=self.language)
        except Exception as e:
            name = generator().get_name_simple(gender=gender)
        print(name)

    def do_info(self, args):
        args = shlex.split(args)
        module = importlib.import_module(f'pynames.generators.{args[0].lower()}')
        if args[0] == 'elven' and len(args) > 1:
            generator = args[1] + 'NamesGenerator'
        elif args[0] == 'iron_kingdoms' and len(args) > 1:
            generator = args[1] + 'FullnameGenerator'
        else:
            generator = [gen for gen in dir(module) if gen.endswith('Generator') and gen not in self.abstract_generators][0]
        generator = getattr(module, generator)
        if args[-1] == 'language':
            print(*sorted(generator().languages))
        elif args[-1] == 'male':
            print(generator().get_names_number(pynames.GENDER.MALE))
        elif args[-1] == 'female':
            print(generator().get_names_number(pynames.GENDER.FEMALE))
        else:
            print(generator().get_names_number())


NameGen().cmdloop()