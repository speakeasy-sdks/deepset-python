# ModelRegistryToken

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
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.get(provider=operations.GetTokenAPIV1ModelRegistryTokensProviderGetProviderModelProvider.OPENAI)

if res.model_registry_token is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider`                                                                                                                                                                 | [operations.GetTokenAPIV1ModelRegistryTokensProviderGetProviderModelProvider](../../models/operations/gettokenapiv1modelregistrytokensprovidergetprovidermodelprovider.md) | :heavy_check_mark:                                                                                                                                                         | The provider of the model registry                                                                                                                                         |


### Response

**[operations.GetTokenAPIV1ModelRegistryTokensProviderGetResponse](../../models/operations/gettokenapiv1modelregistrytokensprovidergetresponse.md)**


## ~~get_token_deprecated~~

Returns the Hugging Face model token. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.get_token_deprecated()

if res.model_registry_token is not None:
    # handle response
```


### Response

**[operations.GetTokenDeprecatedAPIV1ModelRegistryTokenGetResponse](../../models/operations/gettokendeprecatedapiv1modelregistrytokengetresponse.md)**


## list

Returns the model tokens. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.list()

if res.model_registry_tokens is not None:
    # handle response
```


### Response

**[operations.ListTokensAPIV1ModelRegistryTokensGetResponse](../../models/operations/listtokensapiv1modelregistrytokensgetresponse.md)**


## remove

Deletes the model token from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.remove(provider=operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteProviderModelProvider.COHERE)

if res.remove_token_api_v1_model_registry_tokens_provider_delete_202_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider`                                                                                                                                                                             | [operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteProviderModelProvider](../../models/operations/removetokenapiv1modelregistrytokensproviderdeleteprovidermodelprovider.md) | :heavy_check_mark:                                                                                                                                                                     | The provider of the model registry                                                                                                                                                     |


### Response

**[operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteResponse](../../models/operations/removetokenapiv1modelregistrytokensproviderdeleteresponse.md)**


## ~~remove_token_deprecated~~

Deletes the Hugging Face model token from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.remove_token_deprecated()

if res.remove_token_deprecated_api_v1_model_registry_token_delete_202_application_json_any is not None:
    # handle response
```


### Response

**[operations.RemoveTokenDeprecatedAPIV1ModelRegistryTokenDeleteResponse](../../models/operations/removetokendeprecatedapiv1modelregistrytokendeleteresponse.md)**


## save

Imports your model token and saves it in deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.save(create_model_registry_token=shared.CreateModelRegistryToken(
    token='nam',
), provider=operations.SaveTokenAPIV1ModelRegistryTokensProviderPostProviderModelProvider.COHERE)

if res.save_token_api_v1_model_registry_tokens_provider_post_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `create_model_registry_token`                                                                                                                                                  | [shared.CreateModelRegistryToken](../../models/shared/createmodelregistrytoken.md)                                                                                             | :heavy_check_mark:                                                                                                                                                             | N/A                                                                                                                                                                            |
| `provider`                                                                                                                                                                     | [operations.SaveTokenAPIV1ModelRegistryTokensProviderPostProviderModelProvider](../../models/operations/savetokenapiv1modelregistrytokensproviderpostprovidermodelprovider.md) | :heavy_check_mark:                                                                                                                                                             | The provider of the model registry                                                                                                                                             |


### Response

**[operations.SaveTokenAPIV1ModelRegistryTokensProviderPostResponse](../../models/operations/savetokenapiv1modelregistrytokensproviderpostresponse.md)**


## ~~save_token_deprecated~~

Imports your Hugging Face model token and saves it in deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = shared.CreateModelRegistryToken(
    token='aliquid',
)

res = s.model_registry_token.save_token_deprecated(req)

if res.save_token_deprecated_api_v1_model_registry_token_post_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.CreateModelRegistryToken](../../models/shared/createmodelregistrytoken.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.SaveTokenDeprecatedAPIV1ModelRegistryTokenPostResponse](../../models/operations/savetokendeprecatedapiv1modelregistrytokenpostresponse.md)**


## update

Replaces the current model token with a new one. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.model_registry_token.update(update_model_registry_token=shared.UpdateModelRegistryToken(
    token='quasi',
), provider=operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutProviderModelProvider.COHERE)

if res.update_token_api_v1_model_registry_tokens_provider_put_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `update_model_registry_token`                                                                                                                                                    | [shared.UpdateModelRegistryToken](../../models/shared/updatemodelregistrytoken.md)                                                                                               | :heavy_check_mark:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `provider`                                                                                                                                                                       | [operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutProviderModelProvider](../../models/operations/updatetokenapiv1modelregistrytokensproviderputprovidermodelprovider.md) | :heavy_check_mark:                                                                                                                                                               | The provider of the model registry                                                                                                                                               |


### Response

**[operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutResponse](../../models/operations/updatetokenapiv1modelregistrytokensproviderputresponse.md)**


## ~~update_token_deprecated~~

Replaces the current Hugging Face model token with a new one. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = shared.UpdateModelRegistryToken(
    token='vel',
)

res = s.model_registry_token.update_token_deprecated(req)

if res.update_token_deprecated_api_v1_model_registry_token_put_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.UpdateModelRegistryToken](../../models/shared/updatemodelregistrytoken.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateTokenDeprecatedAPIV1ModelRegistryTokenPutResponse](../../models/operations/updatetokendeprecatedapiv1modelregistrytokenputresponse.md)**

