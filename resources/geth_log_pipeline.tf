resource "datadog_logs_custom_pipeline" "geth_log_pipeline" {
  filter {
    query = "source:geth"
  }
  name       = "geth"
  is_enabled = true
  processor {
    status_remapper {
      sources    = ["lvl"]
      name       = "Remap Status Attribute lvl"
      is_enabled = true
    }
  }
}