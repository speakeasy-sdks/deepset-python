# api_token

### Available Operations

* [create_token](#create_token) - Create Token
* [list](#list) - Get Tokens [private]
* [remove](#remove) - Remove Token [private]

## create_token

Creates the API key that you can use to connect deepset Cloud to your application.

### Example Usage

```python
import deepset_cloud
import dateutil.parser
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.CreateToken(
    expires_at=dateutil.parser.isoparse('2022-05-20T13:30:46.463Z'),
)

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.api_token_result is not None:
    # handle response
```

## list

Returns all API keys present in deepset Cloud together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListTokensAPIV1TokenGetRequest(
    after='29396fea-7596-4eb1-8faa-a2352c595590',
    before='7aff1a3a-2fa9-4467-b392-51aa52c3f5ad',
    limit=13571,
    page_number=97101,
)

res = s.api_token.list(req, operations.ListTokensAPIV1TokenGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.token_pagination is not None:
    # handle response
```

## remove

Deletes the API key. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.RemoveTokenAPIV1TokenAPITokenIDDeleteRequest(
    api_token_id='9da1ffe7-8f09-47b0-874f-15471b5e6e13',
)

res = s.api_token.remove(req, operations.RemoveTokenAPIV1TokenAPITokenIDDeleteSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.remove_token_api_v1_token_api_token_id_delete_200_application_json_any is not None:
    # handle response
```
