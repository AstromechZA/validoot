from .exceptions import ValidationError


class And(object):

    def __init__(self, *clauses):
        for clause in clauses:
            if not callable(clause):
                raise TypeError('Argument {!r} is not callable'.format(clause))
        self.clauses = clauses

    def __call__(self, value):
        for clause in self.clauses:
            if clause(value) is not True:
                raise ValidationError(
                    'Value {!r} did not pass clause {!r}'.format(
                        value, clause))
        return True


class Or(object):

    def __init__(self, *clauses):
        for clause in clauses:
            if not callable(clause):
                raise TypeError('Argument {!r} is not callable'.format(clause))
        self.clauses = clauses

    def __call__(self, value):
        for clause in self.clauses:
            if clause(value) is True:
                return True
        raise ValidationError(
            'Value {!r} did not pass any clauses'.format(value))
