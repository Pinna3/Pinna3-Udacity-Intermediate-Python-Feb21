# I was unable to complete b/c routes.dat file contains incofrect info... this is an error in
# Udacity's filesystem that makes it impossible to complete project, moving on disgruntled. I
# followed along with the instructor's solution and wrote the program alongside him anyway for learning
# purposes but the filesystem was broken at the time I came to the project.

import csv
import json

import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines
#{'GNL': '135 Airways', 'RNX': '1Time Airline', ...}


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports
# {'CGY': 'Laguindingan Airport', 'CPO': 'Desierto de Atacama Airport'}


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            source, dest = line[2], line[4]
            if source not in routs:
                routes[source] = []
            routes[source].append(dest)
    return routes


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    frontier = {source}
    seen = {source: {(source, )}}
    for steps in range(max_segments):
        next_frontier = set()
        for airport in frontier:
            for target in routes.get(airport, ()):
                if target not in seen:
                    next_frontier.add(target)
                    seen[target] = set()
                for path in seen[airport]:
                    if len(path) != steps + 1:
                        continue
                    seen[target].add(path + (target, ))
        frontier = next_frontier
    return seen[dest]


def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    for path in paths:
        segments = len(path) - 1
        if segments not in output:
            output[segments] = []
        output[segments].append(rename_path(path, airports))

    with open(f'{source}->{dest} (max {max_segments}).json', 'w') as f:
        json.dump(output, f, indent=2, sort_keys=True)
        

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
