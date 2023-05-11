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
    author='autem',
    node_type='nobis',
)

res = s.models.list(req, operations.ListModelAPIV1ModelGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.model_metas is not None:
    # handle response
```
