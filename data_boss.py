import pandas as pd


class DataBoss:
    """
    Class that acts as the "boss of the data"
    """
    def __init__(self):
        """
        Initializes the file to log data into
        """

        self.file = pd.read_csv("Blackjack_data.csv")

    def write_result(self, results: []):
        """
        Writes the result of a game of blackjack into the csv file
        :param results: List the contains the results. First item: 0 if the dealer wins, 1 if the player wins, 2 if it
        is a push, 10 otherwise. Second item: Numbered specific scenarios for data collection
        :return: None
        """
        if results[0] == 1:
            self.file.loc[0, "Wins"] = str(int(self.file.loc[0, "Wins"]) + 1)
            self.write_win(self.file, results[1])
        elif results[0] == 0:
            self.file.loc[0, "Losses"] = str(int(self.file.loc[0, "Losses"]) + 1)
            self.write_loss(self.file, results[1])
        elif results[0] == 2:
            self.file.loc[0, "Pushes"] = str(int(self.file.loc[0, "Pushes"]) + 1)
            self.write_push(self.file, results[1])

        self.file.loc[8, "Wins"] = str(int(self.file.loc[8, "Wins"]) + 1)

        self.file.to_csv("Blackjack_data.csv", index=False)

    def write_win(self, file, result: int):
        """
        Writes in specific win scenario
        :param file: CSV file writing to
        :param result: Scenario number
        :return: None
        """
        if result == 0:
            file.loc[1, "Wins"] = str(int(file.loc[1, "Wins"]) + 1)
        elif result == 11:
            file.loc[2, "Wins"] = str(int(file.loc[2, "Wins"]) + 1)
        elif result == 15:
            file.loc[3, "Wins"] = str(int(file.loc[4, "Wins"]) + 1)
        elif result == 16:
            file.loc[4, "Wins"] = str(int(file.loc[5, "Wins"]) + 1)

    def write_loss(self, file, result: int):
        """
        Writes in specific loss scenario
        :param file: CSV file writing to
        :param result: Scenario number
        :return: None
        """
        if result == 12:
            file.loc[1, "Losses"] = str(int(file.loc[1, "Losses"]) + 1)
        elif result == 1:
            file.loc[2, "Losses"] = str(int(file.loc[2, "Losses"]) + 1)
        elif result == 2:
            file.loc[3, "Losses"] = str(int(file.loc[3, "Losses"]) + 1)
        elif result == 6:
            file.loc[4, "Losses"] = str(int(file.loc[4, "Losses"]) + 1)
        elif result == 4:
            file.loc[5, "Losses"] = str(int(file.loc[5, "Losses"]) + 1)
        elif result == 5:
            file.loc[6, "Losses"] = str(int(file.loc[6, "Losses"]) + 1)
        elif result == 18:
            file.loc[7, "Losses"] = str(int(file.loc[7, "Losses"]) + 1)

    def write_push(self, file, result: int):
        """
        Writes in specific push scenario
        :param file: CSV file writing to
        :param result: Scenario number
        :return: None
        """
        if result == 3:
            file.loc[1, "Pushes"] = str(int(file.loc[1, "Pushes"]) + 1)
        elif result == 10:
            file.loc[2, "Losses"] = str(int(file.loc[2, "Losses"]) + 1)
        elif result == 13:
            file.loc[3, "Losses"] = str(int(file.loc[3, "Losses"]) + 1)
        elif result == 9:
            file.loc[4, "Losses"] = str(int(file.loc[4, "Losses"]) + 1)
        elif result == 7:
            file.loc[5, "Losses"] = str(int(file.loc[5, "Losses"]) + 1)
        elif result == 8:
            file.loc[6, "Losses"] = str(int(file.loc[6, "Losses"]) + 1)

    def print_file(self):
        """
        Prints the data file
        :return: None
        """
        print("")
        print(self.file)
        print("")
