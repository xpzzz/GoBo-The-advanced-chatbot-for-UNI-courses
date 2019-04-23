import dialogflow_v2 as dialogflow

def list_entity_types(PROJECT_ID):
    "return a list of entity types"
    entity_types_client = dialogflow.EntityTypesClient()
    parent = entity_types_client.project_agent_path(PROJECT_ID)
    entity_types = entity_types_client.list_entity_types(parent)

    entity_type_list = []
    for entity_type in entity_types:
        entity_type_dict = dict()
        print('Entity type id: {}'.format(entity_type.name.split('/')[-1]))
        entity_type_dict["Entity-type-id"] = entity_type.name.split('/')[-1]
        print('Entity type display name: {}'.format(entity_type.display_name))
        entity_type_dict["Entity-type-display-name"] = entity_type.display_name
        print('Number of entities: {}\n'.format(len(entity_type.entities)))
        entity_type_dict["Entity-amount"] = len(entity_type.entities)
        entity_type_list.append(entity_type_dict)
    return entity_type_list




def create_entity_type(PROJECT_ID, display_name, kind):
    """Create an entity type with the given display name."""
    entity_types_client = dialogflow.EntityTypesClient()
    parent = entity_types_client.project_agent_path(PROJECT_ID)
    entity_type = dialogflow.types.EntityType(
        display_name=display_name, kind=kind)
    response = entity_types_client.create_entity_type(parent, entity_type)

    print('Entity type created: \n{}'.format(response))



def delete_entity_type(PROJECT_ID, entity_type_id):
    """Delete entity type with the given entity type name."""
    entity_types_client = dialogflow.EntityTypesClient()

    entity_type_path = entity_types_client.entity_type_path(
        PROJECT_ID, entity_type_id)

    entity_types_client.delete_entity_type(entity_type_path)


# Helper to get entity_type_id from display name.
def _get_entity_type_ids(PROJECT_ID, display_name):
    entity_types_client = dialogflow.EntityTypesClient()

    parent = entity_types_client.project_agent_path(PROJECT_ID)
    entity_types = entity_types_client.list_entity_types(parent)
    entity_type_names = [
        entity_type.name for entity_type in entity_types
        if entity_type.display_name == display_name]

    entity_type_ids = [
        entity_type_name.split('/')[-1] for entity_type_name
        in entity_type_names]

    return entity_type_ids