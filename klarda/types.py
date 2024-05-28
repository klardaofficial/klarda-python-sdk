from __future__ import annotations
from enum import Enum
from typing import Any, Dict, List, Union

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
    def from_dict(cls, data):
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
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "logo_uri": self.logo_uri,
            "price": self.price,
            "volume": self.volume,
            "stable_coin": self.stable_coin,
            "circulating_supply": self.circulating_supply,
            "total_supply": self.total_supply,
            "market_cap": self.market_cap,
            "rank": self.rank,
            "networks": self.networks,
            "token_symbol": self.token_symbol,
            "dominance": self.dominance,
            "high_24h_price": self.high_24h_price,
            "low_24h_price": self.low_24h_price,
            "link": self.link,
        }

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

    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "market_cap": self.market_cap,
            "token_symbol": self.token_symbol,
            "category": self.category,
            "short_description": self.short_description,
            "last_24h_price": self.last_24h_price,
            "price": self.price,
            "volume": self.volume,
        }
    
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
    
class GetTokenIdWithPageAndLimitRequest:
    def __init__(
        self,
        token_id: str,
        page: int = None,
        limit: int = None
    ):
        self.token_id = token_id
        self.page = page
        self.limit = limit

    def to_dict(self):
        return {
            "token_id": self.token_id,
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
    def from_dict(cls, data):
        return cls(
            amount = data.get("amount"),
            name = data.get("name"),
            category = data.get("category"),
            round = data.get("round"),
        )
    
    def to_dict(self):
        return {
            "amount": self.amount,
            "name": self.name,
            "category": self.category,
            "round": self.round,
        }
    
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
    def from_dict(cls, data):
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
    
    def to_dict(self):
        return {
            "token_name": self.token_name,
            "category": self.category,
            "description": self.description,
            "end_date": self.end_date,
            "start_date": self.start_date,
            "total_raise": self.total_raise,
            "type": self.type,
            "web": self.web,
        }
    
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
    
    def to_dict(self):
        return {
            "total_marketCap": self.total_marketCap,
            "total_volume24h": self.total_volume24h,
            "btc_dominance": self.btc_dominance,
            "eth_dominance": self.eth_dominance,
            "created_at": self.created_at,
        }
    
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
    def from_dict(cls, data):
        return cls(
            name = data.get("name"),
            url = data.get("url"),
            description = data.get("description"),
            category = data.get("category"),
            slug = data.get("slug"),
            tvl = data.get("tvl")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "description": self.description,
            "category": self.category,
            "slug": self.slug,
            "tvl": self.tvl,
        }
    
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
    
    def to_dict(self):
        return {
            "actual": self.actual,
            "consensus": self.consensus,
            "content": self.content,
            "event_time": self.event_time,
            "previous": self.previous,
            "star": self.star,
        }
    
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
    
    def to_dict(self):
        return {
            "symbol": self.symbol,
            "change": self.change,
            "logo_uri": self.logo_uri,
            "name": self.name,
            "price": self.price,
        }
    
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
    
    def to_dict(self):
        return {
            "symbol": self.symbol,
            "change": self.change,
            "logo_uri": self.logo_uri,
            "name": self.name,
            "price": self.price,
        }

class GetSearchByQueriesRequest:
    def __init__(
        self,
        q: str,
        type: SearchType,
        page: int = None,
        limit: int = None,
    ):
        self.q = q
        self.type = type
        self.page = page
        self.limit = limit

    def to_dict(self):
        return {
            "q": self.q,
            "type": self.type,
            "page": self.page,
            "limit": self.limit,
        }
    
class GetSearchByQueriesByNewsReply:
    def __init__(
        self,
        link: str,
        content: str,
        creator: str,
        published_at: str,
        source: str,
        thumbnail: str,
        title: str,
    ):
        self.link = link
        self.content = content
        self.creator = creator
        self.published_at = published_at
        self.source = source
        self.thumbnail = thumbnail
        self.title = title
        

    @classmethod
    def from_dict(cls, data):
        return cls(
            link = data.get("link"),
            content = data.get("content"),
            creator = data.get("creator"),
            published_at = data.get("published_at"),
            source = data.get("source"),
            thumbnail = data.get("thumbnail"),
            title = data.get("title")
        )
    
    def to_dict(self):
        return {
            "link": self.link,
            "content": self.content,
            "creator": self.creator,
            "published_at": self.published_at,
            "source": self.source,
            "thumbnail": self.thumbnail,
            "title": self.title,
        }
    
class GetSearchByQueriesByTokenReply:
    def __init__(
        self,
        name: str,
        symbol: str,
        category: str,
        short_description: str,
        logo_uri: str,
        last_24h_price: str,
        price: float,
        volume: float,
        market_cap: float,
        token_symbol: str,
    ):
        self.name = name
        self.symbol = symbol
        self.category = category
        self.short_description = short_description
        self.logo_uri = logo_uri
        self.last_24h_price = last_24h_price
        self.price = price
        self.volume = volume
        self.market_cap = market_cap
        self.token_symbol = token_symbol
        

    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data.get("name"),
            symbol = data.get("symbol"),
            category = data.get("category"),
            short_description = data.get("short_description"),
            logo_uri = data.get("logo_uri"),
            last_24h_price = data.get("last_24h_price"),
            price = data.get("price"),
            volume = data.get("volume"),
            market_cap = data.get("market_cap"),
            token_symbol = data.get("token_symbol")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "category": self.category,
            "short_description": self.short_description,
            "logo_uri": self.logo_uri,
            "last_24h_price": self.last_24h_price,
            "price": self.price,
            "volume": self.volume,
            "market_cap": self.market_cap,
            "token_symbol": self.token_symbol,
        }
    
class GetSearchByQueriesByProtocolReply:
    def __init__(
        self,
        name: str,
        tvl: float,
        change_1d: float,
        change_7d: float,
    ):
        self.name = name
        self.tvl = tvl
        self.change_1d = change_1d
        self.change_7d = change_7d
                

    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data.get("name"),
            tvl = data.get("tvl"),
            change_1d = data.get("change_1d"),
            change_7d = data.get("change_7d"),
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "tvl": self.tvl,
            "change_1d": self.change_1d,
            "change_7d": self.change_7d
        }
    
