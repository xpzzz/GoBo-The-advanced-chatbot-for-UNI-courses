from __future__ import absolute_import

import json



def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
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




if __name__=="__main__":
    #import dialogflow_v2 as df
    import dialogflow_v2beta1 as dialogflow
    import os
    # import json
    from google.api_core.exceptions import InvalidArgument

    project_id = 'gobo-975e5' # TODO do not expose this line
    language_code = 'en-US'
    GOOGLE_APPLICATION_CREDENTIALS = "./df/gobo-97e5e-3b2420f2743d.json" # TODO do not expose this line
    session_id = 'current-user-id'
    # document_display_name='test'
    mime_type='text/csv'
    knowledge_type='FAQ'
    # content_uri=
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS  # TODO do not expose this line
    input_test =["what is the course code?","can you tell where is the outline?","what is COMP9021?"]
    ## create knowledgebase
    #nb_id=create_knowledge_base(DIALOGFLOW_PROJECT_ID,db_name)

    # with open(GOOGLE_APPLICATION_CREDENTIALS, 'r') as f:
    #     data = json.load(f)
    #     print(data)
    # if input_test:
    #     detect_intent_texts(project_id,session_id,input_test,language_code)
    # print_documents(project_id, kb_id="NDkyMTgwMTA3NDAxODM1MzE1Mg")
    # list_knowledge_bases(project_id)