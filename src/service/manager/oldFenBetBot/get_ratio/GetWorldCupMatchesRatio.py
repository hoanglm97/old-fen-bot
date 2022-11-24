from http import HTTPStatus
from src.service.constants.constants import BETS_API_TOKEN
import requests


class GetWorldCupMatchesRatio:
    @classmethod
    def __get_ratio(cls, api_key, sport, regions, markets, odds_format, date_format):
        return requests.get(
            f'https://api.the-odds-api.com/v4/sports/{sport}/odds',
            params={
                'api_key': api_key,
                'regions': regions,
                'markets': markets,
                'oddsFormat': odds_format,
                'dateFormat': date_format,
            }
        )

    def response_ratio(self):
        sport = 'soccer_fifa_world_cup'  # use the sport_key from the /sports endpoint below,

        regions = 'us'  # uk | us | eu | au. Multiple can be specified if comma delimited

        markets = 'totals'  # h2h | spreads | totals. Multiple can be specified if comma delimited

        odds_format = 'decimal'  # decimal | american

        date_format = 'iso'  # iso | unix
        response = self.__get_ratio(BETS_API_TOKEN, sport, regions, markets, odds_format, date_format)
        if not response or response.status_code != HTTPStatus.OK:
            return "something wrong"
        print(response.json())
        return ""
