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

@pytest.mark.webtest
def test_get_search_queries(client: KlardaAPICollection) -> None:
    search_queries = client.get_search_queries(
        params = types.GetSearchByQueriesRequest(
            q = "bitcoin",
            type = types.SearchType.NEWS.value,
            page = 1,
            limit = 10
        )
    )
    assert search_queries
    assert search_queries['total'] > 0
    assert len(search_queries['result'])

@pytest.mark.webtest
def test_get_trending_search(client: KlardaAPICollection) -> None:
    trending_search = client.get_trending_search(
        params = types.GetPageAndLimitRequest(
            page=1,
            limit = 10
        )
    )
    assert trending_search
    assert trending_search['total'] > 0
    assert len(trending_search['result']) == 10

@pytest.mark.webtest
def test_get_token_technical_indicators(client: KlardaAPICollection) -> None:
    token_technical_indicators = client.get_token_technical_indicators(
        params = types.GetTokenTechnicalIndicatorsRequest(
            duration=types.CandleDuration.D1.value,
            token_id="BTC"
        )
    )
    assert token_technical_indicators

@pytest.mark.webtest
def test_get_token_signal(client: KlardaAPICollection) -> None:
    token_signal = client.get_token_signal(
        params = types.GetTokenIdWithPageAndLimitRequest(
            token_id="BTC",
            page=1,
            limit=10
        )
    )
    assert token_signal
    assert token_signal['total'] > 0
    assert len(token_signal['result']) == 10

