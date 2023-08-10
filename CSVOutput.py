import csv

# def add_headers(new_headers, data):
#     for i in range(len(headers)):
#         data[i].insert(0, headers[i])


def write_lists_to_csv(lists, output, new_headers):
    """
    :param lists: List of lists of strings
    :param output: name of the output file
    :param new_headers the headers of the csv file in a list
    :return:
    """
    with open(output, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_headers)
        for i in range(len(lists)):
            writer.writerow(lists[i])


# data to insert
headers = ['first name', 'last name', 'age']
data = [['John', 'Doe', '25'], ['Jane', 'Smith', '30'], ['Tome', 'Williams', '28']]
output_file = 'output.csv'

# running the functions

write_lists_to_csv(data, output_file, headers)
