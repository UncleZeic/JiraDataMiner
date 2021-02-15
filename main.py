#!/usr/bin/env python3
import plotly.graph_objects as go
import argparse

from jiraAccess import JiraAccess

__atlas_board_filter_id = 40443
__atlas_board_id = 1192
__project_name = "AAA"
__number_of_weeks = 6


def parse_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--hostname", help="Host name")
    parser.add_argument("-u", "--username", help="User name")
    parser.add_argument("-p", "--password", help="Password")

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_input_args()

    jiraAccess = JiraAccess(args.hostname, args.username, args.password)
    resolved_story_points_past_weeks = []

    for wi in range(-1, -__number_of_weeks, -1):
        resolved_issues_in_week = jiraAccess.get_resolved_in_week(
            __atlas_board_filter_id, wi)

        resolvedStoryPointsInWeek = sum(JiraAccess.get_story_points(
            issue) or 0 for issue in resolved_issues_in_week)
        resolved_story_points_past_weeks.append(resolvedStoryPointsInWeek)

    fig = go.Figure()
    fig.add_trace(go.Bar(y=resolved_story_points_past_weeks))
    fig.update_layout(title='Hello Figure')
    fig.show()
