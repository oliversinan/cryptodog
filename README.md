# Cryptodog
This repository contains custom Agent checks for monitoring information relating to blockchain/web3/cryptographic assets.

# Setup
## Installing the checks
Utilize the `setup.sh` cript to copy the check to the repective destinations - you need to set the rootpath of your Datadog agent directory.
```
sudo ./setup.sh -d /etc/datadog-agent/
# Restart the agent to apply changes
sudo service datadog-agent restart
```
## Deploying Datadog Resources
This repository comes with predefined Datadog resources to monitor the different checks. Rollout requires Terraform.
```
export TF_VAR_datadog_api_key="<Your-API-Key>"
export TF_VAR_datadog_app_key="<Your-App-Key>"
cd ./resources
terraform init
terraform apply
```

### coingecko.d
Queries Coingecko's API for the latest price of a coin. API Limit of 50 queries per minute

TODO: 
* Extend config to array for querying multiple coins
* Change default interval

### geth.d
Monitor geth client metrics. Example line to start client with metric server, logs and rpc endpoint (for json_rpc when run locally).
```
geth --syncmode light --http --metrics --metrics.addr 127.0.0.1 --log.json 2> ~/logs/geth/log.json
```

TODO:
* Cover more metrics
* Add explanations of metrics to dashboard

### json_rpc.d
Queries a RPC Endpoint for latest value.

TODO:
* Extend to include ABI encoding to e.g. query ERC20 contract balances

## Other Ideas
### defillama.d
