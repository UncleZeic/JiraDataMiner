import plotly.graph_objects as go

from jiraAccess import JiraAccess
from setup import get_credentials


if __name__ == '__main__':
    credential = get_credentials()
    jiraAccess = JiraAccess(credential.hostname, credential.username, credential.password)
    atlas_board_filter_id = 40443
    atlasBoardId = 1192
    projectName = "AAA"

    numberOfWeeks = 6
    resolvedStoryPointsPastWeeks = []
    for wi in range(-1, -numberOfWeeks, -1):
        resolved_issues_in_week = jiraAccess.get_resolved_in_week(atlas_board_filter_id, wi)

        resolvedStoryPointsInWeek = sum(JiraAccess.get_story_points(issue) or 0 for issue in resolved_issues_in_week)
        resolvedStoryPointsPastWeeks.append(resolvedStoryPointsInWeek)

    fig = go.Figure()
    fig.add_trace(go.Bar(y=resolvedStoryPointsPastWeeks))
    fig.update_layout(title='Hello Figure')
    fig.show()
