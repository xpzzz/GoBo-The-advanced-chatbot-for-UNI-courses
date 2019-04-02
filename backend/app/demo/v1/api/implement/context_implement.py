from os.path import dirname

import dialogflow_v2beta1 as dialogflow
from google.api_core.exceptions import InvalidArgument

import argparse


def list_contexts(PROJECT_ID, session_id):
    """
    Returns the a list of context in current session.
    :param PROJECT_ID: the project id of the agent
    :param session_id: the current session id
    :return: a list of contexts with each items in the form of a dict constituted of lifespan and field.
    """
    contexts_client = dialogflow.ContextsClient()
    session_path = contexts_client.session_path(PROJECT_ID, session_id)
    contexts = contexts_client.list_contexts(session_path)

    print('Contexts for session {}:\n'.format(session_path))
    for context in contexts:
        print('Context name: {}'.format(context.name))
        print('Lifespan count: {}'.format(context.lifespan_count))
        print('Fields:')
        for field, value in context.parameters.fields.items():
            if value.string_value:
                print('\t{}: {}'.format(field, value))

    # context_list = []
    # for context in contexts:
    #     new_context_dict = dict()
    #     new_context_dict['context-name'] = context.name
    #     new_context_dict['lifespan-count'] = context.lifespan_count
    #     field_list = []
    #     for field, value in context.parameters.fields.items():
    #         if value.string_value:
    #             field_list.append((field, value))
    # return context_list


def create_context(PROJECT_ID, session_id, context_id, lifespan_count):
    """
     Create a new context.
    :param PROJECT_ID: the project id of the agent
    :param session_id: the current session id
    :param context_id: the context id
    :param lifespan_count: the lifespan of this context
    """
    contexts_client = dialogflow.ContextsClient()

    session_path = contexts_client.session_path(PROJECT_ID, session_id)
    context_name = contexts_client.context_path(PROJECT_ID, session_id, context_id)

    context = dialogflow.types.Context(name=context_name, lifespan_count=lifespan_count)

    response = contexts_client.create_context(session_path, context)
    print('Context created: \n{}'.format(response))


def delete_context(PROJECT_ID, session_id, context_id):
    """
    Delete a context from the agent
    :param PROJECT_ID: the project id of the agent
    :param session_id: the current session id
    :param context_id: the context id
    """
    contexts_client = dialogflow.ContextsClient()
    context_name = contexts_client.context_path(PROJECT_ID, session_id, context_id)

    contexts_client.delete_context(context_name)


