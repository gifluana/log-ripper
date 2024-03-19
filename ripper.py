import re
import sys
import glob

def extract_usernames(log_files, keywords, ignored_usernames):
    users_messages = {}
    pattern = r'\[(\d{2}:\d{2}:\d{2})\] (\w+):'
    
    for log_file in log_files:
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    timestamp = match.group(1)
                    username = match.group(2)
                    message = line.split(': ', 1)[1].strip()
                    
                    if username in ignored_usernames:
                        continue
                    
                    for keyword in keywords:
                        if keyword.lower() in message.lower():
                            if username not in users_messages:
                                users_messages[username] = []
                            users_messages[username].append(f'[{timestamp}] {message}')
                            break
    
    return users_messages

log_files = glob.glob('./*.log') + glob.glob('./*.txt')

keywords = sys.argv[1].split(',')

ignored_usernames = sys.argv[2].split(',') if len(sys.argv) > 2 else []

users_messages = extract_usernames(log_files, keywords, ignored_usernames)

with open('output.txt', 'w', encoding='utf-8') as file:
    for username, messages in users_messages.items():
        file.write(f'{username}:\n')
        for message in messages:
            file.write(f'  {message}\n')

print("""
.####.########..######..##.......##.....##.##....##....###....########
..##.....##....##....##.##.......##.....##.###...##...##.##........##.
..##.....##....##.......##.......##.....##.####..##..##...##......##..
..##.....##.....######..##.......##.....##.##.##.##.##.....##....##...
..##.....##..........##.##.......##.....##.##..####.#########...##....
..##.....##....##....##.##.......##.....##.##...###.##.....##..##.....
.####....##.....######..########..#######..##....##.##.....##.########
""")

print('Os resultados foram salvos no arquivo "output.txt"!')
print('')