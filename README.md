# Issue Metrics Action

This is a fork off of the Github Action [issue-metrics](https://github.com/github/issue-metrics)

Things changed:

1. Pull Request Size Metric - Added metric to calculate pull request size for each pull request, as well as generate the average size for the top level report

2. `action.yml` - This action will run off of the `Dockerfile` in this repository, rather than the published image for the original action

## Updated documentation based on changes:

### Available Metrics

| Metric                            | Description                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| Time to First Response            | The duration from creation to the initial comment or review.\*                             |
| Time to Close                     | The period from creation to closure.\*                                                     |
| Time to Answer (Discussions Only) | The time from creation to an answer.                                                       |
| Time in Label                     | The duration from label application to removal, requires `LABELS_TO_MEASURE` env variable. |
| Pull Request Size (PRs Only)      | An approximated size of pull requests.                                                     |

### Configuration

Below are the allowed configuration options:

| field                         | required | default | description                                                                                                                                                                                     |
| ----------------------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GH_TOKEN`                    | True     |         | The GitHub Token used to scan the repository. Must have read access to all repository you are interested in scanning.                                                                           |
| `SEARCH_QUERY`                | True     |         | The query by which you can filter issues/prs which must contain a `repo:`, `org:`, `owner:`, or a `user:` entry. For discussions, include `type:discussions` in the query.                      |
| `LABELS_TO_MEASURE`           | False    |         | A comma separated list of labels to measure how much time the label is applied. If not provided, no labels durations will be measured. Not compatible with discussions at this time.            |
| `HIDE_AUTHOR`                 | False    |         | If set to any value, the author will not be displayed in the generated markdown file.                                                                                                           |
| `HIDE_TIME_TO_FIRST_RESPONSE` | False    |         | If set to any value, the time to first response will not be displayed in the generated markdown file.                                                                                           |
| `HIDE_TIME_TO_CLOSE`          | False    |         | If set to any value, the time to close will not be displayed in the generated markdown file.                                                                                                    |
| `HIDE_TIME_TO_ANSWER`         | False    |         | If set to any value, the time to answer a discussion will not be displayed in the generated markdown file.                                                                                      |
| `HIDE_LABEL_METRICS`          | False    |         | If set to any value, the time in label metrics will not be displayed in the generated markdown file.                                                                                            |
| `HIDE_PULL_REQUEST_SIZE`      | False    |         | If set to any value, the pull request size metrics will not be displayed in the generated markdown file.                                                                                        |
| `IGNORE_USERS`                | False    |         | A comma separated list of users to ignore when calculating metrics. (ie. `IGNORE_USERS: 'user1,user2'`). To ignore bots, append `[bot]` to the user (ie. `IGNORE_USERS: 'github-actions[bot]'`) |

## Pull Request Size Metric Details

The pull request size metric calculates an approximate pr size with the following formula: `(number of additions +  number of deletions) * 0.5`
Looking at various pr size calculations, this is a commonly used formula as it accounts for Github's decision to count a line changed as +1/-1 (1 addition, 1 deletion). The pr size may always be off by a few lines, however, we do account for the case of 0 additions or 0 deletions.

## Development

### Getting Started (Mac)

1. Clone this repository
2. Install python3, which can be done through Homebrew and should install `pip` as well. Check for python and pip with `python3 --version` and `pip3 --version`.
3. Install virtualenv `pip3 install virtualenv`
4. Create a new virtual environment `python3 -m venv .venv`
5. Activate the virtual environment `source .venv/bin/activate`
6. Install packages with pip in the virtual environment `pip install -r requirements.txt`
7. You can now test and run code in the virtual environment. Test files run with `pytest <test file name>` - ex: `pytest test_pull_request_size.py`
8. When you're done, deactivate the environment with the command `deactivate`

If you use VSCode, you might be prompted to add extensions to properly read python. You can also set the python interpreter by opening the command palette and searching for `Python: Select Interpreter`.

You do not have to set up a `.env` at this time.

### Adding metrics

Try to follow the conventions set by the github/issue-metrics repo when adding new metrics. As much as possible, new methods should be documented the same way as the original methods. A new test file should be added and old tests should be updated where necessary.

Reference documentation:
This action uses `github3.py` to access github objects, here is their documentation home as well as the pages for the two types use most frequently in this project:

- [github3.py](https://github3.readthedocs.io/en/latest/index.html)
- [IssueSearchResult](https://github3.readthedocs.io/en/latest/api-reference/search.html#github3.search.IssueSearchResult)
- [PullRequest](https://github3.readthedocs.io/en/latest/api-reference/pulls.html#github3.pulls.PullRequest)

While adding the pull request size metric, the [Github REST API docs](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#create-a-pull-request) and this [alternate pull request metric project](https://github.com/AlexSim93/pull-request-analytics-action/tree/master) were helpful for getting a better understanding of how to interact with the pull request object.

## Original Documentation

<details>

<summary>Complete Original README:</summary>

[![CodeQL](https://github.com/github/issue-metrics/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/github/issue-metrics/actions/workflows/codeql-analysis.yml) [![Docker Image CI](https://github.com/github/issue-metrics/actions/workflows/docker-image.yml/badge.svg)](https://github.com/github/issue-metrics/actions/workflows/docker-image.yml) [![Python package](https://github.com/github/issue-metrics/actions/workflows/python-package.yml/badge.svg)](https://github.com/github/issue-metrics/actions/workflows/python-package.yml)

This is a GitHub Action that searches for issues/pull requests/discussions in a repository, measures several metrics, and generates a report in form of a GitHub issue.
The issues/pull requests/discussions to search for can be filtered by using a search query.

This action, developed by GitHub OSPO for our internal use, is open-sourced for your potential benefit.
Feel free to inquire about its usage by creating an issue in this repository.

## Available Metrics

| Metric                            | Description                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| Time to First Response            | The duration from creation to the initial comment or review.\*                             |
| Time to Close                     | The period from creation to closure.\*                                                     |
| Time to Answer (Discussions Only) | The time from creation to an answer.                                                       |
| Time in Label                     | The duration from label application to removal, requires `LABELS_TO_MEASURE` env variable. |

\*For pull requests, these metrics exclude the time the PR was in draft mode.

\*For issues and pull requests, comments by issue/pull request author's and comments by bots are excluded.

To find syntax for search queries, check out the documentation on [searching issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/filtering-and-searching-issues-and-pull-requests)
or [searching discussions](https://docs.github.com/en/search-github/searching-on-github/searching-discussions).

## Sample Report

The output of this action is a report in form of a GitHub issue.
Below you see a sample of such a GitHub issue.

![Sample GitHub issue created by the issue/metrics GitHub Action](docs/img/issue-metrics-sample-output.png)

## Getting Started

Create a workflow file (ie. `.github/workflows/issue-metrics.yml`) in your repository with the following contents:

**Note**: `repo:owner/repo` is the repository you want to measure metrics on

```yaml
name: Monthly issue metrics
on:
  workflow_dispatch:
  schedule:
    - cron: "3 2 1 * *"

permissions:
  issues: write
  pull-requests: read

jobs:
  build:
    name: issue metrics
    runs-on: ubuntu-latest
    steps:
      - name: Get dates for last month
        shell: bash
        run: |
          # Calculate the first day of the previous month
          first_day=$(date -d "last month" +%Y-%m-01)

          # Calculate the last day of the previous month
          last_day=$(date -d "$first_day +1 month -1 day" +%Y-%m-%d)

          #Set an environment variable with the date range
          echo "$first_day..$last_day"
          echo "last_month=$first_day..$last_day" >> "$GITHUB_ENV"

      - name: Run issue-metrics tool
        uses: github/issue-metrics@v2
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SEARCH_QUERY: 'repo:owner/repo is:issue created:${{ env.last_month }} -reason:"not planned"'

      - name: Create issue
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: Monthly issue metrics report
          token: ${{ secrets.GITHUB_TOKEN }}
          content-filepath: ./issue_metrics.md
```

## Example use cases

- As a maintainer, I want to see metrics for issues and pull requests on the repository I maintain in order to ensure I am giving them the proper amount of attention.
- As a first responder on a repository, I want to ensure that users are getting contact from me in a reasonable amount of time.
- As an OSPO, I want to see how many open source repository requests are open/closed, and metrics for how long it takes to get through the open source process.
- As a product development team, I want to see metrics around how long pull request reviews are taking, so that we can reflect on that data during retrospectives.

## Support

If you need support using this project or have questions about it, please [open up an issue in this repository](https://github.com/github/issue-metrics/issues). Requests made directly to GitHub staff or support team will be redirected here to open an issue. GitHub SLA's and support/services contracts do not apply to this repository.

## Use as a GitHub Action

1. Create a repository to host this GitHub Action or select an existing repository. This is easiest if it is the same repository as the one you want to measure metrics on.
2. Select a best fit workflow file from the [examples directory](./docs/example-workflows.md) for your use case.
3. Copy that example into your repository (from step 1) and into the proper directory for GitHub Actions: `.github/workflows/` directory with the file extension `.yml` (ie. `.github/workflows/issue-metrics.yml`)
4. Edit the values (`SEARCH_QUERY`, `assignees`) from the sample workflow with your information. See the [SEARCH_QUERY](./docs/search-query.md) section for more information on how to configure the search query.
5. If you are running metrics on a repository other than the one where the workflow file is going to be, then update the value of `GH_TOKEN`. Do this by creating a [GitHub API token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) with permissions to read the repo and write issues. Then take the value of the API token you just created, and [create a repository secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets) where the name of the secret is `GH_TOKEN` and the value of the secret the API token. Then finally update the workflow file to use that repository secret by changing `GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}` to `GH_TOKEN: ${{ secrets.GH_TOKEN }}`. The name of the secret can really be anything. It just needs to match between when you create the secret name and when you refer to it in the workflow file.
6. If you want the resulting issue with the metrics in it to appear in a different repository other than the one the workflow file runs in, update the line `token: ${{ secrets.GITHUB_TOKEN }}` with your own GitHub API token stored as a repository secret. This process is the same as described in the step above. More info on creating secrets can be found [here](https://docs.github.com/en/actions/security-guides/encrypted-secrets).
7. Commit the workflow file to the default branch (often `master` or `main`)
8. Wait for the action to trigger based on the `schedule` entry or manually trigger the workflow as shown in the [documentation](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow).

### Configuration

Below are the allowed configuration options:

| field                         | required | default | description                                                                                                                                                                                     |
| ----------------------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GH_TOKEN`                    | True     |         | The GitHub Token used to scan the repository. Must have read access to all repository you are interested in scanning.                                                                           |
| `SEARCH_QUERY`                | True     |         | The query by which you can filter issues/prs which must contain a `repo:`, `org:`, `owner:`, or a `user:` entry. For discussions, include `type:discussions` in the query.                      |
| `LABELS_TO_MEASURE`           | False    |         | A comma separated list of labels to measure how much time the label is applied. If not provided, no labels durations will be measured. Not compatible with discussions at this time.            |
| `HIDE_AUTHOR`                 | False    |         | If set to any value, the author will not be displayed in the generated markdown file.                                                                                                           |
| `HIDE_TIME_TO_FIRST_RESPONSE` | False    |         | If set to any value, the time to first response will not be displayed in the generated markdown file.                                                                                           |
| `HIDE_TIME_TO_CLOSE`          | False    |         | If set to any value, the time to close will not be displayed in the generated markdown file.                                                                                                    |
| `HIDE_TIME_TO_ANSWER`         | False    |         | If set to any value, the time to answer a discussion will not be displayed in the generated markdown file.                                                                                      |
| `HIDE_LABEL_METRICS`          | False    |         | If set to any value, the time in label metrics will not be displayed in the generated markdown file.                                                                                            |
| `IGNORE_USERS`                | False    |         | A comma separated list of users to ignore when calculating metrics. (ie. `IGNORE_USERS: 'user1,user2'`). To ignore bots, append `[bot]` to the user (ie. `IGNORE_USERS: 'github-actions[bot]'`) |

## Further Documentation

- [Example workflows](./docs/example-workflows.md)
- [Measuring time spent in labels](./docs/measure-time.md)
- [Assigning teams instead of individuals](./docs/assign-team-instead-of-individual.md)
- [Example using the JSON output instead of the markdown output](./docs/example-using-json-instead-markdown-output.md)
- [Configuring the `SEARCH_QUERY`](./docs/search-query.md)
- [Local usage without Docker](./docs/local-usage-without-docker.md)

## Contributions

We would ❤️ contributions to improve this action. Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for how to get involved.

## License

[MIT](LICENSE)

## More OSPO Tools

Looking for more resources for your open source program office (OSPO)? Check out the [`github-ospo`](https://github.com/github/github-ospo) repo for a variety of tools designed to support your needs.

</details>
