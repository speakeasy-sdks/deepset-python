<!-- Start SDK Example Usage -->
```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvalRunsRequest(
    after='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
    before='a05dfc2d-df7c-4c78-8a1b-a928fc816742',
    field=operations.FieldEnum.INTEGRATED_RECALL_SINGLE_HIT,
    filter='cum',
    limit=456150,
    order=operations.OrderEnum.ASC,
    page_number=568434,
    select='aspernatur',
    workspace_name='perferendis',
)

res = s.eval_run.list(req, operations.ListEvalRunsSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.eval_runs_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->