class GetSearchByQueriesBySignalReply:
    def __init__(
        self,
        symbol: str,
        name: str,
        signal: str,
        buy_sell: int,
        signal_time: str,
    ):
        self.symbol = symbol
        self.name = name
        self.signal = signal
        self.buy_sell = buy_sell
        self.signal_time = signal_time
                

    @classmethod
    def from_dict(cls, data):
        return cls(
            symbol = data.get("symbol"),
            name = data.get("name"),
            signal = data.get("signal"),
            buy_sell = data.get("buy_sell"),
            signal_time = data.get("signal_time"),
        )

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "name": self.name,
            "signal": self.signal,
            "buy_sell": self.buy_sell,
            "signal_time": self.signal_time
        }
    
class GetTokenTechnicalIndicatorsRequest:
    def __init__(
        self,
        duration: CandleDuration,
        token_id: str
    ):
        self.duration = duration
        self.token_id = token_id

    def to_dict(self):
        return {
            "duration": self.duration,
            "token_id": self.token_id,
        }
    

class MovingAverageSummary:
    def __init__(self, name: str, value: float, action: int):
        self.name = name
        self.value = value
        self.action = action

    @classmethod
    def from_dict(cls, data: Dict) -> 'MovingAverageSummary':
        return cls(
            name=data.get("name"),
            value=data.get("value"),
            action=data.get("action")
        )
    
class OscillatorsSummary:
    def __init__(self, name: str, value: float, action: int):
        self.name = name
        self.value = value
        self.action = action

    @classmethod
    def from_dict(cls, data: Dict) -> 'OscillatorsSummary':
        return cls(
            name=data.get("name"),
            value=data.get("value"),
            action=data.get("action")
        )
    
class PivotData:
    def __init__(self, name: str, value: Dict):
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, data: Dict) -> 'PivotData':
        return cls(
            name=data.get("name"),
            value=data.get("value")
        )

class MovingAverageData:
    def __init__(self, name_ma: str, value_simple: float, action_simple: int, value_exponential: float, action_exponential: int):
        self.name_ma = name_ma
        self.value_simple = value_simple
        self.action_simple = action_simple
        self.value_exponential = value_exponential
        self.action_exponential = action_exponential

    @classmethod
    def from_dict(cls, data: Dict) -> 'MovingAverageData':
        return cls(
            name_ma=data.get("name_ma"),
            value_simple=data.get("value_simple"),
            action_simple=data.get("action_simple"),
            value_exponential=data.get("value_exponential"),
            action_exponential=data.get("action_exponential")
        )

class TextSummary:
    def __init__(self, name: str, text: List[str]):
        self.name = name
        self.text = text

    @classmethod
    def from_dict(cls, data: Dict) -> 'TextSummary':
        return cls(
            name=data.get("name"),
            text=data.get("text")
        )
    
class Details:
    def __init__(self, symbol: str, moving_average_summary: List[MovingAverageSummary], oscillators_summary: List[OscillatorsSummary], pivot_data: List[PivotData], score: float, stored_time: str, expired_time: str, created_at: str, moving_average_data: List[MovingAverageData]):
        self.symbol = symbol
        self.moving_average_summary = moving_average_summary
        self.oscillators_summary = oscillators_summary
        self.pivot_data = pivot_data
        self.score = score
        self.stored_time = stored_time
        self.expired_time = expired_time
        self.created_at = created_at
        self.moving_average_data = moving_average_data

    @classmethod
    def from_dict(cls, data: Dict) -> 'Details':
        return cls(
            symbol=data.get("symbol"),
            moving_average_summary=[MovingAverageSummary.from_dict(item) for item in data.get("moving_average_summary", [])],
            oscillators_summary=[OscillatorsSummary.from_dict(item) for item in data.get("oscillators_summary", [])],
            pivot_data=[PivotData.from_dict(item) for item in data.get("pivot_data", [])],
            score=data.get("score"),
            stored_time=data.get("stored_time"),
            expired_time=data.get("expired_time"),
            created_at=data.get("created_at"),
            moving_average_data=[MovingAverageData.from_dict(item) for item in data.get("moving_average_data", [])]
        )

class GetTokenTechnicalIndicatorsReply:
    def __init__(self, details: Details, status: str, value: float, statistics: Dict[str, int], text_summary: List[TextSummary]):
        self.details = details
        self.status = status
        self.value = value
        self.statistics = statistics
        self.text_summary = text_summary

    @classmethod
    def from_dict(cls, data: Dict) -> 'GetTokenTechnicalIndicatorsReply':
        return cls(
            details=Details.from_dict(data.get("details")),
            status=data.get("status"),
            value=data.get("value"),
            statistics=data.get("statistics"),
            text_summary=[TextSummary.from_dict(item) for item in data.get("text_summary", [])]
        )
    
    def to_dict(self):
        return {
            "details": self.details,
            "status": self.status,
            "value": self.value,
            "statistics": self.statistics,
            "text_summary": self.text_summary
        }
        
class GetTokenTechnicalIndicatorsReply:
    def __init__(
        self,
        link: str,
        content: str,
        creator: str,
        published_at: str,
        source: str,
        thumbnail: str,
        title: str,
    ):
        self.link = link
        self.content = content
        self.creator = creator
        self.published_at = published_at
        self.source = source
        self.thumbnail = thumbnail
        self.title = title
        

    @classmethod
    def from_dict(cls, **data):
        return cls(
            link = data.get("link"),
            content = data.get("content"),
            creator = data.get("creator"),
            published_at = data.get("published_at"),
            source = data.get("source"),
            thumbnail = data.get("thumbnail"),
            title = data.get("title")
        )

    def to_dict(self):
        return {
            "link": self.link,
            "content": self.content,
            "creator": self.creator,
            "published_at": self.published_at,
            "source": self.source,
            "thumbnail": self.thumbnail,
            "title": self.title
        }
    
class GetTokenIdRequest:
    def __init__(
        self,
        token_id: str
    ):
        self.token_id = token_id

    def to_dict(self):
        return {
            "token_id": self.token_id,
        }
class Media:
    def __init__(self, type: str, url: str):
        self.type = type
        self.url = url

    @classmethod
    def from_dict(cls, data):
        return cls(
            type=data.get("type"),
            url=data.get("url")
        )

