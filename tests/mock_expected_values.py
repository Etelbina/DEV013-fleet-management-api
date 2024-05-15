import datetime

expected_taxis = [{'id': 21, 'plate': 'NNEL-8793'},
            {'id': 56, 'plate': 'JIMF-2287'},
            {'id': 71, 'plate': 'CLLD-1805'},
            {'id': 108, 'plate': 'LNGK-1108'},
            {'id': 165, 'plate': 'HKNN-8042'}]

expected_trajectories = [{'taxi_id': 6418, 'date': datetime.datetime(2008, 2, 2, 14, 25, 54), 'latitude': 116.3043, 'longitude': 39.9622},
                    {'taxi_id': 6418, 'date': datetime.datetime(2008, 2, 2, 14, 30, 55), 'latitude': 116.32259, 'longitude': 39.96596},
                    {'taxi_id': 6418, 'date': datetime.datetime(2008, 2, 2, 14, 32, 44), 'latitude': 116.34547, 'longitude': 39.96616}]


expected_latests = [{'taxi_id': 6598, 'plate': 'FHLB-7962', 'date': datetime.datetime(2008, 2, 8, 17, 37, 43), 'latitude': 116.32706, 'longitude': 39.84801},
                      {'taxi_id': 7088, 'plate': 'HDBL-4695', 'date': datetime.datetime(2008, 2, 8, 12, 14, 46), 'latitude': 117.11593, 'longitude': 40.1541},
                      {'taxi_id': 7249, 'plate': 'CNCJ-2997', 'date': datetime.datetime(2008, 2, 8, 17, 36, 33), 'latitude': 116.291, 'longitude': 39.88672}]