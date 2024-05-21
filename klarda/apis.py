from __future__ import annotations

from typing import Iterable, List, Optional, Union

from klarda import types
from klarda.exceptions import APIError
from klarda.providers import KlardaProvider


class KlardaAPI:
    def __init__(
        self,
        api_key: str,
        endpoint_uri: Optional[str] = None,
    ) -> None:
        self.provider = KlardaProvider(api_key, endpoint_uri)


class KlardaMarketAPI(KlardaAPI):
    def get_token_list(
        self,
        params: types.GetTokenListRequest,
    ) -> List[types.GetTokenListReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/token/list",
            params=params,
            reply=types.GetTokenListReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_new_token_list(
        self,
        params: types.GetTokenListRequest,
    ) -> List[types.GetTokenListReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/token/new",
            params=params,
            reply=types.GetTokenListReply,
        )

        if reply:
            return reply
        else:
            return []

    def get_token_category(
        self
    ) -> List[str]:
        reply = self.provider.make_request_without_params(
            method_url="market/token/category"
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_gainers_or_losers(
        self,
        params: types.GetTopGainersOrLosersRequest,
    ) -> List[types.GetTopGainersOrLosersReply]:
        reply = self.provider.make_request(
            method_url="market/token/top-gainer-loser",
            params=params,
            reply=types.GetTopGainersOrLosersReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_seed_fundraising(
            self,
            params: types.GetPageAndLimitRequest,
    ) -> List[types.GetSeedFundraisingReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/fundraising/private",
            params=params,
            reply=types.GetSeedFundraisingReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_ido_fundraising(
            self,
            params: types.GetPageAndLimitRequest,
    ) -> List[types.GetIDOFundraisingReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/fundraising/ido",
            params=params,
            reply=types.GetIDOFundraisingReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_global_data(
            self
    ) -> types.GetGlobalDataReply:
        reply = self.provider.make_request_without_params(
            method_url="market/global",
        )

        if reply:
            return reply
        else:
            return []
            
    def get_global_protocol_list(
            self,
            params: types.GetPageAndLimitRequest,
    ) -> List[types.GetGlobalProtocolListReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/global/protocol-list",
            params=params,
            reply=types.GetGlobalProtocolListReply,
        )

        if reply:
            return reply
        else:
            return []

    def get_economic_calendar(
            self,
            params: types.GetEconomicCalendarRequest,
    ) -> List[types.GetEconomicCalendarReply]:
        reply = self.provider.make_request(
            method_url="market/stock-market/economic-calendar",
            params=params,
            reply=types.GetEconomicCalendarReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_indices_future(
            self
    ) -> types.GetIndicesFutureOrCommoditiesReply:
        reply = self.provider.make_request_without_params(
            method_url="market/stock-market/indices",
        )

        if reply:
            return reply
        else:
            return []
        
    def get_commodities(
            self
    ) -> types.GetIndicesFutureOrCommoditiesReply:
        reply = self.provider.make_request_without_params(
            method_url="market/stock-market/commodities",
        )

        if reply:
            return reply
        else:
            return []
        
    def get_search_queries(
            self,
            params: types.GetSearchByQueriesRequest
    ) -> Union[
        List[types.GetSearchByQueriesByNewsReply],
        List[types.GetSearchByQueriesByTokenReply],
        List[types.GetSearchByQueriesByProtocolReply],
        List[types.GetSearchByQueriesBySignalReply]
    ]:
        method_url = "market/search/queries"
        if params.type == types.SearchType.NEWS.value:
            reply = self.provider.make_request_with_total(
            method_url=method_url,
            params=params,
            reply=types.GetSearchByQueriesByNewsReply)
            if reply:
                return reply
            else:
                return []
        elif params.type == types.SearchType.TOKEN.value:
            reply = self.provider.make_request_with_total(
            method_url=method_url,
            params=params,
            reply=types.GetSearchByQueriesByTokenReply)
            if reply:
                return reply
            else:
                return []
        elif params.type == types.SearchType.PROTOCOL.value:
            reply = self.provider.make_request_with_total(
            method_url=method_url,
            params=params,
            reply=types.GetSearchByQueriesByProtocolReply)
            if reply:
                return reply
            else:
                return []
        elif params.type == types.SearchType.SIGNAL.value:
            reply = self.provider.make_request_with_total(
            method_url=method_url,
            params=params,
            reply=types.GetSearchByQueriesBySignalReply)
            if reply:
                return reply
            else:
                return []
        else:
            return []
            
    def get_trending_search(
            self,
            params: types.GetPageAndLimitRequest,
    ) -> List[types.GetSearchByQueriesByTokenReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/search/trending",
            params=params,
            reply=types.GetSearchByQueriesByTokenReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_technical_indicators(
            self,
            params: types.GetTokenTechnicalIndicatorsRequest,
    ) -> types.GetTokenTechnicalIndicatorsReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/technical-indicators",
            params=params,
            reply=types.GetTokenTechnicalIndicatorsReply,
        )

        if reply:
            return reply
        else:
            return {}

    def get_token_signal(
            self,
            params: types.GetTokenIdWithPageAndLimitRequest,
    ) -> List[types.GetSearchByQueriesBySignalReply]:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/signal",
            params=params,
            reply=types.GetSearchByQueriesBySignalReply,
        )

        if reply:
            return reply
        else:
            return {}         
        
    def get_token_metadata_profile(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenMetadataProfileReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/metadata/profile",
            params=params,
            reply=types.GetTokenMetadataProfileReply,
        )

        if reply:
            return reply
        else:
            return {}         
        
    def get_token_metadata_fundraising(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenMetadataFundraisingReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/metadata/fundraising",
            params=params,
            reply=types.GetTokenMetadataFundraisingReply,
        )

        if reply:
            return reply
        else:
            return {}

    def get_token_metadata_tokenomics(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenMetadataTokenomicsReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/metadata/tokenomics",
            params=params,
            reply=types.GetTokenMetadataTokenomicsReply,
        )

        if reply:
            return reply
        else:
            return {}

    def get_token_metadata_with_onchain(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenMetadataWithOnchainReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/metadata/onchain",
            params=params,
            reply=types.GetTokenMetadataWithOnchainReply,
        )

        if reply:
            return reply
        else:
            return {}    

    def get_token_exchange_trade_by_symbol(
            self,
            params: types.GetTokenIdRequest,
    ) -> List[types.GetTokenExchangeTradeBySymbolReply]:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/price/exchange-trade",
            params=params,
            reply=types.GetTokenMetadataWithOnchainReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_price_information(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenPriceInformationBySymbolReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/price/information",
            params=params,
            reply=types.GetTokenPriceInformationBySymbolReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_price(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenPriceBySymbolReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/price",
            params=params,
            reply=types.GetTokenPriceBySymbolReply,
        )

        if reply:
            return reply
        else:
            return []

    def get_token_price_history(
            self,
            params: types.GetPriceHistoryByTimestampRequest,
    ) -> types.GetPriceHistoryByTimestampReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/price/history",
            params=params,
            reply=types.GetPriceHistoryByTimestampReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_price_history_timerange(
            self,
            params: types.GetPriceHistoryByTimerangeRequest,
    ) -> List[types.GetPriceHistoryByTimestampReply]:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/price/history-time-range",
            params=params,
            reply=types.GetPriceHistoryByTimestampReply,
        )

        if reply:
            return reply
        else:
            return []

    def get_token_price_ohlcv(
            self,
            params: types.GetPriceOHLCVRequest,
    ) -> List[types.GetPriceOHLCVReply]:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/price/ohlcv",
            params=params,
            reply=types.GetPriceOHLCVReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_holder_history(
            self,
            params: types.GetTokenIdAndChainIdWithLimitRequest,
    ) -> List[types.GetTokenHolderHistoryReply]:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/holder/history",
            params=params,
            reply=types.GetTokenHolderHistoryReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_holder_count(
            self,
            params: types.GetTokenIdAndChainIdRequest,
    ) -> types.GetTokenHolderHistoryReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/holder/counts",
            params=params,
            reply=types.GetTokenHolderHistoryReply,
        )

        if reply:
            return reply
        else:
            return []

    def get_token_holder_distribution(
            self,
            params: types.GetTokenIdAndChainIdRequest,
    ) -> types.GetTokenHolderDistributionReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/holder/distribution",
            params=params,
            reply=types.GetTokenHolderDistributionReply,
        )

        if reply:
            return reply
        else:
            return []      
        
    def get_token_liquidity(
            self,
            params: types.GetTokenLiquidityRequest,
    ) -> types.GetTokenLiquidityReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/onchain/liquidity",
            params=params,
            reply=types.GetTokenLiquidityReply,
        )

        if reply:
            return reply
        else:
            return []      
        
    def get_token_onchain_summary(
            self,
            params: types.GetTokenIdRequest,
    ) -> types.GetTokenOnchainSummaryReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/onchain/summary",
            params=params,
            reply=types.GetTokenOnchainSummaryReply,
        )

        if reply:
            return reply
        else:
            return []    
        
    def get_token_onchain_burn_count(
            self,
            params: types.GetTokenIdRequest,
    ) -> float:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/onchain/burn-counts",
            params=params,
            reply=float,
        )

        if reply:
            return reply
        else:
            return []    
        
    def get_token_onchain_swap_count(
            self,
            params: types.GetTokenLiquidityRequest,
    ) -> types.GetTokenOnchainSwapCountsReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/token/onchain/swap-counts",
            params=params,
            reply=types.GetTokenOnchainSwapCountsReply,
        )

        if reply:
            return reply
        else:
            return []    
        
    def get_token_onchain_smart_money(
            self,
            params: types.GetTokenSmartMoneyResponse,
    ) -> List[types.GetTokenSmartMoneyReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/token/onchain/smart-money",
            params=params,
            reply=types.GetTokenSmartMoneyReply,
        )

        if reply:
            return reply
        else:
            return []    

    def get_token_onchain_cex_flow(
            self,
            params: types.GetTokenOnchainCEXFlowResponse,
    ) -> List[types.GetTokenOnchainCEXFlowReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/token/onchain/cex-flow",
            params=params,
            reply=types.GetTokenOnchainCEXFlowReply,
        )

        if reply:
            return reply
        else:
            return []   
        
    def get_token_onchain_suspicious_volume(
            self,
            params: types.GetSuspiciousVolumeResponse,
    ) -> List[types.GetSuspiciousVolumeReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/token/onchain/suspicious-vol",
            params=params,
            reply=types.GetSuspiciousVolumeReply,
        )

        if reply:
            return reply
        else:
            return []   
    
    def get_token_onchain_dex_gainers(
            self,
            params: types.GetSuspiciousVolumeResponse,
    ) -> List[types.GetDexGainersReply]:
        reply = self.provider.make_request_with_total(
            method_url="market/token/onchain/dex-gainers",
            params=params,
            reply=types.GetDexGainersReply,
        )

        if reply:
            return reply
        else:
            return []   
        
    def get_exchange_list(
            self
    ) -> List[types.GetExchangeListReply]:
        reply = self.provider.make_request_without_params(
            method_url="market/exchange/exchange-list",
        )

        if reply:
            return reply
        else:
            return []
        
    def get_token_amount_by_exchange(
            self,
            params: types.GetTokenAmountByExchangeResponse
    ) -> types.GetTokenAmountByExchangeReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/exchange/token-amount",
            params=params,
            reply=types.GetTokenAmountByExchangeReply,
        )

        if reply:
            return reply
        else:
            return []

    def get_exchange_balance_distribution(
            self,
    ) -> List[types.GetExchangeBalanceDistributionReply]:
        reply = self.provider.make_request_without_params(
            method_url="market/exchange/balance-distribution",
        )

        if reply:
            return reply
        else:
            return []

    def get_nft_metadata(
            self,
            params: types.GetNFTMetadataResponse
    ) -> types.GetNFTMetadataReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/nft/metadata",
            params=params,
            reply=types.GetNFTMetadataReply,
        )

        if reply:
            return reply
        else:
            return []
        
    def get_nft_holders(
            self,
            params: types.GetNFTHolderResponse
    ) -> types.GetNFTHolderReply:
        reply = self.provider.make_request_with_dict_return(
            method_url="market/nft/holder-list",
            params=params,
            reply=types.GetNFTHolderReply,
        )

        if reply:
            return reply
        else:
            return []
        
class KlardaAPICollection(KlardaMarketAPI):
    ...