class KlardaScore:
    def __init__(self, name: str, score: float, rank: int, status: str):
        self.name = name
        self.score = score
        self.rank = rank
        self.status = status

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            score=data.get("score"),
            rank=data.get("rank"),
            status=data.get("status")
        )

class Network:
    def __init__(self, name: str, decimals: int, chain_id: int, address: str, explorer_url: str, standard: str):
        self.name = name
        self.decimals = decimals
        self.chain_id = chain_id
        self.address = address
        self.explorer_url = explorer_url
        self.standard = standard

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            decimals=data.get("decimals"),
            chain_id=data.get("chain_id"),
            address=data.get("address"),
            explorer_url=data.get("explorer_url"),
            standard=data.get("standard")
        )

class GetTokenMetadataProfileReply:
    def __init__(
        self,
        name: str,
        symbol: str,
        category: str,
        short_description: str,
        description: str,
        logo_uri: str,
        medias: list,
        rank: int,
        rank_label: str,
        klarda_score: list,
        sub_id: list,
        networks: list,
        token_symbol: str,
    ):
        self.name = name
        self.symbol = symbol
        self.category = category
        self.short_description = short_description
        self.description = description
        self.logo_uri = logo_uri
        self.medias = medias
        self.rank = rank
        self.rank_label = rank_label
        self.klarda_score = klarda_score
        self.sub_id = sub_id
        self.networks = networks
        self.token_symbol = token_symbol

    @classmethod
    def from_dict(cls, data):
        medias = [Media.from_dict(media) for media in data.get("medias", [])]
        klarda_score = [KlardaScore.from_dict(score) for score in data.get("klarda_score", [])]
        networks = [Network.from_dict(network) for network in data.get("networks", [])]
        
        return cls(
            name=data.get("name"),
            symbol=data.get("symbol"),
            category=data.get("category"),
            short_description=data.get("short_description"),
            description=data.get("description"),
            logo_uri=data.get("logo_uri"),
            medias=medias,
            rank=data.get("rank"),
            rank_label=data.get("rank_label"),
            klarda_score=klarda_score,
            sub_id=data.get("sub_id", []),
            networks=networks,
            token_symbol=data.get("token_symbol")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "category": self.category,
            "short_description": self.short_description,
            "description": self.description,
            "logo_uri": self.logo_uri,
            "medias": self.medias,
            "rank": self.rank,
            "rank_label": self.rank_label,
            "klarda_score": self.klarda_score,
            "sub_id": self.sub_id,
            "networks": self.networks,
            "token_symbol": self.token_symbol,
        }
        
class FundRaising:
    def __init__(self, type: str, tokens_for_sale: int, lookup_period: str, price: float, total_raise: float, start: str = None, exchange_key: str = None):
        self.type = type
        self.tokens_for_sale = tokens_for_sale
        self.lookup_period = lookup_period
        self.price = price
        self.total_raise = total_raise
        self.start = start
        self.exchange_key = exchange_key

    @classmethod
    def from_dict(cls, data):
        return cls(
            type=data.get("type"),
            tokens_for_sale=data.get("tokens_for_sale"),
            lookup_period=data.get("lookup_period"),
            price=data.get("price"),
            total_raise=data.get("total_raise"),
            start=data.get("start"),
            exchange_key=data.get("exchange_key")
        )

class GetTokenMetadataFundraisingReply:
    def __init__(self, name: str, symbol: str, vc_ids: list, fund_raisings: list, token_symbol: str):
        self.name = name
        self.symbol = symbol
        self.vc_ids = vc_ids
        self.fund_raisings = fund_raisings
        self.token_symbol = token_symbol

    @classmethod
    def from_dict(cls, data):
        fund_raisings = [FundRaising.from_dict(fund) for fund in data.get("fund_raisings", [])]
        
        return cls(
            name=data.get("name"),
            symbol=data.get("symbol"),
            vc_ids=data.get("vc_ids", []),
            fund_raisings=fund_raisings,
            token_symbol=data.get("token_symbol")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "vc_ids": self.vc_ids,
            "fund_raisings": self.fund_raisings,
            "token_symbol": self.token_symbol,
        }
    
class Tokenomic:
    def __init__(self, title: str, percent: float):
        self.title = title
        self.percent = percent

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            percent=data.get("percent")
        )

class GetTokenMetadataTokenomicsReply:
    def __init__(self, name: str, symbol: str, tokenomics: list, token_symbol: str):
        self.name = name
        self.symbol = symbol
        self.tokenomics = tokenomics
        self.token_symbol = token_symbol

    @classmethod
    def from_dict(cls, data):
        tokenomics = [Tokenomic.from_dict(tokenomic) for tokenomic in data.get("tokenomics", [])]
        
        return cls(
            name=data.get("name"),
            symbol=data.get("symbol"),
            tokenomics=tokenomics,
            token_symbol=data.get("token_symbol")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "tokenomics": self.tokenomics,
            "token_symbol": self.token_symbol,
        }
    
    
class LowHighPrice:
    def __init__(self, timestamp: str, price: float):
        self.timestamp = timestamp
        self.price = price

    @classmethod
    def from_dict(cls, data):
        return cls(
            timestamp=data.get("timestamp"),
            price=data.get("price")
        )
    
class Token:
    def __init__(self, name: str, symbol: str, logo_uri: str, last_24h_price: float, price: float, low_price: LowHighPrice,
                 high_price: LowHighPrice, volume: float, total_supply: int, circulating_supply: int, market_cap: float,
                 rank: int, klarda_score: list, networks: list, token_symbol: str, dominance: float, high_24h_price: float,
                 low_24h_price: float):
        self.name = name
        self.symbol = symbol
        self.logo_uri = logo_uri
        self.last_24h_price = last_24h_price
        self.price = price
        self.low_price = low_price
        self.high_price = high_price
        self.volume = volume
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.market_cap = market_cap
        self.rank = rank
        self.klarda_score = klarda_score
        self.networks = networks
        self.token_symbol = token_symbol
        self.dominance = dominance
        self.high_24h_price = high_24h_price
        self.low_24h_price = low_24h_price

    @classmethod
    def from_dict(cls, data):
        low_price = LowHighPrice.from_dict(data.get("low_price"))
        high_price = LowHighPrice.from_dict(data.get("high_price"))
        klarda_score = [KlardaScore.from_dict(score) for score in data.get("klarda_score", [])]
        networks = [Network.from_dict(network) for network in data.get("networks", [])]
        
        return cls(
            name=data.get("name"),
            symbol=data.get("symbol"),
            logo_uri=data.get("logo_uri"),
            last_24h_price=data.get("last_24h_price"),
            price=data.get("price"),
            low_price=low_price,
            high_price=high_price,
            volume=data.get("volume"),
            total_supply=data.get("total_supply"),
            circulating_supply=data.get("circulating_supply"),
            market_cap=data.get("market_cap"),
            rank=data.get("rank"),
            klarda_score=klarda_score,
            networks=networks,
            token_symbol=data.get("token_symbol"),
            dominance=data.get("dominance"),
            high_24h_price=data.get("high_24h_price"),
            low_24h_price=data.get("low_24h_price")
        )

