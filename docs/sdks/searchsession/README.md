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


res = s.search_session.create(operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostSecurity(
    http_bearer="",
), 'rem')

if res.search_session_post_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                   | [operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostSecurity](../../models/operations/createsearchsessionapiv1workspacesworkspacenamesearchsessionspostsecurity.md) | :heavy_check_mark:                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                            |
| `workspace_name`                                                                                                                                                                             | *str*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | Type the name of the workspace.                                                                                                                                                              |


### Response

**[operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostResponse](../../models/operations/createsearchsessionapiv1workspacesworkspacenamesearchsessionspostresponse.md)**

