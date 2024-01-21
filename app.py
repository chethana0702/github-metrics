from flask import Flask, jsonify,request
import requests
import os

app = Flask(__name__)
github_api_base_url = 'https://api.github.com'
organization_name = 'chethana0702'

def get_contributors():
    contributors_url = f'{github_api_base_url}/repos/{organization_name}/github-metrics/contributors'
    contributors_response = requests.get(contributors_url)
    contributors_data = contributors_response.json()
    return jsonify({"contributors": contributors_data})

@app.route('/individual-contributions')
def get_individual_contributions():
    # Endpoint to fetch individual code contributions

    # Get the list of commits from the GitHub API
    commits_url = f'{github_api_base_url}/repos/{organization_name}/github-metrics/commits'
    commits_response = requests.get(commits_url)
    commits_data = commits_response.json()

    # Initialize a dictionary to store contributions per author
    contributions_per_author = {}

    # Iterate through commits and count contributions per author
    for commit in commits_data:
        author = commit['commit']['author']['name']
        contributions_per_author[author] = contributions_per_author.get(author, 0) + 1

    return jsonify({"individual_contributions": contributions_per_author})

@app.route('/prs-created')
def get_prs_created():
    try:
        # Fetch all pull requests from the repository
        prs_url = f"{github_api_base_url}/repos/your-username/github-metrics/pulls"
        response = requests.get(prs_url, headers='headers')
        prs_data = response.json()

        # Process PR data to count PRs created by each user
        prs_created_count = {}
        for pr in prs_data:
            user = pr['user']['login']
            prs_created_count[user] = prs_created_count.get(user, 0) + 1

        return jsonify(prs_created_count)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/prs-reviewed')
def get_prs_reviewed():
    # Endpoint to fetch number of PRs reviewed by each individual

    # Get the list of pull requests from the GitHub API
    prs_url = f'{github_api_base_url}/repos/{organization_name}/chethan0702/pulls'
    prs_response = requests.get(prs_url)
    prs_data = prs_response.json()

    # Initialize a dictionary to store the count of PRs reviewed per reviewer
    prs_reviewed_per_reviewer = {}

    # Iterate through pull requests and count PRs reviewed per reviewer
    for pr in prs_data:
        reviews_url = f'{pr["url"]}/reviews'
        reviews_response = requests.get(reviews_url)
        reviews_data = reviews_response.json()

        # Iterate through reviews and count PRs reviewed per reviewer
        for review in reviews_data:
            reviewer = review['user']['login']
            prs_reviewed_per_reviewer[reviewer] = prs_reviewed_per_reviewer.get(reviewer, 0) + 1

    return jsonify({"prs_reviewed": prs_reviewed_per_reviewer})

if __name__ == '__main__':
    app.run(debug=True)
