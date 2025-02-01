# podcast-generator

A GitHub Action that creates a podcast feed from a YAML file. Since YAML is more readable and user-friendly than XML, this action converts your YAML file into a properly formatted podcast feed.

## Features

- Converts a YAML file into a podcast RSS feed.

- Supports Google Play, iTunes, and standard podcast metadata.

- Easy integration with GitHub Actions workflows.
  
## Usage
In your repo, go to settings > Pages and select the main branch as the source. This will create a link to yor page and give all of the content in the main branch a URL. Note the URL for the next step.

### 1. Create Your Podcast YAML File

Ensure you have a feed.yaml file structured like this:

    link: "https://example.com/"
    title: "My Podcast"
    format: "audio/mpeg"
    subtitle: "A great podcast"
    author: "John Doe"
    description: "An example podcast description."
    image: "cover.jpg"
    language: "en-us"
    category: "Technology"
    item:
      - title: "Episode 1"
        description: "The first episode."
        duration: "15:30"
        published: "Wed, 01 Jan 2024 00:00:00 GMT"
        file: "episode1.mp3"
        length: "12345678"

### 2. Add the GitHub Action

In your repository, create a .github/workflows/generate-podcast.yml file and configure it as follows:

    name: Generate Podcast Feed
    
    on:
      push:
        paths:
          - 'feed.yaml'
      workflow_dispatch:
    
    jobs:
      build:
        runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Run Podcast Generator
        uses: ZannyM/podcast-generator@main
        with:
          email: "your-email@example.com"
          name: "Your Name"

      - name: Commit and Push Changes
        run: |
          git config --global user.email "your-email@example.com"
          git config --global user.name "Your Name"
          git add podcast.xml
          git commit -m "Update podcast feed"
          git push

### 3. Customize the Action

Modify the email and name inputs with your GitHub information to ensure the commit is correctly attributed.

## Output

The generated podcast.xml file will be available in your repository, ready to be used as a valid RSS podcast feed.

## Troubleshooting

- Ensure your YAML file is correctly formatted.

- Check the workflow logs in GitHub Actions for any errors.

- If the podcast.xml file is not updating, verify that your repository has write         permissions for the action.

## License

This project is licensed under the MIT License.

## Author

Developed by Zanny Maholobela.
