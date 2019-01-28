import argparse
import datetime
import json

PROBLEM_PLACEHOLDER = "__PROBLEM_ID__"
USER_PLACEHOLDER = "__USER_ID__"

ADD_PARTNER_COMMANDS = [
    {
      "Command": "open",
      "Target": "https://repository.ia-toki.org/problems/programming/{}/statements".format(PROBLEM_PLACEHOLDER),
      "Value": ""
    },
    {
      "Command": "clickAndWait",
      "Target": "link=Partners",
      "Value": ""
    },
    {
      "Command": "clickAndWait",
      "Target": "link=Add Partner",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=username",
      "Value": USER_PLACEHOLDER
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToUpdateProblem",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToUpdateProblem",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToUpdateStatement",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToUpdateStatement",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToUploadStatementResources",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToUploadStatementResources",
      "Value": ""
    },
    {
      "Command": "click",
      "Target": "/html/body/div/main/div[2]/div[2]/div[2]/div/form",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToManageStatementLanguages",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToManageStatementLanguages",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToViewVersionHistory",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToViewVersionHistory",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToRestoreVersionHistory",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToRestoreVersionHistory",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToManageProblemClients",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToManageProblemClients",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToSubmit",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToSubmit",
      "Value": ""
    },
    {
      "Command": "type",
      "Target": "id=isAllowedToManageGrading",
      "Value": "true"
    },
    {
      "Command": "click",
      "Target": "id=isAllowedToManageGrading",
      "Value": ""
    },
    {
      "Command": "clickAndWait",
      "Target": "/html/body/div/main/div[2]/div[2]/div[2]/div/form/div[13]/div/button",
      "Value": ""
    }
]


def read_list(filepath):
    result = []
    with open(filepath) as f:
        for line in f:
            result.append(line.strip())
    return result

def main():
    parser = argparse.ArgumentParser(description='Print kantu script to automate partner addition')
    parser.add_argument('-u', '--user', type=str, required=True, help='path to file containing the list of usernames')
    parser.add_argument('-p', '--problem', type=str, required=True, help='path to file containing the list of problem ids')

    args = parser.parse_args()

    users = read_list(args.user)
    problems = read_list(args.problem)

    kantu_obj = {
        "Name": "Add partner",
        "CreationDate": datetime.datetime.now().strftime("%Y-%m-%d"),
        "Commands": []
    }

    for problem_id in problems:
        for user_id in users:
            for command in ADD_PARTNER_COMMANDS:
                cmd = command.copy()

                for k in cmd.keys():
                    cmd[k] = cmd[k].replace(USER_PLACEHOLDER, user_id).replace(PROBLEM_PLACEHOLDER, problem_id)

                kantu_obj['Commands'].append(cmd)

    print(json.dumps(kantu_obj, indent=2))

main()