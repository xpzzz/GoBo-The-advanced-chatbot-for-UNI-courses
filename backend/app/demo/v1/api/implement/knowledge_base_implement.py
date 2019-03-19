from __future__ import absolute_import
# import document_implement
#used for knowledge base management
import dialogflow_v2beta1 as dialogflow



def counter(PROJECT_ID, KID):
    """
    count the number of documents in a specific knowledgement base
    :parameter PROJECT_ID: The GCP project linked with the agent.
    :parameter KID: ID to Knowledge base by.

    :return num: the number of documents
    """

    client = dialogflow.DocumentsClient()
    knowledge_base_path = client.knowledge_base_path(PROJECT_ID, KID)
    # testing stout
    print('Documents for Knowledge Id: {}'.format(KID))
    iterator = client.list_documents(knowledge_base_path)
    count = 0
    for i in iterator:
        count+=0
    return count

def list_knowledge_bases(PROJECT_ID):
    """List all availabe Knowledge bases.
        called by GET   /knowledge_base
        format returned:
        [
            {
            "knowledge-base-id": "string",
            "display-name": "string",
            "document-amount": 0
            }
        ]
    :parameter  PROJECT_ID: The GCP project linked with the agent.
    :return knowledge_base_list: the list of kbs
    """
    client = dialogflow.KnowledgeBasesClient()
    project_path = client.project_path(PROJECT_ID)
    #testing stout
    print('Knowledge Bases for: {}'.format(PROJECT_ID))
    for knowledge_base in client.list_knowledge_bases(project_path):
        print(' - Display Name: {}'.format(knowledge_base.display_name))
        print(' - Knowledge ID: {}\n'.format(knowledge_base.name))

    #content returned
    knowledge_base_list = []

    for knowledge_base in client.list_knowledge_bases(project_path):
        knowledge_base_dict = dict()
        knowledge_base_dict["knowledge-base-id"] = str(knowledge_base.name.split("/")[-1])
        knowledge_base_dict["display-name"] = str(knowledge_base.display_name)
        knowledge_base_dict["document-amount"] = counter(PROJECT_ID, knowledge_base.name.split("/")[-1])
        knowledge_base_list.append(knowledge_base_dict)
    # returned done, directly use as response
    return knowledge_base_list





def create_knowledge_base(PROJECT_ID, display_name):
    """
    Creates a Knowledge base.
        called by POST   /knowledge_base
        format returned:
        {
          "knowledge-base-id": "string",
          "display-name": "string",
          "document-amount": 0
        }

    :parameter  PROJECT_ID: The GCP project linked with the agent.
    :parameter  display_name: The display name of the Knowledge base.
    :return knowledge_base_dict: the info of new created knowledege base
    """
    client = dialogflow.KnowledgeBasesClient()
    project_path = client.project_path(PROJECT_ID)

    knowledge_base = dialogflow.types.KnowledgeBase(
        display_name=display_name)

    response = client.create_knowledge_base(project_path, knowledge_base)
    #testing stout
    print('Knowledge Base created:\n')
    print('Display Name: {}\n'.format(response.display_name))
    print('Knowledge ID: {}\n'.format(response.name))

    #content returned
    knowledge_base_dict = dict()
    knowledge_base_dict["knowledge-base-id"] = str(response.name.split("/")[-1])
    knowledge_base_dict["display-name"] = str(response.display_name)
    knowledge_base_dict["document-amount"] = 0
    # returned done, directly use as response
    return knowledge_base_dict


def get_knowledge_base(PROJECT_ID, KID):
    """
    Gets a specific Knowledge base.
        called by GET   /knowledge_base/{KID}
        format returned
        {
          "knowledge-base-id": "string",
          "knowledge-base-name": "string",
          "document-amount": 0,
          "documents": [
         {
          "document-id": "searched from knowledge base management",
          "document-name": "stackoverflow",
          "MIME-type": "text/csv",
          "Knowledge-type": "FAQ",
          "content_uri": "gs://test/test01.csv"
         }
       ]
    }

    :parameter     PROJECT_ID: The GCP project linked with the agent.
    :parameter     KID: Id of the Knowledge base.
    :return knowledge_base_dict: the details of a specific knowledge base
    """
    client = dialogflow.KnowledgeBasesClient()
    knowledge_base_path = client.knowledge_base_path(
        PROJECT_ID, KID)

    response = client.get_knowledge_base(knowledge_base_path)
    #testing stout
    print('Got Knowledge Base:')
    print(' - Display Name: {}'.format(response.display_name))
    print(' - Knowledge ID: {}'.format(response.name))
    #content returned
    knowledge_base_dict = dict()
    knowledge_base_dict["knowledge-base-id"] = str(response.name.split("/")[-1])
    knowledge_base_dict["display-name"] = str(response.display_name)
    knowledge_base_dict["document-amount"] = counter(PROJECT_ID,KID)
    knowledge_base_dict["documents"] = document_implement.list_documents(PROJECT_ID, KID)
    # returned done, directly use as response
    return knowledge_base_dict



def delete_knowledge_base(PROJECT_ID, KID):
    """
    Deletes a specific Knowledge base.
        called by DELETE   /knowledge_base/{KID}

     :parameter  PROJECT_ID: The GCP project linked with the agent.
     :parameter  KID: Id of the Knowledge base.

        """
    client = dialogflow.KnowledgeBasesClient()
    knowledge_base_path = client.knowledge_base_path(
        PROJECT_ID, KID)

    response = client.delete_knowledge_base(knowledge_base_path)

    print('Knowledge Base deleted.'.format(response))