class SmartMoney:
    def __init__(self, net: float, token: float):
        self.net = net
        self.token = token

    @classmethod
    def from_dict(cls, data):
        return cls(
            net=data.get("net"),
            token=data.get("token")
        )

class CexFlow:
    def __init__(self, net: float, token: float):
        self.net = net
        self.token = token

    @classmethod
    def from_dict(cls, data):
        return cls(
            net=data.get("net"),
            token=data.get("token")
        )

class HolderInsights:
    def __init__(self, h_0_10: int, h_10_100: int, h_100_1000: int, h_1000_10000: int, h_10000_100000: int, h_100000_1000000: int, h_1000000: int):
        self.h_0_10 = h_0_10
        self.h_10_100 = h_10_100
        self.h_100_1000 = h_100_1000
        self.h_1000_10000 = h_1000_10000
        self.h_10000_100000 = h_10000_100000
        self.h_100000_1000000 = h_100000_1000000
        self.h_1000000 = h_1000000

    @classmethod
    def from_dict(cls, data):
        return cls(
            h_0_10=data.get("h_0_10"),
            h_10_100=data.get("h_10_100"),
            h_100_1000=data.get("h_100_1000"),
            h_1000_10000=data.get("h_1000_10000"),
            h_10000_100000=data.get("h_10000_100000"),
            h_100000_1000000=data.get("h_100000_1000000"),
            h_1000000=data.get("h_1000000")
        )

class GetTokenMetadataWithOnchainReply:
    def __init__(self, token: Token, smart_money: SmartMoney, cex_flow: CexFlow, holder_insights: HolderInsights):
        self.token = token
        self.smart_money = smart_money
        self.cex_flow = cex_flow
        self.holder_insights = holder_insights

    @classmethod
    def from_dict(cls, data):
        token = Token.from_dict(data.get("token"))
        smart_money = SmartMoney.from_dict(data.get("smart_money"))
        cex_flow = CexFlow.from_dict(data.get("cex_flow"))
        holder_insights = HolderInsights.from_dict(data.get("holder_insights"))

        return cls(
            token=token,
            smart_money=smart_money,
            cex_flow=cex_flow,
            holder_insights=holder_insights
        )

    def to_dict(self):
        return {
            "token": self.token,
            "smart_money": self.smart_money,
            "cex_flow": self.cex_flow,
            "holder_insights": self.holder_insights,
        }
    
class GetTokenExchangeTradeBySymbolReply:
    def __init__(
        self,
        trade_symbol: str,
        current_price: float,
        url: str,
        exchange_name: str,
        volume_24h: float,
        change: float,
        change_percent: float,
    ):
        self.trade_symbol = trade_symbol
        self.current_price = current_price
        self.url = url
        self.exchange_name = exchange_name
        self.volume_24h = volume_24h
        self.change = change
        self.change_percent = change_percent

    @classmethod
    def from_dict(cls, **data):
        return cls(
            trade_symbol = data.get("trade_symbol"),
            current_price = data.get("current_price"),
            url = data.get("url"),
            exchange_name = data.get("exchange_name"),
            volume_24h = data.get("volume_24h"),
            change = data.get("change"),
            change_percent = data.get("change_percent")
        )

    def to_dict(self):
        return {
            "trade_symbol": self.trade_symbol,
            "current_price": self.current_price,
            "url": self.url,
            "exchange_name": self.exchange_name,
            "volume_24h": self.volume_24h,
            "change": self.change,
            "change_percent": self.change_percent,
        }
    
class GetTokenPriceInformationBySymbolReply:
    def __init__(
        self,
        name: str,
        symbol: str,
        last_24h_price: float,
        price: float,
        low_price: LowHighPrice,
        high_price: LowHighPrice,
        volume: float,
        market_cap: float,
        token_symbol: str,
    ):
        self.name = name
        self.symbol = symbol
        self.last_24h_price = last_24h_price
        self.price = price
        self.low_price = low_price
        self.high_price = high_price
        self.volume = volume
        self.market_cap = market_cap
        self.token_symbol = token_symbol

    @classmethod
    def from_dict(cls, **data):
        low_price = LowHighPrice.from_dict(data.get("low_price"))
        high_price = LowHighPrice.from_dict(data.get("high_price"))

        return cls(
            name = data.get("name"),
            symbol = data.get("symbol"),
            last_24h_price = data.get("last_24h_price"),
            price = data.get("price"),
            low_price=low_price,
            high_price=high_price,
            volume = data.get("volume"),
            market_cap = data.get("market_cap"),
            token_symbol = data.get("token_symbol")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "last_24h_price": self.last_24h_price,
            "price": self.price,
            "low_price": self.low_price,
            "high_price": self.high_price,
            "volume": self.volume,
            "market_cap": self.market_cap,
            "token_symbol": self.token_symbol,
        }
    
class GetTokenPriceBySymbolReply:
    def __init__(
        self,
        name: str,
        price: float,
        token_symbol: str,
    ):
        self.name = name
        self.price = price
        self.token_symbol = token_symbol

    @classmethod
    def from_dict(cls, **data):
        return cls(
            name = data.get("name"),
            price = data.get("price"),
            token_symbol = data.get("token_symbol")
        )

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "token_symbol": self.token_symbol,
        }
    
class GetPriceHistoryByTimestampRequest:
    def __init__(
        self,
        token_id: str,
        timestamp: str,
    ):
        self.token_id = token_id
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "token_id": self.token_id,
            "timestamp": self.timestamp,
        }

