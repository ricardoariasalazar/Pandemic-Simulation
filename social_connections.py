"""
Created by: Ricardo Arias
Date of creation: May 20, 2020
Last modification: June 7, 2020
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name  # Set the input first name as the name of the Person
        self.last_name = last_name  # Set the input last name as the last name of the Person
        self.full_name = self.first_name + ' ' + self.last_name  # Set the full name (First name + ' ' + Last name)
        self.friends = []  # Set the empty list of the Person's friends

    def add_friend(self, friend_person):
        """
        Adds a new Person's friend to the list
        """
        self.friends.append(friend_person)

    def get_name(self):
        """
        Returns the full name of the Person
        """
        return self.full_name

    def get_friends(self):
        """
        Returns a list with the Person's friends
        """
        return self.friends

    def __repr__(self):
        """
        Print Person Class
        """
        return str(self.full_name)
        # https://stackoverflow.com/questions/12933964/printing-a-list-of-objects-of-user-defined-class


def load_people():
    """
    Reads the data from the file a2_sample_set.txt and load it in a list as a Person
    """
    sample_test = open('./data/dataset.txt', 'r')  # Variable that reads the file
    database = []  # Empty list to store all the records that were read

    for line in sample_test:  # For every line in the file
        first_name = (line.split(': ')[0]).split(' ')[0]  # Split text by ':' and then by ' ' to get the first name
        last_name = (line.split(': ')[0]).split(' ')[1]  # Split text by ':' and then by ' ' to get the last name
        person_to_load = Person(first_name, last_name)  # Create the Person Class with first_name and last_name

        for friend in (line.split(': ')[1]).split(', '):  # Split text by ':' and then by ', ' to get each friend
            person_to_load.add_friend(friend.strip())  # Add friends to the Person created

        database.append(person_to_load)  # Append each Person of the file in a list

    sample_test.close()  # Close the file with the information that were read
    return database


if __name__ == '__main__':
    for person in load_people():
        print(person.get_name(), person.get_friends())

# do not add code here (outside the main block).
