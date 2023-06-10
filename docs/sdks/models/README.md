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

req = operations.ListModelAPIV1ModelGetRequest(
    author='tempora',
    node_type='debitis',
)

res = s.models.list(req, operations.ListModelAPIV1ModelGetSecurity(
    http_bearer="",
))

if res.model_metas is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListModelAPIV1ModelGetRequest](../../models/operations/listmodelapiv1modelgetrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListModelAPIV1ModelGetSecurity](../../models/operations/listmodelapiv1modelgetsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListModelAPIV1ModelGetResponse](../../models/operations/listmodelapiv1modelgetresponse.md)**

