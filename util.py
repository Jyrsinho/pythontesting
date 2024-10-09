import csv


def from_csv_to_dict(filepath: str, read_until: int = -1) -> list[dict]:
    """
    Read a CSV file to a list of dictionaries.

    :param filepath: Path to the CSV file.
    :param read_until: Read only the first `read_until` rows.
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for i, row in enumerate(reader):
            if i == read_until:
                break
            data.append(row)

    return data
