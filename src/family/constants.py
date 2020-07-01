from enum import Enum, auto


class Sex(Enum):
    """
    Sex enumeration for the person.
    values are male or female.
    """
    Male = auto()
    Female = auto()


class RelationShip(Enum):
    """
    class represent constants providing relationships details for the family.
    """
    PATERNAL_UNCLE = auto()
    MATERNAL_UNCLE = auto()
    PATERNAL_AUNT = auto()
    MATERNAL_AUNT = auto()
    SISTER_IN_LAW = auto()
    BROTHER_IN_LAW = auto()
    SON = auto()
    DAUGHTER = auto()
    SIBLINGS = auto()


class Message(Enum):
    """
    class represent constants providing relationships details for the family.
    """
    NOT_YET_IMPLEMENTED = "NOT_YET_IMPLEMENTED"
    PERSON_NOT_FOUND = "PERSON_NOT_FOUND"
    PROVIDE_VALID_RELATION = "PROVIDE_VALID_RELATION"
    CHILD_ADDITION_FAILED = "CHILD_ADDITION_FAILED"
    CHILD_ADDITION_SUCCEEDED = "CHILD_ADDITION_SUCCEEDED "
    NONE = "NONE"
    INVALID_COMMAND = "INVALID_COMMAND"


class Commands(Enum):
    """
    This constants represent the commands supported.
    """
    INVALID_COMMAND = "INVALID_COMMAND"
    ADD_CHILD = "ADD_CHILD"
    ADD_FAMILY_HEAD = "ADD_FAMILY_HEAD"
    ADD_SPOUSE = "ADD_SPOUSE"
