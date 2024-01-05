# APIToken
(*api_token*)

### Available Operations

* [create_token](#create_token) - Create Token
* [list](#list) - Get Tokens [private]
* [remove](#remove) - Remove Token [private]

## create_token

Creates the API key that you can use to connect deepset Cloud to your application.

### Example Usage

```python
import dateutil.parser
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud()

req = components.CreateToken()

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
))

if res.api_token_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.CreateToken](../../models/components/createtoken.md)                                             | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.CreateTokenAPIV1TokenPostSecurity](../../models/operations/createtokenapiv1tokenpostsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.CreateTokenAPIV1TokenPostResponse](../../models/operations/createtokenapiv1tokenpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## list

Returns all API keys present in deepset Cloud together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.api_token.list(after='c184a429-302e-4aca-80db-f1718b882a50', before='80555741-9e79-40e2-b205-5dd402eb66ec', limit=173090, page_number=951993)

if res.token_pagination is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                              | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Enter an ID if you want to see all entries after this ID.                                                            |
| `before`                                                                                                             | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Enter an ID if you want to see all entries before this ID.                                                           |
| `limit`                                                                                                              | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | How many entries do you want to display? Leaving this field empty keeps the default and max 10 results are returned. |
| `page_number`                                                                                                        | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Which page do you want to see? Type the number.                                                                      |


### Response

**[operations.ListTokensAPIV1TokenGetResponse](../../models/operations/listtokensapiv1tokengetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## remove

Deletes the API key. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.api_token.remove(api_token_id='a2f261fc-5692-4af6-b656-f6d45851282a')

if res.any is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_token_id`                                                                                                                                 | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | A unique identifier of the API token that you want to remove. You can run the Get Tokens endpoint to check the IDs of the existing API tokens. |


### Response

**[operations.RemoveTokenAPIV1TokenAPITokenIDDeleteResponse](../../models/operations/removetokenapiv1tokenapitokeniddeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
