from enum import Enum
from dataclasses import dataclass


class SeasonsMonths(Enum):
    winter = ['december', 'january', 'february']
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']
    autumn = ['september', 'october', 'november']

    @classmethod
    @property
    def all_months(cls):
        all = list()
        #
        # for months in (months.value for months in cls):
        #     all.extend(months)
        # return all

        for i in map(all.extend, (months.value for months in cls)):
            pass
        return all

    @classmethod
    def get_season(cls, month):
        for season in cls:
            if month in season.value:
                return season.name


def get_user_month():
    month = input('Enter month: ').lower()
    if month in SeasonsMonths.all_months:
        return month
    return get_user_month()


if __name__ == '__main__':
    user_month = get_user_month()
    print(f'Season is {SeasonsMonths.get_season(user_month)}')