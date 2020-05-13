# vim: set ft=python enc=utf-8 fenc=utf-8 eol sw=0 sts=4 ts=4 ai si sta et:
import abc
import attr
import typing

# TODO: Move exception to decorator module.
# class ArgumentValidationError(Exception):
#    @enum.unique
#    class ArgumentType(enum.Enum):
#        POSITIONAL: str = 'positional'
#        KEYWORD: str = 'keyword'
#
#    def __init__(self, name: str, type_: ArgumentType):
#        super().__init__(f"Validation of {type_.value} argument '{name}' has failed")

# TODO: Add docstring to the class AND _exception, _display_message, _validate_argument.
@attr.s(repr=False, eq=False, order=False, slots=True, auto_attribs=True)
class Clause(abc.ABC):
    _negated: bool = False

    @property
    @abc.abstractmethod
    def _exception(self) -> Exception:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def _display_message(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def _validate_argument(self, value: typing.Any) -> bool:
        raise NotImplementedError

    def __call__(self, argument_value: typing.Any):
        if self._negated == self._validate_argument(argument_value):
            raise self._exception

    def __repr__(self) -> str:
        return f"<{'!' if self._negated else ''}{self._display_message}>"
