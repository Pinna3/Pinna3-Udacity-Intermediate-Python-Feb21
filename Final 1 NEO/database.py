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


        desig_map = {}
        for neo in neos:
            if neo.designation != 'pdes':
                if neo.designation[-3:] not in desig_map.keys():
                    desig_map[neo.designation[-3:]] = [neo]
                else:
                    desig_map[neo.designation[-3:]].append(neo)

        errors = []
        for approach in approaches:
                for obj in desig_map[approach._designation[-3:]]:
#                     print(obj.designation)
#                     print(approach._designation)
                    if obj.designation != approach._designation:
                        continue
                    approach.__dict__['neo'] = obj
                    obj.__dict__['approaches'].append(approach)

#                     else:
#                         errors.append(approach)

#         print(len(errors))
#         print(errors[5])


        print(list(desig_map.keys())[-10])
        print('')
        print(desig_map['484'][0].approaches)
        print('')



#         print(list(desig_map.values())[-1:][0][0]['210P']='hello!!!')
#         print('')


#             desig_map[approach._designation].append(approach)

#         for val in mapping.values():
#             for obj in val[1:]:
#                 obj.neo = val[0]

#         for val in mapping.values():
#             for obj in val[1:]:
#                 val[0].approaches.append(obj)

        manip_neos = []
        for val in desig_map.values():
            for item in val:
                manip_neos.append(item)


#         print(manip_neos[5])
#         print(len(manip_neos))
#         print(len(neos))


        manip_approaches = []
        for item in manip_neos:
            for obj in item.approaches:
                manip_approaches.append(item)

#         print(manip_approaches[5])
#         print(len(manip_approaches))
#         print(len(approaches))


        self._neos = tuple(manip_neos)
        self._approaches = tuple(manip_approaches)


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
