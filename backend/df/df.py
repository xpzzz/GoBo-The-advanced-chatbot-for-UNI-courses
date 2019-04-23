from __future__ import absolute_import


def detect_intent_texts(PROJECT_ID, session_id, texts, language_code = 'en-US'):
    """Returns the result of detect intent with texts as inputs.

        called by post /ask
    :parameter PROJECT_ID: the project id of the agent
    :parameter session_id: Using the same `session_id` maintains continuous conversation.
    :parameter texts: user inputs
    :parameter language_code: language kind, default as en-US
    """
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(PROJECT_ID, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
    text_dict = dict()
    text_dict["text"] = str(response.query_result.fulfillment_text)
    return text_dict




if __name__=="__main__":
    #import dialogflow_v2 as df
    import dialogflow_v2beta1 as dialogflow
    import os
    # import json
    from google.api_core.exceptions import InvalidArgument

    project_id = 'gobo-97e5e'
    language_code = 'en-US'
    GOOGLE_APPLICATION_CREDENTIALS = "../../config/gobo-97e5e-b25d6294eb38.json"
    session_id = 'current-user-id'
    # document_display_name='test'
    mime_type='text/csv'
    knowledge_type='FAQ'
    # content_uri=
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS
    input_test =["what is the course code?","can you tell where is the outline?","what is COMP9021?"]
    ## create knowledgebase
    #nb_id=create_knowledge_base(DIALOGFLOW_PROJECT_ID,db_name)


    if input_test:
        detect_intent_texts(project_id,session_id,input_test,language_code)
    # print_documents(project_id, kb_id="NDkyMTgwMTA3NDAxODM1MzE1Mg")
    # list_knowledge_bases(project_id)