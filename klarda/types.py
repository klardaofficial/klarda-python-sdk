from __future__ import annotations
from enum import Enum
from typing import Any, Union

class GetTokenListReply:
    def __init__(
        self,
        name: str,
        symbol: str,
        logo_uri: str,
        price: Union[float],
        volume: Union[float],
        stable_coin: bool,
        total_supply: Union[float],
        circulating_supply: Union[float],
        market_cap: Union[float],
        rank: Union[int],
        networks: Any,
        token_symbol: str,
        dominance: Union[float],
        high_24h_price: Union[float],
        low_24h_price: Union[float],
        link: str
    ):
        self.name = name
        self.symbol = symbol
        self.logo_uri = logo_uri
        self.price = price
        self.volume = volume
        self.stable_coin = stable_coin
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.market_cap = market_cap
        self.rank = rank
        self.networks = networks
        self.token_symbol = token_symbol
        self.dominance = dominance
        self.high_24h_price = high_24h_price
        self.low_24h_price = low_24h_price
        self.link = link

    @classmethod
    def from_dict(cls, **data):
        return cls(
            name = data.get("name"),
            symbol = data.get("symbol"),
            logo_uri = data.get("logo_uri"),
            price = data.get("price"),
            volume = data.get("volume"),
            stable_coin = data.get("stable_coin"),
            total_supply = data.get("total_supply"),
            circulating_supply = data.get("circulating_supply"),
            market_cap = data.get("market_cap"),
            rank = data.get("rank"),
            networks = data.get("networks"),
            token_symbol = data.get("token_symbol"),
            dominance = data.get("dominance"),
            high_24h_price = data.get("high_24h_price"),
            low_24h_price = data.get("low_24h_price"),
            link = data.get("link"),
        )

class GetTokenListRequest:
    def __init__(
        self,
        category: str = None,
        sort_by: SortBy = None,
        sort_order: SortOrder = None,
        page: Union[int] = None,
        limit: Union[int] = None
    ):
        self.category = category
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.page = page
        self.limit = limit

    def to_dict(self):
        return {
            "category": self.category,
            "sort_by": self.sort_by,
            "sort_order": self.sort_order,
            "page": self.page,
            "limit": self.limit,
        }
    
class GetTopGainersOrLosersReply:
    def __init__(
        self,
        name: str,
        symbol: str,
        token_symbol: str,
        market_cap: Union[float],
        category: str,
        short_description: str,
        last_24h_price: Union[float],
        price: Union[float],
        volume: Union[float],
    ):
        self.name = name
        self.symbol = symbol
        self.token_symbol = token_symbol
        self.market_cap = market_cap
        self.category = category
        self.short_description = short_description
        self.last_24h_price = last_24h_price
        self.price = price
        self.volume = volume

    @classmethod
    def from_dict(cls, **data):
        return cls(
            name = data.get("name"),
            symbol = data.get("symbol"),
            token_symbol = data.get("token_symbol"),
            market_cap = data.get("market_cap"),
            category = data.get("category"),
            short_description = data.get("short_description"),
            last_24h_price = data.get("last_24h_price"),
            price = data.get("price"),
            volume = data.get("volume"),
        )

class GetTopGainersOrLosersRequest:
    def __init__(
        self,
        type: GainersAndLosers,
        limit: Union[int] = None
    ):
        self.type = type
        self.limit = limit

    def to_dict(self):
        return {
            "type": self.type,
            "limit": self.limit,
        }
    
class GetPageAndLimitRequest:
    def __init__(
        self,
        page: int = None,
        limit: int = None
    ):
        self.page = page
        self.limit = limit

    def to_dict(self):
        return {
            "page": self.page,
            "limit": self.limit,
        }
    
class GetSeedFundraisingReply:
    def __init__(
        self,
        amount: float,
        name: str,
        category: str,
        round: str,
    ):
        self.amount = amount
        self.name = name
        self.category = category
        self.round = round

    @classmethod
    def from_dict(cls, **data):
        return cls(
            amount = data.get("amount"),
            name = data.get("name"),
            category = data.get("category"),
            round = data.get("round"),
        )
    
class GetIDOFundraisingReply:
    def __init__(
        self,
        token_name: str,
        category: str,
        description: str,
        end_date: str,
        start_date: str,
        total_raise: float,
        type: str,
        web: str,
    ):
        self.token_name = token_name
        self.category = category
        self.description = description
        self.end_date = end_date
        self.start_date = start_date
        self.total_raise = total_raise
        self.type = type
        self.web = web

    @classmethod
    def from_dict(cls, **data):
        return cls(
            token_name = data.get("token_name"),
            category = data.get("category"),
            description = data.get("description"),
            end_date = data.get("end_date"),
            start_date = data.get("start_date"),
            total_raise = data.get("total_raise"),
            type = data.get("type"),
            web = data.get("web"),
        )
    
