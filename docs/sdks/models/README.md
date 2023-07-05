# models

### Available Operations

* [list](#list) - Get Model [private]

## list

Returns a list of models available for the specified node_type. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.models.list(operations.ListModelAPIV1ModelGetSecurity(
    http_bearer="",
), 'tempora', 'debitis')

if res.model_metas is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `security`                                                                                             | [operations.ListModelAPIV1ModelGetSecurity](../../models/operations/listmodelapiv1modelgetsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |
| `author`                                                                                               | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Author from Hugging Face. The author of the model 'deepset/minilm-uncased-squad2' is 'deepset'.        |
| `node_type`                                                                                            | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Type of the node. E.g. 'PromptNode'                                                                    |


### Response

**[operations.ListModelAPIV1ModelGetResponse](../../models/operations/listmodelapiv1modelgetresponse.md)**
