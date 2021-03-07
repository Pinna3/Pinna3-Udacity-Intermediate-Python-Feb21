import json
import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename, 'r') as filein:
        return json.load(filein)


def main(year=None, category=None):

    data = load_nobel_prizes()['prizes']

    def append_prizelist(index):
        prize_list =[]
        try:
            prize_list.append((data[index]['year'], data[index]['laureates'][0]['motivation']))
        except KeyError:
            prize_list.append((data[index]['year'], 'No prize given.'))
        [print(f'{prize_list[tuple][0]}: {prize_list[tuple][1]}') for tuple in range(len(prize_list))]

    if year != None and category == None:
        [append_prizelist(index) for index in range(len(data)) if data[index]['year'] == year]
    if year == None and category != None:
        [append_prizelist(index) for index in range(len(data)) if data[index]['category'] == category.lower()]
    if year != None and category != None:
        [append_prizelist(index) for index in range(len(data)) if data[index]['year'] == year and data[index]['category'] == category.lower()]


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)
