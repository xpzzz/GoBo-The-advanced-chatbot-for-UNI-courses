from __future__ import absolute_import
#used for documents management

import dialogflow_v2beta1 as dialogflow

KNOWLEDGE_TYPES = ['KNOWLEDGE_TYPE_UNSPECIFIED', 'FAQ', 'EXTRACTIVE_QA']


def list_documents(PROJECT_ID, KID):
    """
    List all Documents in a Knowledge base by its KID.
       indirectly called by GET /knowledge_base/{KID}. directly called by get_knowledge_base Function
       format returned:
         "documents": [
           {
          "document-id": "searched from knowledge base management",
          "document-name": "stackoverflow",
          "MIME-type": "text/csv",
          "Knowledge-type": "FAQ",
          "content_uri": "gs://test/test01.csv"
          }
    :parameter PROJECT_ID: The GCP project linked with the agent.
    :parameter KID: ID to Knowledge base by.
    """
    client = dialogflow.DocumentsClient()
    knowledge_base_path = client.knowledge_base_path(PROJECT_ID, KID)
    #testing stout
    print('Documents for Knowledge Id: {}'.format(KID))
    for document in client.list_documents(knowledge_base_path):
        print(' - Display Name: {}'.format(document.display_name))
        print(' - document ID: {}'.format(document.name))
        print(' - MIME Type: {}'.format(document.mime_type))
        print(' - Knowledge Types:')
        for knowledge_type in document.knowledge_types:
            print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
        print(' - Source: {}\n'.format(document.content_uri))

    #content returned
    document_list = []
    for document in client.list_documents(knowledge_base_path):
        document_dict = dict()
        document_dict["document-name"] = str(document.display_name)
        document_dict["document-id"] = str(document.name)
        document_dict["MIME-type"] = str(document.mime_type)
        knowledge_type_list = [KNOWLEDGE_TYPES[i] for i in document.knowledge_types]
        document_dict["Knowledge-type"] = ",".join(knowledge_type_list)
        document_dict["content_uri"] = document.content_uri

        document_list.append(document_dict)
    #returned only document list, need embeded into a dict of kb
    return document_dict


def create_document(PROJECT_ID, KID, document_name, mime_type,
                    knowledge_type, content_uri):
    """
    Creates a Document.
        called by POST /knowledge_base/{KID}/document:
        format returned:
        {
          {
          "knowledge-base-id": "searched from knowledge base management",
          "document-id": "searched from knowledge base management",
          "display-name": "stackoverflow",
          "MIME-type": "text/csv",
          "Knowledge-type": "FAQ",
          "content_uri": "gs://test/test01.csv"
        }
        }

    :parameter PROJECT_ID: The GCP project linked with the agent.
    :parameter KID: Id of the Knowledge base.
    :parameter document_name: The display name of the Document.
    :parameter mime_type: The mime_type of the Document. e.g. text/csv, text/html,
                            text/plain, text/pdf etc.
    :parameter knowledge_type: The Knowledge type of the Document. e.g. FAQ,
                EXTRACTIVE_QA.
    :parameter content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
                                                        http://mypage.com/faq.html."""
    client = dialogflow.DocumentsClient()
    knowledge_base_path = client.knowledge_base_path(PROJECT_ID,
                                                     KID)

    document = dialogflow.types.Document(
        display_name=document_name, mime_type=mime_type,
        content_uri=content_uri)

    document.knowledge_types.append(
        dialogflow.types.Document.KnowledgeType.Value(knowledge_type))

    response = client.create_document(knowledge_base_path, document)
    #testing stout
    print('Waiting for results...')
    document = response.result(timeout=90)
    print('Created Document:')
    print(' - Display Name: {}'.format(document.display_name))
    print(' - document ID: {}'.format(document.name))
    print(' - MIME Type: {}'.format(document.mime_type))
    print(' - Knowledge Types:')
    for knowledge_type in document.knowledge_types:
        print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
    print(' - Source: {}\n'.format(document.content_uri))

    #content returned
    document_dict = dict()
    document_dict["knowledge-base-id"] = str(KID)
    document_dict["document-name"] = str(document.display_name)
    document_dict["document-id"] = str(document.name)
    document_dict["MIME-type"] = str(document.mime_type)
    knowledge_type_list = [KNOWLEDGE_TYPES[i] for i in document.knowledge_types]
    document_dict["Knowledge-type"] = ",".join(knowledge_type_list)
    document_dict["content_uri"] = document.content_uri
    #returned done, directly use as response
    return document_dict


def get_document(PROJECT_ID, KID, DID):
    """
    Gets a Document in a specific knowledge base by kid
        called by GET   /knowledge_base/{KID}/document/{DID}
        format returned:
        {
      "knowledge-base-id": "searched from knowledge base management",
      "document-id": "searched from knowledge base management",
      "display-name": "stackoverflow",
      "MIME-type": "text/csv",
      "Knowledge-type": "FAQ",
      "content_uri": "gs://test/test01.csv"
    }
    :parameter PROJECT_ID: The GCP project linked with the agent.
    :parameter KID: Id of the Knowledge base.
    :parameter DID: Id of the Document.

    """
    client = dialogflow.DocumentsClient()
    document_path = client.document_path(PROJECT_ID, KID,
                                         DID)

    response = client.get_document(document_path)
    # testing stout
    print('Got Document:')
    print(' - Display Name: {}'.format(response.display_name))
    print(' - Knowledge ID: {}'.format(response.name))
    print(' - MIME Type: {}'.format(response.mime_type))
    print(' - Knowledge Types:')
    for knowledge_type in response.knowledge_types:
        print('    - {}'.format(KNOWLEDGE_TYPES[knowledge_type]))
    print(' - Source: {}\n'.format(response.content_uri))

    # content returned
    document_dict = dict()
    document_dict["knowledge-base-id"] = str(KID)
    document_dict["document-name"] = str(response.display_name)
    document_dict["document-id"] = str(response.name)
    document_dict["MIME-type"] = str(response.mime_type)
    knowledge_type_list = [KNOWLEDGE_TYPES[i] for i in response.knowledge_types]
    document_dict["Knowledge-type"] = ",".join(knowledge_type_list)
    document_dict["content_uri"] = response.content_uri
    # returned done, directly use as response
    return document_dict



def delete_document(PROJECT_ID, KID, DID):
    """
    Deletes a Document.
        called by DELETE   /knowledge_base/{KID}/document/{DID}


    :parameter     PROJECT_ID: The GCP project linked with the agent.
    :parameter     KID: Id of the Knowledge base.
    :parameter     DID: Id of the Document.
    """
    client = dialogflow.DocumentsClient()
    document_path = client.document_path(PROJECT_ID, KID,
                                         DID)

    response = client.delete_document(document_path)
    print('operation running:\n {}'.format(response.operation))
    print('Waiting for results...')
    print('Done.\n {}'.format(response.result()))


