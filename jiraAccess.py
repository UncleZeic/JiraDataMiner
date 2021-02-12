from jira import JIRA

from SprintData import SprintData


class JiraAccess:
    def __init__(self, hostname, username, password):
        self.jira = JIRA(hostname, basic_auth=(username, password))

    @staticmethod
    def has_field(issue, field_name):
        return hasattr(issue.fields, field_name) and getattr(issue.fields, field_name) is not None

    @staticmethod
    def get_story_points(issue):
        story_points_field_name = "customfield_10092"
        if JiraAccess.has_field(issue, story_points_field_name):
            return int(getattr(issue.fields, story_points_field_name))
        else:
            return None

    @staticmethod
    def get_jql_field_and_week(filter_id, issue_field_name, week_index):
        issues_in_week_jql = f'filter = {filter_id} AND issuetype in standardIssueTypes() AND {issue_field_name} >= ' \
                             f'startOfWeek({week_index}w)' \
                             f'AND {issue_field_name} <= endOfWeek({week_index}w)'
        return issues_in_week_jql

    def get_projects(self):
        self.jira.projects()

    def get_project(self, project_name):
        self.jira.project(project_name)

    def get_issue(self, issue_key):
        self.jira.issue(issue_key)

    def get_sprints_data(self, board_id, text_in_board_name):
        sprints = self.jira.sprints(board_id)
        sprints_list = list(filter(lambda x: f"{text_in_board_name}" in x.name, sprints))[-6:]
        for s in sprints_list:
            sprint_issues = self.jira.search_issues(f"sprint = {s.id}")
            sprint_bugs = self.jira.search_issues(f"sprint = {s.id} AND issueType = BUG")
            return SprintData(s.id, s.name, -1, len(sprint_bugs), len(sprint_issues))

    # TODO: @cache results
    def get_resolved_in_week(self, filter_id, week_index):
        resolved_issues_in_week_jql = JiraAccess.get_jql_field_and_week(filter_id, "resolved", week_index)
        resolved_issues_in_week = self.jira.search_issues(resolved_issues_in_week_jql)

        return resolved_issues_in_week
