# API

## API Guidelines

[From data.gv.at, as of November 4th 2025](https://www.data.gv.at/datasets/522d3045-0b37-48d0-b868-57c99726b1c4)

"Die Abfrage der Echtzeitdaten der Wiener Linien unterliegt einem Fair Use-Prinzip
nach den folgenden Regeln: Es sind möglichst nur jene Haltepunkte abzufragen, welche
für eine persönliche Beauskunftung notwendig sind. Das Intervall der Abfragen sollte 15 Sekunden
nicht unterschreiten. Die Wiener Linien behalten sich vor,
bei Verstoß gegen diese Fair Use-Regeln die IP-Adresse zu blockieren."

English translation:

"The retrieval of real-time data from Wiener Linien is subject to a fair use principle
in accordance with the following rules: Where possible, only those stops that
are necessary for personal information should be queried.
The interval between queries should not be less than 15 seconds.
Wiener Linien reserves the right to block the IP address in the
event of a violation of these fair use rules."

TL;DR:

Only query stops that are necessary for your personal information.
Do not use a request interval below 15 seconds.
If you violate these rules, Wiener Linien can block your IP.

## Example request

<https://www.wienerlinien.at/ogd_realtime/monitor?stopId=4903&activateTrafficInfo=stoerunglang>

This request gets

- Departing subway trains from station "Rochusgasse" bound for "Ottakring" in the next 70 minutes
- Traffic Information (Delays, etc.)

## Answer

```json
    {"data":{
        "monitors":[
            {
                "locationStop":{
                    "type":"Feature",
                    "geometry":{
                        "type":"Point",
                        "coordinates":[
                            16.3916398,
                            48.2024522
                        ]
                    },
                    "properties":{
                        "name":"60201104",
                        "title":"Rochusgasse",
                        "municipality":"Wien",
                        "municipalityId":49000001,
                        "type":"stop",
                        "coordName":"WGS84",
                        "gate":"2",
                        "attributes":{
                            "rbl":4903
                        }
                    }
                },
                "lines":[
                    {
                        "name":"U3",
                        "towards":"Ottakring",
                        "direction":"R",
                        "platform":"2",
                        "richtungsId":"2",
                        "barrierFree":false,
                        "realtimeSupported":true,
                        "trafficjam":false,
                        "departures":{
                            "departure":[
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:23:30.000+0100",
                                        "countdown":4
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:28:30.000+0100",
                                        "countdown":9
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:33:30.000+0100",
                                        "countdown":14
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:38:30.000+0100",
                                        "countdown":19
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:43:30.000+0100",
                                        "countdown":24
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:50:00.000+0100",
                                        "countdown":31
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T20:57:30.000+0100",
                                        "countdown":38
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T21:05:00.000+0100",
                                        "countdown":46
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T21:12:30.000+0100",
                                        "countdown":53
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T21:20:00.000+0100",
                                        "countdown":61
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                },
                                {
                                    "departureTime":{
                                        "timePlanned":"2025-11-03T21:27:30.000+0100",
                                        "countdown":68
                                    },
                                    "vehicle":{
                                        "name":"U3",
                                        "towards":"Ottakring",
                                        "direction":"R",
                                        "platform":"2",
                                        "richtungsId":"2",
                                        "barrierFree":true,
                                        "foldingRamp":false,
                                        "realtimeSupported":true,
                                        "trafficjam":false,
                                        "type":"ptMetro",
                                        "attributes":{
                                            
                                        },
                                        "linienId":303
                                    }
                                }
                            ]
                        },
                        "type":"ptMetro",
                        "lineId":303
                    }
                ],
                "refTrafficInfoNames":[
                    "bms_I20251103-0028"
                ],
                "attributes":{
                    
                }
            }
        ],
        "trafficInfos":[
            {
                "refTrafficInfoCategoryId":2,
                "name":"bms_I20251103-0028",
                "priority":"1",
                "owner":"WL",
                "title":"U3: Rettungseinsatz",
                "description":"Die Linie U3 kann derzeit in beiden Richtungen nur unregelmäßig fahren. Grund dafür ist ein Rettungseinsatz im Bereich Herrengasse. ",
                "time":{
                    "start":"2025-11-03T17:00:00.000+0100",
                    "end":"2025-11-03T23:55:00.000+0100"
                },
                "attributes":{
                    "relatedLineTypes":{
                        "U3":"ptMetro"
                    }
                },
                "relatedLines":[
                    "U3"
                ],
                "relatedStops":[
                    4900,
                    4901,
                    4902,
                    4903,
                    4904,
                    4905,
                    4906,
                    4907,
                    4908,
                    4909,
                    4910,
                    4911,
                    4912,
                    4913,
                    4914,
                    4915,
                    4916,
                    4917,
                    4918,
                    4919,
                    4920,
                    4921,
                    4922,
                    4923,
                    4924,
                    4925,
                    4926,
                    4927,
                    4928,
                    4929,
                    4931,
                    4932,
                    4933,
                    4934,
                    4935,
                    4936,
                    4938,
                    4939,
                    4940,
                    4941
                ]
            }
        ],
        "trafficInfoCategories":[
            {
                "id":2,
                "refTrafficInfoCategoryGroupId":1,
                "name":"stoerunglang",
                "trafficInfoNameList":"bms_I20251103-0028",
                "title":"Störung Lang"
            }
        ],
        "trafficInfoCategoryGroups":[
            {
                "id":1,
                "name":"pt"
            }
        ]
    },
    "message":{
        "value":"OK",
        "messageCode":1,
        "serverTime":"2025-11-03T20:18:42.000+0100"
    }
}
```

## Error IDs

- *311*: DB not available
- *316*: Request limit reached
- *320*: GET Request parameter invalid
- *321*: GET Request parameter missing
- *322*: no Data in DB

## Commands

Start the backend:
```uvicorn main:app --reload```
