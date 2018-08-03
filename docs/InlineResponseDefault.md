# InlineResponseDefault

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tr** | **float** | Time repetition (s) | [optional] 
**compile_traceback** | **str** | Traceback of compilation error. | [optional] 
**compiled_at** | **str** | Timestamp of when analysis was compiled | [optional] 
**created_at** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**dataset_id** | **int** |  | 
**description** | **str** |  | [optional] 
**hash_id** | **str** | Hashed analysis id. | [optional] 
**model** | **object** | BIDS model. | [optional] 
**modified_at** | **str** |  | [optional] 
**name** | **str** | Analysis name. | 
**parent_id** | **str** | Parent analysis, if cloned. | [optional] 
**predictions** | **str** | User apriori predictions. | [optional] 
**predictors** | [**list[ApianalysesPredictors]**](ApianalysesPredictors.md) | Predictor id(s) associated with analysis | [optional] 
**private** | **bool** | Analysis private or discoverable? | [optional] 
**runs** | [**list[ApianalysesPredictors]**](ApianalysesPredictors.md) | Runs associated with analysis | [optional] 
**status** | **str** | PASSED, FAILED, PENDING, or DRAFT. | [optional] 
**task_name** | **str** | Task name | [optional] 
**user_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


