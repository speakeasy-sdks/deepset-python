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