#!/usr/bin/env python3
import plotly.graph_objects as go
import argparse

from sprint.jira_access import JiraAccess

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


def get_resolved_story_points(j_a):
    resolved_story_points_past_weeks = []

    for wi in range(-1, -__number_of_weeks, -1):
        resolved_issues_in_week = j_a.get_resolved_in_week(
            __atlas_board_filter_id, wi)

        resolved_story_points_in_week = sum(j_a.get_story_points(
            issue) or 0 for issue in resolved_issues_in_week)
        resolved_story_points_past_weeks.append(resolved_story_points_in_week)

    return resolved_story_points_past_weeks


def go_figure(stories):
    fig = go.Figure()
    fig.add_trace(go.Bar(y=stories))
    fig.update_layout(title='Hello Figure')
    fig.show()


if __name__ == '__main__':
    args = parse_input_args()

    jira_acc = JiraAccess(args.hostname, args.username, args.password)
    resolved_stories = get_resolved_story_points(jira_acc)

    go_figure(stories)
