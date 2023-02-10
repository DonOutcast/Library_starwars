class IncorrectNames:

    def __int__(self, name_for_check: str) -> None:
        self.name_for_check = name_for_check
        self.correction_name = self.__correction()

    def __correction(self) -> str:
        """
        This function correct a name for searchin if is it incorrect
        :return: Name
        :type: :obj: `str`
        """
        return self.__name_to_correct().get(self.name_for_check, self.name_for_check)

    def __name_to_correct(self) -> dict[str: str]:
        """
        This function return a dictionary with all names to correct
        :return: Incorrect name with correct
        :type: :obj: `dict[str: str]`
        """
        return {
            "Sand Crawler": "Sandcrawler"
        }

    def get_name(self) -> str:
        """
        This function return a correction nem
        :return: Name
        :type: :obj: `str`
        """
        return self.correction_name
