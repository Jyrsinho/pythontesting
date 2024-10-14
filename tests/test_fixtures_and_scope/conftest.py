import csv
import os
import shutil

import pytest

from fixtures_and_scope.jokes import Joke


@pytest.fixture(scope="session")
def single_joke_csv_filepath():
    #a fixture that returns the path to a temporary csv file containing a single joke 
    # (the fixture may create the file or the file can be created in another fixture)
    
    #Luodaan directory juureen nimeltään tmp-test-resources
    tmp_test_resources = os.path.join(os.getcwd(), "tmp-test-resources")

    #Varmistetaan, että meidän directory on luotu
    os.makedirs(tmp_test_resources, exist_ok=True)
    
    #Luodaan csv - tiedosto
    temp_jokes_csv = os.path.join(tmp_test_resources, "temp_joke.csv")
    
    #Kirjoitetaan csv-tiedostoon yksi esimerkkivitsi
    with open(temp_jokes_csv, 'w', newline='') as jokes_file:
        writer = csv.writer(jokes_file)
        writer.writerow(["setup", "punchline"])
        writer.writerow(["Did you hear about the kidnapping at school?", "It’s fine, he woke up."])
    
    yield temp_jokes_csv
    shutil.rmtree(tmp_test_resources)


# single_joke — a fixture that returns the joke from the temporary single joke csv file
@pytest.fixture()
def single_joke(single_joke_csv_filepath):
    with open(single_joke_csv_filepath, 'r', newline='') as jokes_file:
        reader = csv.reader(jokes_file)
        contents = list(reader)

        return Joke(setup=contents[1][0], punchline=contents[1][1])


#jokes_csv_filepath — a fixture that returns the path to a temporary csv file containing multiple jokes 
# (the fixture may create the file or the file can be created in another fixture)
@pytest.fixture(scope="session")
def multiple_jokes_csv_filepath(single_joke_csv_filepath):
    # Käytetään tota aiemmin tehtyä directoryä.
    tmp_test_resources = os.path.dirname(single_joke_csv_filepath)

    # Create a new CSV file for multiple jokes in the same directory
    temp_jokes_csv = os.path.join(tmp_test_resources, "temp_multiple_jokes.csv")

    # Write multiple jokes to the CSV file
    with open(temp_jokes_csv, 'w', newline='') as jokes_file:
        writer = csv.writer(jokes_file)
        writer.writerow(["setup", "punchline"])
        writer.writerows([
            ["Why don’t skeletons fight each other?", "They don’t have the guts."],
            ["What do you call fake spaghetti?", "An impasta."],
            ["Why couldn’t the bicycle stand up by itself?", "It was two tired."],
            ["Did you hear about the kidnapping at school?", "It’s fine, he woke up."]
        ])

    yield temp_jokes_csv

    # yield palauttaa nyt ton väliaikaisen tiedoston ja single_joke_filepath_fixturen pitäis huolehtia 
    # ton resurssin pyyhkimisestä.

#jokes — a fixture that returns the jokes from the temporary jokes csv filev

@pytest.fixture()
def jokes(multiple_jokes_csv_filepath):
    with open(multiple_jokes_csv_filepath, 'r', newline='') as jokes_file:
        reader = csv.DictReader(jokes_file)
        jokes_list = [Joke(setup=row['setup'], punchline=row['punchline']) for row in reader]
        return jokes_list


    

