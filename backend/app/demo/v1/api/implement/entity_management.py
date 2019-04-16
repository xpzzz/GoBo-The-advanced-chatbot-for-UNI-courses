from __future__ import absolute_import
import dialogflow_v2 as dialogflow
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../../../../../config/gobo-97e5e-38bad1ed63df.json'
_pid = os.getenv('PROJECT_ID')
def list_entities(PROJECT_ID, entity_type_id):
    """
    :param PROJECT_ID: project id of the agent
    :param entity_type_id: a specific entity type id in gent
    :return: a dict of entities in the form of list.
    """

    entity_types_client = dialogflow.EntityTypesClient()

    parent = entity_types_client.entity_type_path(
        PROJECT_ID, entity_type_id)

    entities = entity_types_client.get_entity_type(parent).entities

    for entity in entities:
        print('Entity value: {}'.format(entity.value))
        print('Entity synonyms: {}\n'.format(entity.synonyms))


def create_entity(PROJECT_ID, entity_type_id, entity_value, synonyms):
    """

    :param PROJECT_ID: project id of the agent
    :param entity_type_id:  a specific entity type id in gent
    :param entity_value:  the entity value
    :param synonyms:  the synonyms corresponding entity value
    :return:
    """
    entity_types_client = dialogflow.EntityTypesClient()

    # Note: synonyms must be exactly [entity_value] if the
    # entity_type's kind is KIND_LIST
    synonyms = synonyms or [entity_value]

    entity_type_path = entity_types_client.entity_type_path(
        PROJECT_ID, entity_type_id)

    entity = dialogflow.types.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms.extend(synonyms)

    response = entity_types_client.batch_create_entities(
        entity_type_path, [entity])

    print('Entity created: {}'.format(response))


def delete_entity(PROJECT_ID, entity_type_id, entity_value):
    """

    :param PROJECT_ID: project id of the agent
    :param entity_type_id:  a specific entity type id in gent
    :param entity_value:  a specific entity value
    :return: None
    """
    entity_types_client = dialogflow.EntityTypesClient()

    entity_type_path = entity_types_client.entity_type_path(
        PROJECT_ID, entity_type_id)

    entity_types_client.batch_delete_entities(
        entity_type_path, [entity_value])

