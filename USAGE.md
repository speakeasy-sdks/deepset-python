<!-- Start SDK Example Usage -->
```python
import deepset_cloud
import dateutil.parser
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.CreateToken(
    expires_at=dateutil.parser.isoparse('2021-10-25T05:21:43.948Z'),
)

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.api_token_result is not None:
    # handle response
```
<!-- End SDK Example Usage -->