from __future__ import annotations
import pytest
from klarda.apis import KlardaAPICollection
from klarda import types


@pytest.mark.webtest
def test_get_token_list(client: KlardaAPICollection) -> None:
    token_list = client.get_token_list(
        params=types.GetTokenListRequest()
    )
    assert token_list
    assert len(token_list['result']) > 0

@pytest.mark.webtest
def test_get_new_token_list(client: KlardaAPICollection) -> None:
    token_list = client.get_new_token_list(
        params=types.GetTokenListRequest()
    )
    assert token_list
    assert len(token_list['result']) > 0

@pytest.mark.webtest
def test_get_token_category(client: KlardaAPICollection) -> None:
    token_category = client.get_token_category()
    assert token_category
    assert len(token_category['data']) > 0

@pytest.mark.webtest
def test_get_token_gainers_or_losers(client: KlardaAPICollection) -> None:
    token_gainers_or_losers = client.get_token_gainers_or_losers(
        params = types.GetTopGainersOrLosersRequest(
            type="gainer",
            limit = 10
        )
    )
    assert token_gainers_or_losers
    assert len(token_gainers_or_losers) == 10

@pytest.mark.webtest
def test_get_seed_fundraising(client: KlardaAPICollection) -> None:
    seed_fundraising = client.get_seed_fundraising(
        params = types.GetPageAndLimitRequest(
            page=1,
            limit = 10
        )
    )
    assert seed_fundraising
    assert seed_fundraising['total'] > 0
    assert len(seed_fundraising['result']) == 10

@pytest.mark.webtest
def test_get_ido_fundraising(client: KlardaAPICollection) -> None:
    ido_fundraising = client.get_ido_fundraising(
        params = types.GetPageAndLimitRequest(
            page=1,
            limit = 10
        )
    )
    assert ido_fundraising
    assert ido_fundraising['total'] > 0
    assert len(ido_fundraising['result']) == 10

@pytest.mark.webtest
def test_get_global_data(client: KlardaAPICollection) -> None:
    global_data = client.get_global_data()

    assert global_data

@pytest.mark.webtest
def test_get_global_protocol_list(client: KlardaAPICollection) -> None:
    global_protocol_list = client.get_ido_fundraising(
        params = types.GetPageAndLimitRequest(
            page=1,
            limit = 10
        )
    )
    assert global_protocol_list
    assert global_protocol_list['total'] > 0
    assert len(global_protocol_list['result']) == 10

@pytest.mark.webtest
def test_get_economic_calendar(client: KlardaAPICollection) -> None:
    economic_calendar = client.get_economic_calendar(
        params = types.GetEconomicCalendarRequest(
            start_date = "2023-05-12T00:00:00.000+00:00",
            end_date = "2023-05-15T00:00:00.000+00:00"
        )
    )
    assert economic_calendar

@pytest.mark.webtest
def test_get_indices_future(client: KlardaAPICollection) -> None:
    indices_future = client.get_indices_future()

    assert indices_future

@pytest.mark.webtest
def test_get_commodities(client: KlardaAPICollection) -> None:
    commodities = client.get_commodities()

    assert commodities