class GetPriceHistoryByTimestampReply:
    def __init__(
        self,
        stored_time: str,
        symbol: str,
        market_cap: float,
        price: float,
        volume: float,
    ):
        self.stored_time = stored_time
        self.symbol = symbol
        self.market_cap = market_cap
        self.price = price
        self.volume = volume

    @classmethod
    def from_dict(cls, **data):
        return cls(
            stored_time = data.get("stored_time"),
            symbol = data.get("symbol"),
            market_cap = data.get("market_cap"),
            price = data.get("price"),
            volume = data.get("volume")
        )
    
    def to_dict(self):
        return {
            "stored_time": self.stored_time,
            "symbol": self.symbol,
            "market_cap": self.market_cap,
            "price": self.price,
            "volume": self.volume,
        }
    

class GetPriceHistoryByTimerangeRequest:
    def __init__(
        self,
        token_id: str,
        start_timestamp: str,
        end_timestamp: str,
    ):
        self.token_id = token_id
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp

    def to_dict(self):
        return {
            "token_id": self.token_id,
            "start_timestamp": self.start_timestamp,
            "end_timestamp": self.end_timestamp,
        }

class GetPriceOHLCVRequest:
    def __init__(
        self,
        token_id: str,
        duration: CandleDuration,
        limit: int = None,
    ):
        self.token_id = token_id
        self.duration = duration
        self.limit = limit

    def to_dict(self):
        return {
            "token_id": self.token_id,
            "duration": self.duration,
            "limit": self.limit,
        }
    
class GetPriceOHLCVReply:
    def __init__(
        self,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: float,
        stored_time: str,
    ):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.stored_time = stored_time

    @classmethod
    def from_dict(cls, **data):
        return cls(
            open = data.get("open"),
            high = data.get("high"),
            low = data.get("low"),
            close = data.get("close"),
            volume = data.get("volume"),
            stored_time = data.get("stored_time")
        )
    
    def to_dict(self):
        return {
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "stored_time": self.stored_time,
        }
    
class GetTokenIdAndChainIdRequest:
    def __init__(
        self,
        token_id: str,
        chain_id: int,
    ):
        self.token_id = token_id
        self.chain_id = chain_id

    def to_dict(self):
        return {
            "token_id": self.token_id,
            "chain_id": self.chain_id,
        }
    
class GetTokenIdAndChainIdWithLimitRequest:
    def __init__(
        self,
        token_id: str,
        chain_id: int,
        limit: int = None,
    ):
        self.token_id = token_id
        self.chain_id = chain_id
        self.limit = limit

    def to_dict(self):
        return {
            "token_id": self.token_id,
            "chain_id": self.chain_id,
            "limit": self.limit,
        }
    
class GetTokenHolderHistoryReply:
    def __init__(
        self,
        symbol: str,
        chain_id: int,
        total_holder: int,
        stored_time: str,
    ):
        self.symbol = symbol
        self.chain_id = chain_id
        self.total_holder = total_holder
        self.stored_time = stored_time

    @classmethod
    def from_dict(cls, **data):
        return cls(
            symbol = data.get("symbol"),
            chain_id = data.get("chain_id"),
            total_holder = data.get("total_holder"),
            stored_time = data.get("stored_time"),
        )
    
    def to_dict(self):
        return {
            "symbol": self.symbol,
            "chain_id": self.chain_id,
            "total_holder": self.total_holder,
            "stored_time": self.stored_time,
        }
    
class GetTokenHolderDistributionReply:
    def __init__(
        self,
        symbol: str,
        chain_id: int,
        h_0_10: int,
        h_10_100: int,
        h_100_1000: int,
        h_1000_10000: int,
        h_10000_100000: int,
        h_100000_1000000: int,
        h_1000000: int,
        stored_time: str,
    ):
        self.symbol = symbol
        self.chain_id = chain_id
        self.h_0_10 = h_0_10
        self.h_10_100 = h_10_100
        self.h_100_1000 = h_100_1000
        self.h_1000_10000 = h_1000_10000
        self.h_10000_100000 = h_10000_100000
        self.h_100000_1000000 = h_100000_1000000
        self.h_1000000 = h_1000000
        self.stored_time = stored_time

    @classmethod
    def from_dict(cls, **data):
        return cls(
            symbol = data.get("symbol"),
            chain_id = data.get("chain_id"),
            h_0_10 = data.get("h_0_10"),
            h_10_100 = data.get("h_10_100"),
            h_100_1000 = data.get("h_100_1000"),
            h_1000_10000 = data.get("h_1000_10000"),
            h_10000_100000 = data.get("h_10000_100000"),
            h_100000_1000000 = data.get("h_100000_1000000"),
            h_1000000 = data.get("h_1000000"),
            stored_time = data.get("stored_time"),
        )
    
    def to_dict(self):
        return {
            "symbol": self.symbol,
            "chain_id": self.chain_id,
            "h_0_10": self.h_0_10,
            "h_10_100": self.h_10_100,
            "h_100_1000": self.h_100_1000,
            "h_1000_10000": self.h_1000_10000,
            "h_10000_100000": self.h_10000_100000,
            "h_100000_1000000": self.h_100000_1000000,
            "h_1000000": self.h_1000000,
            "stored_time": self.stored_time
        }

class GetTokenLiquidityRequest:
    def __init__(
        self,
        address: str,
        chain_id: BlockchainIndexedForDEX,
    ):
        self.address = address
        self.chain_id = chain_id

    def to_dict(self):
        return {
            "address": self.address,
            "chain_id": self.chain_id,
        }
    
class TokenOnchain:
    def __init__(self, address: str, name: str, symbol: str):
        self.address = address
        self.name = name
        self.symbol = symbol

    @classmethod
    def from_dict(cls, data):
        return cls(
            address=data.get("address"),
            name=data.get("name"),
            symbol=data.get("symbol")
        )

class Liquidity:
    def __init__(self, usd: float, base: float, quote: float):
        self.usd = usd
        self.base = base
        self.quote = quote

    @classmethod
    def from_dict(cls, data):
        return cls(
            usd=data.get("usd"),
            base=data.get("base"),
            quote=data.get("quote")
        )

