import requests

from datadog_checks.base import AgentCheck

__version__ = "1.0.0"

class CoingeckoCheck(AgentCheck):
  def check(self, instance):
    coin = instance['coin']
    vs_currencies = instance['vs_currencies'].split(",")
    query_url = "https://api.coingecko.com/api/v3/simple/price?ids=" + coin + "&vs_currencies=" + "%2C".join(vs_currencies)
    response = requests.get(query_url)
    for currency, value in response.json()[coin].items():
        self.gauge(
            "coingecko.price." + coin,
            value,
            tags=["currency:"+currency,"metric_submission_type:gauge"],
        )

