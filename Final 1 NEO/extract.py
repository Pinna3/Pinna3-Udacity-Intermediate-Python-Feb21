"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file"""
    with open(neo_csv_path) as f:
        collection = []
        reader = csv.reader(f)
        for line in reader:
            try:
                collection.append(NearEarthObject(line[3], name=line[4], diameter=line[15], hazardous=line[7]))
            except ValueError:
                collection.append(NearEarthObject(line[3], name=line[4], diameter='nan', hazardous=line[7]))
        return tuple(collection)


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file."""
    with open(cad_json_path) as f:
        collection = []
        reader = json.load(f)
        for approach in reader['data']:
            collection.append(CloseApproach(approach[0], time=approach[3], distance=approach[4], velocity=approach[7], neo=None))
        return tuple(collection)
