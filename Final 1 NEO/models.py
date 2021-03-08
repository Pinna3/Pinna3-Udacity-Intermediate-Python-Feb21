from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    """A near-Earth object (NEO)."""
    def __init__(self, pdes, name=None, diameter='nan', hazardous=False, **info):
        """Create a new `NearEarthObject`."""
        self.designation = str(pdes)
        self.name = name
        self.diameter = float(diameter)
        self.hazardous = hazardous
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is None:
            return f'{self.designation}'
        else:
            return f'{self.designation} {self.name}'

    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous is True:
            haz = 'is'
        else:
            haz = 'is not'

        return f"""NEO {self.fullname} has a diameter of {self.diameter}km and {haz} potentially hazardous."""

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO."""

    def __init__(self, time=None, distance=0.0, velocity=0.0, neo=None, **info):
        """Create a new `CloseApproach`."""
        self._designation = ''
        self.time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float(distance)
        self.velocity = float(velocity)
        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"At {self.time_str}, '{self.neo.fullname}' approaches Earth at a distance of {self.distance} au and a velocity of {self.velocity} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    """A near-Earth object (NEO)."""
    def __init__(self, pdes, name=None, diameter='nan', hazardous=False, **info):
        """Create a new `NearEarthObject`."""
        self.designation = str(pdes)
        self.name = name
        self.diameter = float(diameter)
        self.hazardous = hazardous
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is None:
            return f'{self.designation}'
        else:
            return f'{self.designation} ({self.name})'

    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous is True:
            haz = 'is'
        else:
            haz = 'is not'

        return f"""NEO {self.fullname} has a diameter of {self.diameter}km and {haz} potentially hazardous."""

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO."""

    def __init__(self, time=None, distance=0.0, velocity=0.0, neo=None, **info):
        """Create a new `CloseApproach`."""
        self._designation = ''
        self.time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float(distance)
        self.velocity = float(velocity)
        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"At {self.time_str}, '{self.neo.fullname}' approaches Earth at a distance of {self.distance} au and a velocity of {self.velocity} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

# a = NearEarthObject(1111, name='Mike', diameter=32, hazardous=True, face='sexy', body='sexy')
# ca = CloseApproach(time='1900-Jan-01 00:00', distance=13.2, velocity=134.3, neo=a, appearence='nasty lookin', color='rainbow')
# print(a)
# print(ca)
