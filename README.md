# Deepset Cloud Python SDK

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/deepset-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.ListEvalRunsRequest(
    after='c184a429-302e-4aca-80db-f1718b882a50',
    before='80555741-9e79-40e2-b205-5dd402eb66ec',
    field=operations.Field.CREATED_BY,
    filter='Borders often Virginia',
    limit=460276,
    order=operations.Order.DESC,
    page_number=425334,
    select='Qatari calculating look',
    workspace_name='Convertible',
)

res = s.eval_run.list(req)

if res.eval_runs_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [api_token](docs/sdks/apitoken/README.md)

* [create_token](docs/sdks/apitoken/README.md#create_token) - Create Token
* [list](docs/sdks/apitoken/README.md#list) - Get Tokens [private]
* [remove](docs/sdks/apitoken/README.md#remove) - Remove Token [private]

### [document_store](docs/sdks/documentstore/README.md)

* [check_connection](docs/sdks/documentstore/README.md#check_connection) - Check Connection [private]
* [count_documents](docs/sdks/documentstore/README.md#count_documents) - Count Documents Stream [private]
* [get](docs/sdks/documentstore/README.md#get) - Get Document [private]
* [list_document_streams](docs/sdks/documentstore/README.md#list_document_streams) - Get All Documents Stream
* [list_documents](docs/sdks/documentstore/README.md#list_documents) - Get All Documents [private]
* [search](docs/sdks/documentstore/README.md#search) - Query Documents Stream

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

### [health](docs/sdks/health/README.md)

* [check](docs/sdks/health/README.md#check) - Health
* [get_openapi](docs/sdks/health/README.md#get_openapi) - Redirect

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

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - Get Model [private]

### [notebook](docs/sdks/notebook/README.md)

* [create](docs/sdks/notebook/README.md#create) - Post Notebook [private]
* [get_server_state](docs/sdks/notebook/README.md#get_server_state) - Get Jupyter Lab [private]
* [start](docs/sdks/notebook/README.md#start) - Start Jupyter Lab [private]

### [organization](docs/sdks/organization/README.md)

* [get](docs/sdks/organization/README.md#get) - Get Organization [private]
* [invite](docs/sdks/organization/README.md#invite) - Invite User To Organization [private]

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

### [user](docs/sdks/user/README.md)

* [delete](docs/sdks/user/README.md#delete) - Delete User [private]
* [get](docs/sdks/user/README.md#get) - Get User [private]
* [list](docs/sdks/user/README.md#list) - Get Users [private]
* [me](docs/sdks/user/README.md#me) - Read Users Me [private]
* [update_permission](docs/sdks/user/README.md#update_permission) - Update User Permission [private]

### [workspace](docs/sdks/workspace/README.md)

* [create](docs/sdks/workspace/README.md#create) - Create Workspace [private]
* [delete](docs/sdks/workspace/README.md#delete) - Delete Workspace [private]
* [get](docs/sdks/workspace/README.md#get) - Get Workspace [private]
* [get_stats](docs/sdks/workspace/README.md#get_stats) - Get Workspace Stats [private]
* [list](docs/sdks/workspace/README.md#list) - List Workspaces [private]
* [search_count](docs/sdks/workspace/README.md#search_count) - Search Count [private]
* [search_history](docs/sdks/workspace/README.md#search_history) - Search History [private]
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->



<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:


<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
