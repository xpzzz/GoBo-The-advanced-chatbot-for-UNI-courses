from os.path import dirname

import dialogflow_v2beta1 as dialogflow
from google.api_core.exceptions import InvalidArgument


def detect_intent_texts(PROJECT_ID, session_id, texts, language_code='en-US'):
    """Returns the result of detect intent with texts as inputs.

        called by post /ask
    :parameter PROJECT_ID: the project id of the agent
    :parameter session_id: Using the same `session_id` maintains continuous conversation.
    :parameter texts: user inputs
    :parameter language_code: language kind, default as en-US
    :return text_dict as response, invalid input returns msg
    """

    pathname = dirname(__file__) + '/tmp.json'
    session_client = dialogflow.SessionsClient().from_service_account_json(pathname)

    session = session_client.session_path(PROJECT_ID, session_id)
    print('Session path: {}\n'.format(session))

    # for text in texts:
    #     text_input = dialogflow.types.TextInput(
    #         text=text, language_code=language_code)

    text_input = dialogflow.types.TextInput(
        text=texts, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        return "invalidArgument"

    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    
    text_resp = str(response.query_result.fulfillment_text)
    return {'text': text_resp}
