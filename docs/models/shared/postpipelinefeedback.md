# PostPipelineFeedback


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `is_correct_answer`                            | *bool*                                         | :heavy_check_mark:                             | Feedback if the answer was correct             |
| `is_correct_document`                          | *bool*                                         | :heavy_check_mark:                             | Feedback if the document was matched correctly |
| `result_id`                                    | *str*                                          | :heavy_check_mark:                             | N/A                                            |
| `tags`                                         | list[*str*]                                    | :heavy_minus_sign:                             | A list of tags associated with the feedback.   |