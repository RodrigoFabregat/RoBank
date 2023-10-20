class Transfer():
    def __init__(self, type=str, document=str, motive=float, amount=int, international=bool):
        self._type = type
        self._document = document
        self._motive = motive
        self._amount = amount
        self._international = international


class DepositInter():
    def __init__(self, type=str, document=str, motive=float, amount=int, international=bool, name=str, lastname=str, sex=str, birthdate=str, birthplace=str, terms=bool):
        self._type = type
        self._document = document
        self._motive = motive
        self._amount = amount
        self._international = international
        self._name = name
        self._lastname = lastname
        self._sex = sex
        self._birthdate = birthdate
        self._birthplace = birthplace
        self._terms = terms