class GetTokenLiquidityReply:
    def __init__(self, chainId: BlockchainIndexedForDEX, baseToken: TokenOnchain, quoteToken: TokenOnchain, liquidity: Liquidity):
        self.chainId = chainId
        self.baseToken = baseToken
        self.quoteToken = quoteToken
        self.liquidity = liquidity

    @classmethod
    def from_dict(cls, data):
        baseToken = TokenOnchain.from_dict(data.get("baseToken"))
        quoteToken = TokenOnchain.from_dict(data.get("quoteToken"))
        liquidity = Liquidity.from_dict(data.get("liquidity"))
        
        return cls(
            chainId=data.get("chainId"),
            baseToken=baseToken,
            quoteToken=quoteToken,
            liquidity=liquidity,
        )
    
    def to_dict(self):
        return {
            "chainId": self.chainId,
            "baseToken": self.baseToken,
            "quoteToken": self.quoteToken,
            "liquidity": self.liquidity
        }
    
class GetTokenOnchainSummaryReply:
    def __init__(self, holder: int, liquidity: float, cex_dex: float, trades: int, volume: float):
        self.holder = holder
        self.liquidity = liquidity
        self.cex_dex = cex_dex
        self.trades = trades
        self.volume = volume

    @classmethod
    def from_dict(cls, data):
        return cls(
            holder=data.get("holder"),
            liquidity=data.get("liquidity"),
            cex_dex=data.get("cex_dex"),
            trades=data.get("trades"),
            volume=data.get("volume")
        )
    
    def to_dict(self):
        return {
            "holder": self.holder,
            "liquidity": self.liquidity,
            "cex_dex": self.cex_dex,
            "trades": self.trades,
            "volume": self.volume
        }
    
class TransactionCounts:
    def __init__(self, buys: int, sells: int):
        self.buys = buys
        self.sells = sells

    @classmethod
    def from_dict(cls, data):
        return cls(
            buys=data.get("buys"),
            sells=data.get("sells")
        )
    
class Txns:
    def __init__(self, m5: TransactionCounts, h1: TransactionCounts, h6: TransactionCounts, h24: TransactionCounts):
        self.m5 = m5
        self.h1 = h1
        self.h6 = h6
        self.h24 = h24

    @classmethod
    def from_dict(cls, data):
        m5 = TransactionCounts.from_dict(data.get("m5"))
        h1 = TransactionCounts.from_dict(data.get("h1"))
        h6 = TransactionCounts.from_dict(data.get("h6"))
        h24 = TransactionCounts.from_dict(data.get("h24"))
        
        return cls(
            m5=m5,
            h1=h1,
            h6=h6,
            h24=h24
        )
    
class GetTokenOnchainSwapCountsReply:
    def __init__(self, chainId: BlockchainIndexedForDEX, baseToken: TokenOnchain, quoteToken: TokenOnchain, txns: Txns):
        self.chainId = chainId
        self.baseToken = baseToken
        self.quoteToken = quoteToken
        self.txns = txns

    @classmethod
    def from_dict(cls, data):
        baseToken = TokenOnchain.from_dict(data.get("baseToken"))
        quoteToken = TokenOnchain.from_dict(data.get("quoteToken"))
        txns = Txns.from_dict(data.get("txns"))
        
        return cls(
            chainId=data.get("chainId"),
            baseToken=baseToken,
            quoteToken=quoteToken,
            txns=txns
        )
    
    def to_dict(self):
        return {
            "chainId": self.chainId,
            "baseToken": self.baseToken,
            "quoteToken": self.quoteToken,
            "txns": self.txns,
        }

class VolumeOnchain:
    def __init__(self, m5: float, h1: float, h6: float, h24: float):
        self.m5 = m5
        self.h1 = h1
        self.h6 = h6
        self.h24 = h24

    @classmethod
    def from_dict(cls, data):
        return cls(
            m5=data.get("m5"),
            h1=data.get("h1"),
            h6=data.get("h6"),
            h24=data.get("h24")
        )
    
class GetTokenSmartMoneyResponse:
    def __init__(
        self,
        duration: DurationOnchain = None,
        chain_id: str = None,
        sort_by: SortByDexTxns = None,
        sort_order: str = None,
        page: int = None,
        limit: int = None
    ):
        self.duration = duration
        self.chain_id = chain_id
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.page = page
        self.limit = limit
     

    def to_dict(self):
        return {
            "duration": self.duration,
            "chain_id": self.chain_id,
            "sort_by": self.sort_by,
            "sort_order": self.sort_order,
            "page": self.page,
            "limit": self.limit,
        }
    
class GetTokenSmartMoneyReply:
    def __init__(self, chainId: BlockchainIndexedForDEX, baseTokenSlug: str, quoteTokenSlug: str, pairAddress: str,
                 baseToken: TokenOnchain, quoteToken: TokenOnchain, priceUsd: float, inds: Txns, volume: VolumeOnchain, liquidity: Liquidity):
        self.chainId = chainId
        self.baseTokenSlug = baseTokenSlug
        self.quoteTokenSlug = quoteTokenSlug
        self.pairAddress = pairAddress
        self.baseToken = baseToken
        self.quoteToken = quoteToken
        self.priceUsd = priceUsd
        self.inds = inds
        self.volume = volume
        self.liquidity = liquidity

    @classmethod
    def from_dict(cls, data):
        baseToken = TokenOnchain.from_dict(data.get("baseToken", {}))
        quoteToken = TokenOnchain.from_dict(data.get("quoteToken", {}))
        inds = Txns.from_dict(data.get("inds"))
        volume = VolumeOnchain.from_dict(data.get("volume", {}))
        liquidity = Liquidity.from_dict(data.get("liquidity", {}))

        return cls(
            chainId = data.get("chainId"),
            baseTokenSlug=data.get("baseTokenSlug"),
            quoteTokenSlug=data.get("quoteTokenSlug"),
            pairAddress=data.get("pairAddress"),
            baseToken=baseToken,
            quoteToken=quoteToken,
            priceUsd=data.get("priceUsd"),
            inds=inds,
            volume=volume,
            liquidity=liquidity
        )
    
    def to_dict(self):
        return {
            "chainId": self.chainId,
            "baseToken": self.baseToken,
            "quoteToken": self.quoteToken,
            "baseTokenSlug": self.baseTokenSlug,
            "quoteTokenSlug": self.quoteTokenSlug,
            "pairAddress": self.pairAddress,
            "priceUsd": self.priceUsd,
            "inds": self.inds,
            "volume": self.volume,
            "liquidity": self.liquidity,
        }
    
