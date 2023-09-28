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
import deepset_cloud
import dateutil.parser
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.CreateToken(
    expires_at=dateutil.parser.isoparse('2022-01-11T05:45:42.485Z'),
)

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="",
))

if res.api_token_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [shared.CreateToken](../../models/shared/createtoken.md)                                                     | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.CreateTokenAPIV1TokenPostSecurity](../../models/operations/createtokenapiv1tokenpostsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.CreateTokenAPIV1TokenPostResponse](../../models/operations/createtokenapiv1tokenpostresponse.md)**


## list

Returns all API keys present in deepset Cloud together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.api_token.list(after='fe78f097-b007-44f1-9471-b5e6e13b99d4', before='88e1e91e-450a-4d2a-bd44-269802d502a9', limit=270008, page_number=703737)

if res.token_pagination is not None:
    # handle response
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


## remove

Deletes the API key. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.api_token.remove(api_token_id='b4f63c96-9e9a-43ef-a77d-fb14cd66ae39')

if res.remove_token_api_v1_token_api_token_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_token_id`                                                                                                                                 | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | A unique identifier of the API token that you want to remove. You can run the Get Tokens endpoint to check the IDs of the existing API tokens. |


### Response

**[operations.RemoveTokenAPIV1TokenAPITokenIDDeleteResponse](../../models/operations/removetokenapiv1tokenapitokeniddeleteresponse.md)**

