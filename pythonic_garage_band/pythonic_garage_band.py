from abc import ABC, abstractmethod

class Musician(ABC):
    """
    An abstract base class that represents a generic musician.
    """

    def __init__(self, name):
        """
        Initialize the Musician instance with a name.
        :param name(str): the musician's name.
        """
        self.name = name

    @abstractmethod
    def get_instrument(self):
        """
        Abstract method to get the musician's instrument.
        """
        pass

    @abstractmethod
    def play_solo(self):
        """
        Abstract method to play a solo.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the Musician.
        """
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        """
        Return a 'formal string' representation of the Musician.
        """
        return f"{self.__class__.__name__} instance. Name = {self.name}"


class Guitarist(Musician):
    """
    A class representing a guitarist.
    """

    def get_instrument(self):
        """
        Return the instrument of the guitarist.
        """
        return "guitar"

    def play_solo(self):
        """
        Return a string representing a guitar solo.
        """
        return "face melting guitar solo"


class Bassist(Musician):
    """
    A class representing a bassist.
    """

    def get_instrument(self):
        """
        Return the instrument of the bassist.
        """
        return "bass"

    def play_solo(self):
        """
        Return a string representing a bass solo.
        """
        return "bom bom buh bom"


class Drummer(Musician):
    """
    A class representing a drummer.
    """

    def get_instrument(self):
        """
        Return the instrument of the drummer.
        """
        return "drums"

    def play_solo(self):
        """
        Return a string representing a drum solo.
        """
        return "rattle boom crash"


class Band:
    """
    A class representing a band composed of musicians.
    """
    instances = []

    def __init__(self, name, members):
        """
        Initialize the Band instance with a name and list of members.
        :param name: A string representing the band's name.
        :param members: A list of Musician instances.
        """
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        """
        Return a list of solos played by each member of the band.
        """
        return [member.play_solo() for member in self.members]

    def __str__(self):
        """
        Return a string representation of the Band.
        """
        return f"The band {self.name}"

    def __repr__(self):
        """
        Return a formal string representation of the Band.
        """
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        """
        Class method to return a list of all created Band instances.
        """
        return cls.instances
