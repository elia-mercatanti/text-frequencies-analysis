import sys
import math
import pandas
from collections import Counter
import matplotlib.pyplot as plt


# Asks the text to the user for the analysis and returns it
def get_text():
    while True:
        text_file = input("Insert the name of the text file that you want to read: ")
        try:
            with open("texts/" + text_file, 'r') as my_file:
                text_string = my_file.read().replace('\n', '')
                break
        except FileNotFoundError:
            print("\nThe text file has not been found. The text file needs to be inside 'texts' directory.\n")
    return text_string


# Print the main menu and asks user input
def menu():
    while True:
        print("\n---- Text Frequencies Analysis ----\n")
        print("1) Histogram of the frequency of the 26 letters.")
        print("2) Empirical distribution of q-grams.")
        print("3) Index of coincidence and entropy of the q-grams distribution.")
        print("4) Quit.\n")
        try:
            choice = int(input("Select a function to run: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("\nYou must enter a number from 1 to 4\n")
        except ValueError:
            print("\nYou must enter a number from 1 to 4\n")


def plot_frequencies_hist(data):
    letter_counts = Counter(data)
    df = pandas.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar')
    plt.ylabel('Frequency')
    plt.title("Frequencies of the 26 letters")
    plt.xlabel('Letter')
    plt.savefig('plots/frequency_hist.pdf')
    plt.show()


# Ask the user the q parameter for the q-grams and returns it
def get_q():
    while True:
        try:
            q = int(input("\nInsert the parameter q for the q-grams: "))
            if 1 <= q:
                return q
            else:
                print("\nYou must enter a number q>=1.\n")
        except ValueError:
            print("\nYou must enter a number q>=1.\n")


# Generate all possible q-grams
def generate_q_grams(text, q):
    for i in range(len(text) - (q - 1)):
        yield text[i:i + q]


# Create and return the empirical distribution of all q-grams
def empirical_distribution(text, q):
    emp_dist = {}
    n = 0
    for q_gram in generate_q_grams(text, q):
        if q_gram in emp_dist:
            emp_dist[q_gram] = emp_dist[q_gram] + 1
            n = n + 1
        else:
            emp_dist[q_gram] = 1
            n = n + 1
    for q_gram in emp_dist:
        emp_dist[q_gram] = emp_dist[q_gram]/n

    return emp_dist


# Create and return the empirical distribution of q-grams
def index_of_coincidence(emp_dist):
    idx_confidence = 0
    for q_gram in emp_dist:
        idx_confidence = idx_confidence + emp_dist[q_gram]**2

    return idx_confidence


# Create and return the empirical distribution of q-grams
def entropy(emp_dist):
    dist_entropy = 0
    for q_gram in emp_dist:
        p = emp_dist[q_gram]
        dist_entropy = dist_entropy + p * math.log(p, 2)
    return -1 * dist_entropy


def main():
    # Asks the text to the user for the analysis
    text_string = get_text()

    emp_dist = None

    while True:
        # Ask the user what function wants to run
        choice = menu()

        if choice == 1:
            # Create a list of character form the text and then sort it
            data = list(text_string)
            data.sort()

            # Plot the bar plot of the frequencies
            plot_frequencies_hist(data)
            print("\nHistogram has been plotted and saved inside 'plots' directory.")
            input("\nPress Enter to continue.")
        elif choice == 2:
            # Ask the user the q parameter
            q = get_q()

            # Calculate the empirical distribution of q-grams
            emp_dist = empirical_distribution(text_string, q)

            print("\nEmpirical distribution of q-grams:\n", emp_dist)
            input("\nPress Enter to continue.")
        elif choice == 3:
            if emp_dist is not None:
                # Calculate the empirical distribution and entropy of the q-grams
                idx_confidence = index_of_coincidence(emp_dist)
                dist_entropy = entropy(emp_dist)

                print("\nIndex of coincidence of the q-grams distribution: ", idx_confidence)
                print("Entropy of the q-grams distribution: ", dist_entropy)
                input("\nPress Enter to continue.")
            else:
                print("\nBefore calculate the index of coincidence and entropy of the q-grams you must calculate the "
                      "empirical distribution of the q-grams.")
                input("\nPress Enter to continue.")
        elif choice == 4:
            sys.exit(0)


if __name__ == '__main__':
    main()
