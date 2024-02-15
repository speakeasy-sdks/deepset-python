# SearchSession
(*search_session*)

### Available Operations

* [create](#create) - Create Search Session [private]

## create

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_session.create(workspace_name='<value>')

if res.search_session_post_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.CreateSearchSessionAPIV1WorkspacesWorkspaceNameSearchSessionsPostResponse](../../models/operations/createsearchsessionapiv1workspacesworkspacenamesearchsessionspostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
