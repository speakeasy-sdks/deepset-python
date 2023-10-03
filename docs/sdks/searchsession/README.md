# SearchSession
(*search_session*)

### Available Operations

* [create](#create) - Create Search Session [private]

## create

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.search_session.create(workspace_name='online')

if res.search_session_post_response is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostResponse](../../models/operations/createsearchsessionapiv1workspacesworkspacenamesearchsessionspostresponse.md)**

