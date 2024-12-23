from data.session_metrics import get_session_metrics
import pandas as pd
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.dirname(current_folder)
data_folder = os.path.join(parent_folder, "data/raw")
sample_data = pd.read_csv(f"{data_folder}/train.csv", parse_dates=["timestamp_local"])


def test_get_session_metrics_1():
    df, user_id = sample_data.copy(deep=True), 179371
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                    179371,
                ],
                "session_id": [
                    159697,
                    324039,
                    547796,
                    629439,
                    1051346,
                    1055223,
                    1135988,
                    1427485,
                    1536166,
                    1583844,
                    1864199,
                    2237487,
                    2801202,
                    3008443,
                    3875303,
                    3928567,
                    4089464,
                    5047129,
                    5092772,
                    5097686,
                ],
                "total_session_time": [
                    0.0,
                    0.0,
                    0.0,
                    99.99,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
                "cart_addition_ratio": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_2():
    df, user_id = sample_data.copy(deep=True), 8287
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                    8287,
                ],
                "session_id": [
                    185012,
                    279302,
                    298726,
                    323810,
                    1583804,
                    1786356,
                    1812557,
                    2242336,
                    2854366,
                    2942009,
                    2978783,
                    3028792,
                    3564719,
                    3752200,
                    3799661,
                    3800621,
                    4173888,
                    4364573,
                    4560883,
                ],
                "total_session_time": [
                    122.25,
                    1912.75,
                    58.92,
                    86.83,
                    199.17,
                    173.03,
                    105.79,
                    242.41,
                    0.0,
                    1320.82,
                    176.38,
                    2.33,
                    217.39,
                    513.27,
                    111.01,
                    0.0,
                    75.43,
                    162.91,
                    108.53,
                ],
                "cart_addition_ratio": [
                    20.0,
                    0.0,
                    0.0,
                    25.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    18.18,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    20.0,
                ],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_3():
    df, user_id = sample_data.copy(deep=True), 388076
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                    388076,
                ],
                "session_id": [
                    952534,
                    1791061,
                    2760390,
                    2817197,
                    2981143,
                    2995219,
                    3122858,
                    3393956,
                    3507658,
                    3933722,
                    4323157,
                    4894975,
                    4932215,
                    5056866,
                ],
                "total_session_time": [
                    0.0,
                    9.14,
                    439.09,
                    7623.68,
                    229.07,
                    0.0,
                    175.62,
                    22.18,
                    205.7,
                    134.5,
                    9.99,
                    552.16,
                    50.22,
                    0.0,
                ],
                "cart_addition_ratio": [
                    0.0,
                    100.0,
                    0.0,
                    20.0,
                    0.0,
                    100.0,
                    0.0,
                    0.0,
                    33.33,
                    0.0,
                    0.0,
                    0.0,
                    20.0,
                    0.0,
                ],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_4():
    df, user_id = sample_data.copy(deep=True), 156824
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                    156824,
                ],
                "session_id": [
                    4365,
                    44428,
                    265145,
                    344039,
                    627113,
                    861996,
                    1399174,
                    1841861,
                    2216264,
                    2501641,
                    2725106,
                    3339112,
                    4389491,
                ],
                "total_session_time": [
                    21.26,
                    293.05,
                    0.0,
                    135.8,
                    17.12,
                    1623.28,
                    1593.79,
                    1198.6,
                    692.28,
                    2786.04,
                    2190.99,
                    1891.94,
                    0.0,
                ],
                "cart_addition_ratio": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    5.88,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_5():
    df, user_id = sample_data.copy(deep=True), 247419
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                    247419,
                ],
                "session_id": [
                    794416,
                    991254,
                    1478266,
                    1705082,
                    2497691,
                    2574803,
                    2904873,
                    3031363,
                    3067118,
                    3342906,
                    3588677,
                    5110860,
                ],
                "total_session_time": [
                    1693.3,
                    1674.62,
                    135.02,
                    219.83,
                    40.35,
                    0.0,
                    18.39,
                    578.76,
                    125.99,
                    25.12,
                    41.76,
                    1996.41,
                ],
                "cart_addition_ratio": [
                    60.0,
                    50.0,
                    42.11,
                    0.0,
                    20.0,
                    100.0,
                    50.0,
                    0.0,
                    66.67,
                    50.0,
                    85.71,
                    33.33,
                ],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_6():
    df, user_id = sample_data.copy(deep=True), 211084
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [211084],
                "session_id": [1614418],
                "total_session_time": [337.89],
                "cart_addition_ratio": [18.75],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_7():
    df, user_id = sample_data.copy(deep=True), 211101
    try:
        answer = get_session_metrics(df, user_id)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [211101],
                "session_id": [3331909],
                "total_session_time": [50.77],
                "cart_addition_ratio": [0.0],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed


def test_get_session_metrics_8():
    df, user_id = sample_data.copy(deep=True), 9999999
    try:
        answer = get_session_metrics(df, user_id)
        print(answer)
        if not isinstance(answer, pd.DataFrame):
            print("Returned Object is not a DataFrame")
            answer = pd.DataFrame()

        expected_answer = pd.DataFrame(
            {
                "user_id": [],
                "session_id": [],
                "total_session_time": [],
                "cart_addition_ratio": [],
            }
        )

        pd.testing.assert_frame_equal(
            answer, expected_answer, check_dtype=False, check_exact=False, rtol=0.1
        )

        test_passed = True
    except Exception as e:
        print(e)
        test_passed = False

    assert test_passed