class GetGlobalDataReply:
    def __init__(
        self,
        total_marketCap: float,
        total_volume24h: float,
        btc_dominance: float,
        eth_dominance: float,
        created_at: str,
    ):
        self.total_marketCap = total_marketCap
        self.total_volume24h = total_volume24h
        self.btc_dominance = btc_dominance
        self.eth_dominance = eth_dominance
        self.created_at = created_at
        

    @classmethod
    def from_dict(cls, **data):
        return cls(
            total_marketCap = data.get("total_marketCap"),
            total_volume24h = data.get("total_volume24h"),
            btc_dominance = data.get("btc_dominance"),
            eth_dominance = data.get("eth_dominance"),
            created_at = data.get("created_at")
        )
    
class GetGlobalProtocolListReply:
    def __init__(
        self,
        name: str,
        url: str,
        description: str,
        category: str,
        slug: str,
        tvl: float,
    ):
        self.name = name
        self.url = url
        self.description = description
        self.category = category
        self.slug = slug
        self.tvl = tvl
        

    @classmethod
    def from_dict(cls, **data):
        return cls(
            name = data.get("name"),
            url = data.get("url"),
            description = data.get("description"),
            category = data.get("category"),
            slug = data.get("slug"),
            tvl = data.get("tvl")
        )
    
class GetEconomicCalendarRequest:
    def __init__(
        self,
        start_date: str,
        end_date: str,
        country: str = None
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.country = country

    def to_dict(self):
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "country": self.country,
        }
    
class GetEconomicCalendarReply:
    def __init__(
        self,
        actual: float,
        consensus: float,
        content: str,
        event_time: str,
        previous: float,
        star: float,
    ):
        self.actual = actual
        self.consensus = consensus
        self.content = content
        self.event_time = event_time
        self.previous = previous
        self.star = star
        

    @classmethod
    def from_dict(cls, **data):
        return cls(
            actual = data.get("actual"),
            consensus = data.get("consensus"),
            content = data.get("content"),
            event_time = data.get("event_time"),
            previous = data.get("previous"),
            star = data.get("star")
        )
    
class GetIndicesFutureReply:
    def __init__(
        self,
        symbol: str,
        change: float,
        logo_uri: str,
        name: str,
        price: float,
    ):
        self.symbol = symbol
        self.change = change
        self.logo_uri = logo_uri
        self.name = name
        self.price = price
        

    @classmethod
    def from_dict(cls, **data):
        return cls(
            symbol = data.get("symbol"),
            change = data.get("change"),
            logo_uri = data.get("logo_uri"),
            name = data.get("name"),
            price = data.get("price"),
        )
    
class GetIndicesFutureOrCommoditiesReply:
    def __init__(
        self,
        symbol: str,
        change: float,
        logo_uri: str,
        name: str,
        price: float,
    ):
        self.symbol = symbol
        self.change = change
        self.logo_uri = logo_uri
        self.name = name
        self.price = price
        

    @classmethod
    def from_dict(cls, **data):
        return cls(
            symbol = data.get("symbol"),
            change = data.get("change"),
            logo_uri = data.get("logo_uri"),
            name = data.get("name"),
            price = data.get("price"),
        )

class Blockchain(Enum):
    Arbitrum = "arbitrum"
    Avalanche = "avalanche"
    Avalanche_fuji = "avalanche_fuji"
    Base = "base"
    Bsc = "bsc"
    Eth = "eth"
    Eth_goerli = "eth_goerli"
    Fantom = "fantom"
    Flare = "flare"
    Gnosis = "gnosis"
    Linea = "linea"
    Optimism = "optimism"
    Optimism_testnet = "optimism_testnet"
    Polygon = "polygon"
    Polygon_mumbai = "polygon_mumbai"
    Polygon_zkevm = "polygon_zkevm"
    Rollux = "rollux"
    Scroll = "scroll"
    Syscoin = "syscoin"

class SortBy(Enum):
    MARKET_CAP = "market_cap"
    VOLUME = "volume"
    RANK = "rank"
    PRICE = "price"
    LOW_24H_PRICE = "low_24h_price"
    HIGH_24H_PRICE = "high_24h_price"
    CIRCULATING_SUPPLY = "circulating_supply"
    TOTAL_SUPPLY = "total_supply"
    DOMINANCE = "dominance"
    CHANGE_1H = "change_1h"
    CHANGE_1D = "change_1d"
    CHANGE_1W = "change_1w"
    CHANGE_1M = "change_1m"
    CHANGE_1Y = "change_1y"

class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"

class GainersAndLosers(Enum):
    GAINER = "gainer"
    LOSER = "loser"