class GetTokenOnchainCEXFlowResponse:
    def __init__(
        self,
        duration: DurationOnchain = None,
        sort_by: SortByOnchain = None,
        sort_order: str = None,
        page: int = None,
        limit: int = None
    ):
        self.duration = duration
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.page = page
        self.limit = limit
     

    def to_dict(self):
        return {
            "duration": self.duration,
            "sort_by": self.sort_by,
            "sort_order": self.sort_order,
            "page": self.page,
            "limit": self.limit,
        }
    
class TokenInfo:
    def __init__(self, symbol: str, token_symbol: str, name: str, logo_uri: str):
        self.symbol = symbol
        self.token_symbol = token_symbol
        self.name = name
        self.logo_uri = logo_uri

    @classmethod
    def from_dict(cls, data):
        return cls(
            symbol = data.get("symbol"),
            token_symbol=data.get("token_symbol"),
            name=data.get("name"),
            logo_uri=data.get("logo_uri"),
        )

class GetTokenOnchainCEXFlowReply:
    def __init__(self, token: TokenInfo, value: float):
        self.token = token
        self.value = value

    @classmethod
    def from_dict(cls, data):
        token = TokenInfo.from_dict(data.get("token"))

        return cls(
            token=token,
            value=data.get("value")
        )
    
    def to_dict(self):
        return {
            "token": self.token,
            "value": self.value
        }
    
class GetSuspiciousVolumeResponse(GetTokenSmartMoneyResponse):
    def __init__(
        self,
        duration: DurationOnchain = None,
        chain_id: str = None,
        page: int = None,
        limit: int = None
    ):
        super().__init__(duration, chain_id, page, limit, None, None)
     

    def to_dict(self):
        return {
            "duration": self.duration,
            "chain_id": self.chain_id,
            "page": self.page,
            "limit": self.limit,
        }
    
class GetSuspiciousVolumeReply:
    def __init__(self, baseTokenSlug: str, priceUsd: float, volume: VolumeOnchain, volume_s: VolumeOnchain, 
                 liquidity: float, baseToken: TokenInfo):
        self.baseTokenSlug = baseTokenSlug
        self.priceUsd = priceUsd
        self.volume = volume
        self.volume_s = volume_s
        self.liquidity = liquidity
        self.baseToken = baseToken

    @classmethod
    def from_dict(cls, data):
        baseToken = TokenInfo.from_dict(data.get("baseToken"))
        volume = VolumeOnchain.from_dict(data.get("volume"))
        volume_s = VolumeOnchain.from_dict(data.get("volume_s"))

        return cls(
            baseTokenSlug = data.get("baseTokenSlug"),
            priceUsd = data.get("priceUsd"),
            volume = volume,
            volume_s = volume_s,
            liquidity= data.get("liquidity"),
            baseToken = baseToken
        ) 

    def to_dict(self):
        return {
            "baseTokenSlug": self.baseTokenSlug,
            "priceUsd": self.priceUsd,
            "volume": self.volume,
            "volume_s": self.volume_s,
            "liquidity": self.liquidity,
            "baseToken": self.baseToken
        }
    
class GetDexGainersReply:
    def __init__(self, baseTokenSlug: str, priceUsd: float, volume: VolumeOnchain, volume_s: VolumeOnchain, 
                 liquidity: Liquidity, fdv: float, txns: Txns, baseToken: TokenInfo):
        self.baseTokenSlug = baseTokenSlug
        self.priceUsd = priceUsd
        self.volume = volume
        self.volume_s = volume_s
        self.liquidity = liquidity
        self.fdv = fdv,
        self.txns = txns,
        self.baseToken = baseToken

    @classmethod
    def from_dict(cls, data):
        baseToken = TokenInfo.from_dict(data.get("baseToken"))
        liquidity = Liquidity.from_dict(data.get("liquidity"))
        txns = Txns.from_dict(data.get("txns"))
        volume = VolumeOnchain.from_dict(data.get("volume"))
        volume_s = VolumeOnchain.from_dict(data.get("volume_s"))

        return cls(
            baseTokenSlug = data.get("baseTokenSlug"),
            priceUsd = data.get("priceUsd"),
            volume = volume,
            volume_s = volume_s,
            liquidity = liquidity,
            fdv = data.get("fdv"),
            txns = txns,
            baseToken = baseToken
        )

    def to_dict(self):
        return {
            "baseTokenSlug": self.baseTokenSlug,
            "priceUsd": self.priceUsd,
            "volume": self.volume,
            "volume_s": self.volume_s,
            "liquidity": self.liquidity,
            "fdv": self.fdv,
            "txns": self.txns,
            "baseToken": self.baseToken
        }
    
class GetTokenAmountByExchangeResponse:
    def __init__(
        self,
        exchange_key: str,
        chain_id: str,
        token_id: str
    ):
        self.exchange_key = exchange_key
        self.chain_id = chain_id
        self.token_id = token_id

    def to_dict(self):
        return {
            "exchange_key": self.exchange_key,
            "chain_id": self.chain_id,
            "token_id": self.token_id,
        }

class MediaExchange:
    def __init__(self, media_type: str, url: str):
        self.type = media_type
        self.url = url

    @classmethod
    def from_dict(cls, data):
        return cls(
            media_type=data.get("type"),
            url=data.get("url")
        )
    
class GetExchangeListReply:
    def __init__(self, key: str, name: str, pairs_count: int, medias: list, description: str, country: str, foundation_year: int):
        self.key = key
        self.name = name
        self.pairs_count = pairs_count
        self.medias = [MediaExchange.from_dict(media) for media in medias]
        self.description = description
        self.country = country
        self.foundation_year = foundation_year

    @classmethod
    def from_dict(cls, data):
        return cls(
            key=data.get("key"),
            name=data.get("name"),
            pairs_count=data.get("pairs_count"),
            medias=data.get("medias", []),
            description=data.get("description"),
            country=data.get("country"),
            foundation_year=data.get("foundation_year")
        )

    def to_dict(self):
        return {
            "key": self.key,
            "name": self.name,
            "pairs_count": self.pairs_count,
            "medias": self.medias,
            "description": self.description,
            "country": self.country,
            "foundation_year": self.foundation_year,
        }
    
