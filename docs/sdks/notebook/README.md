# notebook

### Available Operations

* [create](#create) - Post Notebook [private]
* [get_server_state](#get_server_state) - Get Jupyter Lab [private]
* [start](#start) - Start Jupyter Lab [private]

## create

Creates a Jupyter notebook on the Jupyter server. You must have a server ready to create a notebook. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.PostNotebookAPIV1NotebookPostRequest(
    empty_class=shared.EmptyClass(),
    pipeline_id='523c7e0b-c717-48e4-b96f-2a70c688282a',
)

res = s.notebook.create(req, operations.PostNotebookAPIV1NotebookPostSecurity(
    http_bearer="",
))

if res.notebook is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostNotebookAPIV1NotebookPostRequest](../../models/operations/postnotebookapiv1notebookpostrequest.md)   | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.PostNotebookAPIV1NotebookPostSecurity](../../models/operations/postnotebookapiv1notebookpostsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.PostNotebookAPIV1NotebookPostResponse](../../models/operations/postnotebookapiv1notebookpostresponse.md)**


## get_server_state

Returns the state of the Jupyter lab server. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.notebook.get_server_state(operations.GetJupyterLabAPIV1NotebookServerGetSecurity(
    http_bearer="",
))

if res.server is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                       | [operations.GetJupyterLabAPIV1NotebookServerGetSecurity](../../models/operations/getjupyterlabapiv1notebookservergetsecurity.md) | :heavy_check_mark:                                                                                                               | The security requirements to use for the request.                                                                                |


### Response

**[operations.GetJupyterLabAPIV1NotebookServerGetResponse](../../models/operations/getjupyterlabapiv1notebookservergetresponse.md)**


## start

Opens the Jupyter lab. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.NotebookServerPost(
    server_type=shared.NotebookServerPostServerType.GPU_SERVER,
)

res = s.notebook.start(req, operations.StartJupyterLabAPIV1NotebookServerPostSecurity(
    http_bearer="",
))

if res.start_jupyter_lab_api_v1_notebook_server_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [shared.NotebookServerPost](../../models/shared/notebookserverpost.md)                                                                 | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `security`                                                                                                                             | [operations.StartJupyterLabAPIV1NotebookServerPostSecurity](../../models/operations/startjupyterlabapiv1notebookserverpostsecurity.md) | :heavy_check_mark:                                                                                                                     | The security requirements to use for the request.                                                                                      |


### Response

**[operations.StartJupyterLabAPIV1NotebookServerPostResponse](../../models/operations/startjupyterlabapiv1notebookserverpostresponse.md)**

