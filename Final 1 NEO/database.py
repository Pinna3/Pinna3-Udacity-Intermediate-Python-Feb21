from extract import*
from models import NearEarthObject, CloseApproach
import functools

"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches


        # TODO: What additional auxiliary data structures will be useful?


    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        for neo in self._neos:
            if neo.designation == designation.strip():
                for approach in self._approaches:
                    if approach._designation == designation.strip():
                        approach.neo = neo
                        neo.approaches.append(approach)
                return neo
        return None


    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        for neo in self._neos:
            if name != '' and name != None and neo.name == name:
                for approach in self._approaches:
                    if approach._designation == neo.designation:
                        approach.neo = neo
                        neo.approaches.append(approach)
                return neo
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        for approach in self._approaches:
            yield approach



def load():
    database = NEODatabase(load_neos(), load_approaches())
    return database
d = NEODatabase(load_neos(), load_approaches())

a = d._approaches #406785
set_desig = set()
for approach in a:
    set_desig.add(approach._designation)
print(sorted(set_desig)[0:10])
print(len(set_desig))
#set:
# ['100004', '100085', '100756', '100926', '10115', '10145', '10150', '10165', '101869', '101873']
# 23424
#list:
# ['100004', '100004', '100004', '100004', '100004', '100004', '100004', '100004', '100004', '100004']
# 406785

mapping = {}
for pdes in set_desig:
    for neo in d._neos:
        if neo.designation == pdes:
            mapping[pdes] = [neo]

# print(list(mapping.values())[0:10])
# # ['2017 RR15', '2012 YO1', '2019 LU1', '2018 BO5', '402267', '2019 XO2', '2019 QU2', '480883', '2009 UA', '2016 EU28']

for approach in d._approaches:
    mapping[approach._designation].append(approach)

# print(list(mapping.keys())[0:10])
# print(list(mapping.values())[0:10])

for val in mapping.values():
    for obj in val[1:]:
        obj.neo = val[0]

# print(mapping['10115'])
# print('')
# print('')
# print(mapping['101869'])

for val in mapping.values():
    for obj in val[1:]:
        val[0].approaches.append(obj)

print(mapping['10115'][0].__dict__)