class GetExchangeBalanceDistributionReply:
    def __init__(self, name: str, valueUsd: float):
        self.name = name
        self.valueUsd = valueUsd

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            valueUsd=data.get("valueUsd")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "valueUsd": self.valueUsd,
        }
    
class GetTokenAmountByExchangeReply:
    def __init__(self, symbol: str, chain_id: str, exchange_key: str,
                exchange_name:str, amount:float, stored_time: str):
        self.symbol = symbol
        self.chain_id = chain_id
        self.exchange_key = exchange_key
        self.exchange_name = exchange_name
        self.amount = amount
        self.stored_time = stored_time


    @classmethod
    def from_dict(cls, data):
        return cls(
            symbol=data.get("symbol"),
            chain_id=data.get("chain_id"),
            exchange_key=data.get("exchange_key"),
            exchange_name=data.get("exchange_name"),
            amount=data.get("amount"),
            stored_time=data.get("stored_time")
        )
    
    def to_dict(self):
        return {
            "symbol": self.symbol,
            "chain_id": self.chain_id,
            "exchange_key": self.exchange_key,
            "exchange_name": self.exchange_name,
            "amount": self.amount,
            "stored_time": self.stored_time,
        }

class Metadata:
    def __init__(self, blockchain: str, contractAddress: str, tokenId: str, contractType: str, collectionName: str, collectionSymbol: str):
        self.blockchain = blockchain
        self.contractAddress = contractAddress
        self.tokenId = tokenId
        self.contractType = contractType
        self.collectionName = collectionName
        self.collectionSymbol = collectionSymbol

    @classmethod
    def from_dict(cls, data):
        return cls(
            blockchain=data.get("blockchain"),
            contractAddress=data.get("contractAddress"),
            tokenId=data.get("tokenId"),
            contractType=data.get("contractType"),
            collectionName=data.get("collectionName"),
            collectionSymbol=data.get("collectionSymbol")
        )

    def to_dict(self):
        return {
            "blockchain": self.blockchain,
            "contractAddress": self.contractAddress,
            "tokenId": self.tokenId,
            "contractType": self.contractType,
            "collectionName": self.collectionName,
            "collectionSymbol": self.collectionSymbol
        }

class Attribute:
    def __init__(self, trait_type: str, value: str):
        self.trait_type = trait_type
        self.value = value

    @classmethod
    def from_dict(cls, data):
        return cls(
            trait_type=data.get("trait_type"),
            value=data.get("value")
        )

class Attributes:
    def __init__(self, tokenUrl: str, imageUrl: str, name: str, description: str, traits: list, contractType: str):
        self.tokenUrl = tokenUrl
        self.imageUrl = imageUrl
        self.name = name
        self.description = description
        self.traits = [Attribute.from_dict(trait) for trait in traits]
        self.contractType = contractType

    @classmethod
    def from_dict(cls, data):
        return cls(
            tokenUrl=data.get("tokenUrl"),
            imageUrl=data.get("imageUrl"),
            name=data.get("name"),
            description=data.get("description"),
            traits=data.get("traits", []),
            contractType=data.get("contractType")
        )

class GetNFTMetadataResponse:
    def __init__(self, nft_id: str, address: str, chain_id: Blockchain):
        self.nft_id = nft_id
        self.address = address
        self.chain_id = chain_id

    def to_dict(self):
        return {
            "nft_id": self.nft_id,
            "address": self.address,
            "chain_id": self.chain_id
        }
    
class GetNFTMetadataReply:
    def __init__(self, metadata: Metadata, attributes: Attributes):
        self.metadata = metadata
        self.attributes = attributes

    @classmethod
    def from_dict(cls, data):
        metadata = Metadata.from_dict(data.get("metadata"))
        attributes = Attributes.from_dict(data.get("attributes"))

        return cls(
            metadata=metadata,
            attributes=attributes
        )

    def to_dict(self):
        return {
            "metadata": self.metadata,
            "attributes": self.attributes,
        }
    
class GetNFTHolderResponse:
    def __init__(self, address: str, chain_id: Blockchain):
        self.address = address
        self.chain_id = chain_id

    def to_dict(self):
        return {
            "address": self.address,
            "chain_id": self.chain_id
        }
    
   
class GetNFTHolderReply:
    def __init__(self, holders: list):
        self.holders = holders

    @classmethod
    def from_dict(cls, data):
        holders = data.get("holders", [])
        return cls(holders=holders)
    
    def to_dict(self):
        return {
            "holders": self.holders,
        }
    
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

class BlockchainIndexedForDEX(Enum):
    MANTLE = 'mantle',
    FUSE = 'fuse',
    OPTIMISM = 'optimism',
    AVALANCHE = 'avalanche',
    ETHEREUM_POW = 'ethereumpow',
    BASE = 'base',
    OASIS_EMERALD = 'oasisemerald',
    MILKOMEDA_CARDANO = 'milkomedacardano',
    VELAS = 'velas',
    KCC = 'kcc',
    CRONOS = 'cronos',
    PULSE_CHAIN = 'pulechain',
    STEPNETWORK = 'stepnetwork',
    DOGE_CHAIN = 'dogechain',
    MOONRIVER = 'moonriver',
    MOONBEAM = 'moonbeam',
    ARBITRUM = 'arbitrum',
    FANTOM = 'fantom',
    BSC = 'bsc',
    IOTEX = 'iotex',
    HARMONY = 'harmony',
    ETHEREUM = 'ethereum',
    MATIC = 'polygon',

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

class SearchType(Enum):
    NEWS = "news"
    TOKEN = "token"
    PROTOCOL = "protocol"
    SIGNAL = "signal"

class CandleDuration(Enum):
    M5 = "5M"
    M15 = "15M"
    M30 = "30M"
    H1 = "1H"
    H4 = "4H"
    H6 = "6H"
    H12 = "12H"
    D1 = "1D"

class DurationOnchain(Enum):
    H6 = "6H"
    H24 = "24H"

class SortByOnchain(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    NET = "net"

class SortByDexTxns(Enum):
    BUY = "buy"
    SELL = "sell"
    NET = "net"