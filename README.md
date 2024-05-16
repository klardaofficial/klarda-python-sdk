# Klarda Python SDK

Refined Python library for interaction with Klarda's APIs [Klarda APIs](https://docs.klarda.com/reference/klarda-market-api-quickstart)

# Klarda API Quickstart

#### 1. Install Klarda Python SDK from PyPi using pip

```bash
pip install klarda-python-sdk
```

#### 2. Initilize the SDK using our API key

_Note: In order to use our API, you have to get you API key from Klarda's Dashboard._

Get your API key here https://dashboard.klarda.com/account-setting/api and provide it to the `KlardaAPICollection` class.

```python3
from klarda import KlardaAPICollection

klarda_api = KlardaAPICollection("YOUR_API_KEY")
```

#### 3. Use the python sdk and call our api collection.

_Note: More information about the available APIs can be seen in our documentation [Klarda APIs Docs](https://docs.klarda.com/reference/klarda-market-api-quickstart)._

#### Klarda Market/Token API

```python3
from klarda import KlardaAPICollection
from klarda.types import GetTokenListRequest

klarda_api = KlardaAPICollection("YOUR_API_KEY")

response = klarda_api.get_token_list(
    params = GetTokenListRequest(
        page = 1,
        limit = 10,
        sort_by = "volume",
        sort_order = "desc"
    )
)

print(response)
```

More APIs description will be added in the future in this Readme


