# Notebook
(*.notebook*)

### Available Operations

* [create](#create) - Post Notebook [private]
* [get_server_state](#get_server_state) - Get Jupyter Lab [private]
* [start](#start) - Start Jupyter Lab [private]

## create

Creates a Jupyter notebook on the Jupyter server. You must have a server ready to create a notebook. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.notebook.create(empty_class=components.EmptyClass(), pipeline_id='77ad642c-1fc6-4fe0-b241-bcdd89dc7fa5')

if res.notebook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `empty_class`                                                                          | [Optional[components.EmptyClass]](../../models/shared/emptyclass.md)                   | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `pipeline_id`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | A unique identifier of a pipeline. You can obtain it from the List Pipelines endpoint. |


### Response

**[operations.PostNotebookAPIV1NotebookPostResponse](../../models/operations/postnotebookapiv1notebookpostresponse.md)**


## get_server_state

Returns the state of the Jupyter lab server. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.notebook.get_server_state()

if res.server is not None:
    # handle response
    pass
```


### Response

**[operations.GetJupyterLabAPIV1NotebookServerGetResponse](../../models/operations/getjupyterlabapiv1notebookservergetresponse.md)**


## start

Opens the Jupyter lab. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = components.NotebookServerPost()

res = s.notebook.start(req)

if res.any is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.NotebookServerPost](../../models/shared/notebookserverpost.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.StartJupyterLabAPIV1NotebookServerPostResponse](../../models/operations/startjupyterlabapiv1notebookserverpostresponse.md)**

