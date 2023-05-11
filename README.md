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
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetRequest(
    after='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
    before='a05dfc2d-df7c-4c78-8a1b-a928fc816742',
    field=operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetFieldFieldEnum.INTEGRATED_RECALL_SINGLE_HIT,
    filter='cum',
    limit=456150,
    order=operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetOrderOrderEnum.ASC,
    page_number=568434,
    select='aspernatur',
    workspace_name='perferendis',
)

res = s.eval_run.list(req, operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.eval_runs_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [api_token](docs/apitoken/README.md)

* [create_token](docs/apitoken/README.md#create_token) - Create Token
* [list](docs/apitoken/README.md#list) - Get Tokens [private]
* [remove](docs/apitoken/README.md#remove) - Remove Token [private]

### [document_store](docs/documentstore/README.md)

* [check_connection](docs/documentstore/README.md#check_connection) - Check Connection [private]
* [count_documents](docs/documentstore/README.md#count_documents) - Count Documents Stream [private]
* [get](docs/documentstore/README.md#get) - Get Document [private]
* [list_document_streams](docs/documentstore/README.md#list_document_streams) - Get All Documents Stream
* [list_documents](docs/documentstore/README.md#list_documents) - Get All Documents [private]
* [search](docs/documentstore/README.md#search) - Query Documents Stream

### [eval_run](docs/evalrun/README.md)

* [create_eval_run](docs/evalrun/README.md#create_eval_run) - Create Eval Run
* [create_tag](docs/evalrun/README.md#create_tag) - Create Tag [private]
* [delete](docs/evalrun/README.md#delete) - Delete Eval Run
* [delete_tag](docs/evalrun/README.md#delete_tag) - Delete Tag [private]
* [get](docs/evalrun/README.md#get) - Get Eval Run
* [get_node_eval_predictions](docs/evalrun/README.md#get_node_eval_predictions) - Get Node Eval Predictions
* [list](docs/evalrun/README.md#list) - Get Eval Runs
* [list_tags](docs/evalrun/README.md#list_tags) - Get Tags [private]
* [start](docs/evalrun/README.md#start) - Start Eval Run
* [update](docs/evalrun/README.md#update) - Edit Eval Run
* [update_tag](docs/evalrun/README.md#update_tag) - Update Tag [private]

### [evaluation_set](docs/evaluationset/README.md)

* [delete](docs/evaluationset/README.md#delete) - Delete Evaluation Set
* [get](docs/evaluationset/README.md#get) - Get Evaluation Set
* [get_csv](docs/evaluationset/README.md#get_csv) - Get Evaluation Set Csv File
* [import_evaluation_set](docs/evaluationset/README.md#import_evaluation_set) - Import Evaluation Set
* [list](docs/evaluationset/README.md#list) - Get Evaluation Sets
* [retrigger](docs/evaluationset/README.md#retrigger) - Retrigger Label Matching

### [file](docs/file/README.md)

* [delete_multi](docs/file/README.md#delete_multi) - Delete Files
* [delete_single](docs/file/README.md#delete_single) - Delete File
* [get](docs/file/README.md#get) - Get File
* [get_document](docs/file/README.md#get_document) - Get Document
* [get_meta_data](docs/file/README.md#get_meta_data) - Get File Meta
* [list](docs/file/README.md#list) - List Files
* [update_meta_data](docs/file/README.md#update_meta_data) - Update File Meta
* [upload](docs/file/README.md#upload) - Upload File

### [health](docs/health/README.md)

* [check](docs/health/README.md#check) - Health
* [get_openapi](docs/health/README.md#get_openapi) - Redirect

### [model_registry_token](docs/modelregistrytoken/README.md)

* [get](docs/modelregistrytoken/README.md#get) - Get Token [private]
* [~~get_token_deprecated~~](docs/modelregistrytoken/README.md#get_token_deprecated) - Get Token Deprecated [private] :warning: **Deprecated**
* [list](docs/modelregistrytoken/README.md#list) - Get Tokens [private]
* [remove](docs/modelregistrytoken/README.md#remove) - Remove Token [private]
* [~~remove_token_deprecated~~](docs/modelregistrytoken/README.md#remove_token_deprecated) - Remove Token Deprecated [private] :warning: **Deprecated**
* [save](docs/modelregistrytoken/README.md#save) - Save Token [private]
* [~~save_token_deprecated~~](docs/modelregistrytoken/README.md#save_token_deprecated) - Save Token Deprecated [private] :warning: **Deprecated**
* [update](docs/modelregistrytoken/README.md#update) - Update Token [private]
* [~~update_token_deprecated~~](docs/modelregistrytoken/README.md#update_token_deprecated) - Update Token Deprecated [private] :warning: **Deprecated**

### [models](docs/models/README.md)

* [list](docs/models/README.md#list) - Get Model [private]

### [notebook](docs/notebook/README.md)

* [create](docs/notebook/README.md#create) - Post Notebook [private]
* [get_server_state](docs/notebook/README.md#get_server_state) - Get Jupyter Lab [private]
* [start](docs/notebook/README.md#start) - Start Jupyter Lab [private]

### [organization](docs/organization/README.md)

* [get](docs/organization/README.md#get) - Get Organization [private]
* [invite](docs/organization/README.md#invite) - Invite User To Organization [private]

### [pipeline](docs/pipeline/README.md)

* [add_feedback](docs/pipeline/README.md#add_feedback) - Add Feedback
* [create](docs/pipeline/README.md#create) - Create Pipeline
* [delete](docs/pipeline/README.md#delete) - Delete Pipeline
* [deploy](docs/pipeline/README.md#deploy) - Deploy Pipeline
* [get](docs/pipeline/README.md#get) - Get Pipeline
* [get_feedback](docs/pipeline/README.md#get_feedback) - Get Pipeline Feedback
* [get_files](docs/pipeline/README.md#get_files) - Get Pipeline Files
* [get_indexing](docs/pipeline/README.md#get_indexing) - Get Pipeline Indexing
* [get_json](docs/pipeline/README.md#get_json) - Get Pipeline Yaml As Json
* [get_metadata](docs/pipeline/README.md#get_metadata) - Get Pipeline Index Metadata [private]
* [get_metadata_field_values](docs/pipeline/README.md#get_metadata_field_values) - Get Pipeline Metadata Field Values [private]
* [get_min_max_aggregation_metadata](docs/pipeline/README.md#get_min_max_aggregation_metadata) - Get Pipeline Min Max Aggregation Metadata [private]
* [get_stats](docs/pipeline/README.md#get_stats) - Get Pipeline Stats
* [get_yaml](docs/pipeline/README.md#get_yaml) - Get Pipeline Yaml
* [list](docs/pipeline/README.md#list) - List Pipelines
* [search](docs/pipeline/README.md#search) - Search
* [search_history](docs/pipeline/README.md#search_history) - Pipeline Search History [private]
* [set_default](docs/pipeline/README.md#set_default) - Set Default Pipeline
* [undeploy](docs/pipeline/README.md#undeploy) - Undeploy Pipeline
* [update_yaml](docs/pipeline/README.md#update_yaml) - Update Pipeline Yaml

### [search_session](docs/searchsession/README.md)

* [create](docs/searchsession/README.md#create) - Create Search Session [private]

### [shared_prototype](docs/sharedprototype/README.md)

* [create](docs/sharedprototype/README.md#create) - Create Prototype [private]
* [create_external_user](docs/sharedprototype/README.md#create_external_user) - Create External User [private]
* [get](docs/sharedprototype/README.md#get) - Get Shared Prototype [private]
* [list](docs/sharedprototype/README.md#list) - List Prototypes [private]
* [revoke](docs/sharedprototype/README.md#revoke) - Revoke Shared Prototype [private]
* [update](docs/sharedprototype/README.md#update) - Edit Shared Prototype [private]

### [upload_session](docs/uploadsession/README.md)

* [close](docs/uploadsession/README.md#close) - Close Session
* [create](docs/uploadsession/README.md#create) - Create Upload Session
* [get_files](docs/uploadsession/README.md#get_files) - Get Session Files
* [get_status](docs/uploadsession/README.md#get_status) - Get Session Status
* [list](docs/uploadsession/README.md#list) - Get Upload Sessions

### [user](docs/user/README.md)

* [delete](docs/user/README.md#delete) - Delete User [private]
* [get](docs/user/README.md#get) - Get User [private]
* [list](docs/user/README.md#list) - Get Users [private]
* [me](docs/user/README.md#me) - Read Users Me [private]
* [update_permission](docs/user/README.md#update_permission) - Update User Permission [private]

### [workspace](docs/workspace/README.md)

* [create](docs/workspace/README.md#create) - Create Workspace [private]
* [delete](docs/workspace/README.md#delete) - Delete Workspace [private]
* [get](docs/workspace/README.md#get) - Get Workspace [private]
* [get_stats](docs/workspace/README.md#get_stats) - Get Workspace Stats [private]
* [list](docs/workspace/README.md#list) - List Workspaces [private]
* [search_count](docs/workspace/README.md#search_count) - Search Count [private]
* [search_history](docs/workspace/README.md#search_history) - Search History [private]
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
