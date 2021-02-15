#!/usr/bin/env python3
import plotly.express as px
import pandas as pd
import argparse

from sprint.jira_access import JiraAccess


def parse_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--hostname", help="Host name")
    parser.add_argument("-u", "--username", help="User name")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument(
        "--board-filter-id",
        help="Board filter id",
        default=40443)
    parser.add_argument("--board-id", help="Board id", default=1192)
    parser.add_argument("--project", help="Project name", default="AAA")
    parser.add_argument(
        "--weeks",
        help="Number of weeks to retrieve data for", type=int,
        default=6)

    return parser.parse_args()


def get_resolved_story_points(j_a, board_filter_id, number_of_weeks):
    resolved_story_points_past_weeks = []

    for wi in range(-1, -number_of_weeks, -1):
        resolved_issues_in_week = j_a.get_resolved_in_week(
            board_filter_id, wi)

        resolved_story_points_in_week = sum(j_a.get_story_points(
            issue) or 0 for issue in resolved_issues_in_week)
        resolved_story_points_past_weeks.append(resolved_story_points_in_week)

    return resolved_story_points_past_weeks


def px_figure(story_points_list):
    weeks = list(range(-len(story_points_list), 0))
    df = pd.DataFrame(dict(weeks=weeks, story_points=story_points_list))
    fig = px.scatter(x=df.weeks, y=df.story_points, trendline="lowess")

    fig.update_layout(title='Forecast')
    fig.show()


if __name__ == '__main__':
    args = parse_input_args()

    jira_acc = JiraAccess(args.hostname, args.username, args.password)

    stories_points_list = get_resolved_story_points(
        jira_acc, args.board_filter_id, args.weeks)
    # stories_points_list = [43, 42, 172, 78, 30, 31, 22, 32, 11, 8, 11] # Test Data
    px_figure(stories_points_list)
