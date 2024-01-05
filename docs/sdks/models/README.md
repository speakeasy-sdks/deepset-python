# Models
(*models*)

### Available Operations

* [list](#list) - Get Model [private]

## list

Returns a list of models available for the specified node_type. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.models.list(author='string', node_type='string')

if res.response_get_model_api_v1_model_get is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `author`                                                                                        | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Author from Hugging Face. The author of the model 'deepset/minilm-uncased-squad2' is 'deepset'. |
| `node_type`                                                                                     | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Type of the node. E.g. 'PromptNode'                                                             |


### Response

**[operations.ListModelAPIV1ModelGetResponse](../../models/operations/listmodelapiv1modelgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