@pytest.mark.webtest
def test_get_token_metadata_profile(client: KlardaAPICollection) -> None:
    token_metadata_profile = client.get_token_metadata_profile(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_metadata_profile

@pytest.mark.webtest
def test_get_token_metadata_fundraising(client: KlardaAPICollection) -> None:
    token_metadata_fundraising = client.get_token_metadata_fundraising(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_metadata_fundraising

@pytest.mark.webtest
def test_get_token_metadata_tokenomics(client: KlardaAPICollection) -> None:
    token_metadata_tokenomics = client.get_token_metadata_tokenomics(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_metadata_tokenomics

@pytest.mark.webtest
def test_get_token_metadata_with_onchain(client: KlardaAPICollection) -> None:
    token_metadata_with_onchain = client.get_token_metadata_with_onchain(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_metadata_with_onchain


@pytest.mark.webtest
def test_get_token_exchange_trade_by_symbol(client: KlardaAPICollection) -> None:
    token_exchange_trade_by_symbol = client.get_token_exchange_trade_by_symbol(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_exchange_trade_by_symbol
    assert len(token_exchange_trade_by_symbol) > 0

@pytest.mark.webtest
def test_get_token_price(client: KlardaAPICollection) -> None:
    token_price = client.get_token_price(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_price

@pytest.mark.webtest
def test_get_token_price_information(client: KlardaAPICollection) -> None:
    token_price_information = client.get_token_price_information(
        params = types.GetTokenIdRequest(
            token_id="BTC"
        )
    )
    assert token_price_information

@pytest.mark.webtest
def test_get_token_price_history(client: KlardaAPICollection) -> None:
    token_price_history = client.get_token_price_history(
        params = types.GetPriceHistoryByTimestampRequest(
            token_id="BTC",
            timestamp="2023-05-12T00:00:00.000",
        )
    )
    assert token_price_history

@pytest.mark.webtest
def test_get_token_price_history_timerange(client: KlardaAPICollection) -> None:
    token_price_history_timerange = client.get_token_price_history_timerange(
        params = types.GetPriceHistoryByTimerangeRequest(
            token_id="BTC",
            start_timestamp="2023-05-12T00:00:00.000",
            end_timestamp="2023-05-20T00:00:00.000",
        )
    )
    assert token_price_history_timerange
    assert len(token_price_history_timerange) > 0

@pytest.mark.webtest
def test_get_token_price_ohlcv(client: KlardaAPICollection) -> None:
    token_price_ohlcv = client.get_token_price_ohlcv(
        params = types.GetPriceOHLCVRequest(
            token_id="BTC",
            duration=types.CandleDuration.D1.value,
            limit = 10
        )
    )
    assert token_price_ohlcv
    assert len(token_price_ohlcv) == 10

@pytest.mark.webtest
def test_get_token_holder_history(client: KlardaAPICollection) -> None:
    token_holder_history = client.get_token_holder_history(
        params = types.GetTokenIdAndChainIdWithLimitRequest(
            token_id="LINK",
            chain_id=1,
            limit = 10
        )
    )
    assert token_holder_history
    assert len(token_holder_history) == 10

@pytest.mark.webtest
def test_get_token_holder_count(client: KlardaAPICollection) -> None:
    token_holder_counts = client.get_token_holder_count(
        params = types.GetTokenIdAndChainIdRequest(
            token_id="LINK",
            chain_id=1,
        )
    )
    assert token_holder_counts

@pytest.mark.webtest
def test_get_token_holder_distribution(client: KlardaAPICollection) -> None:
    token_holder_distribution = client.get_token_holder_distribution(
        params = types.GetTokenIdAndChainIdRequest(
            token_id="LINK",
            chain_id=1,
        )
    )
    assert token_holder_distribution

@pytest.mark.webtest
def test_get_token_liquidity(client: KlardaAPICollection) -> None:
    token_liquidity = client.get_token_liquidity(
        params = types.GetTokenLiquidityRequest(
            address="0x5aB53EE1d50eeF2C1DD3d5402789cd27bB52c1bB",
            chain_id="ethereum",
        )
    )
    assert token_liquidity

@pytest.mark.webtest
def test_get_token_onchain_summary(client: KlardaAPICollection) -> None:
    token_onchain_summary = client.get_token_onchain_summary(
        params = types.GetTokenIdRequest(
            token_id= "LINK"
        )
    )
    assert token_onchain_summary

@pytest.mark.webtest
def test_get_token_onchain_burn_count(client: KlardaAPICollection) -> None:
    token_onchain_burn_count = client.get_token_onchain_burn_count(
        params = types.GetTokenIdRequest(
            token_id= "USDC"
        )
    )
    assert token_onchain_burn_count

@pytest.mark.webtest
def test_get_token_onchain_swap_count(client: KlardaAPICollection) -> None:
    token_onchain_swap_count = client.get_token_onchain_swap_count(
        params = types.GetTokenLiquidityRequest(
            address="0x5aB53EE1d50eeF2C1DD3d5402789cd27bB52c1bB",
            chain_id="ethereum",
        )
    )
    assert token_onchain_swap_count

@pytest.mark.webtest
def test_get_token_onchain_smart_money(client: KlardaAPICollection) -> None:
    token_onchain_smart_money = client.get_token_onchain_smart_money(
        params = types.GetTokenSmartMoneyResponse(
            duration = types.DurationOnchain.H6.value,
            sort_by=types.SortByDexTxns.BUY.value,
            sort_order=types.SortOrder.DESC.value,
            page=1,
            limit=10
        )
    )
    assert token_onchain_smart_money
    assert len(token_onchain_smart_money['result']) == 10


@pytest.mark.webtest
def test_get_token_onchain_cex_flow(client: KlardaAPICollection) -> None:
    token_onchain_cex_flow = client.get_token_onchain_cex_flow(
        params = types.GetTokenOnchainCEXFlowResponse(
            duration = types.DurationOnchain.H6.value,
            sort_by=types.SortByOnchain.DEPOSIT.value,
            sort_order=types.SortOrder.DESC.value,
            page=1,
            limit=10
        )
    )
    assert token_onchain_cex_flow
    assert len(token_onchain_cex_flow['result']) == 10
    
@pytest.mark.webtest
def test_get_token_onchain_suspicious_volume(client: KlardaAPICollection) -> None:
    token_onchain_suspicious_volume = client.get_token_onchain_suspicious_volume(
        params = types.GetSuspiciousVolumeResponse(
            duration = types.DurationOnchain.H6.value,
            chain_id="ethereum",
            page=1,
            limit=10
        )
    )
    assert token_onchain_suspicious_volume
    assert len(token_onchain_suspicious_volume['result']) == 10

@pytest.mark.webtest
def test_get_token_onchain_dex_gainers(client: KlardaAPICollection) -> None:
    token_onchain_dex_gainers = client.get_token_onchain_dex_gainers(
        params = types.GetSuspiciousVolumeResponse(
            duration = types.DurationOnchain.H6.value,
            chain_id="ethereum",
            page=1,
            limit=10
        )
    )
    assert token_onchain_dex_gainers
    assert len(token_onchain_dex_gainers['result']) == 10

@pytest.mark.webtest
def test_get_exchange_list(client: KlardaAPICollection) -> None:
    exchange_list = client.get_exchange_list()
    assert exchange_list

@pytest.mark.webtest
def test_get_exchange_balance_distribution(client: KlardaAPICollection) -> None:
    exchange_balance_distribution = client.get_exchange_balance_distribution()
    assert exchange_balance_distribution

@pytest.mark.webtest
def test_get_token_amount_by_exchange(client: KlardaAPICollection) -> None:
    token_amount_by_exchange = client.get_token_amount_by_exchange(
        params = types.GetTokenAmountByExchangeResponse(
            exchange_key= "binance",
            chain_id="1",
            token_id="USDT",
        )
    )
    assert token_amount_by_exchange

@pytest.mark.webtest
def test_get_nft_metadata(client: KlardaAPICollection) -> None:
    nft_metadata = client.get_nft_metadata(
        params = types.GetNFTMetadataResponse(
            nft_id="20",
            address= "0xcbaa4ccbb5d5b862b036c9140691ec42b4268aba",
            chain_id="eth",
        )
    )
    assert nft_metadata

@pytest.mark.webtest
def test_get_nft_holders(client: KlardaAPICollection) -> None:
    nft_holders = client.get_nft_holders(
        params = types.GetNFTHolderResponse(
            address= "0xcbaa4ccbb5d5b862b036c9140691ec42b4268aba",
            chain_id=types.Blockchain.Eth.value,
        )
    )
    assert nft_holders

