"""
Created by: Ricardo Arias
Date of creation: May 24, 2020
Last modification: June 7, 2020
"""

from social_connections import *  # Import everything from module social_connections (Person and load_people)
import random                   # Import the function random


class Patient(Person):  # Patient Class inherits everything from Person Class
    def __init__(self, first_name, last_name, health):
        Person.__init__(self, first_name, last_name)
        self.health = health    # Add health to the __init__ method that was not in Person Class

    def get_health(self):
        """
        Returns the points of health of the Patient
        """
        return self.health

    def set_health(self, new_health):
        """
        Sets new points of health to the Patient
        """
        if 0 <= new_health <= 100:  # Check that the points of health are between 0 and 100
            self.health = new_health

    def is_contagious(self):
        """
        Check if the Patient is contagious
        """
        if round(self.health) < 50:
            return True
        else:
            return False

    def infect(self, viral_load):
        """
        Decrease the health of other people in the meeting due to the infection
        """
        if round(self.health) <= 29:    # If the health of the other people is lower than 29 points
            self.health -= (0.1 * viral_load)  # Their health decreases 10% of the viral load
        elif round(self.health) < 50:   # If the health of the other people is between 30 and 49 points
            self.health -= viral_load   # Their health decreases the viral load
        else:       # If the health of the other people is between higher or equal to 50 points
            self.health -= (2 * viral_load)  # Their health decreases 2 times the viral load

        if self.health < 0:     # Health can not be lower than 0
            self.health = 0

    def sleep(self):
        """
        The Patient sleeps at the end of the day and recovers 5 point of health
        """
        if self.health < 95:  # If that makes sure that health is not higher than 100 points
            self.health += 5
        else:
            self.health = 100


def run_simulation(days, meeting_probability, patient_zero_health):
    database = load_patients(75)                    # Load the data in the txt file into a list with the avg health
    database[0].set_health(patient_zero_health)     # The first Patient of the list has the patient_zero_health
    infections = []                                 # Empty list to store the number of people infected

    for day in range(days):  # Days of simulation
        for patient in database:  # Evaluate each Patient created in the database

            if round(patient.get_health()) < 50:  # Gets the initial health of the patient and find the viral load
                patient_viral_load = 5 + (((patient.get_health() - 25) ** 2) / 62)
            else:
                patient_viral_load = 0

            for item in patient.get_friends():   # Get each friend of the Patient for the meeting
                if random.random() <= meeting_probability:  # Probability of the Patient to meet each friend

                    for friend in database:
                        if item == friend.get_name():  # If that checks that the meeting it is not with himself
                            break

                    if round(friend.get_health()) < 50:  # Gets the initial health of the friend and find the viral load
                        friend_viral_load = 5 + (((friend.get_health() - 25) ** 2) / 62)
                    else:
                        friend_viral_load = 0

                    # Meeting of Patient and Friend, were each other is infected by the viral load of the other one
                    patient.infect(friend_viral_load)
                    friend.infect(patient_viral_load)

        people_infected = 0     # Restart the counting of people infected each day
        for patient in database:  # Evaluate each Patient
            if patient.is_contagious():     # If a Patient is contagious
                people_infected += 1        # Count him as people_infected this day

            patient.sleep()                 # At the end of the day each Patient in the database sleeps

        infections.append(people_infected)  # Save the record daily of people infected

    return infections       # Return the list of the people infected daily of the simulation


def load_patients(initial_health):
    """
    Reads the data from the file a2_sample_set.txt and load it in a list as a Patient
    """
    sample_test = open('./data/dataset.txt', 'r')  # Variable that reads the file
    database = []  # Empty list to store all the records that were read

    for line in sample_test:  # For every line in the file
        first_name = (line.split(': ')[0]).split(' ')[0]  # Split text by ':' and then by ' ' to get the first name
        last_name = (line.split(': ')[0]).split(' ')[1]  # Split text by ':' and then by ' ' to get the last name
        patient_to_load = Patient(first_name, last_name, initial_health)  # Create the Patient Class

        for friend in (line.split(': ')[1]).split(', '):  # Split text by ':' and then by ', ' to get each friend
            patient_to_load.add_friend(friend.strip())  # Add friends to the Patient created

        database.append(patient_to_load)  # Append each Patient of the file in a list

    sample_test.close()  # Close the file with the information that were read
    return database


if __name__ == '__main__':
    print(run_simulation(40, 1, 1))

# do not add code here (outside the main block).
