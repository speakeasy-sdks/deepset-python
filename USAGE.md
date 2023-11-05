<!-- Start SDK Example Usage -->


```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListEvalRunsRequest(
    workspace_name='string',
)

res = s.eval_run.list(req)

if res.eval_runs_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->