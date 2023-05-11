# search_session

### Available Operations

* [create](#create) - Create Search Session [private]

## create

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostRequest(
    workspace_name='fugiat',
)

res = s.search_session.create(req, operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.search_session_post_response is not None:
    # handle response
```
