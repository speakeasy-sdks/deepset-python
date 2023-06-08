# model_registry_token

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

s = deepset_cloud.DeepsetCloud()

req = operations.GetTokenAPIV1ModelRegistryTokensProviderGetRequest(
    provider=operations.GetTokenAPIV1ModelRegistryTokensProviderGetProviderModelProvider.HUGGINGFACE,
)

res = s.model_registry_token.get(req, operations.GetTokenAPIV1ModelRegistryTokensProviderGetSecurity(
    http_bearer="",
))

if res.model_registry_token is not None:
    # handle response
```

## ~~get_token_deprecated~~

Returns the Hugging Face model token. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.model_registry_token.get_token_deprecated(operations.GetTokenDeprecatedAPIV1ModelRegistryTokenGetSecurity(
    http_bearer="",
))

if res.model_registry_token is not None:
    # handle response
```

## list

Returns the model tokens. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.model_registry_token.list(operations.ListTokensAPIV1ModelRegistryTokensGetSecurity(
    http_bearer="",
))

if res.model_registry_tokens is not None:
    # handle response
```

## remove

Deletes the model token from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteRequest(
    provider=operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteProviderModelProvider.COHERE,
)

res = s.model_registry_token.remove(req, operations.RemoveTokenAPIV1ModelRegistryTokensProviderDeleteSecurity(
    http_bearer="",
))

if res.remove_token_api_v1_model_registry_tokens_provider_delete_202_application_json_any is not None:
    # handle response
```

## ~~remove_token_deprecated~~

Deletes the Hugging Face model token from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.model_registry_token.remove_token_deprecated(operations.RemoveTokenDeprecatedAPIV1ModelRegistryTokenDeleteSecurity(
    http_bearer="",
))

if res.remove_token_deprecated_api_v1_model_registry_token_delete_202_application_json_any is not None:
    # handle response
```

## save

Imports your model token and saves it in deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.SaveTokenAPIV1ModelRegistryTokensProviderPostRequest(
    create_model_registry_token=shared.CreateModelRegistryToken(
        token='quod',
    ),
    provider=operations.SaveTokenAPIV1ModelRegistryTokensProviderPostProviderModelProvider.OPENAI,
)

res = s.model_registry_token.save(req, operations.SaveTokenAPIV1ModelRegistryTokensProviderPostSecurity(
    http_bearer="",
))

if res.save_token_api_v1_model_registry_tokens_provider_post_201_application_json_any is not None:
    # handle response
```

## ~~save_token_deprecated~~

Imports your Hugging Face model token and saves it in deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.CreateModelRegistryToken(
    token='inventore',
)

res = s.model_registry_token.save_token_deprecated(req, operations.SaveTokenDeprecatedAPIV1ModelRegistryTokenPostSecurity(
    http_bearer="",
))

if res.save_token_deprecated_api_v1_model_registry_token_post_201_application_json_any is not None:
    # handle response
```

## update

Replaces the current model token with a new one. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutRequest(
    update_model_registry_token=shared.UpdateModelRegistryToken(
        token='nihil',
    ),
    provider=operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutProviderModelProvider.OPENAI,
)

res = s.model_registry_token.update(req, operations.UpdateTokenAPIV1ModelRegistryTokensProviderPutSecurity(
    http_bearer="",
))

if res.update_token_api_v1_model_registry_tokens_provider_put_201_application_json_any is not None:
    # handle response
```

## ~~update_token_deprecated~~

Replaces the current Hugging Face model token with a new one. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.UpdateModelRegistryToken(
    token='accusamus',
)

res = s.model_registry_token.update_token_deprecated(req, operations.UpdateTokenDeprecatedAPIV1ModelRegistryTokenPutSecurity(
    http_bearer="",
))

if res.update_token_deprecated_api_v1_model_registry_token_put_201_application_json_any is not None:
    # handle response
```
