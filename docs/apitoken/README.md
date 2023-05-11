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
    expires_at=dateutil.parser.isoparse('2021-04-24T16:27:50.833Z'),
)

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    after='9d8d69a6-74e0-4f46-bcc8-796ed151a05d',
    before='fc2ddf7c-c78c-4a1b-a928-fc816742cb73',
    limit=568434,
    page_number=135218,
)

res = s.api_token.list(req, operations.ListTokensAPIV1TokenGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    api_token_id='05929396-fea7-4596-ab10-faaa2352c595',
)

res = s.api_token.remove(req, operations.RemoveTokenAPIV1TokenAPITokenIDDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.remove_token_api_v1_token_api_token_id_delete_200_application_json_any is not None:
    # handle response
```
