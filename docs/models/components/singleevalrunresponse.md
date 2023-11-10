# SingleEvalRunResponse


## Fields

| Field                                                                                                                                                | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `comment`                                                                                                                                            | *Optional[str]*                                                                                                                                      | :heavy_minus_sign:                                                                                                                                   | Add a comment about this evaluation run.                                                                                                             |
| `created_at`                                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                 | :heavy_check_mark:                                                                                                                                   | The date and time when the evaluation run was created.                                                                                               |
| `created_by`                                                                                                                                         | [components.SingleEvalRunResponseOauthUser](../../models/components/singleevalrunresponseoauthuser.md)                                               | :heavy_check_mark:                                                                                                                                   | The user who created the eval run.                                                                                                                   |
| `eval_results`                                                                                                                                       | List[[Union[components.AnswerNodeEvalRunMetric, components.DocumentNodeEvalRunMetric]](../../models/components/singleevalrunresponseevalresults.md)] | :heavy_minus_sign:                                                                                                                                   | Contains the evaluated pipeline nodes and their overall metrics.                                                                                     |
| `eval_run_id`                                                                                                                                        | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | A unique identifier of the evaluation run.                                                                                                           |
| `last_edited_at`                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                 | :heavy_minus_sign:                                                                                                                                   | The date and time when the evaluation run was last edited.                                                                                           |
| `last_edited_by`                                                                                                                                     | [Optional[components.SingleEvalRunResponseSchemasOauthUser]](../../models/components/singleevalrunresponseschemasoauthuser.md)                       | :heavy_minus_sign:                                                                                                                                   | The user who created the eval run.                                                                                                                   |
| `logs`                                                                                                                                               | List[[components.LogEntry](../../models/components/logentry.md)]                                                                                     | :heavy_check_mark:                                                                                                                                   | Contains the logs of the evaluation run.                                                                                                             |
| `name`                                                                                                                                               | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | Unique name of an evaluation run.                                                                                                                    |
| `parameters`                                                                                                                                         | [components.SingleEvalRunResponseEvalRunParameters](../../models/components/singleevalrunresponseevalrunparameters.md)                               | :heavy_check_mark:                                                                                                                                   | Parameters set for this evaluation run                                                                                                               |
| `pipeline_metrics`                                                                                                                                   | [components.SingleEvalRunResponsePipelineMetric](../../models/components/singleevalrunresponsepipelinemetric.md)                                     | :heavy_check_mark:                                                                                                                                   | The metrics for the whole pipeline.                                                                                                                  |
| `pipeline_parameters`                                                                                                                                | Dict[str, [components.PipelineNodeConfig](../../models/components/pipelinenodeconfig.md)]                                                            | :heavy_check_mark:                                                                                                                                   | The parameters for each pipeline node with key and value.                                                                                            |
| `status`                                                                                                                                             | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | Status of the evaluation run. Returns one of these values: CREATED, STARTED, FAILED, ENDED.                                                          |
| `tags`                                                                                                                                               | List[[components.Tag](../../models/components/tag.md)]                                                                                               | :heavy_check_mark:                                                                                                                                   | A list of tags associated with the evaluation run.                                                                                                   |