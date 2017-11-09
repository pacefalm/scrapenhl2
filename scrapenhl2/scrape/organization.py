"""
This module contains paths to folders.
"""

import os.path

class Organization(object):

    def __init__(self):
        self.organization_setup()

    def check_create_folder(self, *args):
        """
        A helper method to create a folder if it doesn't exist already

        :param args: list of str, the parts of the filepath. These are joined together with the base directory

        :return: nothing
        """
        path = os.path.join(self.get_base_dir(), *args)
        if not os.path.exists(path):
            os.makedirs(path)

    def get_base_dir(self):
        """
        Returns the base directory of this package (one directory up from this file)

        :return: str, the base directory
        """
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def get_raw_data_folder(self):
        """
        Returns the folder containing raw data

        :return: str, /scrape/data/raw/
        """
        return os.path.join(self.get_base_dir(), 'data', 'raw')

    def get_parsed_data_folder(self):
        """
        Returns the folder containing parsed data

        :return: str, /scrape/data/parsed/
        """
        return os.path.join(self.get_base_dir(), 'data', 'parsed')

    def get_team_data_folder(self):
        """
        Returns the folder containing team log data

        :return: str, /scrape/data/teams/
        """
        return os.path.join(self.get_base_dir(), 'data', 'teams')

    def get_other_data_folder(self):
        """
        Returns the folder containing other data

        :return: str, /scrape/data/other/
        """
        return os.path.join(self.get_base_dir(), 'data', 'other')

    def get_season_raw_pbp_folder(self, season):
        """
        Returns the folder containing raw pbp for given season

        :param season: int, current season

        :return: str, /scrape/data/raw/pbp/[season]/
        """
        return os.path.join(self.get_raw_data_folder(), 'pbp', str(season))

    def get_season_raw_toi_folder(self, season):
        """
        Returns the folder containing raw toi for given season

        :param season: int, current season

        :return: str, /scrape/data/raw/toi/[season]/
        """
        return os.path.join(self.get_raw_data_folder(), 'toi', str(season))

    def get_season_parsed_pbp_folder(self, season):
        """
        Returns the folder containing parsed pbp for given season

        :param season: int, current season

        :return: str, /scrape/data/parsed/pbp/[season]/
        """
        return os.path.join(self.get_parsed_data_folder(), 'pbp', str(season))

    def get_season_parsed_toi_folder(self, season):
        """
        Returns the folder containing parsed toi for given season

        :param season: int, current season

        :return: str, /scrape/data/raw/toi/[season]/
        """
        return os.path.join(self.get_parsed_data_folder(), 'toi', str(season))

    def get_season_team_pbp_folder(self, season):
        """
        Returns the folder containing team pbp logs for given season

        :param season: int, current season

        :return: str, /scrape/data/teams/pbp/[season]/
        """
        return os.path.join(self.get_team_data_folder(), 'pbp', str(season))

    def get_season_team_toi_folder(self, season):
        """
        Returns the folder containing team toi logs for given season

        :param season: int, current season

        :return: str, /scrape/data/teams/toi/[season]/
        """
        return os.path.join(self.get_team_data_folder(), 'toi', str(season))

    def organization_setup(self):
        """
        Creates other folder if need be

        :return: nothing
        """
        self.check_create_folder(self.get_other_data_folder())

