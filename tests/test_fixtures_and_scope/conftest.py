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
    temp_jokes_csv = os.path.join(tmp_test_resources, "temp_jokes.csv")
    
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

