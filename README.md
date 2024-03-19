# Log Ripper

## Description
The Log Ripper is a Python script that allows you to extract usernames from Twitch chat logs based on specific criteria. It can be useful for analyzing chat activity or identifying users who have sent messages containing certain keywords.

## Prerequisites
- Python 3.x installed on your system

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using the following command:

    ```bash
    python ripper.py 'word1,word2,word3' 'user1,user2,user3'
    ```

    Replace `'word1,word2,word3'` with a comma-separated list of words that you want to search for in the chat messages. These words can be any keywords or phrases you're interested in.
    
    Replace `'user1,user2,user3'` with a comma-separated list of usernames that you want the script to ignore and not include in the results. This can be useful if you want to exclude certain users from the analysis.

4. The script will process the chat logs and generate a list of usernames that meet the specified criteria. The results will be displayed in the terminal or command prompt.

## Example
To search for messages containing the words "hello" and "world" and exclude the usernames "user1" and "user2", you would run the following command:
