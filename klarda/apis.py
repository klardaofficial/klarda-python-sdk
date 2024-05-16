from __future__ import annotations

from typing import Iterable, List, Optional

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
            
class KlardaAPICollection(KlardaMarketAPI):
    ...