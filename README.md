# Deepset Cloud Python SDK

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/deepset-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvalRunsRequest(
    workspace_name='string',
)

res = s.eval_run.list(req)

if res.eval_runs_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [health](docs/sdks/health/README.md)

* [check](docs/sdks/health/README.md#check) - Health
* [get_openapi](docs/sdks/health/README.md#get_openapi) - Redirect

### [user](docs/sdks/user/README.md)

* [delete](docs/sdks/user/README.md#delete) - Delete User [private]
* [get](docs/sdks/user/README.md#get) - Get User [private]
* [list](docs/sdks/user/README.md#list) - Get Users [private]
* [me](docs/sdks/user/README.md#me) - Read Users Me [private]
* [update_permission](docs/sdks/user/README.md#update_permission) - Update User Permission [private]

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - Get Model [private]

### [model_registry_token](docs/sdks/modelregistrytoken/README.md)

* [get](docs/sdks/modelregistrytoken/README.md#get) - Get Token [private]
* [~~get_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#get_token_deprecated) - Get Token Deprecated [private] :warning: **Deprecated**
* [list](docs/sdks/modelregistrytoken/README.md#list) - Get Tokens [private]
* [remove](docs/sdks/modelregistrytoken/README.md#remove) - Remove Token [private]
* [~~remove_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#remove_token_deprecated) - Remove Token Deprecated [private] :warning: **Deprecated**
* [save](docs/sdks/modelregistrytoken/README.md#save) - Save Token [private]
* [~~save_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#save_token_deprecated) - Save Token Deprecated [private] :warning: **Deprecated**
* [update](docs/sdks/modelregistrytoken/README.md#update) - Update Token [private]
* [~~update_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#update_token_deprecated) - Update Token Deprecated [private] :warning: **Deprecated**

### [notebook](docs/sdks/notebook/README.md)

* [create](docs/sdks/notebook/README.md#create) - Post Notebook [private]
* [get_server_state](docs/sdks/notebook/README.md#get_server_state) - Get Jupyter Lab [private]
* [start](docs/sdks/notebook/README.md#start) - Start Jupyter Lab [private]

### [organization](docs/sdks/organization/README.md)

* [get](docs/sdks/organization/README.md#get) - Get Organization [private]
* [invite](docs/sdks/organization/README.md#invite) - Invite User To Organization [private]

### [api_token](docs/sdks/apitoken/README.md)

* [create_token](docs/sdks/apitoken/README.md#create_token) - Create Token
* [list](docs/sdks/apitoken/README.md#list) - Get Tokens [private]
* [remove](docs/sdks/apitoken/README.md#remove) - Remove Token [private]

### [workspace](docs/sdks/workspace/README.md)

* [create](docs/sdks/workspace/README.md#create) - Create Workspace [private]
* [delete](docs/sdks/workspace/README.md#delete) - Delete Workspace [private]
* [get](docs/sdks/workspace/README.md#get) - Get Workspace [private]
* [get_stats](docs/sdks/workspace/README.md#get_stats) - Get Workspace Stats [private]
* [list](docs/sdks/workspace/README.md#list) - List Workspaces [private]
* [search_count](docs/sdks/workspace/README.md#search_count) - Search Count [private]
* [search_history](docs/sdks/workspace/README.md#search_history) - Search History [private]

### [eval_run](docs/sdks/evalrun/README.md)

* [create_eval_run](docs/sdks/evalrun/README.md#create_eval_run) - Create Eval Run
* [create_tag](docs/sdks/evalrun/README.md#create_tag) - Create Tag [private]
* [delete](docs/sdks/evalrun/README.md#delete) - Delete Eval Run
* [delete_tag](docs/sdks/evalrun/README.md#delete_tag) - Delete Tag [private]
* [get](docs/sdks/evalrun/README.md#get) - Get Eval Run
* [get_node_eval_predictions](docs/sdks/evalrun/README.md#get_node_eval_predictions) - Get Node Eval Predictions
* [list](docs/sdks/evalrun/README.md#list) - Get Eval Runs
* [list_tags](docs/sdks/evalrun/README.md#list_tags) - Get Tags [private]
* [start](docs/sdks/evalrun/README.md#start) - Start Eval Run
* [update](docs/sdks/evalrun/README.md#update) - Edit Eval Run
* [update_tag](docs/sdks/evalrun/README.md#update_tag) - Update Tag [private]

### [evaluation_set](docs/sdks/evaluationset/README.md)

* [delete](docs/sdks/evaluationset/README.md#delete) - Delete Evaluation Set
* [get](docs/sdks/evaluationset/README.md#get) - Get Evaluation Set
* [get_csv](docs/sdks/evaluationset/README.md#get_csv) - Get Evaluation Set Csv File
* [import_evaluation_set](docs/sdks/evaluationset/README.md#import_evaluation_set) - Import Evaluation Set
* [list](docs/sdks/evaluationset/README.md#list) - Get Evaluation Sets
* [retrigger](docs/sdks/evaluationset/README.md#retrigger) - Retrigger Label Matching

### [file](docs/sdks/file/README.md)

* [delete_multi](docs/sdks/file/README.md#delete_multi) - Delete Files
* [delete_single](docs/sdks/file/README.md#delete_single) - Delete File
* [get](docs/sdks/file/README.md#get) - Get File
* [get_document](docs/sdks/file/README.md#get_document) - Get Document
* [get_meta_data](docs/sdks/file/README.md#get_meta_data) - Get File Meta
* [list](docs/sdks/file/README.md#list) - List Files
* [update_meta_data](docs/sdks/file/README.md#update_meta_data) - Update File Meta
* [upload](docs/sdks/file/README.md#upload) - Upload File

### [document_store](docs/sdks/documentstore/README.md)

* [check_connection](docs/sdks/documentstore/README.md#check_connection) - Check Connection [private]
* [count_documents](docs/sdks/documentstore/README.md#count_documents) - Count Documents Stream [private]
* [get](docs/sdks/documentstore/README.md#get) - Get Document [private]
* [list_document_streams](docs/sdks/documentstore/README.md#list_document_streams) - Get All Documents Stream
* [list_documents](docs/sdks/documentstore/README.md#list_documents) - Get All Documents [private]
* [search](docs/sdks/documentstore/README.md#search) - Query Documents Stream

### [pipeline](docs/sdks/pipeline/README.md)

* [add_feedback](docs/sdks/pipeline/README.md#add_feedback) - Add Feedback
* [create](docs/sdks/pipeline/README.md#create) - Create Pipeline
* [delete](docs/sdks/pipeline/README.md#delete) - Delete Pipeline
* [deploy](docs/sdks/pipeline/README.md#deploy) - Deploy Pipeline
* [get](docs/sdks/pipeline/README.md#get) - Get Pipeline
* [get_feedback](docs/sdks/pipeline/README.md#get_feedback) - Get Pipeline Feedback
* [get_files](docs/sdks/pipeline/README.md#get_files) - Get Pipeline Files
* [get_indexing](docs/sdks/pipeline/README.md#get_indexing) - Get Pipeline Indexing
* [get_json](docs/sdks/pipeline/README.md#get_json) - Get Pipeline Yaml As Json
* [get_metadata](docs/sdks/pipeline/README.md#get_metadata) - Get Pipeline Index Metadata [private]
* [get_metadata_field_values](docs/sdks/pipeline/README.md#get_metadata_field_values) - Get Pipeline Metadata Field Values [private]
* [get_min_max_aggregation_metadata](docs/sdks/pipeline/README.md#get_min_max_aggregation_metadata) - Get Pipeline Min Max Aggregation Metadata [private]
* [get_stats](docs/sdks/pipeline/README.md#get_stats) - Get Pipeline Stats
* [get_yaml](docs/sdks/pipeline/README.md#get_yaml) - Get Pipeline Yaml
* [list](docs/sdks/pipeline/README.md#list) - List Pipelines
* [search](docs/sdks/pipeline/README.md#search) - Search
* [search_history](docs/sdks/pipeline/README.md#search_history) - Pipeline Search History [private]
* [set_default](docs/sdks/pipeline/README.md#set_default) - Set Default Pipeline
* [undeploy](docs/sdks/pipeline/README.md#undeploy) - Undeploy Pipeline
* [update_yaml](docs/sdks/pipeline/README.md#update_yaml) - Update Pipeline Yaml

### [search_session](docs/sdks/searchsession/README.md)

* [create](docs/sdks/searchsession/README.md#create) - Create Search Session [private]

### [shared_prototype](docs/sdks/sharedprototype/README.md)

* [create](docs/sdks/sharedprototype/README.md#create) - Create Prototype [private]
* [create_external_user](docs/sdks/sharedprototype/README.md#create_external_user) - Create External User [private]
* [get](docs/sdks/sharedprototype/README.md#get) - Get Shared Prototype [private]
* [list](docs/sdks/sharedprototype/README.md#list) - List Prototypes [private]
* [revoke](docs/sdks/sharedprototype/README.md#revoke) - Revoke Shared Prototype [private]
* [update](docs/sdks/sharedprototype/README.md#update) - Edit Shared Prototype [private]

### [upload_session](docs/sdks/uploadsession/README.md)

* [close](docs/sdks/uploadsession/README.md#close) - Close Session
* [create](docs/sdks/uploadsession/README.md#create) - Create Upload Session
* [get_files](docs/sdks/uploadsession/README.md#get_files) - Get Session Files
* [get_status](docs/sdks/uploadsession/README.md#get_status) - Get Session Status
* [list](docs/sdks/uploadsession/README.md#list) - Get Upload Sessions
<!-- End SDK Available Operations -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

### Example

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = None
try:
    res = s.user.delete(user_id='8db863f6-ef9b-413a-8a70-cb816b33de6b')
except (errors.HTTPValidationError) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.any is not None:
    # handle response
    pass
```

<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.cloud.deepset.ai` | None |

#### Example

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    server_idx=0,
    http_bearer="",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    server_url="https://api.cloud.deepset.ai",
    http_bearer="",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import deepset_cloud
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = deepset_cloud.DeepsetCloud(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `http_bearer` | http          | HTTP Bearer   |

To authenticate with the API the `http_bearer` parameter must be set when initializing the SDK client instance. For example:
```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import dateutil.parser
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud()

req = components.CreateToken()

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="",
))

if res.api_token_result is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
