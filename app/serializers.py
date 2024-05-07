def taxis_serializer(tuples_taxis):
    return [{"id": taxi[0], "plate": taxi[1]} for taxi in tuples_taxis]

def trajectories_serializer(tuples_trajectories):
    return [{"taxi_id": taxi_id[1], "date": taxi_id[2], "latitude": taxi_id[3], "longitude": taxi_id[4]} for taxi_id in tuples_trajectories]
