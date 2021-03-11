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


        neo_desig = set()
        for neo in neos:
            if neo.designation != 'pdes':
                neo_desig.add(neo.designation)

        mapping = {}
        for pdes in neo_desig:
            if pdes[-1] not in mapping.keys():
                mapping[pdes[-1]] = [pdes]
            else:
                mapping[pdes[-1]].append(pdes)
        print(mapping.keys())

#         mapping = {}
#         for pdes in neo_desig:
#             for neo in neos:
#                 if neo.designation == pdes:
#                     mapping[pdes] = [neo]

#         for approach in approaches:
#             mapping[approach._designation].append(approach)

#         for val in mapping.values():
#             for obj in val[1:]:
#                 obj.neo = val[0]

#         for val in mapping.values():
#             for obj in val[1:]:
#                 val[0].approaches.append(obj)

#         manip_neos = []
#         for val in mapping.values():
#             manip_neos.append(val[0])

#         manip_approaches = []
#         for val in mapping.values():
#             for obj in val[1:]:
#                 manip_approaches.append(obj)

#         self._neos = tuple(manip_neos)
#         self._approaches = tuple(manip_approaches)


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

d = NEODatabase(load_neos(), load_approaches())
