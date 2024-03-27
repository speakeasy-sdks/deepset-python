# ModelRegistryToken
(*model_registry_token*)

### Available Operations

* [get](#get) - Get Token [private]
* [~~get_token_deprecated~~](#get_token_deprecated) - Get Token Deprecated [private] :warning: **Deprecated**
* [list](#list) - Get Tokens [private]
* [remove](#remove) - Remove Token [private]
* [~~remove_token_deprecated~~](#remove_token_deprecated) - Remove Token Deprecated [private] :warning: **Deprecated**
* [save](#save) - Save Token [private]
* [~~save_token_deprecated~~](#save_token_deprecated) - Save Token Deprecated [private] :warning: **Deprecated**
* [update](#update) - Update Token [private]
* [~~update_token_deprecated~~](#update_token_deprecated) - Update Token Deprecated [private] :warning: **Deprecated**

## get

Returns the model token. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.get(provider=operations.ModelProvider.COHERE)

if res.model_registry_token is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `provider`                                                           | [operations.ModelProvider](../../models/operations/modelprovider.md) | :heavy_check_mark:                                                   | The provider of the model registry                                   |


### Response

**[operations.GetTokenAPIV1ModelRegistryTokensProviderGetResponse](../../models/operations/gettokenapiv1modelregistrytokensprovidergetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## ~~get_token_deprecated~~

Returns the Hugging Face model token. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.get_token_deprecated()

if res.model_registry_token is not None:
    # handle response
    pass

```


### Response

**[operations.GetTokenDeprecatedAPIV1ModelRegistryTokenGetResponse](../../models/operations/gettokendeprecatedapiv1modelregistrytokengetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

Returns the model tokens. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.list()

if res.response_get_tokens_api_v1_model_registry_tokens_get is not None:
    # handle response
    pass

```


### Response

**[operations.ListTokensAPIV1ModelRegistryTokensGetResponse](../../models/operations/listtokensapiv1modelregistrytokensgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove

Deletes the model token from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.remove(provider=operations.PathParamModelProvider.COHERE)

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `provider`                                                                             | [operations.PathParamModelProvider](../../models/operations/pathparammodelprovider.md) | :heavy_check_mark:                                                                     | The provider of the model registry                                                     |


### Response

**[operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteResponse](../../models/operations/removetokenapiv1modelregistrytokensproviderdeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## ~~remove_token_deprecated~~

Deletes the Hugging Face model token from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.remove_token_deprecated()

if res.any is not None:
    # handle response
    pass

```


### Response

**[operations.RemoveTokenDeprecatedAPIV1ModelRegistryTokenDeleteResponse](../../models/operations/removetokendeprecatedapiv1modelregistrytokendeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## save

Imports your model token and saves it in deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.save(create_model_registry_token=components.CreateModelRegistryToken(
    token='<value>',
), provider=operations.SaveTokenAPIV1ModelRegistryTokensProviderPostPathParamModelProvider.HUGGINGFACE)

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_model_registry_token`                                                                                                                                                    | [components.CreateModelRegistryToken](../../models/components/createmodelregistrytoken.md)                                                                                       | :heavy_check_mark:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `provider`                                                                                                                                                                       | [operations.SaveTokenAPIV1ModelRegistryTokensProviderPostPathParamModelProvider](../../models/operations/savetokenapiv1modelregistrytokensproviderpostpathparammodelprovider.md) | :heavy_check_mark:                                                                                                                                                               | The provider of the model registry                                                                                                                                               |


### Response

**[operations.SaveTokenAPIV1ModelRegistryTokensProviderPostResponse](../../models/operations/savetokenapiv1modelregistrytokensproviderpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## ~~save_token_deprecated~~

Imports your Hugging Face model token and saves it in deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.CreateModelRegistryToken(
    token='<value>',
)

res = s.model_registry_token.save_token_deprecated(req)

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreateModelRegistryToken](../../models/components/createmodelregistrytoken.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.SaveTokenDeprecatedAPIV1ModelRegistryTokenPostResponse](../../models/operations/savetokendeprecatedapiv1modelregistrytokenpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## update

Replaces the current model token with a new one. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model_registry_token.update(update_model_registry_token=components.UpdateModelRegistryToken(
    token='<value>',
), provider=operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutPathParamModelProvider.COHERE)

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `update_model_registry_token`                                                                                                                                                      | [components.UpdateModelRegistryToken](../../models/components/updatemodelregistrytoken.md)                                                                                         | :heavy_check_mark:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `provider`                                                                                                                                                                         | [operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutPathParamModelProvider](../../models/operations/updatetokenapiv1modelregistrytokensproviderputpathparammodelprovider.md) | :heavy_check_mark:                                                                                                                                                                 | The provider of the model registry                                                                                                                                                 |


### Response

**[operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutResponse](../../models/operations/updatetokenapiv1modelregistrytokensproviderputresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## ~~update_token_deprecated~~

Replaces the current Hugging Face model token with a new one. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.UpdateModelRegistryToken(
    token='<value>',
)

res = s.model_registry_token.update_token_deprecated(req)

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.UpdateModelRegistryToken](../../models/components/updatemodelregistrytoken.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateTokenDeprecatedAPIV1ModelRegistryTokenPutResponse](../../models/operations/updatetokendeprecatedapiv1modelregistrytokenputresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
