#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapenhl2.scrape.schedules import (
    _get_current_season,
    schedule_setup,
    _CURRENT_SEASON,
    _SCHEDULES,
)
from unittest.mock import call

def test_get_current_season(mocker):

    now_mock = mocker.patch("arrow.now")

    date_mock = now_mock.return_value
    date_mock.year = 2017
    date_mock.month = 8

    assert _get_current_season() == 2016
    date_mock.month = 9
    assert _get_current_season() == 2017
    date_mock.month = 10
    assert _get_current_season() == 2017


def test_schedule_setup(mocker):

    current_season_mock = mocker.patch(
        "scrapenhl2.scrape.schedules._get_current_season"
    )
    current_season_mock.return_value = 2006
    get_season_schedule_mock = mocker.patch(
        "scrapenhl2.scrape.schedules.get_season_schedule_filename"
    )
    get_season_schedule_mock.side_effect = ["tmp/2005", "tmp/2006"]
    path_exists_mock = mocker.patch(
        "os.path.exists"
    )
    path_exists_mock.side_effect = [True, False]
    gen_schedule_file_mock = mocker.patch(
        "scrapenhl2.scrape.schedules.generate_season_schedule_file"
    )
    season_schedule_mock = mocker.patch(
        "scrapenhl2.scrape.schedules._get_season_schedule"
    )

    schedule_setup()
    get_season_schedule_mock.assert_has_calls([call(2005), call(2006)])
    path_exists_mock.assert_has_calls(get_season_schedule_mock.return_value)
    gen_schedule_file_mock.assert_has_calls([call(2006)])
    season_schedule_mock.assert_has_calls([call(2005), call(2006)])



