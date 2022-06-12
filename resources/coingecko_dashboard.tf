resource "datadog_dashboard_json" "dashboard_json" {
  dashboard = <<EOF
{
   "title":"Coingecko Overview",
   "description":"## Title\n\nExample Dashboard for Coingecko price tracking.",
   "widgets":[
      {
         "id":8205235951385655,
         "definition":{
            "title":"Ethereum Price",
            "title_size":"16",
            "title_align":"left",
            "show_legend":false,
            "legend_layout":"auto",
            "legend_columns":[
               "avg",
               "min",
               "max",
               "value",
               "sum"
            ],
            "time":{
               
            },
            "type":"timeseries",
            "requests":[
               {
                  "formulas":[
                     {
                        "formula":"query1"
                     },
                     {
                        "formula":"query2"
                     }
                  ],
                  "response_format":"timeseries",
                  "queries":[
                     {
                        "query":"avg:coingecko.price.ethereum{currency:usd}",
                        "data_source":"metrics",
                        "name":"query1"
                     },
                     {
                        "query":"avg:coingecko.price.ethereum{currency:eur}",
                        "data_source":"metrics",
                        "name":"query2"
                     }
                  ],
                  "style":{
                     "palette":"dog_classic",
                     "line_type":"solid",
                     "line_width":"normal"
                  },
                  "display_type":"line"
               }
            ],
            "yaxis":{
               "include_zero":false
            }
         },
         "layout":{
            "x":0,
            "y":0,
            "width":4,
            "height":4
         }
      }
   ],
   "template_variables":[
      
   ],
   "layout_type":"ordered",
   "is_read_only":false,
   "notify_list":[
      
   ],
   "reflow_type":"fixed",
   "id":"hxt-zh5-akn"
}
EOF
}