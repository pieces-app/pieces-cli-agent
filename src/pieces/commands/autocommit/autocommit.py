from pieces.settings import Settings
from pieces_os_client.api.qgpt_api import QGPTApi
from pieces_os_client.models.qgpt_relevance_input import QGPTRelevanceInput
from pieces_os_client.models.qgpt_relevance_input_options import QGPTRelevanceInputOptions
    issue_flag = kwargs.get('issue_flag')
    model = Settings.model_id
        commit_message = QGPTApi(Settings.api_client).relevance(
            QGPTRelevanceInput(
                application=Settings.application.id,
                options=QGPTRelevanceInputOptions(question=True)
        if issue_flag:
            issue_prompt = """Please provide the issue number that is related to the changes, If nothing related write 'None'.
                    `Output format WITHOUT ADDING ANYTHING ELSE: "Issue: **ISSUE NUMBER OR NONE HERE**`,
                    `Example: 'Issue: 12', 'Issue: None'`,
                    `Note: Don't provide any other information`
                    `Here are the issues:`\n{issues}"""
            
            # Issues
            repo_details = get_git_repo_name()
            issues = get_repo_issues(*repo_details) if repo_details else [] # Check if we got a vaild repo name

            if issues:
                # Make the issues look nicer
                issue_list = [
                    f"- `Issue_number: {issue['number']}`\n- `Title: {issue['title']}`\n- `Body: {issue['body']}`"
                    for issue in issues
                ]
                issue_list = "\n".join(issue_list) # To string
                try:
                    
                    issue_number = QGPTApi(Settings.api_client).relevance(
                            QGPTRelevanceInput(
                                query=issue_prompt.format(issues=issue_list),
                                paths=paths,
                                application=Settings.application.id,
                                model=model,
                                options=QGPTRelevanceInputOptions(question=True)
                            )).answer.answers.iterable[0].text
            
                    
                    # Extract the issue part
                    issue_number = issue_number.replace("Issue: ", "") 
                    # If the issue is a number 
                    issue_number = int(issue_number)
                    issue_title = next((issue["title"] for issue in issues if issue["number"] == issue_number), None)
                except: 
                    issue_number = None
            else:
        if issue_flag:
            # Adding the Issue number if the user accept it
            if issue_number:
                print("Issue Number: ", issue_number)
                print("Issue Title: ", issue_title)
                r_issue = input("Is this issue related to the commit? (y/n): ")
                if r_issue.lower() == "y":
                    commit_message += f" (issue: #{issue_number})"
                else:
                    issue_number = None
            if issue_number == None and issues:
                console = Console()
                md = Markdown(issue_list)
                console.print(md)
                validate_issue = True
                while validate_issue:
                    issue_number = input("Issue number?\nLeave blanck if none: ").strip()
                    if issue_number.startswith("#") and issue_number[1:].isdigit():
                        issue_number = issue_number[1:]
                        validate_issue = False
                    elif issue_number.isdigit():
                        validate_issue = False
                    elif issue_number == None or issue_number == "":
                        break    
                if not validate_issue:
                    commit_message += f" (issue: #{issue_number})"