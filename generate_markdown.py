import json

DATA_PATH = "src/attempts.json"
OUTPUT_PATH = "README.md"

TIERS_MAP = {
    "G": "God Like",
    "S": "Super Human",
    "A": "Champion",
    "B": "Pro",
    "C": "Average",
    "CP": "Complete",
    "NO": "Notable outcomes"
}

# TODO: Clean up the code and attempt to remove duplicacy
def generate_markdown(data):
    markdown = ""
    header = "WORK IN PROGRESS\n\n"
    header += "# Awesome RL Attempts at Games\n\n"

    data['attempts'].sort(key=lambda attempt: attempt['game']['name'])
    
    game_links = []
    
    previous_name = ""
    for attempt in data['attempts']:
        game = attempt['game']
        if(game['name'] != previous_name):
            game_links.append(f"- [{game['name']}](#{game['name'].replace(' ', '-').lower()})")
            previous_name = game['name']

    header += "## Index:\n" + "\n".join(game_links) + "\n\n"
    markdown += header

    body = ""

    previous_name = ""
    for attempt in data['attempts']:
        game = attempt['game']
        info = attempt['info']

        maybe_platform = f"- **Platform:** {game['platform']}" if game['platform'] != "NA" else ""

        maybe_mode = f"- **Mode:** {game['mode']}" if 'mode' in game else ""

        if(previous_name != game['name']):
            body += f"## {game['name']}\n"
            previous_name = game['name']
        else:
            body += "\n---\n"
            
        if maybe_platform:
            body += f"{maybe_platform}\n"
        if maybe_mode:
            body += f"{maybe_mode}\n"
        
        tier = info['tier']
        maybe_star = "*" if 'caveats' in info else ""
        body += f"- **Tier:** {TIERS_MAP[tier]}{maybe_star} ({tier})\n"

        maybe_objective = f"- **Objective:** {info['objective']}" if 'objective' in info else ""
        if maybe_objective:
            body += f"{maybe_objective}\n"

        maybe_description = f"- **Description:** {info['description']}" if 'description' in info else ""
        if maybe_description:
            body += f"{maybe_description}\n"    

        maybe_t_description = f"- **Technical Description:** {info['t-description']}" if 't-description' in info else ""
        if maybe_t_description:
            body += f"{maybe_t_description}\n"        

        
        if 'caveats' in info:
            body += "- **Caveats:**\n"
            for caveat in info['caveats']:
                body += f"  - {caveat}\n"

        if "references" in info:
            body += "- **References:**\n"
            for reference in info['references']:
                body += f"  - [{reference['description']}]({reference['url']})\n"
            
        body += "\n"

    markdown += body
    return markdown


if __name__ == "__main__":
    with open(DATA_PATH) as data_file:
        data = json.load(data_file)
    
    markdown_data = generate_markdown(data)
    with open(OUTPUT_PATH, "w") as markdown_file:
        markdown_file.write(markdown_data)