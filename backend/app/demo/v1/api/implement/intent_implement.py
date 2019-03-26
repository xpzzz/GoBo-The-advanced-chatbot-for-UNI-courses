import dialogflow_v2 as dialogflow

def list_intents(PROJECT_ID):
    '''
    :param PROJECT_ID: the project id of agent
    :return:return a list of intents in the agent
    '''

    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(PROJECT_ID)

    intents = intents_client.list_intents(parent)

    intent_list =[]
    for intent in intents:
        print('=' * 20)
        intent_dict = dict()
        print('Intent name: {}'.format(intent.name.split('/')[-1]))
        intent_dict["Intent-id"] = str(intent.name.split('/')[-1])
        print('Intent display_name: {}'.format(intent.display_name))
        intent_dict["Display-name"] = str(intent.display_name)
        print('Action: {}\n'.format(intent.action))
        intent_dict["Action"] = str(intent.action)
        print('Root followup intent: {}'.format(
            intent.root_followup_intent_name))
        intent_dict["Root-followup"] = str(intent.root_followup_intent_name)
        print('Parent followup intent: {}\n'.format(
            intent.parent_followup_intent_name))
        intent_dict["Parent-followup"] = str(intent.parent_followup_intent_name)
        input_context_list = [i for i in intent.input_context_names]
        print('Input contexts:')
        for input_context_name in intent.input_context_names:
            print('\tName: {}'.format(input_context_name))
        intent_dict["Input-contexts"] = ",".join(input_context_list)

        output_context_list = [i.name for i in intent.output_contexts]
        print('Output contexts:')
        for output_context in intent.output_contexts:
            print('\tName: {}'.format(output_context.name))
        intent_dict["Output-contexts"] = ",".join(output_context_list)

        intent_list.append(intent_dict)
    return intent_list


def create_intent(PROJECT_ID, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(PROJECT_ID)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)

    print('Intent created: {}'.format(response))


def delete_intent(project_id, intent_id):
    """Delete intent with the given intent type and intent value."""
    intents_client = dialogflow.IntentsClient()

    intent_path = intents_client.intent_path(project_id, intent_id)

    intents_client.delete_intent(intent_path)



def _get_intent_ids(project_id, display_name):
    # Helper to get intent from display name.
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)
    intents = intents_client.list_intents(parent)
    intent_names = [
        intent.name for intent in intents
        if intent.display_name == display_name]

    intent_ids = [
        intent_name.split('/')[-1] for intent_name
        in intent_names]

    return intent_ids