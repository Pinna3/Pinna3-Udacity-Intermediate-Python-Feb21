import json
import helper


def load_nobel_prizes(filename='prize.json'):
    return {}


def main(year, category):
    data = load_nobel_prizes()
    # Add more here!


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)
