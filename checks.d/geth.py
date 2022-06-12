import requests

from datadog_checks.base import AgentCheck

__version__ = "1.0.0"

class GethCheck(AgentCheck):
  def check(self, instance):
    metrics_endpoint = instance['metricsaddress']
    response = requests.get(metrics_endpoint)
    json_response = response.json()

    self.gauge(
        "geth.eth.db.chaindata.disk_read_mean",
        json_response["eth/db/chaindata/disk/read.mean"],
        tags=["metric_submission_type:rate"],
    )

    self.gauge(
        "geth.eth.db.chaindata.disk_write_mean",
        json_response["eth/db/chaindata/disk/write.mean"],
        tags=["metric_submission_type:rate"],
    )

    self.gauge(
        "geth.p2p.dials_count",
        json_response["p2p/dials.count"],
        tags=["metric_submission_type:count"],
    )

    self.gauge(
        "geth.p2p.dials_mean",
        json_response["p2p/dials.mean"],
        tags=["metric_submission_type:rate"],
    )

    self.gauge(
        "geth.p2p.egress_count",
        json_response["p2p/egress.count"],
        tags=["metric_submission_type:count"],
    )

    self.gauge(
        "geth.p2p.egress_mean",
        json_response["p2p/egress.mean"],
        tags=["metric_submission_type:rate"],
    )
    self.gauge(
        "geth.p2p.ingress_count",
        json_response["p2p/ingress.count"],
        tags=["metric_submission_type:count"],
    )

    self.gauge(
        "geth.p2p.ingress_mean",
        json_response["p2p/ingress.mean"],
        tags=["metric_submission_type:rate"],
    )