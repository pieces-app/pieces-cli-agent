import pieces_os_client as pos_client
from pieces.commands import commands_functions
from pieces.settings import Settings
    model = commands_functions.model_id
        commit_message = pos_client.QGPTApi(Settings.api_client).relevance(
            pos_client.QGPTRelevanceInput(
                application=commands_functions.application.id,
                options=pos_client.QGPTRelevanceInputOptions(question=True)
                    issue_number = pos_client.QGPTApi(Settings.api_client).relevance(
                            pos_client.QGPTRelevanceInput(
                                application=commands_functions.application.id,
                                options=pos_client.QGPTRelevanceInputOptions(question=True)