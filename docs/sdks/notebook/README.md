# Notebook
(*notebook*)

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

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.notebook.create(empty_class=shared.EmptyClass(), pipeline_id='b95bc0ab-3c20-4c4f-b789-fd871f99dd2e')

if res.notebook is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `empty_class`                                                                          | [Optional[shared.EmptyClass]](../../models/shared/emptyclass.md)                       | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `pipeline_id`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | A unique identifier of a pipeline. You can obtain it from the List Pipelines endpoint. |


### Response

**[operations.PostNotebookAPIV1NotebookPostResponse](../../models/operations/postnotebookapiv1notebookpostresponse.md)**


## get_server_state

Returns the state of the Jupyter lab server. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.notebook.get_server_state()

if res.server is not None:
    # handle response
```


### Response

**[operations.GetJupyterLabAPIV1NotebookServerGetResponse](../../models/operations/getjupyterlabapiv1notebookservergetresponse.md)**


## start

Opens the Jupyter lab. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = shared.NotebookServerPost(
    server_type=shared.NotebookServerPostServerType.UNKNOWN,
)

res = s.notebook.start(req)

if res.start_jupyter_lab_api_v1_notebook_server_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.NotebookServerPost](../../models/shared/notebookserverpost.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.StartJupyterLabAPIV1NotebookServerPostResponse](../../models/operations/startjupyterlabapiv1notebookserverpostresponse.md)**

