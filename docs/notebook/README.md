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
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.PostNotebookAPIV1NotebookPostRequest(
    request_body={
        "commodi": 'sapiente',
        "dolores": 'deserunt',
        "molestiae": 'accusantium',
    },
    pipeline_id='c688282a-a482-4562-b222-e9817ee17cbe',
)

res = s.notebook.create(req, operations.PostNotebookAPIV1NotebookPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.notebook is not None:
    # handle response
```

## get_server_state

Returns the state of the Jupyter lab server. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.notebook.get_server_state(operations.GetJupyterLabAPIV1NotebookServerGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.server is not None:
    # handle response
```

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
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.start_jupyter_lab_api_v1_notebook_server_post_200_application_json_any is not None:
    # handle response
```
