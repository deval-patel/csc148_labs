from __future__ import annotations

from typing import Dict, List, Union

"""
PRA9103/PRA9104 Lab solution for:

Race Registry
=============

Context: a system for organizing a 5K running race.

When runners register for a race, they provide their name, email address and
their speed category. A speed category indicates how quickly they estimate that
they can finish the race. This allows organizers to start the runners in groups
of roughly equivalent running speed so that faster runners aren't stuck behind
slower runners. The possible speed categories are: under 20 minutes, under 30
minutes, under 40 minutes, and 40 minutes or over. We need to be able get a list
of runners in a given speed category. We also need to be able to look up a
runner to find their speed category. Finally, a runner should be able to change
their email address and speed category, or withdraw from the race entirely.

by Deval and Lance
"""


class Runner:
    """
    A runner.
    """
    _name: str
    _email: str
    _speed: int = 0

    def __init__(self, name: str, email: str, speed: int) -> None:
        self._name = name
        self._email = email
        self.set_speed(speed)

    def set_email(self, email: str) -> None:
        """
        Set's the email.

        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev._email
        'dontemailme@mail.com'
        >>> dev.set_email('newEmailWhoDis?')
        >>> dev._email
        'newEmailWhoDis?'
        """
        self._email = email

    def set_speed(self, speed: int) -> None:
        """
        Set's the speed.
        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev._speed
        20
        >>> dev.set_speed(69)
        >>> dev._speed
        69
        """
        if speed >= 0:
            self._speed = speed

    def get_email(self) -> str:
        """
        Returns the email.

        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev.get_email()
        'dontemailme@mail.com'
        """
        return self._email

    def get_name(self) -> str:
        """
        Returns the name.

        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev.get_name()
        'Deval'
        """
        return self._name

    def get_speed(self) -> int:
        """
        Returns the speed.

        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev.get_speed()
        20
        """
        return self._speed

    def __eq__(self, other: Runner) -> bool:
        """
        Checks if this runnner and the other runner are the same.

        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev
        Runner: (Deval, dontemailme@mail.com, 20)
        >>> dev2 = Runner('Deval', 'dontemailme@mail.com', 69)
        >>> dev2
        Runner: (Deval, dontemailme@mail.com, 69)
        >>> dev == dev2
        True
        >>> dev2.set_email('newEmailWhoDis?')
        >>> dev == dev2
        False

        """
        return self._name == other._name and self._email == other._email

    def __repr__(self) -> str:
        """
        Returns a representation of this runner.

        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> dev
        Runner: (Deval, dontemailme@mail.com, 20)
        """
        return f'Runner: ({self._name}, {self._email}, {self._speed})'


class Registry:
    """
    A race registry.

    >>> registry = Registry()
    >>> gerhard = Runner('Gerhard', 'loser', 35)
    >>> tom = Runner('Tom', 'loser1', 25)
    >>> toni = Runner('Toni', 'loser2', 15)
    >>> margot = Runner('Margot', 'loser3', 25)
    >>> registry.register(gerhard)
    >>> registry.register(tom)
    >>> registry.register(toni)
    >>> registry.register(margot)
    >>> registry.get_runners(30)
    [Runner: (Gerhard, loser, 35)]
    >>> gerhard.set_speed(25)
    >>> registry.register(gerhard)
    >>> registry.get_runners(30)
    []
    """
    runners: Dict[str, List[Runner]]

    def __init__(self) -> None:
        self.runners = {}

    def register(self, runner: Runner) -> None:
        """
        Registers this runner into the race registry.

        >>> registry = Registry()
        >>> registry.runners
        {}
        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> registry.register(dev)
        >>> registry.runners
        {'under 30 minutes': [Runner: (Deval, dontemailme@mail.com, 20)]}

        """
        # Get speed cat of this runner
        speed_cat = self.get_speed_category(runner)
        # Initialize the list for this speed cat if not already existing.
        self.runners.setdefault(speed_cat, [])
        # Finds and removes the runner from our dict, if they are in there.
        self.withdraw(runner)
        # Add the runner into their speed category.
        self.runners[speed_cat].append(runner)

    def withdraw(self, runner: Runner) -> Union[Runner, None]:
        """
        Withdraws this runner from this race registry.

        >>> registry = Registry()
        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> registry.register(dev)
        >>> registry.get_runners(25)
        [Runner: (Deval, dontemailme@mail.com, 20)]
        >>> registry.withdraw(dev)
        >>> registry.get_runners(25)
        []
        """
        # Loop through all speed cats in our dict
        for speed_cat in self.runners:
            # Remove the runner if they are in the list
            if runner in self.runners[speed_cat]:
                return self.runners[speed_cat].remove(runner)
        return None

    def get_runners(self, speed: int) -> List[Runner]:
        """
        Get all of the runners who fall under the speed category of this speed.

        >>> registry = Registry()
        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> registry.register(dev)
        >>> registry.get_runners(25)
        [Runner: (Deval, dontemailme@mail.com, 20)]
        """
        # Get speed category
        speed_cat = Registry.get_speed_mapping(speed)
        # Return the runners
        if speed_cat in self.runners:
            return self.runners[speed_cat]
        return []

    def get_speed_category(self, runner: Runner) -> str:
        """
        Get the speed category of this runner.

        >>> registry = Registry()
        >>> dev = Runner('Deval', 'dontemailme@mail.com', 20)
        >>> registry.register(dev)
        >>> registry.get_speed_category(dev)
        'under 30 minutes'
        """
        speed = runner.get_speed()
        return Registry.get_speed_mapping(speed)

    def get_speed_mapping(speed: int) -> str:
        """
        Gets the speed mapping of a given speed. 

        >>> Registry.get_speed_mapping(5)
        'under 20 minutes'
        >>> Registry.get_speed_mapping(25)
        'under 30 minutes'
        >>> Registry.get_speed_mapping(35)
        'under 40 minutes'
        >>> Registry.get_speed_mapping(40)
        '40 minutes or over'
        >>> Registry.get_speed_mapping(45)
        '40 minutes or over'
        >>> Registry.get_speed_mapping(-1)
        'under 0 minutes?!?!?!?!?!?!?!?!'
        """
        if speed < 0:
            return 'under 0 minutes?!?!?!?!?!?!?!?!'
        if speed < 20:
            return 'under 20 minutes'
        elif speed < 30:
            return 'under 30 minutes'
        elif speed < 40:
            return 'under 40 minutes'
        return '40 minutes or over'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
