import plotly.graph_objects as go
import argparse

from jiraAccess import JiraAccess

def parse_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-h", "--hostname", help="Host name")
    parser.add_argument("-u", "--username", help="User name")
    parser.add_argument("-p", "--password", help="Password")

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    jiraAccess = JiraAccess(args.hostname, args.username, args.password)

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
