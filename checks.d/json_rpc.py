import requests

from datadog_checks.base import AgentCheck

__version__ = "1.0.0"

class JsonRpcCheck(AgentCheck):
  def check(self, instance):
    rpc_address = instance['rpcaddress']
    self.gauge(
        "json_rpc.gas_price",
        _query_gas(rpc_address),
        tags=["chain:ethereum","metric_submission_type:gauge"],
    )


def _query_gas(rpc_address):
  headers = {
      # Already added when you pass json=
      # 'Content-Type': 'application/json',
  }

  json_data = {
      'jsonrpc': '2.0',
      'method': 'eth_gasPrice',
      'params': [],
      'id': 73,
  }

  response = requests.post(rpc_address, headers=headers, json=json_data)
  wei = int(response.json()["result"], 16)
  gwei = wei / 1000000000
  return gwei