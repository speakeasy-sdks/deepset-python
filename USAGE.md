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
    after='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
    before='a05dfc2d-df7c-4c78-8a1b-a928fc816742',
    field=operations.Field.INTEGRATED_RECALL_SINGLE_HIT,
    filter='cum',
    limit=456150,
    order=operations.Order.ASC,
    page_number=568434,
    select='aspernatur',
    workspace_name='perferendis',
)

res = s.eval_run.list(req)

if res.eval_runs_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->