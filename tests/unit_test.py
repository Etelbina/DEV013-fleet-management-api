from app.utils import taxis_serializer, trajectories_serializer, latest_serializer
from .mock_tuples import taxis_tuple, trajectories_tuple, latest_tuple
from .mock_expected_values import expected_taxis, expected_trajectories, expected_latests
import datetime

def test_taxis_ser():
    assert taxis_serializer(taxis_tuple) == expected_taxis

def test_trajectories_ser():
    assert trajectories_serializer(trajectories_tuple) == expected_trajectories

def test_latest_ser():
    assert latest_serializer(latest_tuple) == expected_latests