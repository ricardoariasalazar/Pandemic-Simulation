"""
Created by: Ricardo Arias
Date of creation: May 20, 2020
Last modification: June 4, 2020
"""

from virus_spread import *  # Import everything from module virus_spread (Patients and run_simulation)
import matplotlib.pyplot as plt  # Import a module to graph the simulations


def visual_curve(days, meeting_probability, patient_zero_health):
    """
    Graph the contagion curve with specific parameters of simulation
    """
    people_infected = run_simulation(days, meeting_probability, patient_zero_health)  # Run a simulation
    days_simulation = []  # Empty list to stored the number of days simulated

    count = 0
    for item in people_infected:  # For each value in people_infected list identify the day of the simulation
        count += 1
        days_simulation.append(count)

    plt.plot(days_simulation, people_infected)  # Line graph x = days of sim. and y = people infected
    plt.ylabel('People Infected')  # Label of y-xis
    plt.xlabel('Days')  # Label of x-xis
    plt.grid()  # Activate the grid
    name_png = 'Scenario C.png'  # Name of the image.png that shows the graph
    text = str(days) + ' days, ' + str(meeting_probability*100) + '% of meeting probability and ' + str(patient_zero_health) + ' points of health (patient zero)'
    plt.text(-5, max(people_infected) + 1, text)
    plt.title('Infection Curve')  # Title of the graph

    return plt.savefig(name_png)  # Return an images .png with the visualization of the simulation


if __name__ == '__main__':
    print(visual_curve(90, 0.18, 40))

'''
Do the results match the predictions? 

Yes, the predictions are consistent with the meeting probability. The greater this number, the more contagions will be 
and this can be seen in Scenario A where the infected curve grows rapidly until reaching the maximum number of infected 
people in a couple of days (22 days approx.). Meanwhile, in Scenario B where there are some restrictions, so there is a 
lower probability of being infected, the contagion curve does not grow as fast, so much so that in the 60 days (twice as
long as scenario A) only about half (approx.) of the people become infected. Finally, in Scenario C, with very high 
restrictions and a very low probability of encountering infections in a very long period (90 days), it remains constant 
over time and never exceeds 6 infected people at the time. This is why it can be seen that restriction measures work to 
prevent the spread of the virus among people.
'''
# do not add code here (outside the main block).
