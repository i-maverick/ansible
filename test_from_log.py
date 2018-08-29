from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def parse(self, message):
        pass


class AtmParser(Parser):
    def parse(self, message):
        parsed_message = {}
        return parsed_message


class VisaParser(Parser):
    def parse(self, message):
        parsed_message = {}
        return parsed_message


class Validator(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def unique(self, _chain):
        pass

    @abstractmethod
    def valid(self, _chain):
        pass


class AtmValidator(Validator):
    def unique(self, _chain):
        return True

    def valid(self, _chain):
        return True


class VisaValidator(Validator):
    def unique(self, _chain):
        return True

    def valid(self, _chain):
        return True


def get_parser(proto):
    if proto == 'ATM':
        return AtmParser()
    elif proto == 'VISA':
        return VisaParser()
    else:
        raise NotImplementedError()


def get_validator(proto):
    if proto == 'ATM':
        return AtmValidator()
    elif proto == 'VISA':
        return VisaValidator()
    else:
        raise NotImplementedError()


def get_messages_from_db():
    return {}


def parse_message(proto, message):
    return get_parser(proto).parse(message)


def make_chains(_parsed_messages):
    return {}


def validate(_chain):
    validator = get_validator(chain.proto)
    if not validator.unique(chain):
        return False
    if not validator.valid(chain):
        return False
    return True


def create_test(_chain):
    pass


if __name__ == '__main__':
    messages = get_messages_from_db()
    parsed_messages = []

    for msg in messages:
        parsed = parse_message(msg.proto, msg)
        parsed_messages.append(parsed)

    chains = make_chains(parsed_messages)

    for chain in chains:
        if validate(chain):
            create_test(chain)
