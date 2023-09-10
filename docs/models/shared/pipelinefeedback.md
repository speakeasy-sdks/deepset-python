# PipelineFeedback


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Datetime object, specifies when the feedback was created             |
| `feedback_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | Unique identifier of the feedback                                    |
| `is_correct_answer`                                                  | *bool*                                                               | :heavy_check_mark:                                                   | Feedback if the answer was correct                                   |
| `is_correct_document`                                                | *bool*                                                               | :heavy_check_mark:                                                   | Feedback if the document was matched correctly                       |
| `search_result`                                                      | [FeedbackSearchResult](../../models/shared/feedbacksearchresult.md)  | :heavy_check_mark:                                                   | N/A                                                                  |
| `tags`                                                               | list[[Tag](../../models/shared/tag.md)]                              | :heavy_check_mark:                                                   | A list of tags associated with the feedback.                         |