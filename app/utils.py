def taxis_serializer(tuples_taxis):
    """
    This function transfotm the taxis tuple into a dictionary
    Returns:
        A dictionary of taxis
    """
    return [{"id": taxi[0], "plate": taxi[1]} for taxi in tuples_taxis]

def trajectories_serializer(tuples_trajectories):
    """
    This function transfotm the trajectories tuple into a dictionary
    Returns:
        A dictionary of trajectories
    """
    return [{"taxi_id": taxi_id[1], "date": taxi_id[2], "latitude": taxi_id[3], "longitude": taxi_id[4]} for taxi_id in tuples_trajectories]

def latest_serializer(tuple_latest):
    """
    This function transfotm the tatest trajectories tuple into a dictionary
    Returns:
        A dictionary of latest trajectories
    """
    return [{"taxi_id": taxi_id[3], "plate": taxi_id[1], "date": taxi_id[4], "latitude": taxi_id[5], "longitude": taxi_id[6]} for taxi_id in tuple_latest]